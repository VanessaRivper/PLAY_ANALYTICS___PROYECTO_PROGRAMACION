import sys
from PyQt5.QtWidgets import QApplication
from interfaz import Ventana

app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())
