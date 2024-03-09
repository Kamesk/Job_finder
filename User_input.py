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

key = b'Z1IHJtIquAGruPsZjsQhjZJE0Zv9-M3iR1KsQWqm5hg='
encrypted_username = b'gAAAAABl64ZdN0uwCjOn--GDF6MQf7dl2u1Li_2YMMfsoXE32wFh5Ck4RliaUICvKYjvqY66lARxhxxKS6GmcdZd7yyh3oFxcw4IoctdnJVh72hkQ40x61s='
encrypted_password = b'gAAAAABl64ZdHI4BJT1zkHoVzehdp9O9LLvHeKOt8ZY5CACwvnLgUWldUFh42FrXIA1jf6CxxDfi67h-_DQk-L_DfBvtklpfhQ=='