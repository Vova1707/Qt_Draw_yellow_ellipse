import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QPointF
from PyQt6 import uic
from UI import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.f)

    def f(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        self.draw_ellipse(qp)


    def draw_ellipse(self, qp):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(100, 700)
        y = random.randint(100, 700)
        r = random.randint(10, 100)
        qp.setBrush(color)
        qp.drawEllipse(QPointF(x, y), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())