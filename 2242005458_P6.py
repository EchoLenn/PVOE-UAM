from PySide6.QtWidgets import    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,QRadioButton, QFormLayout, QGridLayout, QVBoxLayout, QMainWindow
import sys
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica 6")

 
        layout = QFormLayout()
        layout.addRow(QLabel("Matricula:"), QLineEdit())
        layout.addRow(QLabel("Nombre:"), QLineEdit())
        layout.addRow(QLabel("Apellidos:"), QLineEdit())

        unidad_label = QLabel("Unidad:")
        unidad_label.setAlignment(Qt.AlignCenter)
        azc = QRadioButton("Azc")
        xoc = QRadioButton("Xoc")
        izt = QRadioButton("Izt")
        unidad_layout = QVBoxLayout()
        unidad_layout.addWidget(azc)
        unidad_layout.addWidget(xoc)
        unidad_layout.addWidget(izt)

        division_label = QLabel("Division:")
        division_label.setAlignment(Qt.AlignCenter)
        cbi = QRadioButton("CBI")
        csh = QRadioButton("CSH")
        cyad = QRadioButton("CyAD")
        division_layout = QVBoxLayout()
        division_layout.addWidget(cbi)
        division_layout.addWidget(csh)
        division_layout.addWidget(cyad)

        grid_layout = QGridLayout()
        grid_layout.addWidget(unidad_label, 0, 0)
        grid_layout.addLayout(unidad_layout, 1, 0)
        grid_layout.addWidget(division_label, 0, 1)
        grid_layout.addLayout(division_layout, 1, 1)

        layout.addRow(grid_layout)
        layout.addRow(QLabel("Asunto:"), QLineEdit())
        layout.addRow(QLabel("Mensaje:"), QTextEdit())



        widget_principal = QWidget()
        widget_principal.setLayout(layout)
        self.resize(400, 350)
        self.setMinimumSize(QSize(300, 250))
        self.setMaximumSize(QSize(600, 500))

        self.setCentralWidget(widget_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())