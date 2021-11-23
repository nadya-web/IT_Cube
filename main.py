import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        uic.loadUi('calc.ui', self)
        self.btns = self.findChildren(QPushButton)
        self.expression = ''
        self.init_Ui()

    def init_Ui(self) -> None:
        # Привязка функций к кнопкам
        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.show_result)

    def show_result(self) -> None:
        sender = self.sender()
        if ord('0') <= ord(sender.text()) <= ord('9'):
            self.table.display(sender.text())
            self.expression += sender.text()
        elif sender.text() == 'С':
            self.expression = ''
            self.table.display(0)
        elif sender.text() == '=':
            if '/0' in self.expression:
                self.error = Error('На ноль делить нельзя!')
                self.error.show()
            if '√-' in self.expression:
                self.error = Error('Корень из отрицательного числа - это комплексное число!')
                self.error.show()
            else:
                self.table.display(eval(self.expression))
        else:
            self.expression += sender.text()


class Error(QWidget):
    def __init__(self, error) -> None:
        super(Error, self).__init__()
        self.setWindowTitle('ошибка!')
        self.main_layout = QVBoxLayout(self)
        self.text = QLabel(error, self)
        self.main_layout.addWidget(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
