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
        self.frame.setGeometry(QRect(70, 50, 591, 321))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 571, 51))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 10, 291, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 80, 571, 211))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 140, 311, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.guvenli_mesafe_value_label = QLabel(self.frame_2)
        self.guvenli_mesafe_value_label.setObjectName(u"guvenli_mesafe_value_label")
        self.guvenli_mesafe_value_label.setGeometry(QRect(150, 20, 161, 17))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 121, 17))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.calculate_button = QPushButton(self.frame_4)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setGeometry(QRect(50, 160, 89, 25))
        self.frequency_lineedit = QLineEdit(self.frame_4)
        self.frequency_lineedit.setObjectName(u"frequency_lineedit")
        self.frequency_lineedit.setGeometry(QRect(240, 100, 113, 25))
        self.freq_unit_combobox = QComboBox(self.frame_4)
        self.freq_unit_combobox.setObjectName(u"freq_unit_combobox")
        self.freq_unit_combobox.setGeometry(QRect(360, 100, 71, 25))
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 141, 20))
        self.antenna_lineedit = QLineEdit(self.frame_4)
        self.antenna_lineedit.setObjectName(u"antenna_lineedit")
        self.antenna_lineedit.setGeometry(QRect(240, 20, 113, 25))
        self.power_lineedit = QLineEdit(self.frame_4)
        self.power_lineedit.setObjectName(u"power_lineedit")
        self.power_lineedit.setGeometry(QRect(240, 60, 113, 25))
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 100, 101, 17))
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 60, 191, 17))
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 20, 31, 17))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Healthy Safety Distance", None))
        self.guvenli_mesafe_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Safety Distance", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Antenna Dimension", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EIRP                               (watt)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"(m)", None))
    # retranslateUi

