from colorama import Fore, Style, init
init(autoreset=True)
import math

while True:
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
    if secim == '1':
        sonuc = islem1 + islem2
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '2':
        sonuc = islem1 - islem2
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '3':
        sonuc = islem1 * islem2
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '4':
        sonuc = islem1 / islem2
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '5':
        sonuc = math.sqrt(islem1)
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '6':
        sonuc = math.pow(islem1, islem2)
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '7':
        sonuc = math.factorial(int(islem1))
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    elif secim == '8':
        sonuc = islem1 % islem2
        print(Fore.MAGENTA + "Sonuç: ", sonuc)
        cikis = input(Fore.YELLOW + "Çıkmak istiyor musunuz? (E/H): ")
        if cikis.upper() == 'E':
            print(Fore.GREEN + "Hesap makinesinden çıkılıyor...")
            break
        elif cikis.upper() == 'H':
            print(Fore.GREEN + "Hesap makinesine devam ediliyor...")
    else:
        print(Fore.RED + "Geçersiz seçim! Lütfen 1, 2, 3, 4, 5, 6, 7 veya 8'ye basınız.")