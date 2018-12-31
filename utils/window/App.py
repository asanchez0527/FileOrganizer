import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenuBar
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from utils.window.Menu import MenuBar


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = 'MoviePlex'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        menuBar = MenuBar(self)
        self.show()




