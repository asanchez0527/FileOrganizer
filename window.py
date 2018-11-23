import tkinter as tk
from tkinter import *
from tkinter import Menu
from scan_directory import scan_directory
from sys import exit
import database.get_entries


def window():
    root = tk.Tk()
    root.title('MovieFlix')
    menu = Menu(root)
    file_menu = Menu(menu)
    file_menu.add_command(label='Scan', command=lambda: scan_directory(root))
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=lambda: exit())
    menu.add_cascade(label='File', menu=file_menu)
    root.config(menu=menu)
    return root
