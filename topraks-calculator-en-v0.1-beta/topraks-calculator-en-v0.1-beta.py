from colorama import Fore, Style, init
init(autoreset=True)
import math
while True:
    ACCOUNT = Fore.CYAN + "=== CALCULATOR ==="
    print(ACCOUNT)
    action1 = float(input(Fore.GREEN + "Enter the first number: "))
    action2 = float(input(Fore.GREEN + "Enter the second number: "))
    print(Fore.RED + "Select the action you want to perform:")
    print(Fore.CYAN + "1. Addition")
    print(Fore.CYAN + "2. Subtraction")
    print(Fore.CYAN + "3. Multiplication")
    print(Fore.CYAN + "4. Division")
    print(Fore.CYAN + "5. Square Root")
    print(Fore.CYAN + "6. Exponentiation")
    print(Fore.CYAN + "7. Factorial")
    print(Fore.CYAN + "8. Modulus")
    pick = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    if pick == '1':
        result = action1 + action2
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '2':
        result = action1 - action2
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '3':
        result = action1 * action2
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '4':
        result = action1 / action2
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '5':
        result = math.sqrt(action1)
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '6':
        result = math.pow(action1, action2)
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '7':
        result = math.factorial(int(action1))
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    elif pick == '8':
        result = action1 % action2
        print(Fore.MAGENTA + "Result: ", result)
        quit = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        continue
