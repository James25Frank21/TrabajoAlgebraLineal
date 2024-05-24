
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QLineEdit
from PyQt6.QtCore import Qt

class InterAlgebraLineal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algebra Lineal")
        self.setGeometry(200,40, 980, 700)
        self.init_ui()

    def init_ui(self):
        self.label_Valor1 = QLabel(self)
        self.label_Valor1.setGeometry(180, 27, 40, 15)
        self.label_Valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor1.setText("Valor 1")


        self.valor1_input = QLineEdit(self)
        self.valor1_input.setGeometry(240, 25, 40, 20)

        self.label_Valor2 = QLabel(self)
        self.label_Valor2.setGeometry(180, 75, 40, 15)
        self.label_Valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor2.setText("Valor 2")


        self.valor2_input = QLineEdit(self)
        self.valor2_input.setGeometry(240, 75, 40, 20)

        self.label_Valor3 = QLabel(self)
        self.label_Valor3.setGeometry(180, 125, 40, 15)
        self.label_Valor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor3.setText("Valor 3")


        self.valor3_input = QLineEdit(self)
        self.valor3_input.setGeometry(240, 125, 40, 20)

        self.label_Valor4 = QLabel(self)
        self.label_Valor4.setGeometry(180, 175, 40, 15)
        self.label_Valor4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor4.setText("Valor 4")


        self.valor4_input = QLineEdit(self)
        self.valor4_input.setGeometry(240, 175, 40, 20)

        self.label_tipoSalida = QLabel(self)
        self.label_tipoSalida.setGeometry(15, 240, 100, 50)
        self.label_tipoSalida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tipoSalida.setText("TIPO DE SALIDA")

        self.btn_Agregar = QPushButton(self)
        self.btn_Agregar.setGeometry(180, 225, 60, 20)
        self.btn_Agregar.setText("INSERTAR")
        #border radius
        self.btn_Agregar.setStyleSheet("background-color: #1733CC; color: white;")


        self.SalidaGrafica = QLabel(self)
        self.SalidaGrafica.setGeometry(360, 10, 280, 280)
        self.SalidaGrafica.setStyleSheet("border: 1px solid black;")
        self.SalidaGrafica.setStyleSheet("background-color: #ffffff;")


        self.linea = QLabel(self)
        self.linea.setGeometry(20, 300, 930, 1)
        self.linea.setStyleSheet("background-color: red;")

    #==============================================================================
        self.label_reflex = QLabel(self)
        self.label_reflex.setGeometry(90, 320, 100, 50)
        self.label_reflex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_reflex.setText("REFLEXIÓN")

        self.SalidaReflexion = QLabel(self)
        self.SalidaReflexion.setGeometry(20, 370, 280, 280)
        self.SalidaReflexion.setStyleSheet("border: 1px solid black;")
        self.SalidaReflexion.setStyleSheet("background-color: #ffffff;")

        self.SalidaRotacion = QLabel(self)
        self.SalidaRotacion.setGeometry(340, 370,280, 280)
        self.SalidaRotacion.setStyleSheet("border: 1px solid black;")
        self.SalidaRotacion.setStyleSheet("background-color: #ffffff;")

        self.label_Rotacion = QLabel(self)
        self.label_Rotacion.setGeometry(420, 320, 100, 50)
        self.label_Rotacion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Rotacion.setText("ROTACIÓN")

        self.SalidaEjeX = QLabel(self)
        self.SalidaEjeX.setGeometry(680, 370, 280, 280)
        self.SalidaEjeX.setStyleSheet("border: 1px solid black;")
        self.SalidaEjeX.setStyleSheet("background-color: #ffffff;")

        self.label_EjeX = QLabel(self)
        self.label_EjeX.setGeometry(720, 320, 180, 50)
        self.label_EjeX.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_EjeX.setText("CORTE EN LA DIRECCIÓN EJE X")

def main():
    app = QApplication(sys.argv)
    player = InterAlgebraLineal()
    player.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()