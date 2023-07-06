from main import *
from tkinter import *



def create_feed(current_user):
    master = Tk(className="Profiles")
    get_dimensions(master)
    master.geometry(f"{screen_width}x{screen_height}")
    # Set the background color
    master.configure(bg="#3569A3")  # Set the color name or use hex code
    # Create a frame for centering the text box
    users = get_users()
    frame = Frame(master, bg="#3569A3")
    frame.place(relx=0, rely=0, relwidth=0.33, relheight=1.0)
    for count,user in enumerate(users):
        user_info = str(user)  # Get the string representation of the user object

        # Create a button for each user with their information as the button text
        button = Button(frame, text=user_info, command=lambda: show_user(user),pady=10)
        button.pack(pady=10, fill="x")
    master.mainloop()
def show_user(user):
    return False

def get_dimensions(screen):
    global screen_height
    global screen_width
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
