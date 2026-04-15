def cargar_datos():
    archivo = open("videojuegos50registros.csv", "r", encoding="utf-8")
    print("Archivo abierto correctamente\n")
    datos = []
for linea in archivo:
    info = linea.strip().split(",")
    datos.append(info)    
archivo.close()
#sigue crear las funciones para el menu


def buscar(datos, entrada):
    contador = 0
    for linea in datos:
        if termino.lower() in linea.lower():
            partes = linea.strip().split(",")
            try:
                nombre = partes[0]
                plataforma = partes[1]
                genero = partes[2]
                ventas = partes[6]
        
                print("Juego:", nombre, "| Plataforma:", plataforma, "| Ventas:", ventas)
                contador += 1
            except:
                continue

    print("\nSe encontraron", contador, "resultados")

    def menu():
    while True:
        print("\n1. Buscar")
        print("2. Estadísticas")
        print("3. Filtrar")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            entrada = input("Ingrese búsqueda: ")
            buscar(datos, entrada)
        elif opcion == "2":
            estadisticas(datos)
        elif opcion == "3":
            filtrar(datos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida")
        
