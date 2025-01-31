from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
import image1
import image
import mysql.connector

class Ui_Form(object):
    def __init__(self , iduser = None):
        super().__init__()
        self.iduser = iduser

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(284, 191)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""QLabel{
                                    color : #FF420E;
                                }
                                """)
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 31, 31))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/th.jpg)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 261, 91))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("""QLabel{
                                        color : #FF420E;
                                        }
                                """)
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 150, 91, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    background-color: #dc3545;  /* Màu đỏ */\n"
        "    color: white;\n"
        "    font-size: 14px;\n"
        "    font-weight: bold;\n"
        "    border: 2px solid #c82333;\n"
        "    border-radius: 15px;\n"
        "    padding: 5px 10px;\n"
        "}\n"
        "\n"
        "/* Khi hover */\n"
        "QPushButton:hover {\n"
        "    background-color: #c82333;\n"
        "    border-color: #bd2130;\n"
        "}\n"
        "\n"
        "/* Khi bấm giữ */\n"
        "QPushButton:pressed {\n"
        "    background-color: #bd2130;\n"
        "    border-color: #721c24;\n"
        "}\n"
        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-20, 0, 341, 201))
        self.label_3.setStyleSheet("image: url(:/newPrefix/hinhnen.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search(self):
        list_name_wants = self.lineEdit.text()

        if not list_name_wants:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please fill out the form")
            return 
        
        try : 
            data = mysql.connector.connect(
                host = "localhost" , 
                user = "root" ,
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("""SELECT name_wants , cost  from list_wants where iduser = %s AND name_wants = %s
                           """,(self.iduser , list_name_wants,))
            result = cursor.fetchone()
            
            if result is None :
                QMessageBox.critical(None , "Error" , "No found data")
            else:
                self.label_2.setText(f"Name list : {result[0]} \n Cost : {result[1]}")
        except Exception as e : 
            QMessageBox.critical(None, "Database Error", f"Database error: {e}")
        finally:
            if cursor : 
                cursor.close()
            if data and data.is_connected():
                data.close()

    def delete(self):
        list_name_wants = self.lineEdit.text()

        if not list_name_wants:
            QMessageBox.warning(None, "Warning", "Please enter the name of the need to delete")
            return
        
        try : 
            data = mysql.connector.connect(
                host = "localhost",
                user = "root" ,
                password = "10112005",
                database = "chat_app"
            )
            cursor = data.cursor()
            cursor.execute("SELECT COUNT(*) FROM list_wants")
            check = cursor.fetchone()

            if check[0] == 0 : 
                QMessageBox.warning(None , "Error" , "You need add data")
            else:
                cursor.execute("DELETE FROM list_wants WHERE iduser = %s AND name_wants = %s",(self.iduser , list_name_wants , ))
                data.commit()
                QMessageBox.information(None , "Successfully" , "Delete data successfully")
                self.label_2.setText("")
        except Exception as e :
            QMessageBox.warning(None , "Error" , f"Failed {e}")
        finally:
            if cursor:
                cursor.close()
            if data and data.is_connected():
                data.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Search"))
        self.pushButton_2.setText(_translate("Form", "Delete"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(iduser=30)  # Example user ID and username
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())