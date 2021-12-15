# pay-calc.py
"""
    This will be a refactor of the original pay app. Want to rewrite it so that it is cleaner
    and more intuitive to use.
    Model for paycheck objects:
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
import calculations as calc

root = tk.Tk()
root.title("Pay-Calc+")
root.geometry("750x450")

count = 0  # iid for paychecks in treeview UNIQUE

# Command functions
def create_paycheck():
    """Takes the user inputs, passes them to the calculate function, and generates a paycheck object that is
    ready to display or add to the database."""
    global count
    # Get info from entry fields, and clean it for calc function
    user_input = {
        "name": nameField.get(),
        "exemptions": int(exemptionsField.get()),
        "gross pay": round(float(grossField.get()), 2),
    }
    paycheck = calc.calculate_deductions(user_input)
    # Insert the paycheck directly into the tree view:
    tree_display.insert(
        parent="",
        index="end",
        iid=count,
        text="12/15/21",
        values=(
            paycheck["name"],
            paycheck["exemptions"],
            paycheck["gross pay"],
            paycheck["federal"],
            paycheck["social security"],
            paycheck["medicare"],
            paycheck["state"],
            paycheck["net"],
            paycheck["net pay"],
        ),
    )
    count += 1


def update_records():
    """Read the paycheck objects from the list and add them to the record base."""
    # TODO Will complete this functionality once db framework is established in next phase.
    pass


nameLbl = tk.Label(root, text="Enter employee name : ", anchor="w")
nameField = tk.Entry(root)
exemptionsLbl = tk.Label(
    root, text="Enter exemptions :  ", anchor="w"
)  # Updated from dependents
exemptionsField = tk.Entry(root)
grossLbl = tk.Label(root, text="Enter gross pay: ", anchor="w")
grossField = tk.Entry(root)
calcBtn = tk.Button(root, text="Calculate", command=create_paycheck)
updateBtn = tk.Button(root, text="Add Entry", command=update_records)

nameLbl.config(width=18)
nameField.config(width=40)
exemptionsLbl.config(width=18)
exemptionsField.config(width=40)
grossLbl.config(width=18)
grossField.config(width=40)
calcBtn.config(width=25)
updateBtn.config(width=25)

nameLbl.grid(row=0, column=0, padx=(20, 8), pady=(20, 8))
nameField.grid(row=0, column=1, pady=(20, 8))
exemptionsLbl.grid(row=1, column=0, padx=(20, 8), pady=(0, 8))
exemptionsField.grid(row=1, column=1, pady=(0, 8))
grossLbl.grid(row=2, column=0, padx=(20, 8), pady=(0, 12))
grossField.grid(row=2, column=1, pady=(0, 12))
calcBtn.grid(row=3, column=0, padx=(60, 8), pady=(0, 8))
updateBtn.grid(row=3, column=1, pady=(0, 8))

# Add the tree:
displayFrame = tk.LabelFrame(root, text="Paychecks")
displayFrame.grid(row=4, column=0, columnspan=2, padx=(30, 0))
tree_display = ttk.Treeview(displayFrame)

# Define the Columns:
tree_display["columns"] = (
    "Name",
    "Exemptions",
    "Gross Pay",
    "Federal",
    "Social",
    "Medicare",
    "State",
    "Net",
    "Net Pay",
)
# Format the columns:
tree_display.column("#0", width=80, minwidth=25)  # '#0' is the phantom column
tree_display.column("Name", anchor="w", width=60)
tree_display.column("Exemptions", anchor="center", width=80)
tree_display.column("Gross Pay", anchor="w", width=60)
tree_display.column("Federal", anchor="center", width=60)
tree_display.column("Social", anchor="center", width=60)
tree_display.column("Medicare", anchor="center", width=60)
tree_display.column("State", anchor="center", width=60)
tree_display.column("Net", anchor="center", width=60)
tree_display.column("Net Pay", anchor="center", width=60)

# Create Headings:
tree_display.heading("#0", text="Timestamp", anchor="w")
tree_display.heading("Name", text="Name", anchor="w")
tree_display.heading("Exemptions", text="Exemptions", anchor="w")
tree_display.heading("Gross Pay", text="Gross Pay", anchor="w")
tree_display.heading("Federal", text="Federal", anchor="center")
tree_display.heading("Social", text="Social", anchor="center")
tree_display.heading("Medicare", text="Medicare", anchor="center")
tree_display.heading("State", text="State", anchor="center")
tree_display.heading("Net", text="Net", anchor="center")
tree_display.heading("Net Pay", text="Net Pay", anchor="center")

# Add Sample Data:
# tree_display.insert(parent='', index='end', iid='s', text="12/15/21", values=('Jim', 2, "$1,200", 23, 12, 18, 43, 186, "987.50"))

tree_display.pack()

root.mainloop()
