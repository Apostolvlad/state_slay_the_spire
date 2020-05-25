from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem

class TableState(QTableWidget):
    tables = dict()
    def __init__(self, parent, name, colomn_names, name_char):
        TableState.name = name
        TableState.tables.update({name:self})
        super().__init__(parent)
        self.name_char = name_char
        self.verticalHeader().setVisible(False)

        self.setColumnCount(len(colomn_names))
        self.setHorizontalHeaderLabels(colomn_names)

    def add_row(self, texts):
        index = self.rowCount()
        self.setRowCount(self.rowCount() + 1)
        for i, e in enumerate(texts):
            self.setItem(index, i, QTableWidgetItem(str(e)))
        #print(self.select)
            #self.setItem(index, i, QTableWidgetItem(e))
            #self.setItem(index, i, QTableWidgetItem(e))
    
    def update(self):
        pass

    @classmethod
    def update(cls):
        print(cls.tables.values())
        for e in cls.tables.values():
            e.update()
