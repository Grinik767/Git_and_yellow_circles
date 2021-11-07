import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(526, 366)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Нарисовать")


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
                self.qp.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
                self.qp.drawEllipse(*coords, h, h)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw()
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
