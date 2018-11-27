from utils.window.window import MainApplication
from sys import platform
import os

def main():
    app = MainApplication()
    if platform == 'darwin':
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    app.mainloop()


if __name__ == '__main__':
    main()
