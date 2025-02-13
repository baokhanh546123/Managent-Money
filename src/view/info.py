from PyQt5 import QtCore, QtGui, QtWidgets
import view.image
import view.image1
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
import sys 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

class Ui_Form(object):
        def __init__(self , iduser  , parent_window = None  ):
                super().__init__()
                self.iduser = iduser
                self.parent_window = parent_window
                self.currentName = None 
                self.key = b'\x1ac\x11jL\n\xf5\xde\xa2a\x94\x88\xa9Jv\xb0' 
                self.iv = b'\xbf\xc1\xb4u\xe2w\x8c6\x84[\xab[\xee\xf9\xec\xc4'  

        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(510, 333)

                self.formLayoutWidget = QtWidgets.QWidget(Form)
                self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 331, 204))
                self.formLayoutWidget.setObjectName("formLayoutWidget")
                
                self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
                self.formLayout.setObjectName(u"formLayout")
                self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
                self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
                self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
                self.formLayout.setContentsMargins(0, 10, 0, 10)
                self.formLayout.setVerticalSpacing(20)
                
                self.formLayout.setObjectName("formLayout")
                self.label = QtWidgets.QLabel(self.formLayoutWidget)
                self.label.setStyleSheet("color: rgb(214, 214, 214);")
                self.label.setObjectName("label")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
                
                self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit.setReadOnly(True)

                self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
                self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_4.setStyleSheet("color: rgb(214, 214, 214);")
                self.label_4.setObjectName("label_4")
                
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_2.setReadOnly(True)
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
                
                self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_3.setStyleSheet("color: rgb(214, 214, 214);")
                self.label_3.setObjectName("label_3")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
                
                self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setReadOnly(True)
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
                
                self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_2.setStyleSheet("color: rgb(214, 214, 214);")
                self.label_2.setObjectName("label_2")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
                
                self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.lineEdit_4.setReadOnly(True)
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
                
                self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 270, 321, 41))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                
                self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                self.pushButton_2.setStyleSheet("QPushButton{\n"
        "    background-color:rgb(255, 181, 249);\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:rgb(240, 71, 255)\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:rgb(255, 8, 222)\n"
        "}\n"
        "")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(self.update_account)
                self.horizontalLayout.addWidget(self.pushButton_2)
                
                self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                self.pushButton.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(255,48,48)\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color:#CD2626\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:#8B1A1A\n"
        "}\n"
        "")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(lambda:self.delete_account(Form))
                self.horizontalLayout.addWidget(self.pushButton)
                
                self.verticalLayoutWidget = QtWidgets.QWidget(Form)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 50, 82, 201))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout.setContentsMargins(0, 10, 6, 10)
                self.verticalLayout.setObjectName("verticalLayout")
                
                self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_4.setEnabled(True)
                self.pushButton_4.setStyleSheet("QPushButton{\n"
        "color: #008B8B;\n"
        "background-color : #00F5FF\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color : #00C5CD\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color : #008B8B\n"
        "}")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.clicked.connect(lambda: self.toggle_readonly("lineEdit"))
                self.verticalLayout.addWidget(self.pushButton_4)
                
                self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_6.setStyleSheet("QPushButton{\n"
        "color: #008B8B;\n"
        "background-color : #00F5FF\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color : #00C5CD\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color : #008B8B\n"
        "}")
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_6.clicked.connect(lambda: self.toggle_readonly("lineEdit_2"))
                self.verticalLayout.addWidget(self.pushButton_6)
                
                self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_5.setStyleSheet("QPushButton{\n"
        "color: #008B8B;\n"
        "background-color : #00F5FF\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color : #00C5CD\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color : #008B8B\n"
        "}")
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_5.clicked.connect(lambda: self.toggle_readonly("lineEdit_3"))
                self.verticalLayout.addWidget(self.pushButton_5)
                
                self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_3.setStyleSheet("QPushButton{\n"
        "color: #008B8B;\n"
        "background-color : #00F5FF\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color : #00C5CD\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color : #008B8B\n"
        "}")
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(lambda: self.toggle_readonly("lineEdit_4"))
                self.verticalLayout.addWidget(self.pushButton_3)
                
                self.label_5 = QtWidgets.QLabel(Form)
                self.label_5.setGeometry(QtCore.QRect(0, 0, 541, 481))
                self.label_5.setStyleSheet("background-image: url(:/newPrefix/1326636.jpg)")
                self.label_5.setText("")
                self.label_5.setObjectName("label_5")
                
                self.label_5.raise_()
                self.formLayoutWidget.raise_()
                self.horizontalLayoutWidget.raise_()
                self.verticalLayoutWidget.raise_()

                self.toggle_state = {
                        "lineEdit": False,
                        "lineEdit_2": False,
                        "lineEdit_3": False,
                        "lineEdit_4": False
                }
                self.infomation()

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)
        #lay du lieu
        def infomation(self):
                try:
                        data = mysql.connector.connect(
                                host="localhost",
                                user="root", 
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
                                self.lineEdit_4.setText(self.decrypt(result[3]))
                        else:
                                print("No user found")

                except mysql.connector.Error as e:
                        print(f"Database Error: {e}")
                finally:
                        if cursor:
                                cursor.close()
                        if data and data.is_connected():
                                data.close()

        def toggle_readonly(self, line_edit_name):
                line_edit = getattr(self, line_edit_name)
                current_state = self.toggle_state[line_edit_name]
                line_edit.setReadOnly(current_state)
                self.toggle_state[line_edit_name] = not current_state

        def set_current_name(self , currentName):
                self.currentName = currentName

        def encrypt(self, plain_text):
                padder = padding.PKCS7(128).padder()
                padded_data = padder.update(plain_text.encode()) + padder.finalize()
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
                encryptor = cipher.encryptor()

                encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
                return base64.b64encode(encrypted_data).decode()

        def decrypt(self,encrypted_text):
    
                encrypted_data = base64.b64decode(encrypted_text)
        
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
                decryptor = cipher.decryptor()

                decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

                unpadder = padding.PKCS7(128).unpadder()
                original_data = unpadder.update(decrypted_data) + unpadder.finalize()

                return original_data.decode()
        
        def update_account(self):
                username = self.lineEdit.text()
                phone = self.lineEdit_2.text()
                address = self.lineEdit_3.text()
                password = self.lineEdit_4.text()

                hashed_password = self.encrypt(password)
                special_characters = ["@", "#", "$", "%", "!", "*", "&"]

                if self.check_user_exist("username",username):
                        QtWidgets.QMessageBox.warning(None, "Warning", "Username have already exits")
                        return False 
                elif len(phone) != 10:
                        QtWidgets.QMessageBox.warning(None, "Warning", "Phone number must be 10 digits")
                        return False 
                elif self.check_user_exist("phone" , phone):
                        QtWidgets.QMessageBox.warning(None, "Warning", "Phone number have already exits")
                        return False 
                elif not address : 
                        QMessageBox.warning(None , "Error" , "Please no address in form ")
                        return False 
                elif not len(password) != 10 and not any(char in special_characters for char in password):
                        QMessageBox.warning(None , "Error" , "Password do not suitable")
                        return False 
                else :

                        try:
                                data = mysql.connector.connect(
                                        host="localhost",
                                        user="root",  # Corrected from 'username' to 'user'
                                        password="10112005",
                                        database="chat_app"
                                )
                                cursor = data.cursor()
                                cursor.execute("UPDATE users SET username = %s, phone = %s, address = %s, password = %s WHERE iduser = %s",
                                                (username, phone, address, hashed_password, self.iduser))
                                data.commit()
                                QtWidgets.QMessageBox.about(None, "Success", "Account updated")
                        except Exception as e:
                                QtWidgets.QMessageBox.about(None, "Error", f"Error: {e}")
                        except mysql.connector.Error as e:
                                QtWidgets.QMessageBox.about(None, "Error", f"Database error: {e}")
                        finally:
                                if cursor:
                                        cursor.close()
                                if data and data.is_connected():
                                        data.close()

        def connect_db(self):
                return mysql.connector.connect(host='localhost', user='root', password='10112005', database='chat_app')

        def check_user_exist(self, field, value):
                query = f"SELECT {field} FROM users WHERE {field} = %s LIMIT 1"
                with self.connect_db() as data:
                        with data.cursor() as cursor:
                                cursor.execute(query, (value,))
                                return cursor.fetchone() is not None
        
        def delete_account(self,currentPage):
                try:
                        data = mysql.connector.connect(
                                host="localhost",
                                username = "root",
                                password = "10112005",
                                database = "chat_app"
                        )
                        cursor = data.cursor()
                        cursor.execute("DELETE FROM stoge_data where iduser = %s",(self.iduser,))
                        cursor.execute("DELETE FROM needs where iduser = %s", (self.iduser,))
                        cursor.execute("DELETE FROM wants where iduser = %s", (self.iduser,))
                        cursor.execute("DELETE FROM savings where iduser = %s", (self.iduser,))
                        cursor.execute("DELETE FROM users WHERE iduser = %s",(self.iduser,))
                        data.commit()
                        QMessageBox.about(None,"Success","Account deleted")
                        self.login(currentPage)
                except Exception as e:
                        QMessageBox.warning(None,"Error",f"Error: {e}")
                except mysql.connector.Error as e:
                        QMessageBox.warning(None,"Error",f"Database error: {e}")
                finally:
                        if cursor:
                               cursor.close()
                        if data and data.is_connected():
                               data.close()
                
        def login(self,currentPage):
                from loginUi1 import Ui_Form as LoginUi
                self.window = QtWidgets.QWidget()
                self.ui = LoginUi()
                self.ui.setupUi(self.window)
                self.window.show()
                currentPage.close()
                if self.parent_window:
                        self.parent_window.close()

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label.setText(_translate("Form", "Username"))
                self.lineEdit.setPlaceholderText(_translate("Form", "username"))
                self.label_4.setText(_translate("Form", "Phone"))
                self.lineEdit_2.setPlaceholderText(_translate("Form", "phone"))
                self.label_3.setText(_translate("Form", "Address"))
                self.lineEdit_3.setPlaceholderText(_translate("Form", "address"))
                self.label_2.setText(_translate("Form", "Password"))
                self.lineEdit_4.setPlaceholderText(_translate("Form", "password"))
                self.pushButton_2.setText(_translate("Form", "Update"))
                self.pushButton.setText(_translate("Form", "Delete"))
                self.pushButton_4.setText(_translate("Form", "Change"))
                self.pushButton_6.setText(_translate("Form", "Change"))
                self.pushButton_5.setText(_translate("Form", "Change"))
                self.pushButton_3.setText(_translate("Form", "Change"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(iduser=1)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())