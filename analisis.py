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
        if p.lower() in fila[1].lower():
            print("Juego:", fila[0], 
                  "| Plataforma:", fila[1], 
                  "| Ventas:", fila[6])
            
            contador += 1
            resultados.append(fila)

    if contador == 0:
         print(f"No se encontraron juegos para la plataforma '{p}'.")
    else:
         print(f"\nTotal encontrado: {contador} registros.")
    return resultados
