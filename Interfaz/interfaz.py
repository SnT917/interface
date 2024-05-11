from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="superhero")
root.title("Aplicativo")

# Set the window size
root.geometry("350x430")
root.resizable(width=False, height=False)

# Load background image
background_image = PhotoImage(file="fondo.png")

# Create a Label widget to display the background image
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

image = PhotoImage(file="logo.png")
selected_option = ""  # Initialize selected_option with an empty string

def checker(button_clicked):
    global selected_option
    if button_clicked == "Débito" and var1.get() == 1:
        var2.set(0)
        selected_option = "Débito"
        print("Débito seleccionado")
    elif button_clicked == "Crédito" and var2.get() == 1:
        var1.set(0)
        selected_option = "Crédito"
        print("Crédito seleccionado")
    else:
        selected_option = ""  # Reset selected_option if no check button is selected

def submit(username, password, selected_date1, selected_date2):
    if not all((username, password, selected_date1, selected_date2)):
        print("Por favor diligencie todos los campos antes de continuar.")
        return
    if not selected_option:
        print("Por favor seleccione el tipo de compensación.")
        return
    print("Usuario:", username)
    print("Password:", password)
    print("Initial Date:", selected_date1)
    print("End Date:", selected_date2)
    print("Selected Option:", selected_option)

# Title Label
title_label = tb.Label(root, text="Compensación MCCA", font=("Open Sans", 16), bootstyle='info')
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=17)

# Username Label and Entry
user_label = tb.Label(root, text="Usuario Nacional:")
user_label.grid(row=1, column=0, padx=20, pady=15, sticky='ew')

user_entry = tb.Entry(root, bootstyle="info")
user_entry.grid(row=1, column=1, padx=20, pady=15, sticky='ew')

# Password Label and Entry
password_label = tb.Label(root, text="Contraseña:")
password_label.grid(row=2, column=0, padx=20, pady=15, sticky='ew')

password_entry = tb.Entry(root, bootstyle="info", show="*")  # Show '*' for password
password_entry.grid(row=2, column=1, padx=20, pady=15, sticky='ew')

# Initial Date Entry
date_ini_label = tb.Label(root, text="Fecha Inicial:")
date_ini_label.grid(row=3, column=0, padx=20, pady=15, sticky='ew')

date_ini = tb.DateEntry(root, bootstyle="info", firstweekday=0, startdate=date.today())
date_ini.grid(row=3, column=1, padx=20, pady=15, sticky='ew')

# End Date Entry
date_end_label = tb.Label(root, text="Fecha Final:")
date_end_label.grid(row=4, column=0, padx=20, pady=15, sticky='ew')

date_end = tb.DateEntry(root, bootstyle="info", firstweekday=0, startdate=date.today())
date_end.grid(row=4, column=1, padx=20, pady=15, sticky='ew')

# Checkbuttons
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="info", text="Débito", variable=var1, onvalue=1, offvalue=0, command=lambda: checker("Débito"))
my_check.grid(row=5, column=0, pady=15)

var2 = IntVar()
my_check = tb.Checkbutton(bootstyle="info", text="Crédito", variable=var2, onvalue=1, offvalue=0, command=lambda: checker("Crédito"))
my_check.grid(row=5, column=1, pady=15)

# Submit Button
submit_button = tb.Button(root, text='Ejecutar', bootstyle="info",  width=23, command=lambda: submit(user_entry.get(), password_entry.get(), date_ini.entry.get(), date_end.entry.get()))
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Create a label with the image
image_label = tb.Label(root, image=image)
image_label.grid(row=7, column=0, columnspan=2)

root.mainloop()