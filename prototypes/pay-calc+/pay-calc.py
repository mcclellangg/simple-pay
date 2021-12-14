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

root = tk.Tk()
root.title("Pay-Calc+")
root.geometry("600x600")


# Command functions
def create_paycheck():
    """Takes the user inputs, passes them to the calculate function, and generates a paycheck object that is
    ready to display or add to the database."""
    # Get info from entry fields, and clean it for calc function
    user_input = {
        'name': nameField.get(),
        'exemptions': int(exemptionsField.get()),
        'gross pay' : round(float(grossField.get()), 2)
    }
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
calcBtn = tk.Button(root, text="Calculate", command=create_paycheck)
updateBtn = tk.Button(root, text="Add Entry", command=update_records)

displayFrame = tk.LabelFrame(root, text="Display Info", width=500, height=400, padx=125, pady=150)
msgLbl = tk.Label(displayFrame, text="Troubleshoot Here", width=40)


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

displayFrame.grid(row=4, column=0, columnspan=2, padx=(40, 30), pady=(20, 0))
displayFrame.pack_propagate(False)
msgLbl.pack()

root.mainloop()
