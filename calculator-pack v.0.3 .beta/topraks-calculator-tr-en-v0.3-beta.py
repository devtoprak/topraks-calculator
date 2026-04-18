from colorama import Fore, init, Style

init(autoreset=True)

dil = input(Fore.CYAN + "Dil seçin / select language (tr/en): ").lower()

if dil == "tr":
        from assets import turkishinterface as ui
        
elif dil == "en":
    from assets import englishinterface as ui

else:
    print("error")
    exit()

ui.baslat()