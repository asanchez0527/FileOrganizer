import tkinter as tk
from utils.file_system.scan_directory import scan_directory


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.root = parent
        self.menu_file = tk.Menu(parent, tearoff=False)
        self.menu_file.label = 'File'
        self.menu_file.add_command(label='Search', command=lambda: scan_directory(parent))
        self.menu_file.add_command(label='Quit', command=self.quit)

        self.menus = (
            self.menu_file,
        )
        for menu in self.menus:
            self.add_cascade(label=menu.label, menu=menu, underline=0)
