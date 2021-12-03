# splash2.py
"""An updated version of the splash prototype based on experiments with the button prototype
this will allow for a display frame that changes based on the buttons clicked by the user."""
from sqlite3.dbapi2 import Error
import tkinter as tk
import sqlite3
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
    openText = tk.Label(displayFrame, text=selected.get(), width=40)
    calcBtn = tk.Button(displayFrame, text="Create Paychecks", width=20, command=open_paycalc)
    recordBtn = tk.Button(displayFrame, text="Company Records", width=20, command=open_records)

    openText.pack(pady=2)
    calcBtn.pack(pady=2)
    recordBtn.pack(pady=2)


def create_file():
    """Destroys any widgets in the display frame and then reads the company name from the entry widget,
    and initializes a new .db file in the company files directory, with a table already created."""

    file_name = entryField.get()
    file_path = r"./company_files/" + file_name + ".db"

    try:
        conn = sqlite3.connect(file_path)
        c = conn.cursor()
        c.execute(
            """CREATE TABLE paychecks (
                date text,
                employee text,
                gross_pay integer,
                fed_deduct integer,
                social_deduct integer,
                med_deduct integer,
                state_deduct integer,
                net_deduct integer,
                net_pay integer
            )"""
        )
        conn.commit()
        conn.close()

        clear_frame()
        confirmText = tk.Label(displayFrame, text=f"{file_name} was created!")
        confirmText.pack()
    except Error as e:
        print(e)


def display_about():
    """Destroys any widgets already in the display frame, and then reads in information from and about file
    and renders it in the display frame."""
    clear_frame()
    aboutText = tk.Label(displayFrame, text="The about text!", width=40)
    aboutText.pack()


def open_paycalc():
    """Command for the calcBtn, opens the paycheck calculator in a new window when clicked."""
    top = tk.Toplevel()
    top.title("Payroll Calculator")
    top.geometry("500x500")

    topLbl = tk.Label(top, text=selected.get())
    topLbl.pack()


def open_records():
    """Command for the recordBtn, opens the paycheck records in a new window when clicked."""
    top = tk.Toplevel()
    top.title("Payroll Records")
    top.geometry("500x500")

    topLbl = tk.Label(top, text=selected.get())
    topLbl.pack()


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
