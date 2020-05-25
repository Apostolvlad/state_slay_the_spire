from .window import Window

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton

from .tab_state import TabState
from parsers import get_character_name
from .tables import TABLES
from .tables.table_state import TableState
class WindowMain(Window): #
    def __init__(self):
        super().__init__(None, 'AS for Slay The Spire', (650, 500), 12)

        self.layout1 = QVBoxLayout(self.widget)
        self.layout1.setContentsMargins(10, 10, 10, 10)
        

        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()

        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout3)


        self.tab_widget = QTabWidget()
        self.layout2.addWidget(self.tab_widget)
        
        state_names = get_character_name()
        for table in TABLES:self.tab_widget.addTab(TabState(self.tab_widget, state_names, table), table.name)



        code_button = dict()
        code_button.update({'Загрузить':self})
        code_button.update({'Очистить':self})
        code_button.update({'Помощь':self})
        code_button.update({'Создатель':self})

        for e in code_button.items():
            btn = QPushButton()
            btn.setText(e[0])
            self.layout3.addWidget(btn)

        self.setLayout(self.layout1)

        #self.vertical_layout.addWidget(self._control_panel)
        #TABLES[0].o.update()
        

    def closeEvent(self, event):         
        pass #self._manager_bot.stop_all()

    

     #   self.show()