# Toprak's Calculator (Beta v0.1)

## NEW UPDATE Beta v0.2

This update includes a logging system. Do not extract it from the folder; otherwise, the logging system will not work.

## 📜 License

This project is licensed under the MIT License. This means the code can be freely used and modified, but the software is provided “as is” and no warranties are provided.

## Language Support

This program offers two language options.

- Turkish interface
- English interface

You can use whichever one you prefer.

## 🤝 Contribute

This project is open to development! If you find a bug or want to add a new feature:

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes and submit a Pull Request.

## How to Use

Follow these steps to run this program on any computer

1. Install Python: Make sure Python 3.x is installed on your computer.
2. Install the Library: Open the terminal (CMD or VS Code Terminal) and type the following command:
   `pip install colorama`

## Roadmap

- new calculation types
- GUI

## Developer

[Developer](https://github.com/devtoprak)

'''python
with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {action1} ve {action2} the numbers have been entered.\n")
        log_file.close()

        with open("topraks-calculator-en-v0.2-beta/hesap_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {sonuc} the result has been calculated\n")

Here is a small portion of the code. If you want to see the rest of the code, simply open the .py file in Visual Studio Code.
