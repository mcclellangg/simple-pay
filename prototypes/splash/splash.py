# splash.py
"""This will be a prototype for my splash screen that first comes up when the user opens the application.
Features that it will have include:
- Open Existing Company
- Initialize New Company
- About
"""
import tkinter as tk


# Tkinter GUI:
root = tk.Tk()
root.title("Simple Pay Splash")
root.geometry("600x800")

# Logo :
logo = tk.Label(root, text="Simple Pay", borderwidth=2, relief="raised")
logo.config(font=("Helvatical bold", 20))
logo.grid(row=0, column=0, ipadx=50, ipady=50, padx=150, pady=20, columnspan=3)

# Set parameters for dropdown:
company_files = [
    "path/to/fooCompany",
    "path/to/fizzCompany",
    "path/to/awesomeCompany",
]

selected = tk.StringVar()
selected.set("Choose Company")

# Menu Labels:
select_file = tk.Label(root, text="Select Company file: ")
select_file.grid(row=1, column=0)
dropdown = tk.OptionMenu(root, selected, *company_files)
dropdown.config(width=35)
dropdown.grid(row=1, column=1)
open_file = tk.Button(root, text='Open')
open_file.grid(row=1, column=2)
create_file = tk.Label(root, text="Create a new Company file")
create_file.grid(row=2, column=0, padx=5, pady=5)
about = tk.Label(root, text="About")
about.grid(row=3, column=0, padx=5, pady=5)


# Start the event loop
root.mainloop()
