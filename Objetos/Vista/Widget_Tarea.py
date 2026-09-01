from PyQt6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QVBoxLayout

class Widget_Tarea(QWidget):
    def __init__(self, tarea, controlador, parent=None):
        super().__init__(parent)
        self.tarea = tarea
        self.controlador = controlador

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)

        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("""
            QCheckBox::indicator { width: 24px; height: 24px; border-radius: 6px; border: 2px solid #7c6fcd; }
            QCheckBox::indicator:checked { background-color: #7c6fcd; }
        """)
        self.checkbox.stateChanged.connect(self.al_cambiar)
        layout.addWidget(self.checkbox)

        textos = QVBoxLayout()
        self.label_titulo = QLabel(tarea.titulo)
        self.label_titulo.setStyleSheet("font-weight: bold; font-size: 15px;")
        self.label_desc = QLabel(tarea.descripcion)
        self.label_desc.setStyleSheet("font-size: 13px; color: #555;")
        textos.addWidget(self.label_titulo)
        textos.addWidget(self.label_desc)
        layout.addLayout(textos)
        self.setStyleSheet("background: white; border-radius: 12px;")
        self.actualizar_estilo()

    def al_cambiar(self, estado):
        if estado:
            self.controlador.completar_tarea(self.tarea.id)
        else:
            self.controlador.descompletar_tarea(self.tarea.id)
        print(f"[DEBUG] id:{self.tarea.id} | estado:{self.tarea.estado} | fecha_completado:{self.tarea.fecha_completado}")
        self.actualizar_estilo()

    def actualizar_estilo(self):
        estilos = {
            "pendiente":            "color: black; background: transparent;",
            "Atrasado":             "color: red; background: transparent;",
            "Completado":           "color: black; background: #d0d0d0;",
            "Completo con retraso": "color: red; background: #d0d0d0;",
        }
        self.setStyleSheet(estilos.get(self.tarea.estado, ""))
