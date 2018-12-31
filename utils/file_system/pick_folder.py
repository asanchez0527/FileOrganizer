from PyQt5.QtWidgets import QFileDialog


# display system dialog for picking folder
def pick_folder():
    path = QFileDialog.getExistingDirectory(directory="/")
    if not path:
        return None
    else:
        return path
