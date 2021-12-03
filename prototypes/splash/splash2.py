# splash2.py
"""An updated version of the splash prototype based on experiments with the button prototype
this will allow for a display frame that changes based on the buttons clicked by the user."""
import tkinter as tk
# import sqlite3
import os

root = tk.Tk()
root.title("Simple Pay Splash 1.95")
root.geometry("600x600")

# Set basic parameters:
selected = tk.StringVar()
selected.set("Choose Company")

company_files = []
for file in os.listdir("./company_files"):
    company_files.append(file)

MESSAGE_TEXT = """Welcome to SimplePay!"""


# Command functions:
def clear_frame():
    """Destroys all widgets in msgFrame"""
    for widget in displayFrame.winfo_children():
        widget.destroy()


def open_selected():
    """Destroys andy widgets in the display frame, and then updates it based on the company file that is
    selected in the dropdown menu."""
    clear_frame()
    openText = tk.Label(displayFrame, text="Company name!", width=40)
    calcBtn = tk.Button(displayFrame, text="Open paycheck calculator!")
    recordBtn = tk.Button(displayFrame, text="Company Records")

    openText.pack()
    calcBtn.pack()
    recordBtn.pack()


def create_file():
    """Destroys any widgets in the display frame and then reads the company name from the entry widget,
    and initializes a new .db file in the company files directory, with a table already created."""
    pass


def display_about():
    """Destroys any widgets already in the display frame, and then reads in information from and about file
    and renders it in the display frame."""
    clear_frame()
    aboutText = tk.Label(displayFrame, text="The about text!", width=40)
    aboutText.pack()


openLbl = tk.Label(root, text="Open Company: ")
dropdown = tk.OptionMenu(root, selected, *company_files)
openBtn = tk.Button(root, text='Open', command=open_selected)
createLbl = tk.Label(root, text="Create Company: ")
entryField = tk.Entry(root, text="Company name")
createBtn = tk.Button(root, text="Create", command=create_file)
aboutBtn = tk.Button(root, text="About", command=display_about)

displayFrame = tk.LabelFrame(root, text="Display Info", width=500, height=400, padx=125, pady=150)
msgText = tk.Label(displayFrame, text=MESSAGE_TEXT, width=40)

dropdown.config(width=35)
entryField.config(width=40, borderwidth=2)
openBtn.config(width=12)
createBtn.config(width=12)
aboutBtn.config(width=12)

openLbl.grid(row=0, column=0, padx=(20, 0), pady=(20, 8))
dropdown.grid(row=0, column=1, pady=(20, 8))
openBtn.grid(row=0, column=2, pady=(20, 8))
createLbl.grid(row=1, column=0, padx=(20, 0), pady=(0, 5))
entryField.grid(row=1, column=1, pady=(0, 5))
createBtn.grid(row=1, column=2, pady=(0, 5))
aboutBtn.grid(row=2, column=0)

displayFrame.grid(row=3, column=0, columnspan=3, padx=(20, 0), pady=(20, 0))
displayFrame.pack_propagate(False)
msgText.pack()

root.mainloop()
