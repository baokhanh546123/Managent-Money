#khao bao thu vien va file con 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime , timedelta 
import sys
import view.image1
import view.image
import mysql.connector
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

                self.formLayoutWidget_3 = QWidget(self.home_page)
                self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
                self.formLayoutWidget_3.setGeometry(QRect(0, 210, 501, 171))
                self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
                self.formLayout_3.setObjectName(u"formLayout_3")
                self.formLayout_3.setContentsMargins(0, 50, 0, 10)
                self.label_12 = QLabel("ChatBot",self.formLayoutWidget_3)
                self.label_12.setObjectName(u"label_12")

                self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

                self.pushButton_19 = QPushButton("Open",self.formLayoutWidget_3)
                self.pushButton_19.setObjectName(u"pushButton_19")
                self.pushButton_19.clicked.connect(self.open_chatBot)
                self.pushButton_19.setStyleSheet(u"QPushButton{\n"
                "color : #90AFC5;\n"
                "background-color:#f3d388;\n"
                "border:2px ;\n"
                "border-radius : 20px;\n"
                "padding : 5px;\n"
                "}\n"
                "QPushButton:hover{\n"
                "background-color : #a5c3cf;\n"
                "border-color : #f3d388;\n"
                "}\n"
                "QPushButton:pressed{\n"
                "background-color : #e59d5c;\n"
                "border-color : #2A3132;\n"
                "}\n"
                "")
                self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pushButton_19)
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
                "    background-color: #ffffff;  /* Màu nền trắng */\n"
                "    color: #333;  /* Màu chữ đậm */\n"
                "    font-size: 14px;\n"
                "    font-weight: bold;\n"
                "    border: 2px solid #ccc;\n"
                "    border-radius: 5px;\n"
                "    padding: 5px;\n"
                "    min-width: 120px;  /* Đặt chiều rộng tối thiểu */\n"
                "}\n"
                "\n"
                "/* Khi hover (di chuột vào) */\n"
                "QComboBox:hover {\n"
                "    background-color: #f8f9fa;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi được focus */\n"
                "QComboBox:focus {\n"
                "    border-color: #0078D7;\n"
                "}\n"
                "\n"
                "/* Khi mở danh sách */\n"
                "QComboBox::drop-down {\n"
                "    border-left: 2px solid #ccc;\n"
                "    width: 20px;\n"
                "}\n"
                "\n"
                "/* Danh sách tùy chọn */\n"
                "QComboBox QAbstractItemView {\n"
                "    background-color: white;\n"
                "    border: 1px solid #ccc;\n"
                "    selection-background-color: #0078D7;\n"
                "    selection-color: white;\n"
                "}\n"
                "\n"
                "/* Khi hover lên từng mục */\n"
                "QComboBox QAbstractItemView::item:hover {\n"
                "    background-color: #f0f0f0;\n"
                "}\n"
                "\n"
                "/* Khi chọn một mục */\n"
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
                self.doubleSpinBox.setMaximum(100)
                self.doubleSpinBox.setSingleStep(0.1)
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
                "    background-color: #28a745;  /* Màu xanh lá */\n"
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
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #1e7e34;\n"
                "    border-color: #155724;\n"
                "}\n"
                "\n"
                "/* Khi được focus */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "}\n"
                "")
                self.pushButton_7.clicked.connect(self.on_button_clicked)
                self.result_output = QLabel(self.input_page)
                self.result_output.setObjectName(u"result_output")
                self.result_output.setGeometry(QRect(10, 60, 481, 71))
                self.result_output.setStyleSheet("color : red")
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* Màu xanh nhạt */\n"
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* Màu xanh nhạt */\n"
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
                "/* Khi hover (di chuột vào) */\n"
                "QPushButton:hover {\n"
                "    background-color: #f0f0f0;\n"
                "    border-color: #888;\n"
                "}\n"
                "\n"
                "/* Khi bấm giữ */\n"
                "QPushButton:pressed {\n"
                "    background-color: #e0e0e0;\n"
                "    border-color: #555;\n"
                "}\n"
                "\n"
                "/* Khi button được focus (chọn bằng bàn phím Tab) */\n"
                "QPushButton:focus {\n"
                "    outline: none;\n"
                "    border: 2px solid #0078D7; /* Màu xanh nhạt */\n"
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

                self.load_button = QtWidgets.QPushButton("Load Data",self.predict_page)
                self.load_button.setGeometry(QtCore.QRect(200, 350 , 75, 24))
                self.load_button.setObjectName("load_button")
                self.load_button.clicked.connect(self.list_saving)
                self.load_button.setStyleSheet("""QPushButton {
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

                self.pushButton_17 = QPushButton("Predict",self.predict_page)
                self.pushButton_17.setObjectName(u"pushButton_17")
                self.pushButton_17.setGeometry(QRect(280, 350, 75, 24))
                self.pushButton_17.clicked.connect(self.predict)
                self.pushButton_17.setStyleSheet("""
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
                self.stackedWidget.addWidget(self.predict_page)

                self.setting_page = QWidget()
                self.setting_page.setObjectName(u"setting")

                #tao form
                self.formLayoutWidget_2 = QWidget(self.setting_page)
                self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
                self.formLayoutWidget_2.setGeometry(QRect(10, 20, 501, 351))
                self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
                self.formLayout_2.setObjectName(u"formLayout_2")
                self.formLayout_2.setHorizontalSpacing(50)
                self.formLayout_2.setVerticalSpacing(30)
                self.formLayout_2.setContentsMargins(20, 50, 30, 10)

                self.label_9 = QLabel("DarkMode/LightMode",self.formLayoutWidget_2)
                self.label_9.setObjectName(u"label_9")
                self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

                self.label_11 = QLabel("Account",self.formLayoutWidget_2)
                self.label_11.setObjectName(u"label_11")
                self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_11)

                self.pushButton_18 = QPushButton("Show",self.formLayoutWidget_2)
                self.pushButton_18.setObjectName(u"pushButton_18")
                self.pushButton_18.clicked.connect(self.show)
                self.pushButton_18.setStyleSheet(u"QPushButton{\n"
        "color : #90AFC5;\n"
        "background-color:#2A3132;\n"
        "border:2px solid #ccc;\n"
        "border-radius : 5px;\n"
        "padding : 5px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color : #336B87;\n"
        "border-color : #2A3132;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color : #763626;\n"
        "border-color : #2A3132;\n"
        "}\n"
        "")
                self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pushButton_18)


                self.label_10 = QLabel("Logout",self.formLayoutWidget_2)
                self.label_10.setObjectName(u"label_10")
                self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

                self.pushButton_8 = QPushButton("Logout",self.formLayoutWidget_2)
                self.pushButton_8.setObjectName(u"pushButton_8")
                self.pushButton_8.clicked.connect(lambda:self.logout(Form))
                self.pushButton_8.setStyleSheet(u"QPushButton{\n"
        "	color:#FD974F;\n"
        "	background-color:#C60000;\n"
        "	border-color:#FEF2E4;\n"
        "	border-radius : 20px;\n"
        "	padding : 5px\n"
        "}\n"
        "QPushButton:hover{\n"
        "	color:#C60000;\n"
        "	background-color:#FEF2E4;\n"
        "	border-color:#C60000;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "	color:#C60000;\n"
        "	background-color:#805a38;\n"
        "	border-color:#C60000;\n"
        "}\n"
        "\n"
        "\n"
        "\n"
        "")

                self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pushButton_8)

                self.horizontalLayout = QHBoxLayout()
                self.horizontalLayout.setSpacing(6)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setContentsMargins(10, 20, 10, 20)

                self.radioButton_2 = QRadioButton("Light Mode",self.formLayoutWidget_2)
                self.radioButton_2.setObjectName(u"radioButton_2")
                self.radioButton_2.toggled.connect(self.switch_mode)
                self.radioButton_2.setChecked(True) # dat lam che do mat dinh
                self.switch_mode()
                self.horizontalLayout.addWidget(self.radioButton_2)

                self.radioButton = QRadioButton("Dark Mode",self.formLayoutWidget_2)
                self.radioButton.setObjectName(u"radioButton")
                self.radioButton.toggled.connect(self.switch_mode)
                self.horizontalLayout.addWidget(self.radioButton)

                self.horizontalLayout.setStretch(0, 5)
                self.horizontalLayout.setStretch(1, 5)

                self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

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

        def get_db_connection(self):
                return mysql.connector.connect(
                        host="localhost",
                        username = "root",
                        password = "10112005",
                        database = "chat_app"
                )
        
        def check_if_can_calculate(self):
                try:
                        data = self.get_db_connection()
                        cursor = data.cursor()
                        cursor.execute("SELECT times FROM stoge_data WHERE iduser = %s ORDER BY times DESC LIMIT 1", (self.iduser,))
                        result = cursor.fetchone()

                        current_time = datetime.now()

                        if result and result[0] is not None:
                                last_click_time = result[0]
                                if isinstance(last_click_time, str):
                                        last_click_time = datetime.strptime(last_click_time, "%Y-%m-%d %H:%M:%S")

                                time_difference = current_time - last_click_time
                                if time_difference.days < 30:
                                        return False 
                                else:
                                        return True 
                        else:
                                return True  
                except Exception as e:
                        print(f"Error checking calculation time: {e}")
                        return False
                finally:
                        if cursor:
                                cursor.close()
                        if data and data.is_connected():
                                data.close()
        #ham tinh toan
        def caculate(self):
                iduser = getattr(self,"iduser",None)
                if not iduser:
                       print("Error")
                       return
                if not self.check_if_can_calculate():
                        QMessageBox.warning(None, "Error", "You need to wait 30 days before calculating again.")
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
                if not self.check_if_can_calculate():
                        QMessageBox.warning(None, "Error", "You need to wait 30 days before calculating again.")
                        return

                self.caculate()                 

        #luu vao database
        def save_to_database(self, iduser, income, tax_rate, income_after, needs, wants, savings):
                try:
                        self.data = self.get_db_connection()
                        self.cursor = self.data.cursor()

        
                        self.cursor.execute("SELECT iduser FROM users WHERE iduser = %s", (iduser,))
                        if not self.cursor.fetchone():
                                print(f"User with iduser {iduser} does not exist in the users table.")
                                return

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
                from view.info import Ui_Form as update_account
                self.window = QWidget()
                self.ui = update_account(iduser = self.iduser , parent_window = self.Form)
                self.ui.setupUi(self.window)
                self.window.show()
                
        def add_savings(self):
                from view.savings import Ui_Form as savings 
                self.window = QWidget()
                self.ui = savings(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_17.setEnabled(False)

        def add_needs(self):
                from view.needs import Ui_Form as needs 
                self.window = QWidget()
                self.ui = needs(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_9.setEnabled(False)

        def add_wants(self):
                from view.wants import Ui_Form as wants
                self.window = QWidget()
                self.ui = wants(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

                if self.ui.warning(True):
                        self.pushButton_10.setEnabled(False)

        def remove_needs(self):
                from view.remove_needs import Ui_Form as remove_needs 
                self.window = QWidget()
                self.ui = remove_needs(iduser=self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def remove_wants(self):
                from view.remove_wants import Ui_Form as remove_wants
                self.window = QWidget()
                self.ui = remove_wants(iduser=self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def remove_savings(self):
                from view.remove_savings import Ui_Form as remove_savings 
                self.window = QWidget()
                self.ui = remove_savings(iduser = self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

        def close(self):
               sys.exit()
        
        def logout(self,currentPage):
                from view.loginUi1 import Ui_Form as BackLogin
                self.window = QtWidgets.QWidget()
                self.ui = BackLogin()
                self.ui.setupUi(self.window)
                self.window.show()
                currentPage.close()
        
        #che do light va dark
        def switch_mode(self):
                if self.radioButton_2.isChecked():
                       self.set_light_mode()
                elif self.radioButton.isChecked():
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
                        data = self.get_db_connection()
                        cursor = data.cursor()

                        cursor.execute("SELECT ten , cost FROM needs WHERE iduser = %s", (self.iduser,))
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
                        data = self.get_db_connection()
                        cursor = data.cursor()
                        cursor.execute("SELECT ten , cost from wants where iduser = %s" , (self.iduser,))

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
                        data = self.get_db_connection()
                        cursor = data.cursor()
                        cursor.execute("SELECT ten, cost FROM savings WHERE iduser = %s", (self.iduser,))
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

                                data = self.get_db_connection()
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
                        pass
                except Exception as e:
                        pass

        def open_chatBot(self):
                from view.chatbot import Ui_Form as ChatBot
                self.window = QWidget()
                self.ui = ChatBot(iduser=self.iduser)
                self.ui.setupUi(self.window)
                self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

