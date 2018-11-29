import tkinter as tk
from utils.file_system.scan_directory import scan_directory
from utils.window.SettingsPage import SettingsPage
from utils.window.StartPage import StartPage


class MenuBar(tk.Menu):
    def __init__(self, parent, controller):
        tk.Menu.__init__(self, parent)
        self.menu_file = tk.Menu(parent, tearoff=False)
        self.menu_file.label = 'File'
        self.menu_file.add_command(label='Search', command=lambda: scan_directory(parent))
        self.menu_file.add_command(label='Quit', command=self.quit)
        self.menu_settings = tk.Menu(parent, tearoff=False)
        self.menu_settings.label = 'Settings'
        self.menu_settings.add_command(label='Settings', command=lambda: controller.show_frame(SettingsPage))
        self.menu_settings.add_command(label='Home', command=lambda: controller.show_frame(StartPage))

        self.menus = (
            self.menu_file,
            self.menu_settings
        )
        for menu in self.menus:
            self.add_cascade(label=menu.label, menu=menu, underline=0)
