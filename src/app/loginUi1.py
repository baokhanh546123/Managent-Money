from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
import mysql.connector
import image
import image1
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from signup import Ui_Form as SignUp
import base64

class Ui_Form(object):
        def __init__(self):
                self.key = b'\x1ac\x11jL\n\xf5\xde\xa2a\x94\x88\xa9Jv\xb0' 
                self.iv = b'\xbf\xc1\xb4u\xe2w\x8c6\x84[\xab[\xee\xf9\xec\xc4'  

        def setupUi(self, Form):
                self.Form = Form
                self.Form.setObjectName("Form")
                self.Form.resize(787, 477)
                self.Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                self.Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

                self.widget = QtWidgets.QWidget(self.Form)
                self.widget.setGeometry(QtCore.QRect(20, 20, 590, 420))
                self.widget.setStyleSheet("QPushButton#pushButton{\n"
        "    background-color:rgba(85, 98, 112, 255);\n"
        "    color:rgba(255, 255, 255, 200);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#pushButton:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(255, 107, 107, 255);\n"
        "    background-position:calc(100% - 10px)center;\n"
        "}\n"
        "QPushButton#pushButton:hover{\n"
        "    background-color:rgba(255, 107, 107, 255);\n"
        "}")
                self.widget.setObjectName("widget")
                
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
                self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "border-radius:10px;")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")

                self.label_3 = QtWidgets.QLabel(self.widget)
                self.label_3.setGeometry(QtCore.QRect(330, 80, 101, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color:rgba(0, 0, 0, 200);")
                self.label_3.setObjectName("label_3")

                self.lineEdit = QtWidgets.QLineEdit(self.widget)
                self.lineEdit.setGeometry(QtCore.QRect(330, 140, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:2px solid rgba(0, 0, 0, 0);\n"
        "border-bottom-color:rgba(46, 82, 101, 200);\n"
        "color:rgb(0, 0, 0);\n"
        "padding-bottom:7px;")
                self.lineEdit.setObjectName("lineEdit")

                self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
                self.lineEdit_2.setGeometry(QtCore.QRect(330, 200, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:2px solid rgba(0, 0, 0, 0);\n"
        "border-bottom-color:rgba(46, 82, 101, 200);\n"
        "color:rgb(0, 0, 0);\n"
        "padding-bottom:7px;")
                self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_2.setObjectName("lineEdit_2")

                self.pushButton = QtWidgets.QPushButton(self.widget)
                self.pushButton.setGeometry(QtCore.QRect(330, 280, 191, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                self.pushButton.setFont(font)
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.clicked_login)

                self.label_4 = QtWidgets.QLabel(self.widget)
                self.label_4.setGeometry(QtCore.QRect(320, 330, 131, 21))
                self.label_4.setStyleSheet("color:red")
                self.label_4.setObjectName("label_4")

                self.label_5 = QtWidgets.QLabel(self.widget)
                self.label_5.setGeometry(QtCore.QRect(110, 170, 131, 61))
                font = QtGui.QFont()
                font.setPointSize(22)
                font.setBold(True)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color:rgba(255, 255, 255, 220);")
                self.label_5.setObjectName("label_5")

                self.label_7 = QtWidgets.QLabel(self.widget)
                self.label_7.setGeometry(QtCore.QRect(50, 221, 251, 201))
                font = QtGui.QFont()
                font.setFamily("Mountain")
                font.setPointSize(12)

                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color:rgb(166, 255, 255);")
                self.label_7.setObjectName("label_7")

                self.label = QtWidgets.QLabel(self.widget)
                self.label.setGeometry(QtCore.QRect(290, 40, 351, 331))
                self.label.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
        "border-radius:10px;")
                self.label.setText("")
                self.label.setObjectName("label")

                self.pushButton_2 = QtWidgets.QPushButton(self.widget)
                self.pushButton_2.setGeometry(QtCore.QRect(460, 330, 91, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)

                self.pushButton_2.setFont(font)
                self.pushButton_2.setGeometry(QRect(460,330,121,40))
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(lambda:self.clicked_signup(self.Form))
                self.pushButton_2.setStyleSheet(""" 
                QPushButton{
                        background-color: #e2dfa2;
                        border-radius : 20px; 
                }
                QPushButton:hover{
                        background-color: #92aac7;
                }
                QPushButton:pressed{
                        background-color: #ed5752;
                }                
                """)

                self.pushButton_3 = QPushButton(self.widget)
                self.pushButton_3.setObjectName(u"pushButton_3")
                self.pushButton_3.setGeometry(QRect(560, 50, 21, 21))
                self.pushButton_3.setStyleSheet(u"QPushButton {\n"
        "        image: url(:/newPrefix/cross-button.png);\n"
        "        background-color: rgba(255, 255, 255, 0);\n"
        "        border: none;\n"
        "    }\n"
        "    QPushButton:hover {\n"
        "        background-color: rgba(255, 255, 255, 50);\n"
        "    }\n"
        "    QPushButton:pressed {\n"
        "        background-color: rgba(255, 255, 255, 100);\n"
        "    }")
                self.pushButton_3.clicked.connect(lambda:self.Form.close())

                self.label.raise_()
                self.label_2.raise_()
                self.label_3.raise_()
                self.lineEdit.raise_()
                self.lineEdit_2.raise_()
                self.pushButton.raise_()
                self.label_4.raise_()
                self.label_5.raise_()
                self.label_7.raise_()
                self.pushButton_2.raise_()
                self.pushButton_3.raise_()

                self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
                self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
                self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
                self.retranslateUi(self.Form)

                QtCore.QMetaObject.connectSlotsByName(self.Form)

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
                
        def clicked_login(self):
                username = self.lineEdit.text()
                password = self.lineEdit_2.text()

                hashed_password = self.encrypt(password)

                if not username or not password:
                        QtWidgets.QMessageBox.warning(None, "Error", "Please fill all fields")
                        return  

                try:
                        data = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='10112005',
                        database='chat_app'
                        )
                        cursor = data.cursor()
                        cursor.execute("SELECT iduser, username, password FROM users WHERE username = %s and password = %s", (username,hashed_password))
                        user = cursor.fetchone()

                        if user:
                                        self.current_iduser = user[0]
                                        QtWidgets.QMessageBox.information(None, "Success", "Successfully logged in")
                                        self.open_main(self.Form, self.current_iduser)
                                        return True
                        else:
                                QtWidgets.QMessageBox.warning(None, "Error", "Username or password incorrect")

                        cursor.close()
                        data.close()
                except mysql.connector.Error as error:
                        QtWidgets.QMessageBox.critical(None, "Error", f"Failed {error}")
                except Exception as e:
                        QtWidgets.QMessageBox.warning(None, "Error", f"Failed {e}")
                finally:
                        if data.is_connected():
                                cursor.close()
                                data.close()

        def clicked_signup(self,currentForm):
                from signup import Ui_Form as SignUiForm
                self.window = QtWidgets.QWidget()
                self.ui = SignUiForm()
                self.ui.setupUi(self.window)
                self.window.show()
                currentForm.close()

        def open_main(self,currentForm,user_id):
                from ex11 import Ui_Form as Main 
                self.window = QtWidgets.QWidget()
                self.ui = Main()
                self.ui.setupUi(self.window)
                self.ui.set_iduser(user_id)
                self.ui.set_user()
                self.window.show()
                currentForm.close()
        
        def Form_close():
            sys.exit(app.exec_())
            
        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label_3.setText(_translate("Form", "Log In"))
                self.lineEdit.setPlaceholderText(_translate("Form", " User Name"))
                self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
                self.pushButton.setText(_translate("Form", "L o g  I n"))
                self.label_4.setText(_translate("Form", "You dont have account ? "))
                self.label_5.setText(_translate("Form", "L O G I N "))
                self.label_7.setText(_translate("Form", ""))
                self.pushButton_2.setText(_translate("Form", "S i g n U p "))
                        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())