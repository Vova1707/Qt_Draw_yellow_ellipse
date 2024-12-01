import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QPointF
from PyQt6 import uic


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
        color = QColor(203, 229, 34)
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