# YAML Dosyalarında `inuse: false` Arama ve Excel'e Aktarma

Bu script, belirttiğiniz klasör ve alt klasörlerdeki tüm `.yaml` ve `.yml` dosyalarını tarar, dosya içeriğinde `inuse: false` olarak işaretlenmiş bölümleri bulur ve bunları bir Excel dosyasına (`output.xlsx`) aktarır.

## Özellikler

- Tüm alt klasörleriyle birlikte arama yapar.
- Çoklu YAML dokümanlarını destekler.
- Bulunan her kayıt için dosya yolunu ve ilgili içeriği listeler.
- Sonuçları kolayca analiz edebilmek için Excel dosyasına kaydeder.

## Gereksinimler

- Python 3.x
- [PyYAML](https://pypi.org/project/pyyaml/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/)

Kurmak için:
```sh
pip install -r requirements.txt
```

## Kullanım

1. Script dosyasını çalıştırın:
    ```sh
    python yaml_inuse_false_to_excel.py
    ```
2. Taramak istediğiniz ana klasörün yolunu girin.
3. `output.xlsx` dosyası, script ile aynı dizine kaydedilecektir.

## Çıktı

Excel dosyasında iki sütun bulunur:
- **Dosya**: `inuse: false` bulunan YAML dosyasının tam yolu.
- **Bulunan İçerik**: İlgili anahtar ve değerlerin tamamı.

## Lisans

MIT
