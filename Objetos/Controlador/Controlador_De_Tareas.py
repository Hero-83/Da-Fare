import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Modelo"))
from Tareas import Tareas
from datetime import date
from Lista_Tareas import Lista_Tareas

class Controlador_De_Tareas:
    def __init__(self):
        self.lista = Lista_Tareas()

    def crear_tarea(self, titulo: str, descripcion: str, fecha_limite: date):
        tarea = Tareas(T=titulo, FL=fecha_limite, DT=descripcion)
        self.lista.agregar_tarea(tarea)
        return tarea

    def obtener_tarea(self, ID: int) -> Tareas | None:
        for tarea in self.lista.LT:
            if tarea.ID == ID:
                return tarea
        return None

    def completar_tarea(self, ID: int):
        tarea = self.obtener_tarea(ID)
        if tarea is None:
            return
        tarea.FCOMP = date.today()
        if tarea.FCOMP > tarea.FL:
            tarea.E = "Completo con retraso"
        else:
            tarea.E = "Completado"

    def actualizar_estado_tareas(self):
        for tarea in self.lista.LT:
            if tarea.E == "pendiente" and date.today() > tarea.FL:
                tarea.E = "Atrasado"
                tarea.DP = (date.today() - tarea.FL).days
        return None

        
    def descompletar_tarea(self, ID: int):
        tarea = self.obtener_tarea(ID)
        if tarea is None:
            return
        tarea.FCOMP = None
        tarea.E = "Atrasado" if date.today() > tarea.FL else "pendiente"