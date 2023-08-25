def primo(numero):
    if numero % 2 == 0:
        print("no es primo")
        return False
    print("Su numero es primo")
    return True


def main():
    num = int(input("Ingrese un numero para saber si este es primo: "))
    primo(num)
    
    
    
if __name__ == '__main__':
    main()

