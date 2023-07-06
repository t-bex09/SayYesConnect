from tkinter import *
from Login import *
from signUp import *
def create_page():
    # Create the Tkinter window
    window = Tk(className="SayYes Connect")

    # Set the screen size
    window.geometry("900x600")  # Set the width and height as desired

    # Set the background color
    window.configure(bg="lightgray")  # Set the color name or use hex code

    # Create the login button
    login_button = Button(window, text="Login", command=login(window))
    login_button.pack(pady=10)

    # Create the sign-up button
    signup_button = Button(window, text="Sign Up", command=signUp(window))
    signup_button.pack(pady=10)

    # Run the Tkinter event loop
    window.mainloop()



if __name__ == "__main__":
    create_page()
