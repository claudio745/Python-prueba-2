def main():
    while True:
        
        print("""
        A continuacion se muestran diferentes opciones:
        1- Kilómetros a Millas
        2- Millas a Kilómetros
        3- Kilogramos a libras
        4- Libras a kilogramos
        5- Celcius a Fahrenheit
        6- Fahrenheit a Celcius
        7- Salir""")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            cant = float(input("Ingrese la cantidad de Kilómetros a convertir: "))
            total = cant * 0.621371
            print("La cantidad de Kilometros ingresada en Millas es: ", total)
        elif opcion == 2:
            cant = float(input("Ingrese la cantidad de Millas a convertir: "))
            total = cant * 1.60934
            print("La cantidad de Millas ingresada en Kilómetros es: ", total)
        elif opcion == 3:
            cant = float(input("Ingrese la cantidad de Kilogramos a convertir: "))
            total = cant * 2.20462
            print("La cantidad de Kilogramos ingresada en Libras es: ", total)
        elif opcion == 4:
            cant = float(input("Ingrese la cantidad de Libras a convertir: "))
            total = cant * 0.453592
            print("La cantidad de Libras ingresada en Kilogramos es: ", total)
        elif opcion == 5:
            cant = float(input("Ingrese la cantidad de Celcius a convertir: "))
            total = (cant * (9/5)) + 32
            print("La cantidad de Celcius ingresada en Fahrenheit es: ", total)
        elif opcion == 6:
            cant = float(input("Ingrese la cantidad de Fahrenheit a convertir: "))
            total = (cant - 32) * (5/9)
            print("La cantidad de Fahrenehit ingresada en Celcius es: ", total)
        elif opcion == 7:
            break


if __name__ == '__main__':
    main()
            