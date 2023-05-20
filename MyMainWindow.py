from PyQt6.QtWidgets import QMainWindow
from PasswordGeneratorWidget import PasswordGeneratorWidget


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Passwortgenerator")

        self.setCentralWidget(PasswordGeneratorWidget(self))
