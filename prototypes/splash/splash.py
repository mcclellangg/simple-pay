# splash.py
"""This will be a prototype for my splash screen that first comes up when the user opens the application.
Features that it will have include:
- Open Existing Company
- Initialize New Company
- About
"""
from sqlite3.dbapi2 import Error
import tkinter as tk
import sqlite3
import os

# Stupid debug print statements:

# Tkinter GUI:
root = tk.Tk()
root.title("Simple Pay Splash")
root.geometry("600x800")

# Logo :
logo = tk.Label(root, text="Simple Pay", borderwidth=2, relief="solid")
logo.config(font=("Helvatical bold", 20))
logo.grid(row=0, column=0, ipadx=50, ipady=50, padx=150, pady=20, columnspan=3)

# Set parameters for dropdown:
company_files = []
for file in os.listdir("./company_files"):
    company_files.append(file)

selected = tk.StringVar()
selected.set("Choose Company")

display_frame_text = tk.StringVar()
display_frame_text.set("Change my text")

entry_default_text = "Enter Company name"


# Command functions:
def about():
    """Command passed to the about button, when clicked this will display information about the app in the display frame."""
    global display_frame_text
    display_frame_text = "This will now show the about text!"  # HACK maybe create an about file that this reads in as text.
    info = tk.Label(display_frame, textvariable=display_frame_text)
    info.grid(row=0, column=0)


def open():
    """Command passed to the open button, when clicked will read which company was chosen from the dropdown, and open
    the file in the about pane with two buttons."""

    pass


def create_file():
    """Command passed to create button when clicked will get the text from the entry label, and create a company file
    based on the name provided. This file will be a database file containing all of the company records."""
    # HACK I will eventually need to create a function that will check the input to ensure there are no
    # issues with the company name (don't want to overwrite, or use unallowed characters.)

    # Read the name in the entry box:
    file_name = entry.get()
    file_path = r"./company_files/" + file_name + ".db"

    # Take that name and create a db file in this directory:
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
    except Error as e:
        print(e)


# Create Labels:
select_file = tk.Label(root, text="Select Company file: ")
dropdown = tk.OptionMenu(root, selected, *company_files)
dropdown.config(
    width=35
)  # HACK may want to have all sizings based off of % relative to starting geometry
open_btn = tk.Button(root, text="Open", command=open)
create_lbl = tk.Label(root, text="Create Company file:")
entry = tk.Entry(root, text="Enter Company name")
entry.config(width=35)
entry.insert(tk.END, entry_default_text)
create_btn = tk.Button(
    root, text="Create", command=create_file
)  # BUG If you add a new file it does not demonstrate this to the user!
about_btn = tk.Button(root, text="About", command=about)

# Display Labels:
select_file.grid(row=1, column=0)
dropdown.grid(row=1, column=1)
open_btn.grid(row=1, column=2)
create_lbl.grid(row=2, column=0, padx=5, pady=5)
entry.grid(row=2, column=1, padx=5, pady=5)
create_btn.grid(row=2, column=2, padx=5, pady=5)
about_btn.grid(row=3, column=0, padx=5, pady=5)

# Create a frame to display company files in:
display_frame = tk.LabelFrame(root, text="Display Panel", padx=125, pady=150)
display_lbl = tk.Label(display_frame, textvariable=display_frame_text)

display_frame.grid(row=4, column=0, columnspan=3, padx=50, pady=40)
display_lbl.grid(row=0, column=0)

# Start the event loop
root.mainloop()
