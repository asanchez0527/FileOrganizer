from utils.window.window import MainApplication
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry('800x600')
    MainApplication(root).pack(side='top', fill='both', expand=True)
    root.mainloop()


if __name__=='__main__':
    main()
