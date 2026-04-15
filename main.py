archivo = open("videojuegos50registros.csv", "r", encoding="utf-8")
print("Archivo abierto correctamente\n")

for i in range(5):
    print(archivo.readline())

archivo.close()
