from tkinter import filedialog


# display system dialog for picking folder
def pick_folder(root):
    path = filedialog.askdirectory()
    if not path:
        return None
    else:
        return path
