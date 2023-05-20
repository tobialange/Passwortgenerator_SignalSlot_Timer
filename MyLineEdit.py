from PyQt6.QtWidgets import QLineEdit

class MyLineEdit(QLineEdit):
    def __init__(self, placeholderText, parent=None):
        super(MyLineEdit, self).__init__(parent)

        self.setReadOnly(True)
        self.setPlaceholderText(placeholderText)
