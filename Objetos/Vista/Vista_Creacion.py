from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateEdit
from PyQt6.QtCore import QDate

class Vista_Creacion(QDialog):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        self.controlador = controlador
        self.setWindowTitle("Nueva Tarea")
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Título"))
        self.input_titulo = QLineEdit()
        layout.addWidget(self.input_titulo)

        layout.addWidget(QLabel("Descripción"))
        self.input_descripcion = QLineEdit()
        layout.addWidget(self.input_descripcion)

        layout.addWidget(QLabel("Fecha límite"))
        self.input_fecha = QDateEdit()
        self.input_fecha.setCalendarPopup(True)
        self.input_fecha.setDate(QDate.currentDate())
        layout.addWidget(self.input_fecha)

        self.btn_crear = QPushButton("Crear")
        self.btn_crear.clicked.connect(self.crear)
        layout.addWidget(self.btn_crear)

    def crear(self):
        from datetime import date
        titulo = self.input_titulo.text()
        descripcion = self.input_descripcion.text()
        q = self.input_fecha.date()
        fecha_limite = date(q.year(), q.month(), q.day())
        self.controlador.crear_tarea(titulo, descripcion, fecha_limite)
        self.accept()
