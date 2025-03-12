from PySide6.QtWidgets import (QApplication, QWidget,
                               QPushButton, QLabel, QGridLayout, QDialog, QVBoxLayout,
                               QLineEdit, QDialogButtonBox, QMenuBar,)
from PySide6.QtCore import Qt, QSize
import sys
import random

# Get player names from the user

global score
score = [0, 0]


def get_score():
    return score


def set_score(winner):
    if winner == 'X':
        score[0] += 1
    else:
        score[1] += 1


class Game():
    def __init__(self):
        self.players = []
        self.players_signs = ['X', 'O']
        self.current_player = random.choice(self.players_signs)
        self.score = get_score()
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def get_player(self):
        return self.current_player

    def switch_player(self):
        self.current_player = self.players_signs[
            0] if self.current_player == self.players_signs[1] else self.players_signs[1]

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return 'winner'

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != '':
                return 'winner'

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return 'winner'

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return 'winner'

        for row in self.board:
            if '' in row:
                return 'continue'

        return 'draw'


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
        self.game = Game()
        
        dialog = PlayerDialog()
        if dialog.exec() == QDialog.Accepted:
            self.player1, self.player2 = dialog.get_names()
            self.game.players.append(self.player1)
            self.game.players.append(self.player2)
        else:
            sys.exit()

        self.createUI()

    def createUI(self):
        self.signs = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = self.game.current_player
        self.score_text = QLabel(f'{self.player1}(X) {score[0]} - {score[1]} {self.player2}(O)')
        self.score_text.setFixedHeight(50)

        layout = QGridLayout()
        layout.addWidget(self.score_text, 0, 0, 1, 3)

        # Create buttons for the board
        self.buttons = {}
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setFixedSize(QSize(150, 150))
                button.setProperty('row', f'{row}')
                button.setProperty('column', f'{column}')
                button.clicked.connect(self.button_clicked)
                layout.addWidget(button, row + 1, column)
                self.buttons[(row, column)] = button

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Set the layout for the QWidget
        self.setLayout(layout)
        self.update()

    def button_clicked(self):
        sender = self.sender()
        cp = self.game.get_player()
        sender.setText(cp)
        self.game.board[int(sender.property('row'))][int(
            sender.property('column'))] = cp
        status = self.game.check_winner()
        
        if status == 'winner':
            set_score(cp)
            self.restart()
        elif status == 'draw':
            self.restart()
        else:
            self.game.switch_player()
            sender.setEnabled(False)

    def restart(self):
        self.game = Game()
        self.current_player = self.game.current_player
        self.score_text.setText(f'{self.player1}(X) {score[0]} - {score[1]} {self.player2}(O)')
        for row in range(3):
            for column in range(3):
                button = self.buttons[(row, column)]
                button.setText('')
                button.setEnabled(True)
        


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = Xox()
    window.show()
    sys.exit(app.exec())
