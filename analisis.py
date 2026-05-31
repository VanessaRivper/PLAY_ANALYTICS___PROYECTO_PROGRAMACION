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
    return total, suma, promedio

def filtrar(datos, p):
    resultados = []
    
    for fila in datos:
        try:
            if p.lower() in fila[1].lower():
                print("Juego:", fila[0], 
                      "| Plataforma:", fila[1], 
                      "| Ventas:", fila[6])
                resultados.append(fila)
        except:
            continue

    if contador == 0:
         print(f"No se encontraron juegos para la plataforma '{p}'.")
    else:
         print(f"\nTotal encontrado: {contador} registros.")
    return resultados
    
def comparar(datos, p1, p2):
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
    return c1, suma1, c2, suma2    

def grafico_cantidad(datos):

    plataformas = {}

    for fila in datos:
        try:
            plataforma = fila[1]

            if plataforma in plataformas:
                plataformas[plataforma] += 1
            else:
                plataformas[plataforma] = 1

        except:
            continue

    plataformas_ordenadas = sorted(
        plataformas.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    nombres = [item[0] for item in plataformas_ordenadas]
    cantidades = [item[1] for item in plataformas_ordenadas]

    return nombres, cantidades


def grafico_ventas(datos):

    ventas = {}

    for fila in datos:

        try:
            plataforma = fila[1]
            venta = float(fila[6])

            if plataforma in ventas:
                ventas[plataforma] += venta
            else:
                ventas[plataforma] = venta

        except:
            continue

    ventas_ordenadas = sorted(
        ventas.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    nombres = [item[0] for item in ventas_ordenadas]
    totales = [item[1] for item in ventas_ordenadas]

    return nombres, totales


