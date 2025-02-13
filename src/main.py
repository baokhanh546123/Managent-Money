from view.loginUi1 import Ui_Form as login
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
