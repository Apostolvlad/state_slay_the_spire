from parsers import get_folder

from window import WindowMain


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication #QMainWindow, QTextEdit, QAction, 
    import sys
    app = QApplication(sys.argv)
    ex = WindowMain()
    ex.show()
    sys.exit(app.exec_())
