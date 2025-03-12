from PySide6.QtWidgets import (QApplication, QWidget,
                               QPushButton, QLabel, QGridLayout, QDialog, QVBoxLayout,
                               QLineEdit, QDialogButtonBox, QMenuBar,)
from PySide6.QtCore import Qt, QSize
import sys

# Get player names from the user


class PlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enter Player Names')
        self.layout = QVBoxLayout()
        self.setFixedSize(QSize(400, 400))

        self.player1_input = QLineEdit(self)
        self.player1_input.setPlaceholderText('Player 1 Name')
        self.player1_input.setFixedHeight(50)
        self.layout.addWidget(self.player1_input)

        self.player2_input = QLineEdit(self)
        self.player2_input.setPlaceholderText('Player 2 Name')
        self.player2_input.setFixedHeight(50)
        self.layout.addWidget(self.player2_input)
        

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.setOrientation(Qt.Vertical)
        
        button_ok = self.buttons.button(QDialogButtonBox.Ok)
        button_ok.setText('Start Game')
        button_ok.setProperty('dialog_buttons', True)
        button_cancel = self.buttons.button(QDialogButtonBox.Cancel)
        button_cancel.setText('Exit')
        button_cancel.setProperty('dialog_buttons', True)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setAlignment(self.buttons, Qt.AlignCenter)
        self.setLayout(self.layout)

    def get_names(self):
        return self.player1_input.text(), self.player2_input.text()

# Create the main window


class Xox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XOX')
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(QSize(450,500))

        dialog = PlayerDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.player1, self.player2 = dialog.get_names()
        else:
            sys.exit()

        self.createUI()

    def createUI(self):
        self.signs = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
        self.score_text = QLabel(f'{self.player1} 0 - 0 {self.player2}')
        self.score_text.setFixedHeight(50)

        layout = QGridLayout()
        layout.addWidget(self.score_text, 0, 0, 1, 3)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setFixedSize(QSize(150, 150))
                button.setProperty('row', f'{row}')
                button.setProperty('column', f'{column}')
                button.clicked.connect(self.button_clicked)
                layout.addWidget(button, row+1, column)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def button_clicked(self):
        sender = self.sender()
        sender.setText("X")
        sender.setEnabled(False)
        print(sender.property('classes'))


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = Xox()
    
    window.show()
    sys.exit(app.exec())
