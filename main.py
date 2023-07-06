from tkinter import *
from Login import *
from signUp import *
from generator import generate_random_users
Users = generate_random_users(50)
Companies = []
#font = alata
def create_page():
    # Create the Tkinter window
    window = Tk(className="SayYes Connect")
    set_dimensions(window)
    window.geometry(f"{screen_width}x{screen_height}")
    # Set the background color
    window.configure(bg="#3569A3")  # Set the color name or use hex code
    # Create a frame for centering the text box
    frame = Frame(window)
    frame.pack(pady=20)

    # Create the text box with default text
    text_entry = Entry(frame, font=("Great Vibes", 24), bg="#F1CCD8", width=23)
    text_entry.insert(0, "Welcome to SayYes Connect")
    text_entry.pack()

    # Position the frame at the center top
    frame.place(relx=0.5, rely=0, anchor=N)
    # Create the login button
    login_button = Button(window, text="Login", command=login, width = int(screen_width//100), height=int(screen_height//100),background="#F1CCD8")
    login_button.pack(pady=20,expand=False, side=TOP)
    login_button.place(x=int((screen_width//2)-(screen_width//200)-100),y=int(screen_height//2))
    # Create the sign-up button
    signup_button = Button(window, text="Sign Up", command=signUp, width = int(screen_width//100), height=int(screen_height//100),background="#F1CCD8")
    signup_button.pack(pady=20,expand=False, side=TOP)
    signup_button.place(x=int((screen_width//2)+(screen_width//200)),y=int(screen_height//2) )
    # Run the Tkinter event loop
    window.mainloop()

def get_users():
    return Users
def add_user(user):
    Users.append(user)
def get_companies():
    return Companies
def add_company(company):
    Companies.append(company)

def set_dimensions(screen):
    global screen_height
    global screen_width
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

if __name__ == "__main__":
    create_page()
