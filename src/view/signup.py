from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import view.image
import view.image1
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import mysql.connector
class Ui_Form(object):
        def __init__(self, iduser=None):
                super().__init__()
                self.iduser = iduser
                self.key = b'\x1ac\x11jL\n\xf5\xde\xa2a\x94\x88\xa9Jv\xb0' 
                self.iv = b'\xbf\xc1\xb4u\xe2w\x8c6\x84[\xab[\xee\xf9\xec\xc4' 
        def setupUi(self, Form):
                self.Form = Form
                Form.setObjectName("Form")
                Form.resize(820, 502)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

                self.label_2 = QtWidgets.QLabel(Form)
                self.label_2.setGeometry(QtCore.QRect(360, 50, 551, 381))
                self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
                                        "border-radius:10px;")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")

                self.label = QtWidgets.QLabel(Form)
                self.label.setGeometry(QtCore.QRect(40, 30, 531, 431))
                self.label.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                        "border-radius:10px;")
                self.label.setText("")
                self.label.setObjectName("label")

                self.lineEdit_2 = QtWidgets.QLineEdit(Form)
                self.lineEdit_2.setGeometry(QtCore.QRect(83, 134, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.lineEdit_2.setObjectName("lineEdit_2")

                self.lineEdit = QtWidgets.QLineEdit(Form)
                self.lineEdit.setGeometry(QtCore.QRect(300, 134, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit.setObjectName("lineEdit")

                self.label_3 = QtWidgets.QLabel(Form)
                self.label_3.setGeometry(QtCore.QRect(83, 74, 101, 31))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color:rgba(0, 0, 0, 200);")
                self.label_3.setObjectName("label_3")

                self.label_4 = QtWidgets.QLabel(Form)
                self.label_4.setGeometry(QtCore.QRect(60, 410, 161, 21))
                self.label_4.setStyleSheet("color:red;")
                self.label_4.setObjectName("label_4")
                font_2 = QtGui.QFont()
                font_2.setPointSize(11)
                font_2.setBold(True)
                self.label_4.setFont(font_2)

                self.lineEdit_3 = QtWidgets.QLineEdit(Form)
                self.lineEdit_3.setGeometry(QtCore.QRect(80, 194, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit_3.setObjectName("lineEdit_3")

                self.lineEdit_4 = QtWidgets.QLineEdit(Form)
                self.lineEdit_4.setGeometry(QtCore.QRect(300, 194, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_4.setFont(font)
                self.lineEdit_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit_4.setObjectName("lineEdit_4")

                self.lineEdit_5 = QtWidgets.QLineEdit(Form)
                self.lineEdit_5.setGeometry(QtCore.QRect(80, 260, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_5.setFont(font)
                self.lineEdit_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_5.setObjectName("lineEdit_5")

                self.lineEdit_6 = QtWidgets.QLineEdit(Form)
                self.lineEdit_6.setGeometry(QtCore.QRect(300, 260, 190, 40))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.lineEdit_6.setFont(font)
                self.lineEdit_6.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "padding-bottom:7px;")
                self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_6.setObjectName("lineEdit_6")

                self.label_5 = QtWidgets.QLabel(Form)
                self.label_5.setGeometry(QtCore.QRect(580, 200, 181, 61))
                font = QtGui.QFont()
                font.setPointSize(22)
                font.setBold(True)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color:rgba(255, 255, 255, 220); ")
                self.label_5.setObjectName("label_5")

                self.pushButton = QtWidgets.QPushButton(Form)
                self.pushButton.setGeometry(QtCore.QRect(230, 330, 110, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("""
                QPushButton{
                        background-color: rgb(208, 255, 176);
                        border-radius : 20px ;
                }
                QPushButton:hover{
                        background-color:#4b7447;
                        border-radius : 20px ;
                }
                QPushButton:pressed{
                        background-color:#f9dc24;
                        border-radius : 20px ;
                }
                """)
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.signup_button)

                self.pushButton_2 = QtWidgets.QPushButton(Form)
                self.pushButton_2.setGeometry(QtCore.QRect(230, 400, 110, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("""
                QPushButton{
                        background-color:rgb(216, 234, 255);
                        border-radius : 20px;
                }
                        QPushButton:hover{
                        background-color: #e2dfa2;
                }
                        QPushButton:pressed{
                        background-color: #ed5752;
                }
                """)
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(lambda: self.login(Form))

                self.pushButton_3 = QPushButton(Form)
                self.pushButton_3.setObjectName(u"pushButton_3")
                self.pushButton_3.setGeometry(QRect(50, 40, 21, 21))
                self.pushButton_3.setStyleSheet(u"""
                QPushButton {
                        image: url(:/newPrefix/cross-button.png);
                        background-color: rgba(255, 255, 255, 0);
                        border: none;
                }
                QPushButton:hover {
                        background-color: rgba(255, 255, 255, 50);
                }
                QPushButton:pressed {
                        background-color: rgba(255, 255, 255, 100);
                }
                """)
                self.pushButton_3.clicked.connect(lambda: Form.close())

                self.label_6 = QtWidgets.QLabel(Form)
                self.label_6.setGeometry(QtCore.QRect(580, 300, 321, 121))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setItalic(True)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color:rgb(166, 255, 255);")
                self.label_6.setText("")
                self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_6.setIndent(2)
                self.label_6.setOpenExternalLinks(False)
                self.label_6.setObjectName("label_6")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

                self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
                self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
                self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
                self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        def encrypt(self, plain_text):
                padder = padding.PKCS7(128).padder()
                padded_data = padder.update(plain_text.encode()) + padder.finalize()
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
                encryptor = cipher.encryptor()
                encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
                return base64.b64encode(encrypted_data).decode()

        def decrypt(self, encrypted_text):
                encrypted_data = base64.b64decode(encrypted_text)
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
                unpadder = padding.PKCS7(128).unpadder()
                original_data = unpadder.update(decrypted_data) + unpadder.finalize()
                return original_data.decode()

        def connect_db(self):
                return mysql.connector.connect(host='localhost', user='root', password='10112005', database='chat_app')

        def check_user_exist(self, field, value):
                query = f"SELECT {field} FROM users WHERE {field} = %s LIMIT 1"
                with self.connect_db() as data:
                        with data.cursor() as cursor:
                                cursor.execute(query, (value,))
                                return cursor.fetchone() is not None

        def register_user(self, username, hashed_password, phone, address, fullname):
                if self.check_user_exist("username", username):
                        QMessageBox.warning(None, "Error", "Username have already exits")
                        return False
                if self.check_user_exist("phone", phone):
                        QMessageBox.warning(None, "Lỗi", "Phone have already exits!")
                        return False
                try:
                        with self.connect_db() as data:
                                with data.cursor() as cursor:
                                        cursor.execute(
                                                "INSERT INTO users (username, password, phone, address, fullname, times) VALUES (%s, %s, %s, %s, %s, NOW())",
                                                (username, hashed_password, phone, address, fullname)
                                        )
                                        data.commit()
                                        QMessageBox.information(None, "Sucess", "Succesfully!")
                                        return True
                except mysql.connector.Error as error:
                        QMessageBox.warning(None, "Error", f"Falied: {error}")
                        return False

        def signup_button(self):
                username = self.lineEdit_2.text()
                phone = self.lineEdit.text()
                address = self.lineEdit_4.text()
                fullname = self.lineEdit_3.text()
                password = self.lineEdit_5.text()
                co_password = self.lineEdit_6.text()

                hashed_password = self.encrypt(password)

                special_characters = "!@#$%^&*()-_=+"
                if not all([username, phone, address, fullname, password, co_password]):
                        QMessageBox.warning(None, "Error", "Please fill in all required fields!")
                        return False

                if len(password) < 8 or not any(char in special_characters for char in password):
                        QMessageBox.warning(None, "Error", "Password must be at least 8 characters long and contain at least one special character!")
                        return False

                if len(phone) != 10:
                        QMessageBox.warning(None, "Error", "Phone number must be exactly 10 digits!")
                        return False

                if password != co_password:
                        QMessageBox.warning(None, "Error", "Passwords do not match!")
                        return False


                if self.register_user(username, hashed_password, phone, address, fullname):
                        self.login(self.Form)

        def login(self, currentForm):
                from view.loginUi1 import Ui_Form as LoginForm
                self.login_window = QtWidgets.QWidget()
                self.ui = LoginForm()
                self.ui.setupUi(self.login_window)
                self.login_window.show()
                if currentForm:
                        currentForm.close()
        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.lineEdit_2.setPlaceholderText(_translate("Form", "Username"))
                self.lineEdit.setPlaceholderText(_translate("Form", "Phone"))
                self.label_3.setText(_translate("Form", "Sign Up"))
                self.label_4.setText(_translate("Form", "You have an account!!!"))
                self.lineEdit_3.setPlaceholderText(_translate("Form", "Fullname"))
                self.lineEdit_4.setPlaceholderText(_translate("Form", "Address"))
                self.lineEdit_5.setPlaceholderText(_translate("Form", "Password"))
                self.lineEdit_6.setPlaceholderText(_translate("Form", "Confirm Password"))
                self.label_5.setText(_translate("Form", "S I G N U P"))
                self.pushButton.setText(_translate("Form", "S i g n U p"))
                self.pushButton_2.setText(_translate("Form", "L o g i n"))

        def Form_close(self):
                sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())