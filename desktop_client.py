import sys
import os
from PySide6 import QtWidgets


class MetallicDesktopClient(QtWidgets.QMainWindow):
    def __init__(self):
        super(MetallicDesktopClient, self).__init__()
        os.system("pyside6-uic gui.ui > gui.py")
        from gui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        

app = QtWidgets.QApplication(sys.argv)
client = MetallicDesktopClient()
sys.exit(app.exec_())