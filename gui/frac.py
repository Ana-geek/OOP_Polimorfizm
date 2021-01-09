from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from models.fractions import Fraction


class MainWindowVec(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi(open('C:/Users/user/PycharmProjects/OOP_Polimorfizm_hw/templates/fr.ui'))

    def set_slots(self):
        self.__win.pushButton.clicked.connect(self.slot1)

    def show(self) -> None:
        self.set_slots()
        self.__win.show()

    def slot1(self):
        pass
        """
        Action for pushButton
        """
        try:
            x1 = int(self.__win.lineEdit_x1.text())
            y1 = int(self.__win.lineEdit_y1.text())

            x2 = int(self.__win.lineEdit_x2.text())
            y2 = int(self.__win.lineEdit_y2.text())

            f1 = Fraction(x1, y1)
            f2 = Fraction(x2, y2)

            result_sum = f1 + f2
            self.__win.lineEdit_add_result.setText(str(result_sum))
            print(result_sum)

            result_sub = f1 - f2
            self.__win.lineEdit_sub_result.setText(str(result_sub))
            print(result_sub)

            result_mul = f1 * f2
            self.__win.lineEdit_mul_result.setText(str(result_mul))
            print(result_mul)

            result_div = f1 / f2
            self.__win.lineEdit_div_result.setText(str(result_div))
            print(result_div)

        except ValueError:
            QMessageBox.critical(self, 'Error', 'Numbers ONLY!')
