# tree.py
"""
    Experimental tkinter application to test tree view. This seems like it would be way better for
    making the records database.
    {'timestamp': 'DATETIME object',
    'name': STRING,
    'exemptions': INTEGER,
    'gross pay': FLOAT round 2,
    'federal': FLOAT round 2,
    'social security': FLOAT round 2,
    'medicare': FLOAT round 2,
    'state': FLOAT round 2,
    'net': FLOAT round 2,
    'net pay': FLOAT round 2
    }
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x600")
root.title("Tree Test")

my_tree = ttk.Treeview(root)

# Define Columns:
my_tree['columns'] = (
    'Name',
    'Exemptions',
    'Gross Pay',
    )

# Format the columns:
my_tree.column("#0", width=80, minwidth=25)  # '#0' is the phantom column
my_tree.column("Name", anchor="w", width=100)
my_tree.column("Exemptions", anchor="center", width=100)
my_tree.column("Gross Pay", anchor="w", width=100)

# Create Headings:
my_tree.heading("#0", text="Timestamp", anchor="w")
my_tree.heading("Name", text="Name", anchor="w")
my_tree.heading("Exemptions", text="Exemptions", anchor="w")
my_tree.heading("Gross Pay", text="Gross Pay", anchor="w")

# Add Data:
my_tree.insert(parent='', index='end', iid=0, text="Parent", values=('Jim', 2, "$1,200"))

# Create a list of data, and add it through iteration:
data = [
    ["Jim", 2, "$1,200"],
    ["John", 1, "$1,100"],
    ["Cary", 2, "$800"],
    ["Susan", 3, "$1,600"],
    ["Jim", 1, "$750"],
    ["Nick", 0, "$900"],
]
count = 1  # Since we have 0 as an id at line 47
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="Parent", values=(record[0], record[1], record[2]))
    count += 1

my_tree.pack(pady=40)

root.mainloop()
