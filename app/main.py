import sys
from models.fractions import Fraction
from PyQt5.QtWidgets import QApplication
from gui.frac import MainWindowVec


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindowVec()
    win.show()

    sys.exit(app.exec())



