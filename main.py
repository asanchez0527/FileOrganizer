from utils.window.window import MainApplication
import tkinter as tk
import os
from sys import platform


def main():
    root = tk.Tk()
    root.geometry('800x600')
    MainApplication(root).pack(side='top', fill='both', expand=True)
    if platform == 'darwin':
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    root.mainloop()


if __name__ == '__main__':
    main()
