# pay-calc.py
"""
    This will be a refactor of the original pay app. Want to rewrite it so that it is cleaner
    and more intuitive to use.
"""
import tkinter as tk

root = tk.Tk()
root.title("Pay-Calc+")
root.geometry("600x600")


# Command functions
def calculate_deductions():
    """Automatically calculates deductions provided in entry fields, and returns a paystub to the user."""
    pass


def update_records():
    """Takes the paystub that has been created, attaches a timestamp, and puts it into the database."""
    pass



nameLbl = tk.Label(root, text="Enter employee name : ", anchor="w")
nameField = tk.Entry(root)
exemptionsLbl = tk.Label(root, text="Enter exemptions :  ", anchor="w")  # Updated from dependents
exemptionsField = tk.Entry(root)
grossLbl = tk.Label(root, text="Enter gross pay: ", anchor="w")
grossField = tk.Entry(root)
calcBtn = tk.Button(root, text="Calculate", command=calculate_deductions)
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

root.mainloop()
