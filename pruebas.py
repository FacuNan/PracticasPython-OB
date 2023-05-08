import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)


label = ttk.Label(window, text="Usuario")
label.grid(column=0, row =0, sticky=tk.W, padx=10, pady=10)


input = ttk.Entry(window)
input.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)

password = ttk.Label(window, text="Password")
password.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

password_input= ttk.Entry(window, show='0')
password_input.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10)



button = ttk.Button(window, text="login")
button.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

window.mainloop()

