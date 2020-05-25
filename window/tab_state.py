'''
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QTabWidget

'''
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

class TabState(QWidget):
    def __init__(self, parent, names, table):
        super().__init__(parent)
        self.layout1 = QVBoxLayout(self)
        self.tab_widget = QTabWidget()
        self.layout1.addWidget(self.tab_widget)

        for name in names: self.tab_widget.addTab(table(self, name), name)
        '''
        self._names = names

        self._tables = list()
        for name in self._names: 
            t = table(self, name)
            self._tables.append(t)
            self.tab_widget.addTab(t, name)
        '''
        self.setLayout(self.layout1)
