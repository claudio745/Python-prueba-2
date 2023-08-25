def main():
    articulos = []
    coste = []
    
    while True:
        opcion = int(input("Ingrese 1 si desea añadir un articulo a la cesta, si no desea añadir nada ingrese 0: "))
        if opcion == 1:
            articulo = str(input("Ingrese un articulo de la compra: "))
            costo = int(input("Ingrese el costo del articulo: "))
            articulos.append(articulo)
            coste.append(costo)
        elif opcion == 0:
            largo = len(articulos)
            for i in range(largo):
                print("El articulo " + articulos[i] + " tiene un coste de: " + str(coste[i]))
            break
                
            
if __name__ == '__main__':
    main()
        
    