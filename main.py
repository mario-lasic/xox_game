from PySide6.QtWidgets import (QApplication, QWidget, 
                               QPushButton, QLabel, QGridLayout)
import sys

class Xox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('XOX')
        self.setGeometry(100, 100, 400, 400)

        self.createUI()

    
    def createUI(self):
        self.signs = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'

        layout = QGridLayout()
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setProperty('classes', 'row column')
                button.clicked.connect(self.button_clicked)
                layout.addWidget(button, row, column)
        
        self.setLayout(layout)

    def button_clicked(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Xox()
    window.show()
    sys.exit(app.exec_())