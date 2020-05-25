from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QTabWidget

class TableHero(QTableWidget):
    def __init__(self, parent, colomns):
        super().__init__(parent)
        self.verticalHeader().setVisible(False)
        self.setColumnCount(len(colomns))
        self.setHorizontalHeaderLabels(colomns)

    def add_row(self, index, texts):
        self.setRowCount(self.rowCount() + 1)
        for i, e in enumerate(texts):
            self.setItem(index, i, QTableWidgetItem(e))
            self.setItem(index, i, QTableWidgetItem(e))
            self.setItem(index, i, QTableWidgetItem(e))
    
 

class Tab(QWidget):
    def __init__(self, parent, colomns):
        super().__init__(parent)
        self.layout1 = QVBoxLayout(self)

        self.tab_widget = QTabWidget()
        self.layout1.addWidget(self.tab_widget)
        
        self._tables = dict()
        for name in ('Латоносец', 'Безмолвная', 'Дефект', 'Соцерцающая'):
            self.tab_widget.addTab(TableHero(self, name, colomns), name)




        self.setLayout(self.layout1)
        
    
