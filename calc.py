from math import factorial
from decimal import Decimal
import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLCDNumber
from PyQt5 import uic


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.l_num = 0
        self.r_num = 0
        self.r_input = ''
        self.sign = ''

        grid = self.gridLayout
        for i in range(grid.rowCount()):
            for j in range(grid.columnCount()):
                button = grid.itemAtPosition(i, j).widget()
                print(button.objectName())
                if (i < 3 and j < 3) or (i == 3 and j == 0) or (i == 3 and j == 1):
                    button.clicked.connect(self.OnClickNum)
                else:
                    button.clicked.connect(self.OnClickSign)

    def OnClickSign(self):
        sign = self.sender().text()
        if sign == 'С':
            self.l_num = 0
            self.r_num = 0
            self.r_input = ''
            self.sign = ''
            self.table.display(self.l_num)
        elif sign == '√':
            if self.r_input == '':
                self.r_num = self.l_num
                self.l_num = 0
            else:
                self.r_num = Decimal(self.r_input)

            if self.r_num >= 0:
                self.r_num = self.r_num ** 0.5
                self.r_input = ''
                self.table.display(self.r_num)
            else:
                self.table.display('error')
        elif sign == '!':
            if self.r_input == '':
                self.r_num = self.l_num
                self.l_num = 0
            else:
                self.r_num = Decimal(self.r_input)

            if self.r_num >= 0:
                self.r_num = factorial(int(self.r_num))
                self.r_input = ''
                self.table.display(self.r_num)
            else:
                self.table.display('error')
        else:
            error = ''
            if self.sign == '':
                self.l_num = 0 if self.r_input == '' else Decimal(self.r_input)
                self.r_num = 0
                self.r_input = ''
            else:
                if self.r_input != '':
                    self.r_num = Decimal(self.r_input)
                self.r_input = ''

                if self.sign == '+':
                    self.l_num = self.l_num + self.r_num
                elif self.sign == '-':
                    self.l_num = self.l_num - self.r_num
                elif self.sign == '*':
                    self.l_num = self.l_num * self.r_num
                elif self.sign == '/':
                    if self.r_num != 0:
                        self.l_num = self.l_num / self.r_num
                    else:
                        error = 'error'
                elif self.sign == '^':
                    self.l_num = self.l_num ** self.r_num

                self.r_num = 0

            self.sign = sign
            if error:
                self.table.display(error)
            else:
                self.table.display(str(self.l_num))

    def OnClickNum(self):
        text = self.sender().text()
        if text == '.':
            if '.' in self.r_input:
                return
        self.r_input += text
        self.table.display(self.r_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
