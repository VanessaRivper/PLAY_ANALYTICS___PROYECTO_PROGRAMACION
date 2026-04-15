archivo = open("videojuegos50registros.csv", "r", encoding="utf-8")
print("Archivo abierto correctamente\n")

datos = []

for linea in archivo:
    info = linea.strip().split(",")
    datos.append(info)
    
archivo.close()

#sigue crear las funciones para el menu 
def buscar(datos, entrada):
    resultados = []
    for fila in datos:
        if entrada.lower() in ",".join(fila).lower():
            resultados.append(fila)
    print(f"Se encontraron {len(resultados)} registros")
    for r in resultados:
        print(r)
        
def estadisticas
def filtrar
