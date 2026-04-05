# Toprak's Calculator (Beta v0.2)

## YENİ GÜNCELLEME Beta v0.2

 bu güncellemede log sistemi eklenmiştir. Klasörün içinden çıkartmayın, aksi takdirde log sistemi çalışmaz.

## 📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Bu, kodun serbestçe kullanılabileceği, değiştirilebileceği ancak yazılımın "olduğu gibi" sunulduğu ve herhangi bir garanti verilmediği anlamına gelir.

## Dil desteği

Bu programın iki dil seçeneği vardır.

- türkçe arayüz
- ingilizce arayüz

dilediğinizi kullanabilirsiniz.

## 🤝 Katkıda Bulunma

Bu proje gelişime açıktır! Eğer bir hata bulursanız veya yeni bir özellik eklemek isterseniz:

1. Bu depoyu fork edin.
2. Yeni bir özellik dalı oluşturun.
3. Değişikliklerinizi commit edin ve bir Pull Request gönderin.

## Nasıl Kullanılır?

Bu programı herhangi bir bilgisayarda çalıştırmak için şu adımları izleyin

1. Python Yükleyin: Bilgisayarınızda Python 3.x sürümünün kurulu olduğundan emin olun.
2. Kütüphaneyi Kurun: Terminali (CMD veya VS Code Terminal) açın ve şu komutu yazın:
   `pip install colorama`

## Yol haritasi

- yeni hesaplama türleri
- Grafik arayüz

## Yapımcı

[Yapımcı](https://github.com/devtoprak)

## Kodlardan kesitler

with open("topraks-calculator-tr-v0.2-beta/hesap_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {islem1} ve {islem2} sayıları girildi.\n")
        log_file.close()

        with open("topraks-calculator-tr-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} sonucu hesaplandı.\n")

bunlar kodlarin birazidir diger kodları gormek istiyorsaniz .py uzantili dosyayi Visual Studio Code ile acmanız yeterlidir.
