import sys
from ui import Ui_MainWindow
from PySide2 import QtWidgets,QtGui
from health_distance import distance
from PyQt5.QtWidgets import QMessageBox
class HealthWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(HealthWindow,self).__init__()
        self.setupUi(self)

        #set the combobox values
        self.freq_unit_combobox.addItems(['Hz','kHz','MHz','GHz'])

        #validator for inputs
        number_validator = QtGui.QDoubleValidator(0,99999,2)
        number_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)

        self.antenna_lineedit.setValidator(number_validator)
        self.power_lineedit.setValidator(number_validator)
        self.frequency_lineedit.setValidator(number_validator)

        self.calculate_button.clicked.connect(self.calculate_health_distance)



    def calculate_health_distance(self):
        flip = 0
        warning_list = []
        antenna_long = (self.antenna_lineedit.text())
        power = (self.power_lineedit.text())
        frequency = ((self.frequency_lineedit.text()))
        frequency_unit = self.freq_unit_combobox.currentText()
        
        if not self.antenna_lineedit.text():
            flip = flip + 1
            warning_list.append("You have to enter antenna height")
            antenna_long = 0
        else:
            antenna_long = float(antenna_long)
        if not self.power_lineedit.text():
            flip = flip + 1 
            warning_list.append("You have to enter power value")
            power = 0
        else:
            power = float(power)

        if self.frequency_lineedit.text():
            frequency = float(frequency)
        result = distance(antenna_long, power, frequency,frequency_unit)
        if result == "error":
            flip = flip + 1 
            warning_list.append("Frequency must be in the range of 10kHz to 30GHz")
        if flip > 0:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Critical)
            warnings = ""
            for item in warning_list:
                warnings = warnings + item  + "\n"
            msg.setText(warnings)
            msg.exec_()
            return
        else:
            self.guvenli_mesafe_value_label.setText(str(result) + " m")

app = QtWidgets.QApplication(sys.argv)
window = HealthWindow()
window.show()
app.exec_()

