
import tkinter as tk
from tkinter import ttk

window = tk.Tk()



window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

userName = ttk.Label(window, text= "username:")
userName.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

entrada = ttk.Entry(window)

entrada.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10)



labelContrasenia = ttk.Label(window, text="Contraseña:")

labelContrasenia.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)


entrada_contrasenia = ttk.Entry(window, show='*' )
entrada_contrasenia.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)


button= ttk.Button(window, text="Login")

button.grid(column=1, row =3, padx=10, pady=10)

window.mainloop()