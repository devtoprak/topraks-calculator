from colorama import Fore, Style, init
import math
from datetime import datetime
import os
import traceback
init(autoreset=True)


FILE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FILE_PATH, "calculator_log.txt")

try:
    while True:
        CALCULATOR = Fore.CYAN + "=== CALCULATOR ==="
        print(CALCULATOR)
        
        num1 = float(input(Fore.GREEN + "Enter the first number: "))
        num2 = float(input(Fore.GREEN + "Enter the second number: "))
        
        
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}: Numbers {num1} and {num2} were entered.\n")
        
        print(Fore.RED + "Select the operation you want to perform:")
        print(Fore.CYAN + "1. Addition")    
        print(Fore.CYAN + "2. Subtraction")    
        print(Fore.CYAN + "3. Multiplication")
        print(Fore.CYAN + "4. Division")
        print(Fore.CYAN + "5. Square root")
        print(Fore.CYAN + "6. Exponentiation")
        print(Fore.CYAN + "7. Factorial")
        print(Fore.CYAN + "8. Modulo (Remainder)")
        
        choice = input("Make your choice (1/2/3/4/5/6/7/8): ")
        
        if choice == '1':
            result = num1 + num2
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '2':
            result = num1 - num2
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '3':
            result = num1 * num2
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '4':
            if num2 == 0:
                print(Fore.RED + "Error: A number cannot be divided by zero!")
                continue
            result = num1 / num2
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '5':
            result = math.sqrt(num1)
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '6':
            result = math.pow(num1, num2)
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '7':
            result = math.factorial(int(num1))
            print(Fore.MAGENTA + "Result: ", result)
        elif choice == '8':
            result = num1 % num2
            print(Fore.MAGENTA + "Result: ", result)
        else:
            print(Fore.RED + "Invalid choice! Please select an operation from the menu.")
            continue 
            
        
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()}: Result {result} was calculated.\n")
            
        exit_choice = input(Fore.YELLOW + "Do you want to exit? (Y/N): ")
        if exit_choice.upper() == 'Y':
            print(Fore.GREEN + "Exiting the calculator...")
            break
        elif exit_choice.upper() == 'N':
            print(Fore.GREEN + "Continuing with the calculator...\n")

except Exception as e:
    print(Fore.RED + "\nAn unexpected error occurred!")
    print(Fore.RED + "Error details:")
    traceback.print_exc()
    input(Fore.YELLOW + "\nPress Enter to close the window...")