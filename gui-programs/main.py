from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="New Text", font=FONT)
my_label.grid(column=0, row=0)


# def button_clicked():
#     my_label.config(text=user_input.get())


button = Button(text="Click Me")
button.grid(column=1, row=1)

button = Button(text="Click Me")
button.grid(column=2, row=0)

my_label = Label(text="New Text", font=FONT)
my_label.grid(column=3, row=2)

# user_input = Entry(width=10)
# user_input.pack()









window.mainloop()