from tkinter import *


def login():
    master = Tk()
    Label(master, text='Username').grid(row=0)
    Label(master, text='Password').grid(row=1)
    first_name = StringVar()
    last_name = StringVar()
    first_name_entry = Entry(master, textvariable=first_name)
    last_name_entry = Entry(master, textvariable=last_name)
    
    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)

    def get_names():  # Use nonlocal to update the global variables
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        print("Username: ", fname)
        print("Password: ", lname)
        master.destroy()

    submit_button = Button(master, text="Submit", command=get_names)
    submit_button.grid(row=2, columnspan=2)

    master.mainloop()