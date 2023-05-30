from scanner import Scanner

def main():
    s = Scanner('<article></article>')
    tokens = s.scanAll()
    print("Se encontraron los siguientes tokens:")
    for t in tokens:
        msg = f'-> {t}'
        print(msg);
if __name__ == '__main__':
    main()