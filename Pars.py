
import tkinter as tk
from tkinter import Tk, scrolledtext

from miha import pars

root = Tk()
root.title("WOW, PARSING!")
root.resizable(width=False, height=False)
root.geometry('900x650')
root['bg'] = "grey"

button = tk.Button(root, text="Quit", fg='black', bg='yellow', command=quit).place(x=750, y=20)
action = tk.Button(root, text='!Find out your folders!', fg='red', bg='white', command=pars).place(x=690, y=55)

console = scrolledtext.ScrolledText(root, state='disable').place(x=0, y=0)

root.mainloop()