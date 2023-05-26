from scanner import Scanner

def main():
    s = Scanner('not true or false')
    tokens = s.scanAll()
    print(tokens)

if __name__ == '__main__':
    main()