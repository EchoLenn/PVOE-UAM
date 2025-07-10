from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,QLineEdit, QTextEdit, QPushButton, QLabel,QVBoxLayout, QFormLayout, QGridLayout)
from PySide6.QtCore import Qt, Slot
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica 7")
        self.setFixedSize(800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        form_layout = QFormLayout()

        self.fecha_input = QLineEdit()
        self.fecha_input.setFixedSize(250, 30)

        self.matricula_input = QLineEdit()
        self.matricula_input.setFixedSize(250, 30)

        self.nombre_input = QLineEdit()
        self.nombre_input.setFixedSize(250, 30)

        self.mensaje_input = QTextEdit()
        self.mensaje_input.setFixedSize(250, 200)

        self.enviar_btn = QPushButton("Enviar Mensaje")
        self.enviar_btn.setFixedSize(300, 40)
        self.enviar_btn.clicked.connect(self.enviar_mensaje)

        form_layout.addRow("Fecha:", self.fecha_input)
        form_layout.addRow("Matricula:", self.matricula_input)
        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Mensaje:", self.mensaje_input)
        form_layout.addRow(self.enviar_btn)

        mensaje_layout = QVBoxLayout()

        self.titulo_label = QLabel("Mensajes UAM")
        self.titulo_label.setFixedSize(300, 40)
        

        self.mensajes_label = QLabel()
        self.mensajes_label.setFixedSize(300, 400)
        self.mensajes_label.setAlignment(Qt.AlignTop)
        self.mensajes_label.setWordWrap(True)
        self.mensajes_label.setText("")

        mensaje_layout.addWidget(self.titulo_label)
        mensaje_layout.addWidget(self.mensajes_label)

        grid_layout.addLayout(form_layout, 0, 0)
        grid_layout.addLayout(mensaje_layout, 0, 1)
    @Slot()
    def enviar_mensaje(self):
        fecha = self.fecha_input.text()
        matricula = self.matricula_input.text()
        nombre = self.nombre_input.text()
        mensaje = self.mensaje_input.toPlainText()

        nuevo_texto = (
            f"Fecha: {fecha}\n"
            f"Matricula: {matricula}\n"
            f"Nombre: {nombre}\n"
            f"Mensaje: {mensaje}\n"
            f"---------------------\n\n"
        )

        actual = self.mensajes_label.text()
        self.mensajes_label.setAlignment(Qt.AlignTop)
        self.mensajes_label.setText(actual + nuevo_texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
