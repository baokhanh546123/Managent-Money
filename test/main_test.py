import unittest
from PyQt5 import QtWidgets
from view.ex11 import Ui_Form
import sys
import mysql.connector
class TestUiForm(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.app = QtWidgets.QApplication(sys.argv)
        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)

    def tearDown(self):
        """Clean up after each test."""
        self.form.close()
        self.app.quit()

    def test_set_iduser(self):
        """Test setting the user ID."""
        self.ui.set_iduser(7)
        self.assertEqual(self.ui.iduser, 7)

    def test_calculate_budget(self):
        """Test the budget calculation."""
        self.ui.set_iduser(7)
        self.ui.spinBox.setValue(1000000)  # Set income to 1,000,000 VND
        self.ui.doubleSpinBox.setValue(10)  # Set tax rate to 10%
        self.ui.caculate()
        result = self.ui.result_output.text()
        self.assertIn("Income after tax: 900000.00 VND", result)
        self.assertIn("Needs (50%): 450000.00 VND", result)
        self.assertIn("Wants (30%): 270000.00 VND", result)
        self.assertIn("Savings (20%): 180000.00 VND", result)

    def test_switch_to_dark_mode(self):
        """Test switching to dark mode."""
        self.ui.radioButton.setChecked(True)
        self.ui.switch_mode()
        self.assertEqual(self.ui.FrameContent.styleSheet(), """
                QWidget {
                        background-color: #2C2C2C;
                        color: #FFFFFF;
                }
                QRadioButton {
                        color: #FFFFFF;
                }
                QTextBrowser{color : #00CCCC;}
                """)

    def test_switch_to_light_mode(self):
        """Test switching to light mode."""
        self.ui.radioButton_2.setChecked(True)
        self.ui.switch_mode()
        self.assertEqual(self.ui.FrameContent.styleSheet(), """
                QWidget {
                        background-color: #FFFFFF;
                        color: #000000;
                }
                QRadioButton {
                        color: #000000;
                }
                """)

    def test_show_home_page(self):
        """Test switching to the home page."""
        self.ui.show_home()
        self.assertEqual(self.ui.stackedWidget.currentWidget(), self.ui.home_page)

    def test_show_input_page(self):
        """Test switching to the input page."""
        self.ui.show_input()
        self.assertEqual(self.ui.stackedWidget.currentWidget(), self.ui.input_page)

    def test_show_graph_page(self):
        """Test switching to the graph page."""
        self.ui.show_graph()
        self.assertEqual(self.ui.stackedWidget.currentWidget(), self.ui.graphic_page)

    def test_show_predict_page(self):
        """Test switching to the predict page."""
        self.ui.show_predict()
        self.assertEqual(self.ui.stackedWidget.currentWidget(), self.ui.predict_page)

    def test_show_setting_page(self):
        """Test switching to the setting page."""
        self.ui.setting()
        self.assertEqual(self.ui.stackedWidget.currentWidget(), self.ui.setting_page)

    def add_test_user(self):
        """Add a test user to the users table."""
        try:
            data = self.ui.get_db_connection()
            cursor = data.cursor()
            cursor.execute("INSERT INTO users (iduser, username) VALUES (%s, %s)", (7, "test_user"))
            data.commit()
        except mysql.connector.Error as e:
            print(f"Failed to add test user: {e}")
        finally:
            if data.is_connected():
                cursor.close()
                data.close()
if __name__ == "__main__":
    unittest.main()