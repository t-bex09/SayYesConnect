from tkinter import *
from Login import *
from signUp import *
def create_page():
    # Create the Tkinter window
    window = Tk(className="SayYes Connect")

    # Set the screen size
    window.geometry("900x600")  # Set the width and height as desired

    # Set the background color
    window.configure(bg="lightblue")  # Set the color name or use hex code

    # Create the login button
    login_button = Button(window, text="Login", command=login, width=10,height=5)
    login_button.pack(pady=20,expand=False, side=TOP)
    login_button.place(x=350,y=400)
    # Create the sign-up button
    signup_button = Button(window, text="Sign Up", command=signUp, width=10,height=5)
    signup_button.pack(pady=20,expand=False, side=TOP)
    signup_button.place(x=450,y=400 )
    # Run the Tkinter event loop
    window.mainloop()



if __name__ == "__main__":
    create_page()
