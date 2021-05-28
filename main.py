from PIL import Image
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTextEdit
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QButtonGroup, QComboBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image, ImageDraw
import os
import shutil
from color import MyColor
import numpy as np


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем дизайн
        uic.loadUi('design.ui', self)
        self.x = 4
        # Имя картинки
        self.name = "Ванная комната"
        self.initUI()
        # переносим картинки из папки data в папку user
        self.copy_files()
        # изначально цвет заливки участка изображения - чёрный
        self.color = (255, 255, 255)
        # изначально функция раскрашивания недоступна
        self.paint = False

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
