import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

user_input1 = simpledialog.askstring("Job_input", "Enter Prefered_Job")
user_input2 = simpledialog.askstring("Location_Input", "Enter Prefered_Location")
if user_input1 and user_input2 is not None:
    # User provided input
    print(user_input1, user_input2)
else:
    # User canceled the prompt
    print("No input provided.")

root.destroy()