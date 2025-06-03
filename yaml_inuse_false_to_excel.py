import os
import yaml
import pandas as pd

def find_yaml_files(root_dir):
    yaml_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(('.yaml', '.yml')):
                yaml_files.append(os.path.join(dirpath, file))
    return yaml_files

def extract_inuse_false(yaml_file):
    results = []
    with open(yaml_file, 'r', encoding='utf-8') as f:
        try:
            docs = list(yaml.safe_load_all(f))
        except Exception as e:
            print(f"Hata ({yaml_file}): {e}")
            return results
    for doc in docs:
        if isinstance(doc, dict):
            if doc.get('inuse', True) is False:
                results.append({'file': yaml_file, 'content': doc})
            # Eğer alt anahtarlar varsa:
            for key, value in doc.items():
                if isinstance(value, dict) and value.get('inuse', True) is False:
                    results.append({'file': yaml_file, 'content': {key: value}})
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict) and item.get('inuse', True) is False:
                            results.append({'file': yaml_file, 'content': {key: item}})
    return results

def main(root_dir):
    all_results = []
    yaml_files = find_yaml_files(root_dir)
    for yfile in yaml_files:
        all_results.extend(extract_inuse_false(yfile))
    # Excel için uygun hale getir
    rows = []
    for r in all_results:
        rows.append({
            'Dosya': r['file'],
            'Bulunan İçerik': str(r['content'])
        })
    df = pd.DataFrame(rows)
    df.to_excel('output.xlsx', index=False)
    print(f"{len(rows)} kayıt bulundu ve output.xlsx dosyasına yazıldı.")

if __name__ == "__main__":
    ana_klasor = input("Taramak istediğiniz ana klasörü girin: ").strip()
    main(ana_klasor)
