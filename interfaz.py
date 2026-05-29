from PyQt5.QtWidgets import *
from analisis import *
from archivos import *

import pandas as pd
import matplotlib.pyplot as plt

class ventana(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("PLAY ANALYTICS")
    self.resize(700, 500)
    self.datos = cargar_datos()
    self.crear_interfaz()
  
  def crear_interfaz(self):
    layout = QVBoxLayout()
    tit = QLabel("PLAY ANALYTICS")
    layout.addWidget(tit)
    
    self.entrada = QLineEdit()
    self.entrada.setPlaceholderText("Buscar videojuegos o consola")
    layout.addWidget(self.entrada)
    #Botones 
    
    b_buscar = QPushButton("Buscar")
    b_buscar.clicked.connect(self.realizar_busqueda)
    layout.addWidget(b_buscar)
    
    b_estadisticas = QPushButton("Estadísticas")
    b_estadisticas.clicked.connect(self.mostrar_estadisticas)
    layout.addWidget(b_estadisticas)
    
    b_filtrar = QPushButton("Filtrar")
    b_filtrar.clicked.connect(self.realizar_filtro)
    layout.addWidget(b_filtrar)

    b_historial = QPushButton("Ver historial")
    b_historial.clicked.connect(self.mostrar_historial)
    layout.addWidget(b_historial)

    b_comparar = QPushButton("Comparar plataformas")
    b_comparar.clicked.connect(self.comparar_plataformas)
    layout.addWidget(b_comparar)

    b_grafico = QPushButton("Mostrar gráfico")
    b_grafico.clicked.connect(self.mostrar_grafico)
    layout.addWidget(b_grafico)

    b_salir = QPushButton("Salir")
    b_salir.clicked.connect(self.close)
    layout.addWidget(b_salir)

    self.resultados_txt = QTextEdit()
    self.resultados_txt.setReadOnly(True)
    layout.addWidget(self.resultados_txt)    

    self.setLayout(layout)

  def realizar_busqueda(self):
        termino = self.entrada.text().strip()
        if not termino:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa un término de búsqueda.")
            return
            
        resultados = buscar(self.datos, termino)
        guardar_hist(termino, len(resultados))
        

        self.resultados_txt.clear()
        self.resultados_txt.append(f"--- RESULTADOS DE BÚSQUEDA PARA '{termino}' ({len(resultados)} encontrados) ---\n")
        
        for fila in resultados:
            nombre = fila[0][:38] + "..." if len(fila[0]) > 38 else fila[0]
            self.resultados_txt.append(f"Juego: {nombre:<42} | Plataforma: {fila[1]:<6} | Ventas: {fila[6]}")

  def mostrar_estadisticas(self):
        total = len(self.datos)
        suma = 0
        cantidad = 0

        for fila in self.datos:
            try:
                suma += float(fila[6])
                cantidad += 1
            except:
                continue

        promedio = suma / cantidad

        self.resultados_txt.clear()
        self.resultados_txt.append("ESTADÍSTICAS\n")
        self.resultados_txt.append(f"Total videojuegos: {total}")
        self.resultados_txt.append(f"Ventas totales: {round(suma,2)} millones")
        self.resultados_txt.append(f"Promedio ventas: {round(promedio,2)} millones")

        guardar_hist("estadisticas", 1)



  def realizar_filtro(self):

        plataforma = self.entrada.text().strip()
        if not plataforma:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Ingrese una plataforma"
            )
            return

        resultados = []

        self.resultados_txt.clear()
        for fila in self.datos:
            try:
                if plataforma.lower() in fila[1].lower():
                    resultados.append(fila)
                    self.resultados_txt.append(
                        f"Juego: {fila[0]} | Plataforma: {fila[1]} | Ventas: {fila[6]}"
                    )

            except:
                continue
        self.resultados_txt.append(
            f"\nTotal encontrados: {len(resultados)}"
        )
        guardar_hist("filtro", len(resultados))



  def mostrar_historial(self):

        self.resultados_txt.clear()
        try:
            archivo = open("historial.csv", "r", encoding="utf-8")
            for linea in archivo:
                self.resultados_txt.append(linea)
            archivo.close()
        except:
            self.resultados_txt.append("No hay historial")



  def comparar_plataformas(self):

        texto = self.entrada.text().strip()
        if "," not in texto:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Ingrese dos plataformas separadas por coma.\nEjemplo: PS3,PS4"
            )
            return

        p1, p2 = texto.split(",")

        suma1 = 0
        suma2 = 0

        c1 = 0
        c2 = 0

        for fila in self.datos:
            try:
                plataforma = fila[1]
                ventas = float(fila[6])
                if p1.lower().strip() == plataforma.lower():
                    suma1 += ventas
                    c1 += 1
                if p2.lower().strip() == plataforma.lower():
                    suma2 += ventas
                    c2 += 1
            except:
                continue

        self.resultados_txt.clear()
        self.resultados_txt.append("COMPARACIÓN\n")
        if c1 > 0:
            self.resultados_txt.append(
                f"{p1} -> Juegos: {c1} | Promedio ventas: {round(suma1/c1,2)}"
            )
        if c2 > 0:
            self.resultados_txt.append(
                f"{p2} -> Juegos: {c2} | Promedio ventas: {round(suma2/c2,2)}"
            )


  def mostrar_grafico(self):

        plataformas = {}
        
        for fila in self.datos:
            try:
                plataforma = fila[1]
                if plataforma in plataformas:
                    plataformas[plataforma] += 1
                else:
                    plataformas[plataforma] = 1
            except:
                continue
        nombres = list(plataformas.keys())[:10]
        cantidades = list(plataformas.values())[:10]
        plt.figure(figsize=(10,5))
        plt.bar(nombres, cantidades)
        plt.title("Cantidad de videojuegos por plataforma")
        plt.xlabel("Plataformas")
        plt.ylabel("Cantidad")
        plt.show()
