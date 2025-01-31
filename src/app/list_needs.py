from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from ex11 import Ui_Form as Main
import image1
import sys 
class Ui_Form(object):
    def __init__(self, iduser = None):
        super().__init__()
        self.iduser = iduser

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 200)

        #name of needs 
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 20))
        self.label.setObjectName("label")
        #cost
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 49, 16))
        self.label_2.setObjectName("label_2")
        #input name of needs
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 181, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 401, 201))
        self.label_3.setStyleSheet(u"background-image: url(:/newPrefix/hasd.jpg);")

        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 381, 168))

        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(10, 25, 10, 25)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color : #e6df44\n"
"")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color : #e6df44\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.pushButton_3 = QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
            "background-color:#75b1a9\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:#f0810f\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:#e6df44\n"
            "}")
        self.pushButton_3.clicked.connect(self.five)
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
            "background-color:#75b1a9\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:#f0810f\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:#e6df44\n"
            "}")
        self.pushButton_2.clicked.connect(self.two)
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
        "background-color:#75b1a9\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#f0810f\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color:#e6df44\n"
        "}")
        self.pushButton.clicked.connect(self.one)
        self.horizontalLayout_3.addWidget(self.pushButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color : #e6df44\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 180, 51, 21))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
            "border : None ;\n"
            "border-radius:20px;\n"
            "background-color:#75b1a9\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:#f0810f\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:#e6df44\n"
            "}")
        self.pushButton_4.clicked.connect(self.option)
        self.label_3.raise_()
        self.pushButton_4.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.warning(False)
        
    def check_needs(self):
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("SELECT needs FROM stoge_data WHERE iduser = %s ORDER BY times DESC", (self.iduser,))
            result = cursor.fetchone()

            if result is None : 
                QMessageBox.warning(None , "Error" , "Please caculate needs ")
                return False 
            else:
                while cursor.nextset():
                    pass 
                return True 


        except mysql.connector.Error as error : 
            QMessageBox.warning(None , "Error" , f"Failed {error}")
            return False 
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
                
    def one(self):
        name = self.lineEdit.text()
        if not self.check_needs():
            return 
        elif not name : 
            QtWidgets.QMessageBox.warning(None, "Warning", "Please fill out the form")
            return 
        
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("INSERT INTO list_needs (iduser , name_needs , cost , times) VALUES (%s, %s , %s , NOW())", (self.iduser , name , 100000))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been saved")
            self.warning(False)
            self.lineEdit.clear()
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
    
    def two(self):
        name = self.lineEdit.text()
        if not self.check_needs():
            return
        elif not name : 
            QtWidgets.QMessageBox.warning(None, "Warning", "Please fill out the form")
            return
        
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("INSERT INTO list_needs (iduser , name_needs , cost , times ) VALUES (%s, %s , %s , NOW())", (self.iduser , name , 200000))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been saved")
            self.warning(False)
            self.lineEdit.clear()
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
    
    def five(self):
        name = self.lineEdit.text()
        if not self.check_needs:
            return
        elif not name : 
            QtWidgets.QMessageBox.warning(None, "Warning", "Please fill out the form")
            return 
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("INSERT INTO list_needs (iduser , name_needs , cost , times) VALUES (%s, %s , %s,NOW())", (self.iduser , name , 500000))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been saved")
            self.warning(False)

            self.lineEdit.clear()
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
    
    def option(self):
        name = self.lineEdit.text()
        cost = self.lineEdit_2.text()

        if not self.check_needs() : 
            return 
        elif not name and not cost :
            QtWidgets.QMessageBox.warning(None, "Warning", "Please fill out the form")
            return 
        elif int(cost) < 100000:
            QMessageBox.warning(None, "Error", "Cost must be greater than 100000")
            return    
        
        try:
            data = mysql.connector.connect(
                host="localhost",
                username = "root",
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("INSERT INTO list_needs (iduser , name_needs , cost ,times) VALUES (%s, %s , %s,NOW())", (self.iduser , name , cost))
            data.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Data has been saved")
            self.warning(False)

            self.lineEdit.clear()
            self.lineEdit_2.clear()
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor :
                cursor.close()
            if data and data.is_connected():
                data.close()
        
    def warning(self,checked = False):
        try:
            data = mysql.connector.connect(
                host="localhost",
                user="root",
                password="10112005",
                database="chat_app"
            )
            cursor = data.cursor()
            cursor.execute("SELECT needs FROM stoge_data WHERE iduser = %s order by times desc ", (self.iduser,))
            needs = cursor.fetchone()
            cursor.fetchall()

            if needs:
                needs_budget = needs[0]
                cursor.execute("SELECT SUM(cost) AS Total_cost FROM list_needs WHERE iduser = %s", (self.iduser,))
                sum_needs = cursor.fetchone()
                if sum_needs and sum_needs[0] is not None:
                    total_cost = sum_needs[0]
                    if total_cost > needs_budget:
                        QMessageBox.warning(None, "Warning", f"Total cost of needs ({total_cost}) exceeds your budget ({needs_budget})")
                        QMessageBox.information(None , "Notify" , "If you continue add list , you will become bad guy")
                        
                        self.lineEdit.setReadOnly(True)
                        self.lineEdit_2.setReadOnly(True)

                        self.pushButton.setEnabled(False)
                        self.pushButton_2.setEnabled(False)
                        self.pushButton_3.setEnabled(False)
                        self.pushButton_4.setEnabled(False)
                        
                        checked = True

                    else:
                        QMessageBox.information(None, "Info", f"Total cost of needs ({total_cost}) is within your budget ({needs_budget})")
        
        except mysql.connector.Error as e:
            QMessageBox.warning(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor:
                cursor.close()
            if data and data.is_connected():
                data.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name of needs"))
        self.label_2.setText(_translate("Form", "Cost"))
        self.pushButton.setText(_translate("Form", "100000"))
        self.pushButton_2.setText(_translate("Form", "200000"))
        self.pushButton_3.setText(_translate("Form", "500000"))
        self.label_7.setText(_translate("Form", "Option"))
        self.pushButton_4.setText(_translate("Form", "Enter"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
