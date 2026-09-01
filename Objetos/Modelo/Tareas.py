from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date

_id_counter = 0

@dataclass
class Tareas:
    T: str
    FL: date
    FC: date = field(default_factory=date.today)
    DP: int = 0
    DT: str = ""
    E: str = "pendiente"
    SUBT: int | None = None
    FCOMP: date | None = None
    ID: int = field(init=False)

    def __post_init__(self):
        global _id_counter
        self.ID = _id_counter
        _id_counter += 1


