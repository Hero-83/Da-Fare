from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date

_id_counter = 0

@dataclass
class Tareas:
    titulo: str
    fecha_limite: date
    fecha_creacion: date = field(default_factory=date.today)
    dias_retraso: int = 0
    descripcion: str = ""
    estado: str = "pendiente"
    subtareas: int | None = None
    fecha_completado: date | None = None
    id: int = field(init=False)

    def __post_init__(self):
        global _id_counter
        self.id = _id_counter
        _id_counter += 1


