# buttons.py

"""Another prototype, this time to experiment with creating a blank frame of fixed size that will update based on certain
buttons that the user will press. The plan is to then port this as the display frame in splash.py"""
import tkinter as tk

root = tk.Tk()
root.title("Simple Pay Buttons")
root.geometry("600x800")


def about():
    """"Will change a global tkinter string variable to display about info in the msgFrame"""
    clear_frame()
    aboutText = tk.Label(msgFrame, text="The about text!", width=40)
    aboutText.pack()


def open_file():
    """Will destroy labels in the msgFrame and replace them with company name and two buttons to navigate to other parts
    of the program, payroll calculator, and record display"""
    clear_frame()
    openText = tk.Label(msgFrame, text="Company name!", width=40)
    calcBtn = tk.Button(msgFrame, text="Open paycheck calculator!")
    recordBtn = tk.Button(msgFrame, text="Company Records")

    openText.pack(expand=False)
    calcBtn.pack(expand=False)
    recordBtn.pack(expand=False)


def create():
    """Will destroy labels in the msgFrame, and update with a message to the user that the company of _____ name was created
    successfully!"""
    clear_frame()
    successText = tk.Label(msgFrame, text="Company was successfully created!", width=40)

    successText.pack()


def clear_frame():
    """Destroys all widgets in msgFrame"""
    for widget in msgFrame.winfo_children():
        widget.destroy()


msgFrame = tk.LabelFrame(root, text="Display Panel", width=500, height=400, padx=125, pady=150)
msgText = tk.Label(msgFrame, text="Change me please", width=40)
aboutBtn = tk.Button(root, text='Click for about info!', padx=5, pady=5, command=about)
openBtn = tk.Button(root, text='Open Company file', padx=5, pady=5, command=open_file)
createBtn = tk.Button(root, text='Create Company file', padx=5, pady=5, command=create)

aboutBtn.pack()
openBtn.pack()
createBtn.pack()
msgFrame.pack()
msgFrame.pack_propagate(False)
msgText.pack()

root.mainloop()
