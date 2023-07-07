from main import *
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image

def create_feed(current_user):
    master = Tk(className="Profiles")
    get_dimensions(master)
    master.geometry(f"{screen_width}x{screen_height}")
    master.configure(bg="#3569A3")  # Set the background color
    
    # Create a frame for displaying the current user's information
    current_user_frame = Frame(master, bg="#3569A3")
    current_user_frame.place(relx=0.6, rely=0.4, relwidth=0.33, relheight=1.0)
    
    # Create a label to display the current user's bio
    current_user_label = Label(current_user_frame, text=current_user.bio(), pady=10, bg="#F1CCD8")
    current_user_label.pack(fill="x")
    
    # Create a frame for displaying other users
    other_users_frame = Frame(master, bg="#3569A3")
    other_users_frame.place(relx=0, rely=0, relwidth=0.33, relheight=1.0)
    
    # Create a Canvas widget for other users
    canvas = Canvas(other_users_frame, bg="#F1CCD8")
    canvas.pack(side=LEFT, fill="both", expand=True)
    
    # Create a Scrollbar widget
    scrollbar = Scrollbar(other_users_frame, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill="y")
    
    # Configure the Canvas to work with the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Create a frame inside the Canvas to hold the users
    users_frame = Frame(canvas, bg="#F1CCD8")
    canvas.create_window((0, 0), window=users_frame, anchor="nw")
    
    # Get all users except the current user
    users = get_users()
    other_users = [user for user in users if user != current_user]
    
    def show_user(user):
        # Clear the current user frame
        current_user_frame.pack_forget()
        
        # Create a new frame for displaying user information
        frame2 = Frame(master, bg="#3569A3")
        frame2.place(relx=0.6, rely=0.4, relwidth=0.33, relheight=1.0)
        
        # Create a label to display the user's bio
        current_user_label2 = Label(frame2, text=user.bio(), pady=10, bg="#F1CCD8")
        current_user_label2.pack(fill="x")
    
    # Create buttons for other users
    for user in other_users:
        button = Button(users_frame, text=str(user), command=lambda user=user: show_user(user), pady=10, bg="#F1CCD8")
        button.pack(fill="x", pady=20)
    
    master.mainloop()
def get_dimensions(screen):
    global screen_height
    global screen_width
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
