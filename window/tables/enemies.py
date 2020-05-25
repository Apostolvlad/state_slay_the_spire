from .table_state import TableState
from parsers import get_enemies, ErrorFinish

class Enemies(TableState):
    o = None
    def __init__(self, parent, name_char):
        o = self
        super().__init__(parent, 'Враги', ('Название', 'Этаж', 'Всего боёв', 'Поражений', 'Шанс победы'), name_char)
        self.update()
    
    def update(self):
        try:
            for e in get_enemies(name = self.name_char):
                self.add_row(e)
        except ErrorFinish:
            print(self.name_char)
            return 0

