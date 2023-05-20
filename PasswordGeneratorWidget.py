from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSlider, QCheckBox, QErrorMessage, QLabel
from PyQt6.QtCore import pyqtSlot, QRandomGenerator, Qt, QTimer
from MyLineEdit import MyLineEdit

class PasswordGeneratorWidget(QWidget):
    generatePassword = pyqtSlot()
    generateToken = pyqtSlot()
    setLength = pyqtSlot(int)

    def __init__(self, parent=None):
        super(PasswordGeneratorWidget, self).__init__(parent)

        self.generator = QRandomGenerator.securelySeeded()
        self.errorMessage = QErrorMessage(self)

        layout = QGridLayout(self)
        self.setLayout(layout)

        generatorButton = QPushButton(self)
        generatorButton.setText("Passwort generieren")
        generatorButton.clicked.connect(self.generatePassword)

        slider = QSlider(self)
        slider.setRange(1, 128)
        slider.setOrientation(Qt.Orientation.Horizontal)
        slider.valueChanged.connect(self.setLength)
        slider.setValue(12)

        self.checkboxCharactersSmall = QCheckBox(self)
        self.checkboxCharactersSmall.setText("Kleinbuchstaben")

        self.checkboxCharactersBig = QCheckBox(self)
        self.checkboxCharactersBig.setText("Großbuchstaben")

        self.checkboxNumbers = QCheckBox(self)
        self.checkboxNumbers.setText("Ziffern")

        self.checkboxCharactersSpecial = QCheckBox(self)
        self.checkboxCharactersSpecial.setText("Sonderzeichen")

        self.passwordLine = MyLineEdit("Hier steht das Passwort", self)

        timer = QTimer(self)
        timer.start(5*1000)
        timer.timeout.connect(self.generateToken)

        self.tokenLine = MyLineEdit("Gleich kommt der Token", self)

        layout.addWidget(generatorButton, 1, 1)
        layout.addWidget(slider, 2, 1)
        layout.addWidget(self.checkboxCharactersSmall, 3, 1)
        layout.addWidget(self.checkboxCharactersBig, 4, 1)
        layout.addWidget(self.checkboxNumbers, 5, 1)
        layout.addWidget(self.checkboxCharactersSpecial, 6, 1)
        layout.addWidget(self.passwordLine, 7, 1)
        layout.addWidget(QLabel("Token"), 8, 1)
        layout.addWidget(self.tokenLine, 9, 1)

    def setLength(self, length: int):
        self.__length = length

    def generatePassword(self):
        symbols = []
        if self.checkboxCharactersSmall.isChecked() is True:
            symbols += ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        if self.checkboxCharactersBig.isChecked() is True:
            symbols += ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        if self.checkboxNumbers.isChecked() is True:
            symbols += ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        if self.checkboxCharactersSpecial.isChecked() is True:
            symbols += ('!', '§', '$', '%', '&', '/', '(', ')', '=', '?', '+', '*', '#', '-', '_')

        if len(symbols) == 0:
            self.errorMessage.showMessage("Keine Symbole ausgewählt")
        else:
            passwordString = ""
            for i in range(0, self.__length):
                index = self.generator.bounded(0, len(symbols))

                char = symbols[index]

                passwordString += char

            self.passwordLine.setText(passwordString)

    def generateToken(self):
        symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        tokenString = ""
        for i in range(0, 5):
            index = self.generator.bounded(0, len(symbols))

            char = symbols[index]

            tokenString += char

        self.tokenLine.setText(tokenString)
