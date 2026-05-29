from PyQt.QtWidgets import *
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
    self.emtrada.setPlaceholderText("Buscar videojuegos o consola")
    layout.addWidget(self.entrada)
    
    b_buscar = QPushButton("Buscar")
    b_buscar.clicked.connect(self.realizar_busqueda)
    layout.addWidget(b_buscar)
    
    b_estadisticas = QPushButton("Estadísticas")
    b_estadisticas.clicked.connect(self.mostrar_estadisticas)
    layout.addWidget(b_estadisticas)
    
    b_filtrar = QPushButton("Filtrar")
    b_filtrar.clicked.connect(self.realizar_filtro)
    layout.addWidget(b_filtrar)

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

    
