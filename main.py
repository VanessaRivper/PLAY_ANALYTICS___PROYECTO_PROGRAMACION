with open("videojuegos50registros.cvs", "r", encoding = "utf-8") as datos
for linea in datos:
             datos = linea.split(",")
             print(datos)
