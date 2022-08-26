from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)


def button_clicked():
    result = float(miles_input.get()) * 1.6
    km_result_label.config(text=result)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)









window.mainloop()