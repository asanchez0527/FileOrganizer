from PyQt5.QtWidgets import QAction, QMenuBar
from utils.file_system.scan_directory import scan_directory



class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__()
        QMenuBar.__init__(self, parent)

        file_menu = self.addMenu('&File')
        exit = QAction("Exit", parent)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        exit.triggered.connect(parent.close)
        file_menu.addAction(exit)
        search = QAction("Search", parent)
        search.triggered.connect(scan_directory)
        file_menu.addAction(search)



        tools_menu = self.addMenu('&Tools')
        help_menu = self.addMenu('&Help')


