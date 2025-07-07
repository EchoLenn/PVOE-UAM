import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Primer")
        self.setFixedSize(QSize(200, 120))

        display = QLineEdit()

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_c = QPushButton("C")
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_plus = QPushButton("+")
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_minus = QPushButton("-")
        button_0 = QPushButton("0")
        button_equal = QPushButton("=")

        layout = QGridLayout()

        layout.addWidget(display, 0, 0, 1, 4)
        layout.addWidget(button_1, 1, 0)
        layout.addWidget(button_2, 1, 1)
        layout.addWidget(button_3, 1, 2)
        layout.addWidget(button_c, 1, 3)
        layout.addWidget(button_4, 2, 0)
        layout.addWidget(button_5, 2, 1)
        layout.addWidget(button_6, 2, 2)
        layout.addWidget(button_plus, 2, 3)
        layout.addWidget(button_7, 3, 0)
        layout.addWidget(button_8, 3, 1)
        layout.addWidget(button_9, 3, 2)
        layout.addWidget(button_minus, 3, 3)
        layout.addWidget(button_0, 4, 0)
        layout.addWidget(button_equal, 4, 1, 1, 2)

        widget_principal = QWidget()
        widget_principal.setLayout(layout)
        self.setCentralWidget(widget_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()