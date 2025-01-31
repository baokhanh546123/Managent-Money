#khao bao thu vien va file con 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import image
import mysql.connector
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime , timedelta 
import matplotlib.pyplot as plt 

class Ui_Form(object):
        def __init__(self):
                self.iduser = None 
                self.caculate_count = 0
        def setupUi(self, Form):
                self.Form = Form
                Form.setObjectName("Form")
                Form.resize(829, 598)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                
                #chuong trinh
                self.FrameContent = QtWidgets.QFrame(Form)
                self.FrameContent.setGeometry(QtCore.QRect(30, 50, 631, 381))
                self.FrameContent.setStyleSheet("background-color:rgb(244, 252, 255)\n"
        "")     
                self.frame_7 = QFrame(Form)
                self.frame_7.setObjectName("frame_7")
                self.frame_7.setGeometry(QRect(30,0,551,51))
                self.frame_7.setStyleSheet("background-color: rgb(59, 135, 234);")
                self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

                self.welcome_text = QLabel(self.frame_7)
                self.welcome_text.setObjectName("welcome_text")
                self.welcome_text.setGeometry(QRect(40, 20, 341, 21))
                font1 = QFont()
                font1.setPointSize(14)
                font1.setBold(True)
                font1.setItalic(True)
                self.welcome_text.setFont(font1)
                
                self.frame_8 = QFrame(Form)
                self.frame_8.setObjectName("frame_8")
                self.frame_8.setGeometry(QRect(580, 0, 81, 51))
                self.frame_8.setStyleSheet(u"background-color : red ; ")
                self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
                self.bn_close = QPushButton(self.frame_8)
                self.bn_close.setObjectName(u"bn_close")
                self.bn_close.setGeometry(QRect(20, 0, 41, 51))
                self.bn_close.setMaximumSize(QSize(55, 55))
                self.bn_close.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgba(0,0,0,0);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	background-color: rgb(0,143,150);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	background-color: rgba(0,0,0,0);\n"
        "}")
                icon = QIcon()
                icon.addFile(u"D:/python/PyQt5/Project2/SC_pyqt5_LoginUI2-main/closeAsset 43.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
                self.bn_close.setIcon(icon)
                self.bn_close.setIconSize(QSize(22, 22))
                self.bn_close.setFlat(True)
                self.bn_close.clicked.connect(self.close)

                self.FrameContent.setFrameShape(QFrame.Shape.StyledPanel)
                self.FrameContent.setFrameShadow(QFrame.Shadow.Raised)
                self.FrameContent.setObjectName("FrameContent")

                self.FameTooBar = QtWidgets.QFrame(self.FrameContent)
                self.FameTooBar.setGeometry(QtCore.QRect(0, 0, 121, 401))
                self.FameTooBar.setStyleSheet("background-color: rgb(183, 220, 255);\n"
        "")
                self.FameTooBar.setFrameShape(QFrame.Shape.StyledPanel)
                self.FameTooBar.setFrameShadow(QFrame.Shadow.Raised)
                self.FameTooBar.setObjectName("FameTooBar")

                self.frame = QtWidgets.QFrame(self.FameTooBar)
                self.frame.setGeometry(QtCore.QRect(0, 0, 120, 80))
                self.frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 81, 81))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")

                self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton.setStyleSheet("background-color : white;\n"
        "image: url(:/newPrefix/home.png);\n"
        "")
                self.pushButton.setText("")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.show_home)
                self.verticalLayout.addWidget(self.pushButton)

                self.frame_2 = QtWidgets.QFrame(self.FameTooBar)
                self.frame_2.setGeometry(QtCore.QRect(0, 80, 120, 80))
                self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_2.setObjectName("frame_2")

                self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
                self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 0, 81, 81))
                self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")

                self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_2.setStyleSheet("background-color : white;\n"
        "image : url(:/newPrefix/pencil.png);\n"
        "")
                self.pushButton_2.setText("")
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(self.show_input)
                self.verticalLayout_2.addWidget(self.pushButton_2)

                self.frame_3 = QtWidgets.QFrame(self.FameTooBar)
                self.frame_3.setGeometry(QtCore.QRect(0, 160, 120, 80))
                self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_3.setObjectName("frame_3")
                self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
                self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 0, 81, 81))
                self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")

                self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
                self.pushButton_3.setStyleSheet("background-color : white;\n"
        "image: url(:/newPrefix/chart-medium.png);\n"
        "")
                self.pushButton_3.setText("")
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_3.clicked.connect(self.show_graph)
                self.verticalLayout_3.addWidget(self.pushButton_3)

                self.frame_4 = QtWidgets.QFrame(self.FameTooBar)
                self.frame_4.setGeometry(QtCore.QRect(0, 240, 120, 80))
                self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_4.setObjectName("frame_4")
                self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_4)
                self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 0, 81, 81))
                self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")

                self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
                self.pushButton_4.setStyleSheet("background-color : white;\n"
        "image: url(:/newPrefix/chart-up.png);\n"
        "")
                self.pushButton_4.setText("")
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_4.clicked.connect(self.show_predict)
                self.verticalLayout_4.addWidget(self.pushButton_4)

                self.frame_5 = QtWidgets.QFrame(self.FameTooBar)
                self.frame_5.setGeometry(QtCore.QRect(0, 320, 120, 80))
                self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_5.setObjectName("frame_5")

                self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame_5)
                self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 0, 81, 81))
                self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_5.setObjectName("verticalLayout_5")

                self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
                self.pushButton_5.setStyleSheet("background-color : white;\n"
        "image: url(:/newPrefix/lock-unlock.png);\n"
        "")
                self.pushButton_5.setText("")
                self.pushButton_5.setObjectName("pushButton_5")
                self.verticalLayout_5.addWidget(self.pushButton_5)
                self.pushButton_5.clicked.connect(self.setting)

                self.stackedWidget = QtWidgets.QStackedWidget(self.FrameContent)
                self.stackedWidget.setGeometry(QtCore.QRect(120, 0, 511, 401))
                self.stackedWidget.setObjectName("stackedWidget")

                self.home_page = QtWidgets.QWidget()
                self.home_page.setObjectName("home_page")

                self.label = QtWidgets.QLabel(self.home_page)
                self.label.setGeometry(QtCore.QRect(150, 10, 209, 51))
                self.label.setText("50/30/20 Budgeting Rule")
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                self.label.setFont(font)
                self.label.setObjectName("label")

                self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.home_page)
                self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 60, 505, 321))
                self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
                self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_6.setObjectName("verticalLayout_6")

                self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_6)
                self.textBrowser.setObjectName("textBrowser")
                self.textBrowser.append("The 50/30/20 budgeting rule is a straightforward financial framework designed to help individuals manage their money effectively. This method divides after-tax income into three categories: 50% for needs, such as housing, utilities, and groceries; 30% for wants, which includes discretionary spending on entertainment and leisure activities; and 20% for savings and debt repayment. By adhering to this simple structure, individuals can ensure that they are meeting their essential expenses while also enjoying personal indulgences and building a secure financial future. This rule serves as a practical guide for anyone looking to achieve a balanced budget and improved financial health.")
                self.verticalLayout_6.addWidget(self.textBrowser)

                self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_6)
                self.textBrowser_2.setObjectName("textBrowser_2")
                self.textBrowser_2.append("Quy tắc ngân sách 50/30/20 là một khuôn khổ tài chính đơn giản được thiết kế để giúp cá nhân quản lý tiền bạc của họ một cách hiệu quả. Phương pháp này chia thu nhập sau thuế thành ba loại: 50% cho nhu cầu, chẳng hạn như nhà ở, tiện ích và thực phẩm; 30% cho mong muốn, bao gồm chi tiêu tùy ý cho giải trí và các hoạt động vui chơi; và 20% cho tiết kiệm và trả nợ. Bằng cách tuân thủ cấu trúc đơn giản này, cá nhân có thể đảm bảo rằng họ đang đáp ứng các khoản chi tiêu thiết yếu trong khi cũng tận hưởng những điều xa xỉ cá nhân và xây dựng một tương lai tài chính an toàn. Quy tắc này phục vụ như một hướng dẫn thực tiễn cho bất kỳ ai đang tìm cách đạt được ngân sách cân bằng và cải thiện sức khỏe tài chính.")
                self.verticalLayout_6.addWidget(self.textBrowser_2)
                self.stackedWidget.addWidget(self.home_page)

                self.input_page = QWidget()
                self.input_page.setObjectName(u"input_page")
                self.formLayoutWidget = QWidget(self.input_page)
                self.formLayoutWidget.setObjectName(u"formLayoutWidget")
                self.formLayoutWidget.setGeometry(QRect(10, 0, 481, 51))
                self.formLayout = QFormLayout(self.formLayoutWidget)
                self.formLayout.setObjectName(u"formLayout")
                self.formLayout.setContentsMargins(0, 0, 0, 0)
                self.label_3 = QLabel("Income",self.formLayoutWidget)
                self.label_3.setObjectName(u"label_3")

                self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

                self.spinBox = QSpinBox(self.formLayoutWidget)
                self.spinBox.setObjectName(u"spinBox")
                self.spinBox.setStyleSheet(u"QComboBox {\n"
                "    background-color: #ffffff;  /* M\u00e0u n\u1ec1n tr\u1eafng */\n"
                "    color: #333;  /* M\u00e0u ch\u1eef \u0111\u1eadm */\n"
                "    font-size: 14px;\n"
                "    font-weight: bold;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 5px;\n"
                "    padding: 5px;\n"
                "    min-width: 120px;  /* \u0110\u1eb7t chi\u1ec1u r\u1ed9ng t\u1ed1i thi\u1ec3u */\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QComboBox:hover {\n"
                "    background-color: #f8f9fa;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi \u0111\u01b0\u1ee3c focus */\n"
                "QComboBox:focus {\n"
                "    border-color: #0078D7;\n"
                "}\n"
                "\n"
                "/* Khi m\u1edf danh s\u00e1ch */\n"
                "QComboBox::drop-down {\n"
                "    border-left: 2px solid #ccc;\n"
                "    width: 20px;\n"
                "}\n"
                "\n"
                "/* Danh s\u00e1ch t\u00f9y ch\u1ecdn */\n"
                "QComboBox QAbstractItemView {\n"
                "    background-color: white;\n"
                "    border: 1px solid #ccc;\n"
                "    selection-background-color: #0078D7;\n"
                "    selection-color: white;\n"
                "}\n"
                "\n"
                "/* Khi hover l\u00ean t\u1eebng m\u1ee5c */\n"
                "QComboBox QAbstractItemView::item:hover {\n"
                "    background-color: #f0f0f0;\n"
                "}\n"
                "\n"
                "/* Khi ch\u1ecdn m\u1ed9t m\u1ee5c */\n"
                "QComboBox QAbstractItemView::item:selected {\n"
                "    background-color: #0078D7;\n"
                "    color: white;\n"
                "}\n"
                "")
                self.spinBox.setPrefix("VND")
                self.spinBox.setMinimum(100000)
                self.spinBox.setMaximum(1000000000)

                self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox)

                self.label_4 = QLabel("Tax",self.formLayoutWidget)
                self.label_4.setObjectName(u"label_4")

                self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

                self.doubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
                self.doubleSpinBox.setObjectName(u"doubleSpinBox")
                self.doubleSpinBox.setMaximum(1.000000000000000)
                self.doubleSpinBox.setSingleStep(0.100000000000000)
                self.doubleSpinBox.setSuffix("%")

                self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox)

                self.line = QFrame(self.input_page)
                self.line.setObjectName(u"line")
                self.line.setGeometry(QRect(10, 50, 481, 16))
                self.line.setFrameShape(QFrame.Shape.HLine)
                self.line.setFrameShadow(QFrame.Shadow.Sunken)
                self.pushButton_7 = QPushButton("Caculate",self.input_page)
                self.pushButton_7.setObjectName(u"pushButton_7")
                self.pushButton_7.setGeometry(QRect(210, 150, 101, 21))
                self.pushButton_7.setStyleSheet(u"QPushButton {\n"
                "    background-color: #28a745;  /* M\u00e0u xanh l\u00e1 */\n"
                "    color: white;\n"
                "    font-size: 14px;\n"
                "    font-weight: bold;\n"
                "    border: 2px solid #218838;\n"
                "    border-radius: 5px;\n"
                "    width: 101px;\n"
                "    height: 21px;\n"
                "}\n"
                "\n"
                "/* Khi hover */\n"
                "QPushButton:hover {\n"
                "    background-color: #218838;\n"
                "    border-color: #1e7e34;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #1e7e34;\n"
                "    border-color: #155724;\n"
                "}\n"
                "\n"
                "/* Khi \u0111\u01b0\u1ee3c focus */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "}\n"
                "")
                self.result_output = QLabel(self.input_page)
                self.result_output.setObjectName(u"result_output")
                self.result_output.setGeometry(QRect(10, 60, 481, 71))
                self.pushButton_9 = QPushButton(self.input_page)
                self.pushButton_9.setObjectName(u"pushButton_9")
                self.pushButton_9.setGeometry(QRect(10, 210, 161, 61))
                self.pushButton_9.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/plus-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7;\n"
                "}\n"
                "")  
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_9.setGraphicsEffect(shadow)
                self.pushButton_9.show()   
                self.pushButton_9.clicked.connect(self.add_needs)

                self.pushButton_6 = QPushButton(self.input_page)
                self.pushButton_6.setObjectName(u"pushButton_6")
                self.pushButton_6.setGeometry(QRect(10, 310, 161, 61))
                self.pushButton_6.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/cross-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* M\u00e0u xanh nh\u1eb9 */\n"
                "}\n"
                "")     
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_6.setGraphicsEffect(shadow)
                self.pushButton_6.show()
                self.pushButton_6.clicked.connect(self.remove_needs)

                self.label_6 = QLabel("Add to list for to needs " , self.input_page)
                self.label_6.setObjectName(u"label_6")
                self.label_6.setGeometry(QRect(30, 180, 131, 21))

                self.pushButton_10 = QPushButton(self.input_page)
                self.pushButton_10.setObjectName(u"pushButton_10")
                self.pushButton_10.setGeometry(QRect(180, 210, 161, 61))
                self.pushButton_10.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/plus-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7;\n"
                "}\n"
                "")     
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_10.setGraphicsEffect(shadow)
                self.pushButton_10.show()
                self.pushButton_10.clicked.connect(self.add_wants)

                self.pushButton_17 = QPushButton(self.input_page)
                self.pushButton_17.setObjectName(u"pushButton_17")
                self.pushButton_17.setGeometry(QRect(350, 210, 161, 61))
                self.pushButton_17.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/plus-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7;\n"
                "}\n"
                "")
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_17.setGraphicsEffect(shadow)
                self.pushButton_17.show()
                self.pushButton_17.clicked.connect(self.add_savings)

                self.label_19 = QLabel("Add to list for to wants" , self.input_page)
                self.label_19.setObjectName(u"label_19")
                self.label_19.setGeometry(QRect(200, 180, 131, 21))

                self.label_20 = QLabel("Add to list for to savings" , self.input_page)
                self.label_20.setObjectName(u"label_20")
                self.label_20.setGeometry(QRect(370, 180, 141, 21))

                self.pushButton_30 = QPushButton(self.input_page)
                self.pushButton_30.setObjectName(u"pushButton_30")
                self.pushButton_30.setGeometry(QRect(180, 310, 161, 61))
                self.pushButton_30.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/cross-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* M\u00e0u xanh nh\u1eb9 */\n"
                "}\n"
                "")
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_30.setGraphicsEffect(shadow)
                self.pushButton_30.show()
                self.pushButton_30.clicked.connect(self.remove_wants)

                self.pushButton_31 = QPushButton(self.input_page)
                self.pushButton_31.setObjectName(u"pushButton_31")
                self.pushButton_31.setGeometry(QRect(350, 310, 161, 61))
                self.pushButton_31.setStyleSheet(u"QPushButton {\n"
                "    image: url(:/newPrefix/cross-button.png);\n"
                "    background-color: white;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 10px;\n"
                "    padding: 5px;\n"
                "}\n"
                "\n"
                "/* Khi hover (di chu\u1ed9t v\u00e0o) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi b\u1ea5m gi\u1eef */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button \u0111\u01b0\u1ee3c focus (ch\u1ecdn b\u1eb1ng b\u00e0n ph\u00edm Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* M\u00e0u xanh nh\u1eb9 */\n"
                "}\n"
                "")
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                self.pushButton_31.setGraphicsEffect(shadow)
                self.pushButton_31.show()
                self.pushButton_31.clicked.connect(self.remove_savings)

                self.label_21 = QLabel("Remove to list needs",self.input_page)
                self.label_21.setObjectName(u"label_21")
                self.label_21.setGeometry(QRect(40, 280, 111, 21))

                self.label_22 = QLabel("Remove to list wants",self.input_page)
                self.label_22.setObjectName(u"label_22")
                self.label_22.setGeometry(QRect(210, 280, 111, 21))

                self.label_23 = QLabel("Remove to list savings",self.input_page)
                self.label_23.setObjectName(u"label_23")
                self.label_23.setGeometry(QRect(370, 280, 111, 21))
                self.stackedWidget.addWidget(self.input_page)

                self.graphic_page = QtWidgets.QWidget()
                self.graphic_page.setObjectName(u"graphic_page")

                self.stackedWidget_2 = QStackedWidget(self.graphic_page)
                self.stackedWidget_2.setObjectName("stackedWidget_2")
                self.stackedWidget_2.setGeometry(QRect(0 , 10 , 501 , 321))

                self.pie_needs = QWidget()
                self.pie_needs.setObjectName("pie_needs")

                self.graphic_pie_needs = QGraphicsView(self.pie_needs)
                self.graphic_pie_needs.setObjectName(u"graphic_pie_needs")
                self.graphic_pie_needs.setGeometry(QRect(10,10,491,311))
                
                self.stackedWidget_2.addWidget(self.pie_needs)

                self.pie_wants = QWidget()
                self.pie_wants.setObjectName("pie_wants")
                
                self.graphic_pie_wants = QGraphicsView(self.pie_wants)
                self.graphic_pie_wants.setObjectName(u"graphic_pie_wants")
                self.graphic_pie_wants.setGeometry(QRect(10,10,491,311))

                self.stackedWidget_2.addWidget(self.pie_wants)

                self.update_button = QPushButton(self.graphic_page)
                self.update_button.setObjectName("update_button")
                self.update_button.setGeometry(QRect(210 , 350 , 75 , 24))
                self.update_button.setText("Update")
                self.update_button.clicked.connect(self.update_chart)
                self.update_button.setStyleSheet("""
                QPushButton {
                        background-color: #ec96a4;
                        border: 2px solid #ccc;
                        border-radius: 8px;
                        padding: 3px;
                }
                QPushButton:hover {
                        background-color: #5d535e;
                        border-color: #888;
                }
                QPushButton:pressed {
                        background-color: #dfe166;
                        border-color: #555;
                }
                QPushButton:focus {
                        outline: none;
                        border: 2px solid #0078D7; 
                }
              
                """)

                self.pushButton_12 = QPushButton(self.graphic_page)
                self.pushButton_12.setObjectName('pushButton_12')
                self.pushButton_12.setGeometry(QRect(300, 350 , 75 , 24))
                self.pushButton_12.setText("Needs")
                self.pushButton_12.setStyleSheet("""
                        QPushButton {
                                background-color: #c4dfe6;
                                border: 2px solid #ccc;
                                border-radius: 10px;
                                padding: 5px;
                                }
                        QPushButton:hover {
                                background-color: #66a5ad;
                                border-color: #888;
                                }
                        QPushButton:pressed {
                                background-color: #a2c523;
                                border-color: #555;
                                }
                        QPushButton:focus {
                                outline: none;
                                border: 2px solid #0078D7; 
                                }                          
                """)
                self.pushButton_12.clicked.connect(self.show_pie_needs)

                self.pushButton_13 = QPushButton(self.graphic_page)
                self.pushButton_13.setObjectName('pushButton_13')
                self.pushButton_13.setGeometry(QRect(120, 350 , 75 , 24))
                self.pushButton_13.setText("Wants")
                self.pushButton_13.setStyleSheet("""
                        QPushButton {
                                background-color: #6fb98f;
                                border: 2px solid #ccc;
                                border-radius: 10px;
                                padding: 5px;
                        }
                        QPushButton:hover {
                                background-color: #2c7873;
                                border-color: #888;
                        }
                        QPushButton:pressed {
                                background-color: #a2c523;
                                border-color: #555;
                        }
                        QPushButton:focus {
                                outline: none;
                                border: 2px solid #0078D7; 
                        }
              
              
                """)
                self.pushButton_13.clicked.connect(self.show_pie_wants)

                self.stackedWidget.addWidget(self.graphic_page)
                self.pie_chart()

                self.predict_page = QWidget()
                self.predict_page.setObjectName("predict_page")

                self.label_2 = QLabel("Predict for your goal" , self.predict_page)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setGeometry(QRect(50, 20, 171, 41))
                font1 = QFont()
                font1.setPointSize(12)
                font1.setBold(True)
                font1.setItalic(True)
                self.label_2.setFont(font1)

                self.comboBox = QComboBox(self.predict_page)
                self.comboBox.setObjectName(u"comboBox")
                self.comboBox.setGeometry(QRect(230, 30, 131, 20))
                self.comboBox.currentIndexChanged.connect(self.predict)

                self.stackedWidget_3 = QStackedWidget(self.predict_page)
                self.stackedWidget_3.setObjectName(u"stackedWidget_3")
                self.stackedWidget_3.setGeometry(QRect(0, 70, 501, 231))

                self.page = QWidget()
                self.page.setObjectName(u"page")

                self.label_5 = QLabel(self.page)
                self.label_5.setObjectName(u"label_5")
                self.label_5.setGeometry(QRect(40, 90, 360, 71))
                font2 = QFont()
                font2.setPointSize(11)
                font2.setBold(True)
                font2.setItalic(True)
                self.label_5.setFont(font2)
                self.stackedWidget_3.addWidget(self.page)
                self.stackedWidget.addWidget(self.predict_page)

                self.load_button = QtWidgets.QPushButton(self.predict_page)
                self.load_button.setGeometry(QtCore.QRect(200, 350 , 75, 24))
                self.load_button.setObjectName("load_button")
                self.load_button.setText("Load Savings")
                self.load_button.clicked.connect(self.list_saving)

                self.pushButton_17 = QPushButton("Predict",self.predict_page)
                self.pushButton_17.setObjectName(u"pushButton_17")
                self.pushButton_17.setGeometry(QRect(280, 350, 75, 24))
                self.pushButton_17.clicked.connect(self.predict)
                self.stackedWidget.addWidget(self.predict_page)

                self.setting_page = QWidget()
                self.setting_page.setObjectName("setting_page")
                
                self.label_9 = QLabel(self.setting_page)
                self.label_9.setObjectName("label_9")
                self.label_9.setGeometry(QRect(30,20,121,16))
                self.label_9.setText("LighMode/DarkMode")
                
                self.lightMode = QRadioButton("Light Mode" , self.setting_page)
                self.lightMode.setObjectName("lightMode")
                self.lightMode.setGeometry(QRect(170,20,89,20))
                self.lightMode.toggled.connect(self.switch_mode)
                self.lightMode.setChecked(True) # dat lam che do mat dinh
                self.switch_mode()

                self.darkMode = QRadioButton("Dark Mode" , self.setting_page)
                self.darkMode.setObjectName("darkMode")
                self.darkMode.setGeometry(QRect(280,20,89,20))
                self.darkMode.toggled.connect(self.switch_mode)

                self.label_10 = QLabel("Logout",self.setting_page)
                self.label_10.setObjectName(u"label_10")
                self.label_10.setGeometry(QRect(40, 120, 111, 16))

                self.pushButton_8 = QPushButton(self.setting_page)
                self.pushButton_8.setObjectName(u"pushButton_8")
                self.pushButton_8.setGeometry(QRect(180, 120, 191, 21))
                self.pushButton_8.setStyleSheet(u"color:red;\n"
        "")
                self.pushButton_8.setText("Logout")
                self.pushButton_8.clicked.connect(lambda:self.logout(Form))

                self.label_11 = QLabel("Account",self.setting_page)
                self.label_11.setObjectName(u"label_11")
                self.label_11.setGeometry(QRect(40, 70, 111, 16))

                self.pushButton_15 = QPushButton("Show",self.setting_page)
                self.pushButton_15.setObjectName(u"pushButton_15")
                self.pushButton_15.setGeometry(QRect(180, 70, 191, 21))
                self.pushButton_15.setStyleSheet(u"color:blue;\n")
                self.pushButton_15.clicked.connect(self.show)

                self.stackedWidget.addWidget(self.setting_page)
        #cac nut trong frametoolbar
        def show_home(self):
            self.stackedWidget.setCurrentWidget(self.home_page)

        def show_input(self):
            self.stackedWidget.setCurrentWidget(self.input_page)

        def show_graph(self):
            self.stackedWidget.setCurrentWidget(self.graphic_page)

        def show_predict(self):
            self.stackedWidget.setCurrentWidget(self.predict_page)

        def setting(self):
            self.stackedWidget.setCurrentWidget(self.setting_page)
        
        #xac dinh user 
        def set_iduser(self,iduser):
                self.iduser = iduser
                print(f"User ID set to: {iduser}")
                return iduser
        
        def get_iduser(self, iduser):
                try:
                        self.data = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="10112005",
                        database="chat_app"
                        )
                        self.cursor = self.data.cursor()
                        query = "SELECT iduser FROM users WHERE iduser = %s"
                        self.cursor.execute(query, (iduser,))
                        result = self.cursor.fetchone()

                        if result:
                                return result[0]  # Trả về iduser
                        else:
                                print("User not found.")
                                return None  # Không tìm thấy username

                except Exception as e:
                        print(f"Error fetching iduser: {e}")
                        return None
                finally:
                        if self.data.is_connected():
                                self.cursor.close()
                                self.data.close()

        def set_user(self):
                username = self.get_user(self.iduser)
                if username:
                        self.welcome_text.setText(f"Welcome , {username}")
                else:
                        self.welcome_text.setText("Welcome Guest")
                        
        def get_user(self, user_id):
                try:
                        data = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="10112005",
                        database="chat_app"
                        )
                        cursor = data.cursor()
                        if isinstance(user_id, int):
                                cursor.execute("SELECT username FROM users WHERE iduser = %s", (user_id,))

                        result = cursor.fetchone()
                        if result:
                                return result[0]
                        else:
                                print(f"User not found for identifier: {user_id}")
                                return None
                except Exception as e:
                        print(f"Error fetching user: {e}")
                        return None
                finally:
                        if data.is_connected() and 'data' in locals():
                                cursor.close()
                                data.close()

        def check_monthly(self):
                try:
                        data = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="10112005",
                        database="chat_app"
                        )
                        cursor = data.cursor()

                        cursor.execute("SELECT times FROM stoge_data WHERE iduser = %s ORDER BY times DESC LIMIT 1 ", (self.iduser,))
                        result = cursor.fetchone()

                        current_time = datetime.now()

                        if result and result[0] is not None:
                                last_click_time = result[0]
                                if isinstance(last_click_time, str):
                                        last_click_time = datetime.strptime(last_click_time, "%Y-%m-%d %H:%M:%S")

                                time_difference = current_time - last_click_time
                                print(time_difference)
                                if time_difference.days < 30:
                                        QMessageBox.warning(None, "Error", f"You need to wait {30 - time_difference.days} more days to click again.")
                                        return
                                        
                                else:
                                        cursor.execute("UPDATE stoge_data SET times = NOW() WHERE iduser = %s", (self.iduser,))
                                        data.commit()
                                        QMessageBox.information(None, "Success", "Action allowed. Last click time updated.")
                        else:
                                cursor.execute("SELECT COUNT(*) from stoge_data where iduser = %s" , (self.iduser,))
                                user_exists = cursor.fetchone()[0]

                                if user_exists == 0 :
                                        cursor.execute("INSERT INTO stoge_data (iduser, times) VALUES (%s, NOW())", (self.iduser,))
                                        data.commit()
                                        QMessageBox.information(None, "Success", "Action allowed. Record created with current time.")

                        cursor.execute("SELECT last_activity FROM stoge_data WHERE iduser = %s ORDER BY last_activity DESC", (self.iduser,))
                        result = cursor.fetchone()

                        if result and result[0] is not None:
                                last_activity_time = result[0]
                                if isinstance(last_activity_time, str):
                                        last_activity_time = datetime.strptime(last_activity_time, "%Y-%m-%d %H:%M:%S")

                                inactivity_days = (current_time - last_activity_time).days

                                if inactivity_days < 30:
                                        QMessageBox.warning(None, "Inactive Warning", "You have been active within the last 30 days.")
                                        return
                                else:
                                        cursor.execute("UPDATE stoge_data SET last_activity = NOW() WHERE iduser = %s", (self.iduser,))
                                        data.commit()
                        else:
                                cursor.execute("SHOW COLUMNS FROM stoge_data LIKE 'last_activity'")
                                if cursor.fetchone() is None:
                                        cursor.execute("ALTER TABLE stoge_data ADD COLUMN last_activity DATETIME DEFAULT NOW();")

                                cursor.execute("UPDATE stoge_data SET last_activity = NOW() WHERE iduser = %s", (self.iduser,))
                                data.commit()

                        cursor.close()
                        data.close()

                except Exception as e:
                        QMessageBox.critical(None, "Error", str(e))
                finally:
                        if 'data' in locals() and data.is_connected():
                                data.close()
        #ham tinh toan
        def caculate(self):
                iduser = getattr(self,"iduser",None)
                if not iduser:
                       print("Error")
                       return

                income = self.spinBox.value()
                tax_rate = self.doubleSpinBox.value() / 100
                income_after = income * (1 - tax_rate)

                needs = income_after * 0.5 
                wants = income_after * 0.3
                savings = income_after * 0.2

                
                result = (
                        f"Income after tax: {income_after:.2f} VND\n"
                        f"Needs (50%): {needs:.2f} VND\n"
                        f"Wants (30%): {wants:.2f} VND\n"
                        f"Savings (20%): {savings:.2f} VND"
                )
                self.result_output.setText(result)
                self.save_to_database(iduser , income, tax_rate, income_after, needs, wants, savings)       

        def on_button_clicked(self):
                if self.caculate_count is not None:
                        self.caculate_count += 1
                        if self.caculate_count >= 2:
                                self.check_monthly()
                        self.caculate()                 

        #luu vao database
        def save_to_database(self, iduser, income, tax_rate, income_after, needs, wants, savings):
                try:
                        self.data = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="10112005",
                        database="chat_app"
                        )
                        self.cursor = self.data.cursor()

                        query = """
                                INSERT INTO stoge_data (iduser, income, tax_rate, income_after, needs, wants, savings, times)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                                """
                        self.cursor.execute(query, (iduser, income, tax_rate, income_after, needs, wants, savings))
                        self.data.commit()
                        print("Data inserted successfully!")

                except mysql.connector.Error as e:
                        print(f"Failed to insert data: {e}")

                finally:
                        if self.data.is_connected():
                                self.cursor.close()
                                self.data.close()

        def show(self):
                from info import Ui_Form as update_account
                self.window = QWidget()
                self.ui = update_account(iduser = self.iduser , parent_window = self.Form)
                self.ui.setupUi(self.window)
                self.window.show()
                
        def add_savings(self):
                from add_list_3 import Ui_Form as savings 
                self.window = QWidget()
                self.ui = savings(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_17.setEnabled(False)

        def add_needs(self):
                from list_needs import Ui_Form as needs 
                self.window = QWidget()
                self.ui = needs(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_9.setEnabled(False)

        def add_wants(self):
                from add_list_2 import Ui_Form as wants
                self.window = QWidget()
                self.ui = wants(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_10.setEnabled(False)

        def remove_needs(self):
                from remove_list_needs import Ui_Form as remove_needs 
                self.window = QWidget()
                self.ui = remove_needs(iduser=self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def remove_wants(self):
                from remove_list_wants import Ui_Form as remove_wants
                self.window = QWidget()
                self.ui = remove_wants(iduser=self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def remove_savings(self):
                from remove_list_savings import Ui_Form as remove_savings 
                self.window = QWidget()
                self.ui = remove_savings(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def close(self):
               sys.exit(1)
        
        def logout(self,currentPage):
                from loginUi1 import Ui_Form as BackLogin
                self.window = QtWidgets.QWidget()
                self.ui = BackLogin()
                self.ui.setupUi(self.window)
                self.window.show()
                currentPage.close()
        
        #che do light va dark
        def switch_mode(self):
                if self.lightMode.isChecked():
                       self.set_light_mode()
                elif self.darkMode.isChecked():
                        self.set_dark_mode()  

        def set_light_mode(self):
                self.FrameContent.setStyleSheet("""
                QWidget {
                        background-color: #FFFFFF;
                        color: #000000;
                }
                QRadioButton {
                        color: #000000;
                }
                """)

        def set_dark_mode(self):
                self.FrameContent.setStyleSheet("""
                QWidget {
                        background-color: #2C2C2C;
                        color: #FFFFFF;
                }
                QRadioButton {
                        color: #FFFFFF;
                }
                QTextBrowser{color : #00CCCC;}
                """)
        
        #ham tinh do lon phan tram
        def scale_data(self , data , target_sum ):
                current_sum = sum(data)
                if current_sum == 0 :
                      return data
                scale_data = target_sum / current_sum
                return [value * scale_data for value in data]
        #ve do thi
        def pie_chart(self):
                self.pie_chart_needs()
                self.pie_chart_wants()

        def pie_chart_needs(self):
                try:
                        data = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='10112005',
                        database='chat_app'
                        )
                        cursor = data.cursor()

                        cursor.execute("SELECT name_needs, cost FROM list_needs WHERE iduser = %s", (self.iduser,))
                        result = cursor.fetchall()

                        name_needs = [row[0] for row in result]
                        cost = [row[1] for row in result]

                        scaled_cost = self.scale_data(cost, 50)  # Scale to 30 (60% of 80)
                        figure = plt.figure(figsize=(5, 4))
                        plt.pie(scaled_cost, labels=name_needs, 
                                autopct=lambda pct: f"{pct:.1f}%\n({pct * 50 / 100:.1f})", 
                                startangle=140)
                        plt.title("Needs Pie")

                        canvas = FigureCanvas(figure)
                        scene = QGraphicsScene()
                        scene.addWidget(canvas)
                        self.graphic_pie_needs.setScene(scene)

                except Exception as e:
                        print(f"Exception occurred: {e}")  # Debugging

                finally:
                        if 'cursor' in locals():
                                cursor.close()
                        if 'data' in locals() and data.is_connected():
                                data.close()
                     
        def pie_chart_wants(self):
                try:
                        data = mysql.connector.connect(
                                host='localhost',
                                user='root', 
                                password='10112005',
                                database='chat_app'
                        )
                        cursor = data.cursor()
                        cursor.execute("SELECT name_wants, cost from list_wants where iduser = %s" , (self.iduser,))

                        result = cursor.fetchall()
                
                        name_wants = [row[0] for row in result]
                        cost = [row[1] for row in result]

                        scaled_cost = self.scale_data(cost, 30)  # Scale to 20 (40% of 50)
                
                        figure = plt.figure(figsize=(5,4))
                        plt.pie(scaled_cost, labels=name_wants, 
                                autopct=lambda pct: f"{pct:.1f}%\n({pct*30/100:.1f})", 
                                startangle=140)
                        plt.title("Wants Pie ")

                        canvas = FigureCanvas(figure)
                        scene = QGraphicsScene()
                        scene.addWidget(canvas)
                        self.graphic_pie_wants.setScene(scene)

                except Exception as e:
                        print(e)

        def update_chart(self):
               self.pie_chart()

        def show_pie_needs(self):
               self.stackedWidget_2.setCurrentWidget(self.pie_needs)

        def show_pie_wants(self):
               self.stackedWidget_2.setCurrentWidget(self.pie_wants)
        
        def list_saving(self):
                try:
                        data = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='10112005',
                                database='chat_app'
                        )
                        cursor = data.cursor()
                        cursor.execute("SELECT name_savings, cost FROM list_savings WHERE iduser = %s", (self.iduser,))
                        list_savings = cursor.fetchall()

                        self.comboBox.clear()  
                        self.savings_data = {}
                        for row in list_savings:
                                name_saving, cost = row
                                self.comboBox.addItem(name_saving)
                                self.savings_data[name_saving] = cost  # Store cost in the dictionary
                except Exception as e:
                        QtWidgets.QMessageBox.warning(None, "Warning", f"You have not saved any money yet: {e}")
                except mysql.connector.Error as e:
                        QtWidgets.QMessageBox.warning(None, "Warning", f"You have not saved any money yet: {e}")
                finally:
                        if 'cursor' in locals():
                                cursor.close()
                        if 'data' in locals() and data.is_connected():
                                data.close()

        def predict(self):
                try:
                        selected_saving = self.comboBox.currentText()
                        print(self.savings_data)
                        if selected_saving in self.savings_data:
                                cost = self.savings_data[selected_saving]

                                data = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='10112005',
                                database='chat_app'
                                )
                                cursor = data.cursor()
                                cursor.execute("SELECT savings FROM stoge_data WHERE iduser = %s", (self.iduser,))
                                result = cursor.fetchone()
                                savings = result[0] if result[0] is not None else 0

                                if savings > 0:
                                        ratio = cost / savings
                                        self.label_5.setText(f"Monthly prediction for {selected_saving}: {int(ratio)} month")
                                        
                                else:
                                        self.label_5.setText("No savings data available")
                        else:
                                self.label_5.setText("No savings data available")

                except mysql.connector.Error as e:
                        QtWidgets.QMessageBox.warning(None, "Error", f"Database error: {e}")
                except Exception as e:
                        QtWidgets.QMessageBox.warning(None, "Error", f"Error: {e}")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

