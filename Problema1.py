
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QLineEdit
from PyQt6.QtCore import Qt

class InterAlgebraLineal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algebra Lineal")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        self.label_Valor1 = QLabel(self)
        self.label_Valor1.setGeometry(25, 27, 40, 15)
        self.label_Valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor1.setText("Valor 1")


        self.valor1_input = QLineEdit(self)
        self.valor1_input.setGeometry(90, 25, 40, 20)

        self.label_Valor2 = QLabel(self)
        self.label_Valor2.setGeometry(25, 75, 40, 15)
        self.label_Valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor2.setText("Valor 2")


        self.valor2_input = QLineEdit(self)
        self.valor2_input.setGeometry(90, 75, 40, 20)

        self.label_Valor3 = QLabel(self)
        self.label_Valor3.setGeometry(25, 125, 40, 15)
        self.label_Valor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor3.setText("Valor 3")


        self.valor3_input = QLineEdit(self)
        self.valor3_input.setGeometry(90, 125, 40, 20)

        self.label_Valor4 = QLabel(self)
        self.label_Valor4.setGeometry(25, 175, 40, 15)
        self.label_Valor4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor4.setText("Valor 4")


        self.valor4_input = QLineEdit(self)
        self.valor4_input.setGeometry(90, 175, 40, 20)

        self.label_tipoSalida = QLabel(self)
        self.label_tipoSalida.setGeometry(5, 240, 100, 50)
        self.label_tipoSalida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tipoSalida.setText("TIPO DE SALIDA")

        self.btn_Agregar = QPushButton(self)
        self.btn_Agregar.setGeometry(90, 225, 60, 20)
        self.btn_Agregar.setText("INSERTAR")
        #border radius
        self.btn_Agregar.setStyleSheet("background-color: #1733CC; color: white;")


        self.SalidaGrafica = QLabel(self)
        self.SalidaGrafica.setGeometry(220, 20, 240, 240)
        self.SalidaGrafica.setStyleSheet("border: 1px solid black;")
        self.SalidaGrafica.setStyleSheet("background-color: #ffffff;")



def main():
    app = QApplication(sys.argv)
    player = InterAlgebraLineal()
    player.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()