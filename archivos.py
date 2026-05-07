import csv
from datetime import datetime


def cargar_datos():
  
  datos = []

  archivo = open("Video_Games_Sales.csv", "r", encoding = "utf-8")

  lector = csv.reader(archivo)

  next(lector)

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

def guardar_csv(nombre, datos):
  archivo = open(nombre, "w", newline = "", encoding = "utf-8")
  escritor = csv.writer(archivo)
  for fila in datos:
    escritor.writerow(fila)
  
  archivo.close()
