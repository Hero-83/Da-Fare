class Controlador_ID:
    def __init__(self):
        self.__ID = 0

    def get_id(self) -> int:
        self.__ID += 1
        return self.__ID
