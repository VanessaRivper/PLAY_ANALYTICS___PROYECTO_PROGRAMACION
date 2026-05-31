from PyQt5.QtWidgets import *
from analisis import *
from archivos import *

import matplotlib.pyplot as plt

class Ventana(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("PLAY ANALYTICS - Grupo 2")
    self.resize(700, 500)
    self.datos = cargar_datos()
    self.crear_interfaz()
    self.ultimos_resultados = []
  
  def crear_interfaz(self):
    layout = QVBoxLayout()
    tit = QLabel("PLAY ANALYTICS")
    layout.addWidget(tit)
    
    self.entrada = QLineEdit()
    self.entrada.setPlaceholderText("Buscar videojuegos o consola")
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

    b_comparar = QPushButton("Comparar plataformas")
    b_comparar.clicked.connect(self.comparar_plataformas)
    layout.addWidget(b_comparar)

    b_grafico = QPushButton("Mostrar gráfico")
    b_grafico.clicked.connect(self.mostrar_grafico)
    layout.addWidget(b_grafico)
    
    b_grafico2 = QPushButton("Gráfico de ventas")
    b_grafico2.clicked.connect(self.mostrar_grafico_ventas)
    layout.addWidget(b_grafico2)

    b_historial = QPushButton("Ver historial")
    b_historial.clicked.connect(self.mostrar_historial)
    layout.addWidget(b_historial)

    b_exportar = QPushButton("Exportar CSV")
    b_exportar.clicked.connect(self.exportar_csv)
    layout.addWidget(b_exportar)

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
        self.ultimos_resultados = resultados
        guardar_hist(termino, len(resultados))

        self.resultados_txt.clear()
        self.resultados_txt.append(f"--- RESULTADOS DE BÚSQUEDA PARA '{termino}' ({len(resultados)} encontrados) ---\n")
        
        for fila in resultados:
            nombre = fila[0][:38] + "..." if len(fila[0]) > 38 else fila[0]
            self.resultados_txt.append(f"Juego: {nombre:<42} | Plataforma: {fila[1]:<6} | Ventas: {fila[6]}")

  def mostrar_estadisticas(self):
    total, suma, promedio = estadisticas(self.datos)
    
    self.resultados_txt.clear()
    self.resultados_txt.append("ESTADÍSTICAS\n")
    self.resultados_txt.append(f"Total videojuegos: {total}")
    self.resultados_txt.append(f"Ventas totales: {round(suma,2)} millones")
    self.resultados_txt.append(f"Promedio ventas: {round(promedio,2)} millones")
    guardar_hist("estadisticas", 1)

  def realizar_filtro(self):
    plataforma = self.entrada.text().strip()
    if not plataforma:
      QMessageBox.warning(self, 
                          "Advertencia", 
                          "Ingrese una plataforma"
                         )
      return
    resultados = filtrar_plataforma(self.datos, plataforma)
    self.resultados_txt.clear()

    for fila in resultados:
      self.resultados_txt.append(f"Juego: {fila[0]} | Plataforma: {fila[1]} | Ventas: {fila[6]}")
      
    self.resultados_txt.append(f"\nTotal encontrados: {len(resultados)}")
    self.ultimos_resultados = resultados
    guardar_hist("filtro", len(resultados))

  def comparar_plataformas(self):
    texto = self.entrada.text().strip()
    if "," not in texto:
      QMessageBox.warning(self,
                          "Advertencia",
                          "Ingrese dos plataformas separadas por coma.\nEjemplo: PS3,PS4"
      )
      return
            
    partes = texto.split(",")
    p1 = partes[0].strip().lower()
    p2 = partes[1].strip().lower()    

    c1, suma1, c2, suma2 =  comparar(self.datos,p1,p2)

    self.resultados_txt.clear()
    self.resultados_txt.append("COMPARACIÓN\n")
    if c1 > 0:
      self.resultados_txt.append(f"{p1.upper()} -> Juegos: {c1} | Promedio ventas: {round(suma1/c1,2)}")
    else:
      self.resultados_txt.append(f"{p1.upper()} -> No se encontraron registros.")
              
    if c2 > 0:
      self.resultados_txt.append(f"{p2.upper()} -> Juegos: {c2} | Promedio ventas: {round(suma2/c2,2)}")
    else:
      self.resultados_txt.append(f"{p2.upper()} -> No se encontraron registros.")


  def mostrar_grafico(self):
    nombres, cantidades = grafico_cantidad(self.datos)
    
    plt.figure(figsize=(10,5))
    plt.bar(nombres, cantidades, color ='#A9DFBF')
    plt.title("Cantidad de videojuegos por plataforma")
    plt.xlabel("Plataformas")
    plt.ylabel("Cantidad de titulos")
    plt.show()
    
  def mostrar_grafico_ventas(self):
    nombres, totales = grafico_ventas(self.datos) 

    plt.figure(figsize=(10,5))
    plt.plot(nombres, totales, marker="o")
    plt.title("Ventas totales por plataforma")
    plt.xlabel("Plataformas")
    plt.ylabel("Ventas")
    plt.show()

  def mostrar_historial(self):

    self.resultados_txt.clear()

    try:
        archivo = open("historial.csv", "r", encoding="utf-8")
        self.resultados_txt.append("HISTORIAL\n")
        for linea in archivo:
            self.resultados_txt.append(linea.strip())
        archivo.close()
    except:
        self.resultados_txt.append("No hay historial guardado")

  def exportar_csv(self):
    try:
        guardar_csv("Resultados.csv", self.ultimos_resultados)
        QMessageBox.information(self,
            "Éxito",
            "Resultados exportados correctamente")
    except:
        QMessageBox.warning(self,
            "Error",
            "No hay resultados para exportar")
