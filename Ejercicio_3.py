def main():
    palabra = str(input("Ingrese una palabra para saber si es palindromo: "))
    palindromo = palabra[::-1]
    print(palabra)
    print(palindromo)
    if palabra == palindromo:
        print("La palabra es un palindromo")
    else:
        print("La palabra no es palindromo")
        
if __name__ == '__main__':
    main()