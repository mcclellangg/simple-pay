# pay.py
"""Want to combine the ideas of the weekly paycheck calculator, and the idea of saving records to a file
in one tkinter application. Prompt user for employee info, and then make calculations based off of input,
display these too user for verification, and give them the option to update the database.
Also would like to show all records sorted by time, then employee alphabetically."""

import tkinter as tk
import sqlite3
import datetime

# Tkinter GUI
root = tk.Tk()
root.title("Payroll Records")
root.geometry("650x800")

# HACK Initialize table in database:
'''
conn = sqlite3.connect("payroll.db")
c = conn.cursor()

# Create a table:
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
'''


# Functions for program:
def calc_state():
    """
    Source: https://www.tax.virginia.gov/sites/default/files/inline-files/Employer%20Withholding%20Instructions.pdf

    A function to calculate state withholding amount each week.
    Will take gross pay, and # of dependents as arguments, and return
    the amount to be withheld for this pay period. This function will assume
    that the pay periods occur on a weekly basis. This function also assumes there will
    be no calculations for people 65+, or taking blind exemptions.

    Original Formula:
    (G)P - [$3,000 + (E1 X $930) + (E2 X 800)] = T

    Modified Formula:
    (G)P - [$3,000 + (E1 X $930)] = T

    """
    gross_pay = float(grossPayTextbox.get())
    E1 = int(dependentsTextbox.get())
    P = 52
    w = 0  # Annualized tax to be withheld

    # Calculate Annualized taxable income(t):
    t = (gross_pay * P) - (3000 + (E1 * 930))
    # Use t to calculate w (annualized tax to be withheld):
    if t < 3000:
        w = round((float(t) * 0.02), 2)
    elif t >= 3000 and t < 5000:
        w = round(((t - 3000) * 0.03), 2) + 60
    elif t >= 5000 and t < 17000:
        w = round(((t - 5000) * 0.05), 2) + 120
    elif t >= 17000:
        w = round(((t - 17000) * 0.0575), 2) + 720
    # Calculate amount to withhold
    amount_to_withhold = round((w / P))

    return str(amount_to_withhold)


def calc_fed():
    """
    Source: https://www.irs.gov/pub/irs-pdf/p15t.pdf

    A function designed to calculate federal withholding amounts on a weekly basis.
    For simplicity sake, this function will be designed to work for Single or Married Filing Seperately individuals only.
    It will also assume that the employee does not have multiple jobs (Using a W-4 form that is from before 2019 or 2020
    and beyond but not checking the box in step 2 on that form). This formula will also only solve for someone with an annual
    salary range of $0 - $90,325.

    Formula:
    (G)P - (E1 X $4300) = T

    Then check table and calculate excess

    LIMITATIONS: DOES NOT CHECK FOR NEGATIVE INPUTS
    """
    gross_pay = float(grossPayTextbox.get())
    E1 = float(dependentsTextbox.get())
    P = 52  # The number of pay periods per year
    w = 0  # Annualized tax to be withheld

    # Calculate Annualized taxable income(t):
    t = (gross_pay * P) - (E1 * 4300)

    # Use t to calculate w (annualized tax to be withheld):
    if t < 3950:
        w = 0
    elif t >= 3950 and t < 13900:
        w = round(((t - 3950) * 0.10), 2)
    elif t >= 13900 and t < 44475:
        w = round(((t - 13900) * 0.12), 2) + 995
    elif t >= 44475 and t < 90325:
        w = round(((t - 44475) * 0.22), 2) + 4664

    # Calculate amount to withhold
    amount_to_withhold = round((w / P))

    return str(amount_to_withhold)


def calc_medicare():
    """Calculates amount of medicare to deduct based on the grosspay from input"""
    entryNumber = float(grossPayTextbox.get())
    deduction = entryNumber * 0.0145
    return str(round(deduction, 2))


def calc_social():
    """Calculates amount of social security to deduct based on grosspay from input"""
    entryNumber = float(grossPayTextbox.get())
    deduction = entryNumber * 0.062
    return str(round(deduction, 2))


def calc_net_deuctions():
    """Calculates the total deductions"""
    federal = float(calc_fed())
    social = float(calc_social())
    med = float(calc_medicare())
    state = float(calc_state())
    total = federal + social + med + state
    return str(round(total, 2))


def calc_net_pay():
    gross_pay = float(grossPayTextbox.get())
    total_deductions = float(calc_net_deuctions())
    net = round(gross_pay - total_deductions, 2)
    return str(net)


# New functions for this app:
def make_calculations():
    t = "           "
    # Make Header label to display info:
    header_label = tk.Label(
        root,
        text="Name\tGross Pay\tFederal\tSocial\tMedicare\tState\tNet Deductions\tNet Pay",
    )
    header_label.grid(row=5, column=0, columnspan=2)

    deductions_label = tk.Label(
        root,
        text=employeeTextbox.get()
        + t
        + grossPayTextbox.get()
        + t
        + calc_fed()
        + t
        + calc_social()
        + t
        + calc_medicare()
        + t
        + calc_state()
        + t
        + calc_net_deuctions()
        + t
        + calc_net_pay(),
    )
    deductions_label.grid(row=6, column=0, columnspan=2)


def submit():
    conn = sqlite3.connect("payroll.db")
    c = conn.cursor()

    c.execute(
        """INSERT INTO paychecks VALUES(
            :date, :employee, :gross_pay, :fed_deduct, :social_deduct, :med_deduct, :state_deduct, :net_deduct, :net_pay)""",
        {
            "date": "{: %m/%d/%Y }".format(datetime.datetime.now()),
            "employee": employeeTextbox.get(),
            "gross_pay": grossPayTextbox.get(),
            "fed_deduct": calc_fed(),
            "social_deduct": calc_social(),
            "med_deduct": calc_medicare(),
            "state_deduct": calc_state(),
            "net_deduct": calc_net_deuctions(),
            "net_pay": calc_net_pay(),
        },
    )
    # Commit changes and close connection:
    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect("payroll.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM paychecks")
    records = c.fetchall()
    print(records)
    # Display records on a label in tkinter:
    display_records = ""
    for record in records:
        display_records += str(record) + "\n"

    query_label = tk.Label(root, text=display_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes, and close connection
    conn.commit()
    conn.close()


# Get the weekly paycheck info:
employeeLabel = tk.Label(root, text="Enter employee name: ")
employeeLabel.grid(row=1, column=0, padx=10, pady=5)
employeeTextbox = tk.Entry(root, width=30)
employeeTextbox.grid(row=1, column=1, padx=10, pady=5)
dependentsLabel = tk.Label(root, text="Enter number of dependents: ")
dependentsLabel.grid(row=2, column=0, padx=10, pady=5)
dependentsTextbox = tk.Entry(root, width=30)
dependentsTextbox.grid(row=2, column=1, padx=10, pady=5)
grossPayLabel = tk.Label(root, text="Enter gross pay: ")
grossPayLabel.grid(row=3, column=0, padx=10, pady=5)
grossPayTextbox = tk.Entry(root, width=30)
grossPayTextbox.grid(row=3, column=1, padx=10, pady=5)

# Create Calculate and submit buttons:
calc_btn = tk.Button(root, text="Calculate", command=make_calculations)
calc_btn.grid(row=4, column=0, pady=10, padx=10, ipadx=120)
submit_btn = tk.Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=4, column=1, pady=10, padx=10, ipadx=70)

# Create query button:
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, pady=10, padx=10, ipadx=100)

# Start the event loop
root.mainloop()
