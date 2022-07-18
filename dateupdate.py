from tkinter import Tk
from tkinter.filedialog import askdirectory

# Prevents root window from appearing
Tk().withdraw()

# Choose current working directory to use
current_directory = askdirectory()

print(current_directory)
