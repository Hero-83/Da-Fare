import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Controlador"))
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea
from Controlador_De_Tareas import Controlador_De_Tareas
from Vista_Creacion import Vista_Creacion
from Widget_Tarea import Widget_Tarea

class Vista_Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Da Fare")
        self.setMinimumSize(400, 600)

        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: #eeecf4;")
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)

        titulo = QLabel("DA FARE")
        titulo.setStyleSheet("font-size: 28px; font-weight: bold; color: #1a1a2e;")
        layout.addWidget(titulo)

        barra = QHBoxLayout()
        barra.setContentsMargins(0, 0, 0, 0)
        barra.setSpacing(0)
        barra_widget = QWidget()
        barra_widget.setStyleSheet("background: white; border-radius: 12px;")
        barra_inner = QHBoxLayout(barra_widget)
        barra_inner.setContentsMargins(12, 4, 4, 4)
        self.busqueda = QLineEdit()
        self.busqueda.setPlaceholderText("🔍 Buscar...")
        self.busqueda.setStyleSheet("border: none; background: transparent; padding: 4px;")
        self.btn_agregar = QPushButton("+")
        self.btn_agregar.setFixedSize(40, 40)
        self.btn_agregar.setStyleSheet("""
            QPushButton {
                background-color: #7c6fcd;
                color: white;
                font-size: 24px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover { background-color: #6a5db8; }
        """)
        barra_inner.addWidget(self.busqueda)
        barra_inner.addWidget(self.btn_agregar)
        barra.addWidget(barra_widget)
        layout.addLayout(barra)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none; background: transparent;")
        self.contenedor_tareas = QWidget()
        self.contenedor_tareas.setStyleSheet("background: transparent;")
        self.layout_tareas = QVBoxLayout(self.contenedor_tareas)
        self.layout_tareas.setSpacing(8)
        self.layout_tareas.addStretch()
        scroll.setWidget(self.contenedor_tareas)
        layout.addWidget(scroll)

        self.controlador = Controlador_De_Tareas()
        self.btn_agregar.clicked.connect(self.abrir_creacion)

    def abrir_creacion(self):
        dialogo = Vista_Creacion(self.controlador, self)
        if dialogo.exec():
            self.refrescar_tareas()

    def refrescar_tareas(self):
        self.controlador.actualizar_estado_tareas()
        while self.layout_tareas.count() > 1:
            item = self.layout_tareas.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        for tarea in self.controlador.lista.LT:
            print(f"[DEBUG] ID:{tarea.ID} | T:{tarea.T} | DT:{tarea.DT} | FL:{tarea.FL} | FC:{tarea.FC} | E:{tarea.E} | SUBT:{tarea.SUBT} | FCOMP:{tarea.FCOMP}")
            widget = Widget_Tarea(tarea, self.controlador)
            self.layout_tareas.insertWidget(self.layout_tareas.count() - 1, widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Vista_Principal()
    ventana.show()
    sys.exit(app.exec())
