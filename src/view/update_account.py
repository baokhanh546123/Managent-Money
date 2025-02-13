from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
import view.image
import view.image1

class Ui_Form(object):
    def __init__(self,iduser = None):
        super().__init__()
        self.iduser = iduser

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 318)

        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 50, 300, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)  # Make the QLineEdit read-only
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)  # Make the QLineEdit read-only
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)  # Make the QLineEdit read-only
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)  # Make the QLineEdit read-only
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 240, 321, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.update_account)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.delete_account)
        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(370, 50, 101, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        
        self.formLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()

        self.infomation()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Phone", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Update", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Change", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Change", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Change", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Change", None))

    def infomation(self):
        try:
            data = mysql.connector.connect(
                host="localhost",
                user="root",  # Corrected from 'username' to 'user'
                password="10112005",
                database="chat_app"
            )
            cursor = data.cursor()
            cursor.execute("SELECT username, phone, address, password FROM users WHERE iduser = %s", (self.iduser,))
            print(self.iduser)
            result = cursor.fetchone()  # Fetch one result

            if result:
                print(f"Result: {result}")  # Debugging print statement
                self.lineEdit.setText(result[0])
                self.lineEdit_2.setText(result[1])
                self.lineEdit_3.setText(result[2])
                self.lineEdit_4.setText(result[3])
            else:
                print("No user found")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if data and data.is_connected():
                data.close()

    def delete_account(self):
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("DELETE FROM users WHERE iduser = %s", (self.iduser,))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been deleted")
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
    
    def update_account(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()

        if self.lineEdit.setReadOnly(True) and self.lineEdit_2.setReadOnly(True) and self.lineEdit_3.setReadOnly(True) and self.lineEdit_4.setReadOnly(True):
            self.lineEdit.setReadOnly(False)
            self.lineEdit_2.setReadOnly(False)
            self.lineEdit_3.setReadOnly(False)
            self.lineEdit_4.setReadOnly(False)
        else:
            self.lineEdit.setReadOnly(True)
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit_3.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("UPDATE users SET username = %s, password = %s, address = %s, phone = %s WHERE iduser = %s", (username, password, address, phone, self.iduser))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been updated")
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())