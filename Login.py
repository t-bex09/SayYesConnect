from tkinter import *
import main
from Feed import *
def login():
    master = Tk()
    master.configure(bg="#3569A3")
    Label(master, text='Username',bg="#F1CCD8").grid(row=0)
    Label(master, text='Password',bg="#F1CCD8").grid(row=1)
    username = StringVar()
    password = StringVar()
    username_entry = Entry(master, textvariable=username)
    password_entry = Entry(master, textvariable=password)
    
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def attempt_login():  # Use nonlocal to update the global variables
        username = username_entry.get()
        password = password_entry.get()
        users = main.get_users()
        for user in users:
            if user.username == username and user.password == password:
                master.destroy()
                create_feed(user)
                return True
        master.destroy()
        login()

    submit_button = Button(master, text="Submit", command=attempt_login,bg="#F1CCD8")
    submit_button.grid(row=2, columnspan=2)

    master.mainloop()