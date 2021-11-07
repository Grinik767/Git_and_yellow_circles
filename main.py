import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.run)
        self.status = None

    def run(self):
        self.status = True
        self.update()

    def draw(self):
        if self.status:
            for _ in range(randrange(2, 11)):
                h = randrange(20, 100)
                coords = [randrange(60, 400), randrange(60, 250)]
                self.qp.drawEllipse(*coords, h, h)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.qp.setBrush(QColor(255, 255, 0))
        self.draw()
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
