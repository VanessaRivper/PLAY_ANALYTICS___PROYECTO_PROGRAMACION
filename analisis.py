def buscar(datos, termino):
    contador = 0
    resultados = []
    
    for fila in datos:
        texto = ",".join(fila).lower()
        if termino.lower() in texto:
            try:
                nombre = fila[0]
                plataforma = fila[1]
                genero = fila[2]
                ventas = fila[6]
                
                print("Juego:", nombre, 
                      "| Plataforma:", plataforma, 
                      "| Ventas:", ventas)
                
                contador += 1
                resultados.append(fila)
                
            except:
                continue
                
    print("\nSe encontraron", contador, "resultados")
    
    return resultados


def estadisticas(datos):
    total = len(datos)
    suma = 0
    cantidad = 0
    plataformas = set()
    for fila in datos:
        try:
            suma += float(fila[6])
            cantidad += 1
            plataformas.add(fila[1])
        except:
            continue
            
    if cantidad > 0:
        promedio = suma / cantidad
    else:
        promedio = 0
    
    print(f"\nTotal de videojuegos: {total}")
    print(f"Ventas totales: {round(suma,2)} millones")
    print(f"Promedio de ventas: {round(promedio,2)} millones")
    print(f"Plataformas únicas: {len(plataformas)}")


def filtrar(datos):
    
    print("Consolas: PS3, PS4, PS2, X360, XOne, PC, PSP, Wii")
    
    p = input("De las anteriores consolas ingresa la quieras filtrar: ").strip()
    
    contador = 0
    resultados = []
    
    for fila in datos:
        try:
            if p.lower() in fila[1].lower():
                print("Juego:", fila[0], 
                      "| Plataforma:", fila[1], 
                      "| Ventas:", fila[6])
            
                contador += 1
                resultados.append(fila)
        except:
            continue

    if contador == 0:
         print(f"No se encontraron juegos para la plataforma '{p}'.")
    else:
         print(f"\nTotal encontrado: {contador} registros.")
    return resultados
def comparar(datos):

    p1 = input("Ingrese la primera plataforma: ")
    p2 = input("Ingrese la segunda plataforma: ")

    suma1 = 0
    suma2 = 0

    c1 = 0
    c2 = 0

    for fila in datos:

        try:

            plataforma = fila[1]
            ventas = float(fila[6])

            if p1.lower() == plataforma.lower():
                suma1 += ventas
                c1 += 1

            if p2.lower() == plataforma.lower():
                suma2 += ventas
                c2 += 1

        except:
            continue

    print("\n--- RESULTADOS ---")

    if c1 > 0:
        print(p1)
        print("Cantidad:", c1)
        print("Promedio ventas:", round(suma1 / c1, 2))

    if c2 > 0:
        print("\n" + p2)
        print("Cantidad:", c2)
        print("Promedio ventas:", round(suma2 / c2, 2))

    if c1 == 0:
        print("\nNo se encontraron juegos para", p1)

    if c2 == 0:
        print("\nNo se encontraron juegos para", p2)
