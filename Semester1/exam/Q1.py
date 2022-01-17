"""Q1 by Stefana Chiritescu
    A00282343"""

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def reset():
    value2 = int(resetVar.get())
    entry2.delete(0, END)
    entry2.insert(END, value2)


'''New method code'''
# Add method
def add():
    value1 = int(entry2.get())
    value2 = int(addVar.get())
    result = value1 + value2
    entry3.delete(0, END)
    entry3.insert(END, result)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)


label2 = Label(frame, text="Value1", fg="blue", width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

button1 = Button(frame, text="Reset", fg="black", font=("arial", 10, "bold"), command=reset)
button1.grid(row=1, column=0, sticky=W+E)


list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
resetVar = StringVar()
combo1 = OptionMenu(frame, resetVar, *list1)
resetVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)


'''NEW GUI CODE'''
# Add button
button2 = Button(frame, text="Add", fg="black", font=("arial", 10, "bold"), command=add)
button2.grid(row=2, column=0, sticky=W+E)

# Add comboBox
list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
addVar = StringVar()
combo2 = OptionMenu(frame, addVar, *list2)
addVar.set("1")
combo2.grid(row=2, column=1, sticky=W+E)

# Result label
label3 = Label(frame, text="Result", fg="blue", width=15, font=("arial", 10, "bold"))   #
label3.grid(row=3, column=0, sticky=W+E)

# Result entry widget
entry3 = Entry(frame)
entry3.insert(END, '1')
entry3.grid(row=3, column=1, sticky=W+E)


mainloop()