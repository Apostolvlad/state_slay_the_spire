from .tab import Tab

class Karts(Tab):
    def __init__(self, parent):
        super().__init__(parent, 'Карты')
        #self.set_headers(('Название', 'Всего', 'Брали', 'Не брали', '%'))

        #self.add_row(0, (' - ', ' - ', ' -', ' -', ' -'))