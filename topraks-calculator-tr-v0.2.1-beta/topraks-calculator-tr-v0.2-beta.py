from colorama import Fore, Style, init
import math
from datetime import datetime
import os
import traceback


init(autoreset=True)


DOSYA_YOLU = os.path.dirname(os.path.abspath(__file__))
LOG_DOSYASI = os.path.join(DOSYA_YOLU, "hesap_log.txt")

try:
    while True:
        HESAP = Fore.CYAN + "=== HESAP MAKINESI ==="
        print(HESAP)
        
        islem1 = float(input(Fore.GREEN + "İlk sayıyı girin: "))
        islem2 = float(input(Fore.GREEN + "İkinci sayıyı girin: "))
        
        
        with open(LOG_DOSYASI, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}: {islem1} ve {islem2} sayıları girildi.\n")
        
        print(Fore.RED + "Yapmak istediğiniz işlemi seçin:")
        print(Fore.CYAN + "1. Toplama")    
        print(Fore.CYAN + "2. Çıkarma")    
        print(Fore.CYAN + "3. Çarpma")
        print(Fore.CYAN + "4. Bölme")
        print(Fore.CYAN + "5. Karekök alma")
        print(Fore.CYAN + "6. Üs alma")
        print(Fore.CYAN + "7. Faktöriyel alma")
        print(Fore.CYAN + "8. Mod alma")
        
        secim = input("Seçiminizi yapın (1/2/3/4/5/6/7/8): ")
        
        if secim == '1':
            sonuc = islem1 + islem2
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '2':
            sonuc = islem1 - islem2
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '3':
            sonuc = islem1 * islem2
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '4':
            
            if islem2 == 0:
                print(Fore.RED + "Hata: Bir sayı sıfıra bölünemez!")
                continue
            sonuc = islem1 / islem2
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '5':
            sonuc = math.sqrt(islem1)
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '6':
            sonuc = math.pow(islem1, islem2)
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '7':
            sonuc = math.factorial(int(islem1))
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        elif secim == '8':
            sonuc = islem1 % islem2
            print(Fore.MAGENTA + "Sonuç: ", sonuc)
        else:
            print(Fore.RED + "Geçersiz seçim! Lütfen menüden bir işlem seçin.")
            continue 
        
        with open(LOG_DOSYASI, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} sonucu hesaplandı.\n")
            
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...\n")

except Exception as e:
    print(Fore.RED + "\nBeklenmeyen bir hata oluştu!")
    print(Fore.RED + "Hata detayı:")
    traceback.print_exc()
    input(Fore.YELLOW + "\nPencereyi kapatmak için Enter'a basın...")