import os
from os import listdir
from os.path import isfile, join
from scanner import Scanner

DIRECTORY = os.getcwd()

def main():
    
    menu()

def menu():
    
    os.system('cls')
    
    input_user = None
    
    while(True):
        os.system('cls')
        print('MENU LEXER | UTN - SINTAXIS\n')
        print('1) Ingresar por teclado.')
        print('2) Leer un archivo.')
        try:
            input_user = int(input('\n> Ingrese una opcion [1 - 2]: '))
            if(input_user == 1):
                inputUserTxt()
                break
            elif(input_user == 2):
                readFromTxt()
                break
            else:
                print('ERROR: la opcion ingresada no es valida')
                input('\nPresione intro para seguir...')
        except:
            print('ERROR: solo puede ingresar numeros.')
            input('\nPresione intro para seguir...')
        
def readFromTxt():
    
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
                print('ERROR: la opcion ingresada no es valida.')
                input('\nPresione intro para seguir...')
        except:
            print('ERROR: solo puede ingresar numeros.')
            input('\nPresione intro para seguir...')
        
        
    
    name_file = only_txt[int(input_user) - 1]
    
    file_to_read = open(f'{name_file}', 'r', encoding='UTF-8')

    s = Scanner(file_to_read.read())
    
    tokens = s.scanAll()
    
    if tokens:
        os.system('cls')
        print(f'Archivo cargado: {name_file}')
        print("\nSe encontraron los siguientes tokens: \n")
        for t in tokens:
            print(f'-> {t}')
    else:
        os.system('cls')
        print('No se hallaron tokens.')
    
     
    

def inputUserTxt():
    
    os.system('cls')
    s = Scanner(input('> Ingrese el texto: '))
    tokens = s.scanAll()
    if tokens:
        os.system('cls')
        print("\nSe encontraron los siguientes tokens: \n")
        for t in tokens:
            print(f'-> {t}')
    else:
        os.system('cls')
        print('No se hallaron tokens.')
    
    
            
if __name__ == '__main__':
    main()