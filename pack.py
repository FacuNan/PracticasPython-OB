import tkinter as tk
window = tk.Tk()
label_saludo = tk.Label(window, text="Hola", background="red")

button = tk.Button(window, text="añadir", background="black", fg="white")
button.pack(ipadx=30, ipady=10, expand= True, side="left")

label_saludo.pack(fill='x', side="right")

window.mainloop()
