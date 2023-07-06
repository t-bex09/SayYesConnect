from tkinter import *


def signUp():
    master = Tk()
    Label(master, text='First Name').grid(row=0)
    Label(master, text='Last Name').grid(row=1)
    first_name = StringVar()
    last_name = StringVar()
    first_name_entry = Entry(master, textvariable = first_name)
    last_name_entry = Entry(master, textvariable=last_name)
    
    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)
    mainloop()
    fname = first_name.get()
    lname = last_name.get()
    print("First Name: " + fname)
    print("Last Name: " + lname)
    return True