from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="New Text", font=("Courier", 10, "normal"))
my_label.pack()


def button_clicked():
    my_label.config(text="I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()










window.mainloop()