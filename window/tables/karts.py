from .table_state import TableState

class Karts(TableState):
    o = None
    def __init__(self, parent, info_type):
        o = self
        super().__init__(parent, 'Карты', ('Название', 'Всего', 'Взятых', 'Невзятых', 'Соотношение'), info_type)