from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTextBrowser, QVBoxLayout, QScrollArea
import json
import os
import mysql.connector
import view.image
import view.image1

class Ui_Form(object):
    def __init__(self, iduser=None):
        super().__init__()
        self.iduser = iduser
        self.data_file = "D:/python/PyQt5/Project2/SC_pyqt5_LoginUI2-main/App/src/config/chatbot_data.json"
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        
        self.verticalLayout = QVBoxLayout(Form)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        
        self.chatDisplay = QTextBrowser()
        self.chatDisplay.setStyleSheet("font-size: 14px; padding: 10px;")
        self.scrollArea.setWidget(self.chatDisplay)
        
        self.inputBox = QtWidgets.QLineEdit(Form)
        self.inputBox.setPlaceholderText("Prompt...")
        self.inputBox.setStyleSheet("font-size: 14px; padding: 5px;")
        self.inputBox.returnPressed.connect(self.chat)
        
        self.sendButton = QtWidgets.QPushButton("Send", Form)
        self.sendButton.clicked.connect(self.chat)
        self.sendButton.setStyleSheet("padding: 5px; font-size: 14px;")
        
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.inputBox)
        self.verticalLayout.addWidget(self.sendButton)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                return
    
    def get_db_connection(self):
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password="10112005",
                database="chat_app"
            )
    
    def chat(self):
        chat_info = self.inputBox.text().strip().lower()
        if not chat_info:
            return 
        
        self.chatDisplay.append(f"<b>You:</b> {chat_info}")
        response = self.get_response(chat_info)
        
        if response:
            self.chatDisplay.append(f"<b>Bot:</b> {response}")
        else:
            QMessageBox.warning(None, "Bot don't learn", "Please teach the bot to answer")
        
        self.inputBox.clear()
        self.chatDisplay.verticalScrollBar().setValue(self.chatDisplay.verticalScrollBar().maximum())
    
    def fetch_username(self):
        try:
            data = self.get_db_connection()
            cursor = data.cursor()
            cursor.execute("SELECT username FROM users WHERE iduser = %s LIMIT 1", (self.iduser,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Guest"
        except mysql.connector.Error as error:
            return "Guest"
        
    def fetch_cost(self, table_name, ten ):
        if table_name not in ["needs", "wants", "savings"]:
                QMessageBox.warning(None, "Error", "Invalid list type.")
                return
        try:
            data = data = self.get_db_connection()
            cursor = data.cursor()
            cursor.execute("SELECT cost FROM {} WHERE iduser = %s OR ten LIKE %s ORDER BY times LIMIT 1".format(table_name), (self.iduser, f"%{ten}%"))
            result = cursor.fetchone()
            if result is not None :
                return result[0]
        except mysql.connector.Error as error:
            QMessageBox.warning(None, "Error", f"Failed to add: {error}")
        finally:
            cursor.close()
            data.close()
    
        
    def fetch_add_list(self, table_name, ten , cost):
        if table_name not in ["needs", "wants", "savings"]:
                QMessageBox.warning(None, "Error", "Invalid list type.")
                return
        try:
            data = self.get_db_connection()
            cursor = data.cursor()
            cursor.execute("INSERT INTO {} (iduser, ten, cost, times) VALUES (%s, %s, %s, NOW())".format(table_name), (self.iduser, ten, cost))
            data.commit()
            QMessageBox.information(None, "Success", "Added Successfully")
            
        except mysql.connector.Error as error:
            QMessageBox.warning(None, "Error", f"Failed to add: {error}")
        finally:
            cursor.close()
            data.close()
    
    def fetch_remove_list(self, table_name, ten, cost):
        if table_name not in ["needs", "wants", "savings"]:
                QMessageBox.warning(None, "Error", "Invalid list type.")
                return
        try:
            data = self.get_db_connection()
            cursor = data.cursor()
            cursor.execute("SELECT COUNT(*) FROM {} WHERE iduser = %s".format(table_name), (self.iduser,))
            result = cursor.fetchone()
            if result[0] == 0 :
                QMessageBox.warning("No data")
            else:
                cursor.execute("DELETE FROM {} WHERE ten = %s AND cost = %s AND iduser = %s".format(table_name), (ten, cost, self.iduser))
                data.commit()
                QMessageBox.information(None, "Success", "Removed Successfully")
        except mysql.connector.Error as error:
            QMessageBox.warning(None, "Error", f"Failed to remove: {error}")
        finally:
            cursor.close()
            data.close()
            
    def check_budget(self, list_type, cost):
        try:
            data = self.get_db_connection()
            cursor = data.cursor()
            cursor.execute(f"SELECT {list_type} FROM stoge_data WHERE iduser = %s ORDER BY times DESC", (self.iduser,))
            budget = cursor.fetchone()
            cursor.fetchall()

            if budget:
                budget_amount = budget[0]
                cursor.execute(f"SELECT SUM(cost) AS Total_cost FROM {list_type} WHERE iduser = %s", (self.iduser,))
                total_cost = cursor.fetchone()
                if total_cost and total_cost[0] is not None:
                    if total_cost[0] + cost > budget_amount:
                        QMessageBox.warning(None, "Warning", f"Total cost of {list_type} ({total_cost[0] + cost}) exceeds your budget ({budget_amount})")
                        QMessageBox.information(None, "Notify", "If you continue to add to the list, you will exceed your budget.")
                        return False
            return True
        except mysql.connector.Error as e:
            QMessageBox.warning(None, "Database Error", f"Database error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if data and data.is_connected():
                data.close()
    
    def add_list(self, chat_info):
        if chat_info.startswith("add"):
            parts = chat_info.split()
            if len(parts) < 3:
                return "Error: Syntax should be 'add (needs|wants|savings) (name) (cost)'"

            list_type = parts[1]
            if list_type not in ["needs", "wants", "savings"]:
                return "Error: List type must be 'needs', 'wants', or 'savings'."
            try:
                cost = float(parts[-1])                  
                ten = " ".join(parts[2:-1]).strip().lower()  
                if not ten:
                    return "Error: Name cannot be empty."
                if not self.check_budget(list_type,cost):
                    return f"Error: Total cost of {list_type} exceeds your budget."
                
                self.fetch_add_list(list_type, ten, cost)
                return f"Added '{ten}' with cost {cost} to the list of {list_type}."
            except ValueError:
                return "Error: Cost must be a valid number."
        return None
    
    def remove_list(self, chat_info):
        if chat_info.startswith("remove"):
            parts = chat_info.split()
            if len(parts) < 3:
                return "Error: Syntax should be 'remove (needs|wants|savings) (name) (cost)'"

            list_type = parts[1]
            if list_type not in ["needs", "wants", "savings"]:
                return "Error: List type must be 'needs', 'wants', or 'savings'."

            try:
                cost = float(parts[-1])
                ten = " ".join(parts[2:-1]).strip()
                if not ten:
                    return "Error: Name cannot be empty."

                cost_check = self.fetch_cost(list_type, ten)
                if cost_check is not None and cost != cost_check:
                    response, ok = QtWidgets.QInputDialog.getText(None, "Confirm Cost", f"You mean {cost_check}. Do you want to fix it? (y/n):")
                    if ok and response.strip().lower() == "y":
                        cost = cost_check
                    elif ok and response.strip().lower() == "n":
                        return "Removal canceled."

                self.fetch_remove_list(list_type, ten, cost)
                return f"Removed '{ten}' with cost {cost} from the list of {list_type}."
            except ValueError:
                return "Error: Cost must be a valid number."

        return None


    def get_response(self, chat_info):
        if chat_info.lower() in ["hi", "hello"]:
            username = self.fetch_username()
            return f"Hello, {username}! Can I help you?"
        
        add_response = self.add_list(chat_info)
        if add_response:

            return add_response
        
        remove_response = self.remove_list(chat_info)
        if remove_response:
            return remove_response
        
        for keyword in self.data.keys():
            if keyword in chat_info:
                return self.data[keyword]

        response, ok = QtWidgets.QInputDialog.getText(None, "Teach the bot", f"What should the bot respond to '{chat_info}'?")
        if ok and response:
            self.data[chat_info] = response
            with open(self.data_file, "w") as file:
                json.dump(self.data, file)
            return response
        else:
            return None
    
    def retranslateUi(self, Form):
        Form.setWindowTitle("CHATBOT")
        Form.setWindowIcon(QtGui.QIcon("D:\\python\\PyQt5\\Project2\\SC_pyqt5_LoginUI2-main\\App\\image\\chatbot.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())