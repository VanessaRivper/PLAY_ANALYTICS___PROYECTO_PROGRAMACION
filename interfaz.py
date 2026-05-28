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

    
