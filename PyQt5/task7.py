import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QRadioButton, QVBoxLayout


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        uic.loadUi('create_flag.ui', self)
        self.color_btns = self.findChildren(QRadioButton)
        self.create_btn = self.findChildren(QPushButton)[0]
        self.result = self.findChildren(QLabel)[1]
        self.result.setVisible(False)
        self.init_Ui()

    def init_Ui(self) -> None:
        # Привязка функций к кнопкам
        self.create_btn.clicked.connect(self.show_result)

    def show_result(self):
        self.checkbox_list = list(filter(lambda checkbox: checkbox.isChecked(), self.color_btns))
        if len(self.checkbox_list) == 3:
            self.result.setText(f'Цвет: {self.checkbox_list[0].text()}, {self.checkbox_list[1].text()}, {self.checkbox_list[2].text()}')
            self.result.setVisible(True)
        else:
            self.error = Error()
            self.error.show()


class Error(QWidget):
    def __init__(self) -> None:
        super(Error, self).__init__()
        self.setWindowTitle('ошибка!')
        self.main_layout = QVBoxLayout(self)
        self.text = QLabel('вы выбрали слишком мало цветов!', self)
        self.main_layout.addWidget(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
