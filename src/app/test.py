import unittest
from PyQt5.QtWidgets import QApplication
from ex11 import Ui_Form as Main

class TestYourClassName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.window = Main()

    def test_predict(self):
        
        self.window.comboBox.setCurrentIndex(0)
        
        
        self.window.predict()
        self.assertEqual(self.window.stackedWidget_3.currentIndex(), 0)

    def test_caculate(self):
        self.window.spinBox.setValue(1000000)
        self.window.doubleSpinBox.setValue(10)
        self.window.caculate()
        self.assertEqual(self.window.needs, 450000)
        self.assertEqual(self.window.wants, 270000)
        self.assertEqual(self.window.savings, 180000)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

if __name__ == '__main__':
    unittest.main()