from Tareas import Tareas
from dataclasses import dataclass, field

@dataclass
class Lista_Tareas:
    tareas: list[Tareas] = field(default_factory=list)

    def agregar_tarea(self, tarea: Tareas):
        self.tareas.append(tarea)
