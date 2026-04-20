def cargar_datos():
    archivo = open("videojuegos50registros.csv", "r", encoding="utf-8")
    print("Archivo abierto correctamente\n")
    datos = []
    next(archivo)  
    for linea in archivo:
        info = linea.strip().split(",")
        datos.append(info)    
    archivo.close()
    return datos 
def buscar(datos, termino):
    contador = 0
    for fila in datos:
        texto = ",".join(fila).lower()
        if termino.lower() in texto:
            try:
                nombre = fila[0]
                plataforma = fila[1]
                genero = fila[2]
                ventas = fila[6]
                print("Juego:", nombre, "| Plataforma:", plataforma, "| Ventas:", ventas)
                contador += 1
            except:
                continue
    print("\nSe encontraron", contador, "resultados")
def estadisticas(datos):
    total = len(datos)
    suma = 0
    for fila in datos:
        try:
            suma += float(fila[6])
        except:
            continue
    promedio = suma / total
    print(f"\nTotal de videojuegos: {total}")
    print(f"Ventas totales: {round(suma,2)} millones")
    print(f"Promedio de ventas: {round(promedio,2)} millones")
def filtrar(datos):
     print("Consolas: PS3, PS4, PS2, X360, XOne, PC, PSP, Wii")
    p = input("De las anteriores consolas ingresa la quieras filtrar: ").strip()
    contador = 0
    for fila in datos:
        if p.lower() in fila[1].lower():
            print("Juego:", fila[0], "| Plataforma:", fila[1], "| Ventas:", fila[6])
            contador += 1
    if contador == 0:
         print(f"No se encontraron juegos para la plataforma '{p}'.")
    else:
         print(f"\nTotal encontrado: {contador} registros.")
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
        
