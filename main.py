from PySide6.QtWidgets import (QApplication, QWidget,
                               QPushButton, QLabel, QGridLayout, QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox)
import sys


class PlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enter Player Names')
        self.layout = QVBoxLayout()

        self.player1_input = QLineEdit(self)
        self.player1_input.setPlaceholderText('Player 1 Name')
        self.layout.addWidget(self.player1_input)

        self.player2_input = QLineEdit(self)
        self.player2_input.setPlaceholderText('Player 2 Name')
        self.layout.addWidget(self.player2_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

    def get_names(self):
        return self.player1_input.text(), self.player2_input.text()


class Xox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XOX')
        self.setGeometry(100, 100, 400, 400)

        dialog = PlayerDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.player1, self.player2 = dialog.get_names()
        else:
            sys.exit()

        self.createUI()

    def createUI(self):
        self.signs = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
        self.result_field = QLabel()
        self.result_field.setText(f'{self.current_player} turn')

        layout = QGridLayout()
        layout.addWidget(self.result_field, 0, 0, 0, 3)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setProperty('classes', 'row column')
                button.clicked.connect(self.button_clicked)
                layout.addWidget(button, row+1, column)
        
        self.setLayout(layout)

    def button_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Xox()
    window.show()
    sys.exit(app.exec_())
