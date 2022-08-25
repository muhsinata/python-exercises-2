from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="New Text", font=FONT)
my_label.pack()


def button_clicked():
    my_label.config(text=user_input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

user_input = Entry(width=10)
user_input.pack()









window.mainloop()