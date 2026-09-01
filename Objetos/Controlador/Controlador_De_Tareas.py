import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Modelo"))
from Tareas import Tareas
from datetime import date
from Lista_Tareas import Lista_Tareas

class Controlador_De_Tareas:
    def __init__(self):
        self.lista = Lista_Tareas()

    def crear_tarea(self, titulo: str, descripcion: str, fecha_limite: date):
        tarea = Tareas(titulo=titulo, fecha_limite=fecha_limite, descripcion=descripcion)
        self.lista.agregar_tarea(tarea)
        return tarea

    def obtener_tarea(self, id: int) -> Tareas | None:
        for tarea in self.lista.tareas:
            if tarea.id == id:
                return tarea
        return None

    def completar_tarea(self, id: int):
        tarea = self.obtener_tarea(id)
        if tarea is None:
            return
        tarea.fecha_completado = date.today()
        if tarea.fecha_completado > tarea.fecha_limite:
            tarea.estado = "Completo con retraso"
        else:
            tarea.estado = "Completado"

    def actualizar_estado_tareas(self):
        for tarea in self.lista.tareas:
            if tarea.estado == "pendiente" and date.today() > tarea.fecha_limite:
                tarea.estado = "Atrasado"
                tarea.dias_retraso = (date.today() - tarea.fecha_limite).days
        return None

    def descompletar_tarea(self, id: int):
        tarea = self.obtener_tarea(id)
        if tarea is None:
            return
        tarea.fecha_completado = None
        tarea.estado = "Atrasado" if date.today() > tarea.fecha_limite else "pendiente"