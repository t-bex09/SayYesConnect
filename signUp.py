from tkinter import *
from User import User
import main
def signUp():
    master = Tk(className="Registration")
    master.geometry("300x300")
    master.configure(bg="#3569A3")
    Label(master, text='First Name',bg="#F1CCD8").grid(row=0)
    Label(master, text='Last Name',bg="#F1CCD8").grid(row=1)
    Label(master, text='Username',bg="#F1CCD8").grid(row=2)
    Label(master, text='Password',bg="#F1CCD8").grid(row=3)
    Label(master, text='Age',bg="#F1CCD8").grid(row=4)
    Label(master, text='Gender',bg="#F1CCD8").grid(row=5)
    Label(master, text='College',bg="#F1CCD8").grid(row=6)
    Label(master, text='Major',bg="#F1CCD8").grid(row=7)
    Label(master, text='Degree Level',bg="#F1CCD8").grid(row=8)
    Label(master, text='Current Occupation',bg="#F1CCD8").grid(row=9)
    Label(master, text='Current Company',bg="#F1CCD8").grid(row=10)
    Label(master, text='Any struggles in your job search?',bg="#F1CCD8").grid(row=11)
    first_name = StringVar()
    last_name = StringVar()
    age = IntVar()
    gender = StringVar()
    college = StringVar()
    major = StringVar()
    degree = StringVar()
    occupation = StringVar()
    company = StringVar()
    username = StringVar()
    password = StringVar()
    struggles = StringVar()
    username_entry = Entry(master, textvariable=username)
    password_entry = Entry(master,textvariable=password)
    first_name_entry = Entry(master, textvariable=first_name)
    last_name_entry = Entry(master, textvariable=last_name)
    age_entry = Entry(master)
    gender_entry = Entry(master, textvariable=gender)
    college_entry = Entry(master, textvariable=college)
    major_entry = Entry(master, textvariable=major)
    degree_entry = Entry(master, textvariable=degree)
    occupation_entry = Entry(master, textvariable=occupation)
    company_entry = Entry(master, textvariable=company)
    struggles_entry = Entry(master, textvariable=struggles,width=40)
    username_entry.grid(row=2,column=1)
    password_entry.grid(row=3,column=1)
    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1,column=1)
    age_entry.grid(row=4, column=1)
    gender_entry.grid(row=5, column=1)
    college_entry.grid(row=6, column=1)
    major_entry.grid(row=7, column=1)
    degree_entry.grid(row=8, column=1)
    occupation_entry.grid(row=9, column=1)
    company_entry.grid(row=10,column=1)
    struggles_entry.grid(row=11,column=1)
    def create_user():  # Use nonlocal to update the global variables
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        college = college_entry.get()
        major = major_entry.get()
        degree = degree_entry.get()
        occupation = occupation_entry.get()
        company = company_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        struggles = struggles_entry.get()
        new_user = User(fname,lname,age,gender,college,major,degree,occupation,company,username,password,struggles)
        main.add_user(new_user)
        master.destroy()

    submit_button = Button(master, text="Submit", command=create_user,bg="#F1CCD8")
    submit_button.grid(row=12, columnspan=5)

    master.mainloop()
