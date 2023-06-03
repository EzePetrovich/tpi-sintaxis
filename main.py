import os
from os import listdir
from os.path import isfile, join
from colorama import Fore
from colorama import init
from scanner import Scanner

DIRECTORY = os.getcwd()

'''
    1. Must -> Encontrar error en línea | Should -> Que muestre el error
    2. Detectar el contenido de las etiquetas como -> <text>
'''

def main():
    init(autoreset=True)
    menu()

def menu():
    os.system('cls')
    input_user = None
    
    while(True):
        os.system('cls')
        print('╔═════════════════════════════╗')
        print('║ MENU LEXER | UTN - SINTAXIS ║')
        print('╚═════════════════════════════╝\n')
        print('1) Ingresar por teclado.')
        print('2) Leer un archivo.')
        print('0) Salir')
        try:
            input_user = int(input('\n> Ingrese una opcion: '))
            if(input_user == 1):
                answer = inputUserTxt() 
            elif(input_user == 2):
                answer = readFromTxt()
            elif(input_user == 0):
                break
            else:
                print('ERROR: la opcion ingresada no es valida')
                input('\nPresione intro para seguir...')
            if answer == 'n':
                    break
        except:
            print('ERROR: solo puede ingresar numeros.')
            input('\nPresione intro para seguir...')
        
def readFromTxt() -> str:
    input_user = None
    list_files = [f for f in listdir(DIRECTORY) if isfile(join(DIRECTORY, f))]
    only_txt = []

    for f in list_files:
        if(f.endswith('.txt')):
            only_txt.append(f)
    
    while(True):
        cont = 0
        os.system('cls')
        print('Opcion -> Leer desde un archivo.\n')
        
        for f in only_txt:
            cont += 1
            print(f'{cont}) {f}')
            
        try:
            input_user = int(input('\n> Seleccione una opcion: '))
            if(input_user > 0 and input_user <= cont):
                break
            else:
                print(f'\n{Fore.RED}ERROR: {Fore.WHITE}la opcion ingresada no es valida.')
                input('\nPresione intro para seguir...')
        except:
            print(f'\n{Fore.RED}ERROR: {Fore.WHITE}solo puede ingresar numeros.')
            input('\nPresione intro para seguir...')
    
    name_file = only_txt[int(input_user) - 1]
    file_to_read = open(f'{name_file}', 'r', encoding='UTF-8')
    s = Scanner(file_to_read.read())
    tokens = s.scanAll()
    
    return showTokens(tokens, name_file)
    
    
     
    

def inputUserTxt() -> str:
    os.system('cls')
    s = Scanner(input('> Ingrese el texto: '))
    tokens = s.scanAll()
    
    return showTokens(tokens, None)

def showTokens(tokens, name_file):
    while(True):
        os.system('cls')
        if(name_file):
            print(f'Archivo cargado: {name_file}')
        if tokens:
            print(f"\nSe encontraron los siguientes tokens: \n")
                
            for t in tokens:
                print(f'{Fore.LIGHTGREEN_EX}{t.token_type}{Fore.WHITE} » {Fore.LIGHTYELLOW_EX}{t.lexeme}')
                
            answer = input('\n¿Desea realizar otra operación? [s/n]: ')
            if answer == 's' or answer == 'n':
                return answer
            else:
                print(f'\n{Fore.RED}ERROR: {Fore.WHITE}la opción ingresada no es valida.')
                input('\nPresione intro para seguir...')

        else:
            print(f'{Fore.RED}No se hallaron tokens.')
            answer = input('\n¿Desea realizar otra operación? [s/n]: ')
            if answer == 's' or answer == 'n':
                return answer
            else:
                print(f'\n{Fore.RED}ERROR: {Fore.WHITE}la opción ingresada no es valida.')
                input('\nPresione intro para seguir...')
            
if __name__ == '__main__':
    main()