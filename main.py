import os
from os import listdir
from os.path import isfile, join
from scanner import Scanner

RED = "\033[31m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[37m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

DIRECTORY = os.getcwd()


def main():
    menu()


def menu():
    os.system("cls")
    input_user = None

    while True:
        os.system("cls")
        print("╔═════════════════════════════╗")
        print("║ MENU LEXER | UTN - SINTAXIS ║")
        print("╚═════════════════════════════╝\n")
        print("1) Ingresar por teclado.")
        print("2) Leer un archivo.")
        print("0) Salir")
        # try:
        input_user = int(input("\n> Ingrese una opcion: "))
        if input_user == 1:
            answer = inputUserTxt()
        elif input_user == 2:
            answer = readFromTxt()
        elif input_user == 0:
            break
        else:
            print("ERROR: la opcion ingresada no es valida")
            input("\nPresione intro para seguir...")
        if answer == "n":
            break
        # except:
        #    print("ERROR: solo puede ingresar numeros.")
        #    input("\nPresione intro para seguir...")


def readFromTxt() -> str:
    input_user = None
    list_files = [f for f in listdir(DIRECTORY) if isfile(join(DIRECTORY, f))]
    only_txt = []

    for f in list_files:
        if f.endswith(".txt"):
            only_txt.append(f)

    while True:
        cont = 0
        os.system("cls")
        print("Opcion -> Leer desde un archivo.\n")

        for f in only_txt:
            cont += 1
            print(f"{cont}) {f}")

        try:
            input_user = int(input("\n> Seleccione una opcion: "))
            if input_user > 0 and input_user <= cont:
                break
            else:
                print(f"\n{RED}ERROR: {WHITE}la opcion ingresada no es valida.")
                input("\nPresione intro para seguir...")
        except:
            print(f"\n{RED}ERROR: {WHITE}solo puede ingresar numeros.")
            input("\nPresione intro para seguir...")

    name_file = only_txt[int(input_user) - 1]
    file_to_read = open(f"{name_file}", "r", encoding="UTF-8")
    s = Scanner(file_to_read.read())
    tokens = s.scanAll()

    return showTokens(tokens, name_file)


def inputUserTxt() -> str:
    os.system("cls")
    s = Scanner(input("> Ingrese el texto: "))
    tokens = s.scanAll()

    return showTokens(tokens, None)


def showTokens(tokens, name_file):
    while True:
        os.system("cls")
        if name_file:
            print(f"Archivo cargado: {name_file}")
        if tokens:
            print(f"\n{GREEN}Tokens \n{YELLOW}Lexema\n{RED}Errores{WHITE}")
            print(f"\nTokens encontrados: \n")

            digits_to_space = len(str(len(tokens)))

            for dicts in tokens:
                n_spacing = digits_to_space - len(str(dicts["line"]))
                spacing = " " * n_spacing
                line_column = spacing + str(dicts["line"]) + "│ "

                print(f"{line_column}", end="")
                dict_array_length = len(dicts["tokens"])
                for token in dicts["tokens"]:
                    if not isinstance(token, str):
                        print(
                            f"{GREEN}{token.token_type} {WHITE}» {YELLOW}{token.lexeme}{WHITE}",
                            end=(f"{WHITE}|" if dict_array_length > 1 else ""),
                        )
                        dict_array_length -= 1
                    else:
                        print(f"{RED}{token}", end=f"{WHITE}")
                else:
                    print()

            answer = input("\n¿Desea realizar otra operación? [s/n]: ")
            if answer == "s" or answer == "n":
                return answer
            else:
                print(f"\n{RED}ERROR: {WHITE}la opción ingresada no es valida.")
                input("\nPresione intro para seguir...")

        else:
            print(f"{RED}No se hallaron tokens.{WHITE}")
            answer = input("\n¿Desea realizar otra operación? [s/n]: ")
            if answer == "s" or answer == "n":
                return answer
            else:
                print(f"\n{RED}ERROR: {WHITE}la opción ingresada no es valida.")
                input("\nPresione intro para seguir...")


if __name__ == "__main__":
    main()
