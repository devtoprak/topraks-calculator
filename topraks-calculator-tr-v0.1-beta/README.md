# Toprak's Calculator (Beta v0.1)

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
- işlem geçmişini bir .txt dosyasına kaydetme
- Grafik arayüz

## Yapımcı

[Yapımcı](https://github.com/devtoprak)

'''python
    HESAP = Fore.CYAN + "=== HESAP MAKINESI ==="
    print(HESAP)
    islem1 = float(input(Fore.GREEN + "İlk sayıyı girin: "))
    islem2 = float(input(Fore.GREEN + "İkinci sayıyı girin: "))
    print(Fore.RED + "Yapmak istediğiniz işlemi seçin:")
    print(Fore.CYAN + "1. Toplama")
    print(Fore.CYAN + "2. Çıkarma")
    print(Fore.CYAN + "3. Çarpma")
    print(Fore.CYAN + "4. Bölme")
    print(Fore.CYAN + "5. karekok alma")
    print(Fore.CYAN + "6. us alma")
    print(Fore.CYAN + "7. faktoriyel alma")
    print(Fore.CYAN + "8. mod alma")
    secim = input("Seçiminizi yapın (1/2/3/4/5/6/7/8): ")

bunlar kodlarin birazidir diger kodları gormek istiyorsaniz .py uzantili dosyayi Visual Studio Code ile acmanız yeterlidir.
