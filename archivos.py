import csv
from datetime import datetime


def cargar_datos():
  
  datos = []

archivo = open("Video_Games_Sales.csv", "r", endcoding = "utf-8")

lee = csv.reader(archivo)

next(lextor)

for fila in lector:
  datos.append(fila)
  
archivo.close()
return datos

def guardar_hist(consulta, cantidad):
  archivo = open("historial.csv", "a", newline = "", encoding = "utf-8")

escritor = csv.writer(archivo)

fecha = datetime. now()

escritor.writerow([fecha, consulta, cantidad])

archivo.close()
