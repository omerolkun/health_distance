# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 50, 591, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 101, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 70, 67, 17))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 110, 141, 17))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 150, 67, 17))
        self.antenna_lineedit = QLineEdit(self.frame)
        self.antenna_lineedit.setObjectName(u"antenna_lineedit")
        self.antenna_lineedit.setGeometry(QRect(240, 70, 113, 25))
        self.power_lineedit = QLineEdit(self.frame)
        self.power_lineedit.setObjectName(u"power_lineedit")
        self.power_lineedit.setGeometry(QRect(240, 110, 113, 25))
        self.frequency_lineedit = QLineEdit(self.frame)
        self.frequency_lineedit.setObjectName(u"frequency_lineedit")
        self.frequency_lineedit.setGeometry(QRect(240, 150, 113, 25))
        self.calculate_button = QPushButton(self.frame)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setGeometry(QRect(50, 210, 89, 25))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 10, 171, 17))
        self.freq_unit_combobox = QComboBox(self.frame)
        self.freq_unit_combobox.setObjectName(u"freq_unit_combobox")
        self.freq_unit_combobox.setGeometry(QRect(360, 150, 71, 25))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 190, 311, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.guvenli_mesafe_value_label = QLabel(self.frame_2)
        self.guvenli_mesafe_value_label.setObjectName(u"guvenli_mesafe_value_label")
        self.guvenli_mesafe_value_label.setGeometry(QRect(150, 20, 161, 17))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 121, 17))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Anten boyutu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"(m)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EIRP                    (watt)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frekans", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Saglik Guvenlik Mesafesi", None))
        self.guvenli_mesafe_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Guvenli mesafe :", None))
    # retranslateUi

