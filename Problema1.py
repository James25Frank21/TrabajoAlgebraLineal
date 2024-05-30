import sys
import numpy as np
import matplotlib
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):  # clase para crear la grafica
    def __init__(self, parent=None, width=5, height=4, dpi=100):  # constructor de la clase
        fig = Figure(figsize=(width, height), dpi=dpi)  # creamos la figura
        self.axes = fig.add_subplot(111)  # agregamos un subplot a la figura
        super(MplCanvas, self).__init__(fig)  # llamamos al constructor de la clase padre


class InterAlgebraLineal(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(InterAlgebraLineal, self).__init__(*args, **kwargs)
        self.setWindowTitle("Algebra Lineal")
        self.setGeometry(75, 40, 1210, 675)
        self.setWindowIcon(QIcon("reading-book.png"))
        self.setStyleSheet("background-color: #F7F7F7;")
        self.init_ui()

    def init_ui(self):
        self.label_Valor = QLabel(self)
        self.label_Valor.setGeometry(255, 7, 60, 20)
        self.label_Valor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor.setText(" X " + "            " + "  Y ")

        self.label_Valor1 = QLabel(self)
        self.label_Valor1.setGeometry(160, 27, 60, 15)
        self.label_Valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor1.setText("Valor1 (X,Y)")

        self.valor1X_input = QLineEdit(self)
        self.valor1X_input.setGeometry(240, 25, 40, 20)

        self.valor1Y_input = QLineEdit(self)
        self.valor1Y_input.setGeometry(290, 25, 40, 20)

        self.label_Valo = QLabel(self)
        self.label_Valo.setGeometry(255, 57, 60, 20)
        self.label_Valo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valo.setText(" X " + "            " + "  Y ")

        self.label_Valor2 = QLabel(self)
        self.label_Valor2.setGeometry(160, 75, 60, 15)
        self.label_Valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor2.setText("Valor2 (X,Y)")

        self.valor2X_input = QLineEdit(self)
        self.valor2X_input.setGeometry(240, 75, 40, 20)

        self.valor2Y_input = QLineEdit(self)
        self.valor2Y_input.setGeometry(290, 75, 40, 20)

        self.label_Val = QLabel(self)
        self.label_Val.setGeometry(255, 108, 60, 20)
        self.label_Val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Val.setText(" X " + "            " + "  Y ")

        self.label_Valor3 = QLabel(self)
        self.label_Valor3.setGeometry(160, 125, 60, 15)
        self.label_Valor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor3.setText("Valor3 (X,Y)")

        self.valor3X_input = QLineEdit(self)
        self.valor3X_input.setGeometry(240, 125, 40, 20)

        self.valor3Y_input = QLineEdit(self)
        self.valor3Y_input.setGeometry(290, 125, 40, 20)

        self.label_Va = QLabel(self)
        self.label_Va.setGeometry(255, 158, 60, 20)
        self.label_Va.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Va.setText(" X " + "            " + "  Y ")

        self.label_Valor4 = QLabel(self)
        self.label_Valor4.setGeometry(160, 175, 60, 15)
        self.label_Valor4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Valor4.setText("Valor4 (X,Y)")

        self.valor4X_input = QLineEdit(self)
        self.valor4X_input.setGeometry(240, 175, 40, 20)

        self.valor4Y_input = QLineEdit(self)
        self.valor4Y_input.setGeometry(290, 175, 40, 20)

        self.label_tipoSalida = QLabel(self)
        self.label_tipoSalida.setGeometry(15, 285, 100, 50)
        self.label_tipoSalida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tipoSalida.setText("TIPO DE SALIDA")

        self.btn_Agregar = QPushButton(self)
        self.btn_Agregar.setGeometry(255, 225, 60, 20)
        self.btn_Agregar.setText("GRAFICAR")
        self.btn_Agregar.setStyleSheet("background-color: #1733CC; color: white;")
        self.btn_Agregar.clicked.connect(self.plot_graph)
        self.btn_Agregar.clicked.connect(self.plot_graphReflexion)
        self.btn_Agregar.clicked.connect(self.plot_graphDireccionEjeX)
        self.btn_Agregar.clicked.connect(self.plot_graphFigura)

        self.btn_Agregar2 = QPushButton(self)
        self.btn_Agregar2.setGeometry(100, 225, 62, 20)
        self.btn_Agregar2.setText("TRIANGULO")
        self.btn_Agregar2.setStyleSheet("background-color: #6495ED; color: black;")
        self.btn_Agregar2.clicked.connect(self.triangulo)

        self.btn_Agregar3 = QPushButton(self)
        self.btn_Agregar3.setGeometry(175, 225, 72, 20)
        self.btn_Agregar3.setText("RECTANGULO")
        self.btn_Agregar3.setStyleSheet("background-color: #6495ED; color: black;")
        self.btn_Agregar3.clicked.connect(self.rectangulo)


        self.SalidaGrafica = QWidget(self)
        self.SalidaGrafica.setGeometry(415, 10, 380, 290)
        self.SalidaGrafica.setStyleSheet("border: 1px solid black; background-color: #7FFF00;")

        layout = QVBoxLayout(self.SalidaGrafica)
        self.SalidaGrafica.setLayout(layout)

        self.linea = QLabel(self)
        self.linea.setGeometry(20, 320, 1170, 1)
        self.linea.setStyleSheet("background-color: red;")

        self.label_reflex = QLabel(self)
        self.label_reflex.setGeometry(150, 320, 100, 50)
        self.label_reflex.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_reflex.setText("REFLEXIÓN EN")

        self.btn_ReflexionX = QPushButton(self)
        self.btn_ReflexionX.setGeometry(255, 335, 20, 20)
        self.btn_ReflexionX.setText("X")
        self.btn_ReflexionX.setStyleSheet("background-color: #1733CC; color: white;")
        self.btn_ReflexionX.clicked.connect(self.plot_graphReflexion)

        self.btn_ReflexionY = QPushButton(self)
        self.btn_ReflexionY.setGeometry(290, 335, 20, 20)
        self.btn_ReflexionY.setText("Y")
        self.btn_ReflexionY.setStyleSheet("background-color: #1733CC; color: white;")
        self.btn_ReflexionY.clicked.connect(self.plot_graphReflexionY)


        self.SalidaReflexion = QWidget(self)
        self.SalidaReflexion.setGeometry(20, 370, 380, 290)
        self.SalidaReflexion.setStyleSheet("border: 1px solid black; background-color: #7FFF00;")

        layout1 = QVBoxLayout(self.SalidaReflexion)
        self.SalidaReflexion.setLayout(layout1)

        self.SalidaRotacion = QWidget(self)
        self.SalidaRotacion.setGeometry(415, 370, 380, 290)
        self.SalidaRotacion.setStyleSheet("border: 1px solid black; background-color: #7FFF00;")

        layout2 = QVBoxLayout(self.SalidaRotacion)
        self.SalidaRotacion.setLayout(layout2)

        self.labelRotacion = QLabel(self)
        self.labelRotacion.setGeometry(530, 320, 100, 50)
        self.labelRotacion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRotacion.setText("ROTACIÓN")

        # un input y boton para la rotación
        self.label_rota = QLineEdit(self)
        self.label_rota.setGeometry(630, 335, 25, 20)
        self.label_rota.setText("45°")
        #self.label_rota.mouseDoubleClickEvent(self.label_rota.setText(""))

        


        self.btn_Rotaci = QPushButton(self)
        self.btn_Rotaci.setGeometry(680, 335, 45, 20)
        self.btn_Rotaci.setText("ROTAR")
        self.btn_Rotaci.setStyleSheet("background-color: #1733CC; color: white;")
        self.btn_Rotaci.clicked.connect(self.plot_graphAngulo)

        self.SalidaEjeX = QWidget(self)
        self.SalidaEjeX.setGeometry(810, 370, 380, 290)
        self.SalidaEjeX.setStyleSheet("border: 1px solid black; background-color: #7FFF00;")

        layout3 = QVBoxLayout(self.SalidaEjeX)
        self.SalidaEjeX.setLayout(layout3)

        self.label_EjeX = QLabel(self)
        self.label_EjeX.setGeometry(920, 320, 180, 50)
        self.label_EjeX.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_EjeX.setText("CORTE EN LA DIRECCIÓN EJE X")
    def triangulo(self):
        self.valor1X_input.setText("0")
        self.valor1Y_input.setText("0")
        self.valor2X_input.setText("0")
        self.valor2Y_input.setText("0")
        self.valor3X_input.setText("1")
        self.valor3Y_input.setText("1")
        self.valor4X_input.setText("0")
        self.valor4Y_input.setText("1")

    def rectangulo(self):
        self.valor1X_input.setText("0")
        self.valor1Y_input.setText("0")
        self.valor2X_input.setText("1")
        self.valor2Y_input.setText("0")
        self.valor3X_input.setText("1")
        self.valor3Y_input.setText("1")
        self.valor4X_input.setText("0")
        self.valor4Y_input.setText("1")

    def plot_graph(self):
        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return


        def aplicacion_tr(t, p):
            p1 = np.matmul(t, p)
            return p1

        def puntoE(p):
            num = p.shape[0]
            p = p.T
            return np.vstack([p, np.ones((1, num))])

        def get_rotz(ax):
            ang = np.deg2rad(ax)
            r = np.eye(4)
            r[0, 0], r[0, 1], r[1, 0], r[1, 1] = np.cos(ang), -np.sin(ang), np.sin(ang), np.cos(ang)
            return r


        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)
        M = get_rotz(45)
        xn = puntoE(x)
        P1 = aplicacion_tr(M, xn)
        # Crear la gráfica en el widget
        sc = MplCanvas(self.SalidaRotacion, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.plot(P1[0], P1[1], 'b')
        sc.axes.axis([-1.5, 1.5, -1.5, 1.5])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')

        layout = self.SalidaRotacion.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaRotacion.setLayout(layout)


    def plot_graphAngulo(self):
        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
            angulo = float(self.label_rota.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return



        def aplicacion_tr(t, p):
            p1 = np.matmul(t, p)
            return p1

        def puntoE(p):
            num = p.shape[0]
            p = p.T
            return np.vstack([p, np.ones((1, num))])

        def get_rotz(ax):
            ang = np.deg2rad(ax)
            r = np.eye(4)
            r[0, 0], r[0, 1], r[1, 0], r[1, 1] = np.cos(ang), -np.sin(ang), np.sin(ang), np.cos(ang)
            return r


        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)
        M = get_rotz(angulo)
        xn = puntoE(x)
        P1 = aplicacion_tr(M, xn)
        # Crear la gráfica en el widget
        sc = MplCanvas(self.SalidaRotacion, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.plot(P1[0], P1[1], 'b')
        sc.axes.axis([-1.5, 1.5, -1.5, 1.5])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')

        layout = self.SalidaRotacion.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaRotacion.setLayout(layout)

    def plot_graphReflexion(self):

        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return

        def aplicacion_tr(t, p):
            p1 = np.matmul(t, p)
            return p1

        def puntoE(p):
            num = p.shape[0]
            p = p.T
            return np.vstack([p, np.ones((1, num))])

        def reflexionEn_y():
            r = np.eye(4)
            r[0, 0] = -1  # Reflexión respecto al eje Y
            return r

        def reflexionEn_x():
            r = np.eye(4)
            r[1, 1] = -1
            return r

        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)
        M = reflexionEn_x()
        xn = puntoE(x)
        P1 = aplicacion_tr(M, xn)

        # Crear la gráfica en el widget
        sc = MplCanvas(self.SalidaReflexion, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.plot(P1[0], P1[1], 'b')
        sc.axes.axis([-10, 10, -10, 10])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')

        layout = self.SalidaReflexion.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaReflexion.setLayout(layout)


    def plot_graphReflexionY(self):

        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return

        def aplicacion_tr(t, p):
            p1 = np.matmul(t, p)
            return p1

        def puntoE(p):
            num = p.shape[0]
            p = p.T
            return np.vstack([p, np.ones((1, num))])

        def reflexionEn_y():
            r = np.eye(4)
            r[0, 0] = -1  # Reflexión respecto al eje Y
            return r

        def reflexionEn_x():
            r = np.eye(4)
            r[1, 1] = -1
            return r

        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)

        M = reflexionEn_y()
        xn = puntoE(x)
        P1 = aplicacion_tr(M, xn)

        # Crear la gráfica en el widget
        sc = MplCanvas(self.SalidaReflexion, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.plot(P1[0], P1[1], 'b')
        sc.axes.axis([-10, 10, -10, 10])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')

        layout = self.SalidaReflexion.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaReflexion.setLayout(layout)

    def plot_graphDireccionEjeX(self):
        # Obtener valores de los QLineEdits
        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return

        def aplicacion_tr(t, p):
            p1 = np.matmul(t, p)
            return p1

        def puntoE(p):
            num = p.shape[0]
            p = p.T
            return np.vstack([p, np.ones((1, num))])

        def get_shear_x():
            sh = np.eye(4)
            sh[0, 1] = 1
            return sh

        # Procesar puntos de entrada y realizar corte en la dirección X
        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)
        #kt = self.label_k.text()
        M = get_shear_x()
        xn = puntoE(x)
        P1 = aplicacion_tr(M, xn)

        # Crear la gráfica en el widget para la transformación de corte en la dirección X
        sc = MplCanvas(self.SalidaEjeX, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.plot(P1[0], P1[1], 'b')
        sc.axes.axis([-10, 10, -10, 10])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')


        layout = self.SalidaEjeX.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaEjeX.setLayout(layout)

    def plot_graphFigura(self):
        try:
            a = float(self.valor1X_input.text())
            b = float(self.valor1Y_input.text())
            c = float(self.valor2X_input.text())
            d = float(self.valor2Y_input.text())
            e = float(self.valor3X_input.text())
            f = float(self.valor3Y_input.text())
            g = float(self.valor4X_input.text())
            h = float(self.valor4Y_input.text())
        except ValueError:
            print("Por favor, introduzca valores numéricos válidos.")
            return

        x = np.array([[a, b, 0], [c, d, 0], [e, f, 0], [g, h, 0], [a, b, 0]], np.float32)


        sc = MplCanvas(self.SalidaGrafica, width=5, height=4, dpi=100)
        sc.axes.plot(x[:, 0], x[:, 1], 'r')
        sc.axes.axis([-1.5, 1.5, -1.5, 1.5])
        sc.axes.grid(True)
        sc.axes.set_xlabel('X')
        sc.axes.set_ylabel('Y')

        layout = self.SalidaGrafica.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        layout.addWidget(sc)
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        self.SalidaGrafica.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    player = InterAlgebraLineal()
    player.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
