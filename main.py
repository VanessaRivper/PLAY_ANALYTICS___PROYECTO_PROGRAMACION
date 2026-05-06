def menu():
    datos = cargar_datos()
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
            print("¡Adiós!")
            break
        else:
            print("Opción inválida")
menu()
        
