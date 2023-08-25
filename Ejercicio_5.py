def main():
    palabra = str(input("Ingrese la palabra que desee: "))
    letra = str(input("Ingrese la palabra que desee contar: "))
    contador = 0
    for letras in palabra:
        if letras == letra:
            contador = contador + 1
    
    print("La letra " + letra + " aparece " + str(contador) + " veces")


if __name__ == '__main__':
    main()