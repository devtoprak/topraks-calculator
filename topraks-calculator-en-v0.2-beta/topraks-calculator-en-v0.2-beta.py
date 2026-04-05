from colorama import Fore, Style, init
init(autoreset=True)
import math
from datetime import datetime

while True:
    HESAP = Fore.CYAN + "=== CALCULATOR ==="
    print(HESAP)
    action1 = float(input(Fore.GREEN + "Enter the first number: "))
    action2 = float(input(Fore.GREEN + "Enter the second number: "))
    with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {action1} and {action2} The numbers have been entered.\n")
        log_file.close()
    print(Fore.RED + "Select the operation you want to perform:")
    print(Fore.CYAN + "1. Addition")    
    print(Fore.CYAN + "2. Subtraction")    
    print(Fore.CYAN + "3. Multiplication")
    print(Fore.CYAN + "4. Division")
    print(Fore.CYAN + "5. Square Root")
    print(Fore.CYAN + "6. Exponentiation")
    print(Fore.CYAN + "7. Factorial")
    print(Fore.CYAN + "8. Modulus")
    secim = input("Select your operation (1/2/3/4/5/6/7/8): ")
    if secim == '1':
        sonuc = action1 + action2
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '2':
        sonuc = action1 - action2
        
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '3':
        sonuc = action1 * action2
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '4':
        sonuc = action1 / action2
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '5':
        sonuc = math.sqrt(action1)
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '6':
        sonuc = math.pow(action1, action2)
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '7':
        sonuc = math.factorial(int(action1))
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    elif secim == '8':
        sonuc = action1 % action2
        print(Fore.MAGENTA + "Result: ", sonuc)
        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} result calculated.\n")
        cikis = input(Fore.YELLOW + "Exit? (Y/N): ")
        if cikis.upper() == 'Y':
            print(Fore.GREEN + "Calculator exiting...")
            break
        elif cikis.upper() == 'N':
            print(Fore.GREEN + "Calculator continuing...")
    else:
        print(Fore.RED + "Invalid selection! Please press 1, 2, 3, 4, 5, 6, 7 or 8.")