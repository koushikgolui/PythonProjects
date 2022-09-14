from tkinter import *


def mile_to_km():
    user_input = float(inp_mile.get())
    final_output = round(user_input * 1.609, 4)
    label_km_calc.config(text=f"{final_output}")


km = 0.0
window = Tk()
window.minsize(width=400, height=200)
window.title("Mile to KM Converter")
window.config(padx=30, pady=20)

inp_mile = Entry()
inp_mile.grid(column=1, row=0)

label_mile = Label(text="Miles", font=("arial", 15, "normal"), padx=20)
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to", font=("arial", 15, "normal"))
label_equal.grid(column=0, row=1)


label_km_calc = Label(text=f"{km}", font=("arial", 15, "normal"))
label_km_calc.grid(column=1, row=1)

label_km = Label(text="KM", font=("arial", 15, "normal"))
label_km.grid(column=2, row=1)

button_calc = Button(text="Calculate", font=("arial", 15, "bold"), command=mile_to_km)
button_calc.grid(column=1, row=3)

window.mainloop()
