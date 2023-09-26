import sys
import PyQt6 as Qt
import design
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QDoubleValidator
from math import cos, sin, tan, pi

class App(design.Ui_Form, Qt.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxA.setValidator(QDoubleValidator())
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.buttonClose.clicked.connect(self.closeHandler)

    def resultHandler(self):
        if self.boxA.text() == '':
            QMessageBox.about(self, "Неверные данные", "Неверные данные")
            return
        a = float(self.boxA.text().replace(',', '.'))
        depth = self.boxComma.value()
        res1 = (sin(4*a))/(1+cos(4*a)) * (cos(2*a))/(1+cos(2*a)) 
        res2 = 1/tan(3/2*pi - a)
        QMessageBox.about(self, "Result", ("Z1: " + ("{0:." + str(depth) +"f}").format(res1))+"\n"+("Z2: " +("{0:." + str(depth) +"f}").format(res2)))


    def clearHandler(self):
        self.boxA.clear()
        self.boxComma.setValue(2)

    def closeHandler(self):
        QCoreApplication.quit()

    
def main():
    app = Qt.QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()