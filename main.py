from tkinter import *

def create_page():
    # Create the Tkinter window
    window = Tk(className="SayYes Connect")

    # Set the screen size
    window.geometry("900x600")  # Set the width and height as desired

    # Set the background color
    window.configure(bg="lightgray")  # Set the color name or use hex code

    # Run the Tkinter event loop
    window.mainloop()



if __name__ == "__main__":
    create_page()
