# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(523, 378)
        Form.setMinimumSize(QSize(523, 378))
        Form.setMaximumSize(QSize(523, 378))
        self.formula1 = QLabel(Form)
        self.formula1.setObjectName(u"formula1")
        self.formula1.setGeometry(QRect(10, 10, 351, 71))
        self.formula1.setPixmap(QPixmap(u"assets/Z1.png"))
        self.formula1.setScaledContents(True)
        self.formula2 = QLabel(Form)
        self.formula2.setObjectName(u"formula2")
        self.formula2.setGeometry(QRect(10, 90, 181, 51))
        self.formula2.setPixmap(QPixmap(u"/assets/Z2.png"))
        self.formula2.setScaledContents(True)
        self.boxA = QTextEdit(Form)
        self.boxA.setObjectName(u"boxA")
        self.boxA.setGeometry(QRect(40, 200, 231, 21))
        self.labelA = QLabel(Form)
        self.labelA.setObjectName(u"labelA")
        self.labelA.setGeometry(QRect(20, 200, 16, 16))
        font = QFont()
        font.setPointSize(12)
        self.labelA.setFont(font)
        self.labelComma = QLabel(Form)
        self.labelComma.setObjectName(u"labelComma")
        self.labelComma.setGeometry(QRect(20, 280, 141, 31))
        font1 = QFont()
        font1.setPointSize(9)
        self.labelComma.setFont(font1)
        self.labelComma.setWordWrap(True)
        self.boxComma = QSpinBox(Form)
        self.boxComma.setObjectName(u"boxComma")
        self.boxComma.setGeometry(QRect(160, 280, 61, 31))
        self.boxComma.setMinimum(2)
        self.buttonResult = QPushButton(Form)
        self.buttonResult.setObjectName(u"buttonResult")
        self.buttonResult.setGeometry(QRect(380, 190, 113, 32))
        self.buttonClear = QPushButton(Form)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setGeometry(QRect(380, 230, 113, 32))
        self.buttonClose = QPushButton(Form)
        self.buttonClose.setObjectName(u"buttonClose")
        self.buttonClose.setGeometry(QRect(380, 270, 113, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.formula1.setText("")
        self.formula2.setText("")
        self.labelA.setText(QCoreApplication.translate("Form", u"\u03b1", None))
        self.labelComma.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439", None))
        self.buttonResult.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.buttonClear.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.buttonClose.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

