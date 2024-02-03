from tkinter import messagebox
import copy
import hashlib
import random 
import tkinter
from tkinter import *
import custom_button
import main_menu
import os
import utils
from PIL import ImageTk, Image
from tkinter import Entry
import password
import multi_segments 


s_image = []
s_image.append("")
width=0
def load_menu(window, frame):
    frame.pack_forget()
    password.start(window)

def load_segments(window,frame):
    frame.pack_forget()
    multi_segments.start(window)
    

# saves image selected by user
def clicked(canvases, canvas, img_name, event):
    for c in canvases:
        c.config(highlightthickness=0)
    canvas.config(highlightthickness=1, highlightbackground="black")
    base_name, extension = os.path.splitext(img_name)
    base_name_without_number = ''.join(filter(lambda x: not x.isdigit(), base_name))
    s_image[0] = base_name_without_number
    print(s_image[0])

def get_images_from_directory(category, num_images):
    directory = "credentialImages"
    file_list = [file for file in os.listdir(directory) if file.startswith(category)]
    selected_images = random.sample(file_list, min(num_images, len(file_list)))
    return selected_images


def new_images(login_frame):
    canvases=[]
    photo_images=[]
    total_width=0
    categories = ["cat", "mouse", "flower"]
    num_images_per_category = 1

    # Iterate over categories to create canvases with images
    for i, category in enumerate(categories):
        # Get random images for the current category
        selected_images = get_images_from_directory(category, num_images_per_category)

        for j, img_name in enumerate(selected_images):
            canvas = Canvas(login_frame, width=110, height=70)
            
            canvas.bind("<Button-1>", lambda event, canvas=canvas, img_name=img_name: clicked(canvases, canvas, img_name, event))
            img_path = os.path.join("credentialImages", img_name)
            img = Image.open(img_path)
            img = img.resize((90, 60))
            photo_img = ImageTk.PhotoImage(img)
            photo_images.append(photo_img)  # Retain a reference to prevent garbage collection
            canvas.create_image(10, 10, anchor="nw", image=photo_img)
            canvases.append(canvas)
            # Update total width
            total_width += canvas.winfo_reqwidth()

    
    # Calculate the starting x-coordinate to center the canvases
    start_x = (1280 - total_width-150) // 2
    
    # Shuffle the order of canvases
    random.shuffle(canvases)
    for i, canvas in enumerate(canvases):
        canvas.place(x=start_x+150 * i + 50, y=290) 
    
    return photo_images,canvases

    
# authenticate credentials provided by users
global auth
def authenticate(window, login_frame, selected_image, selected_password, selected_name,photo_images, canvases):
    auth=0
    # checks if there is no empty entry
    if selected_name == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif selected_name == "" and selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    print("hiii",selected_image)

    # taking hash of password entered as its hash stored in backend
    h = hashlib.new('sha512_256')
    h.update(selected_password.encode())
    selected_password = h.hexdigest()
    filepath = "credentialImages/orig_credentials.txt"  # File Path
    f = open(filepath, "r")
    name = ""
    password = ""
    image = ""
    str = ""
    isUser = 0
    # file reading to get original credentials
    while True:
        string = f.readline()  # Reading file line by line
        if string == "":
            if (isUser == 0):
                print("username not exist")
                messagebox.showinfo("Login System", "password is not correct")
            break
        info = string.split(" ")
        name = copy.deepcopy(info[0])
        password = copy.deepcopy(info[1])
        image = copy.deepcopy(info[2])
        name = name.rstrip()
        password = password.rstrip()
        image = image.rstrip()

        # checks the credentials by somparing with original one
        if name == selected_name:
            isUser = 1
            if password == selected_password:
                if image == selected_image:
                    print("password level authenticated!!")
                    auth=1
                    utils.create_popup(msg="Loading next method...", font="Gabriola 28 bold")
                    # messagebox.showinfo("Login System", "Authenticated!!")
                    break
                else:
                    print("image is not correct")
                    messagebox.showinfo("Login System", "Wrong Username/Password")
                    break
            else:
                print("password is not correct")
                messagebox.showinfo("Login System", "Wrong Username/Password")
                for c in canvases:
                    c.config(highlightthickness=0)
                new_photo_images, new_canvases = new_images(login_frame)
                # Replace old references with new ones
                photo_images[:] = new_photo_images
                canvases[:] = new_canvases
                break
    if auth == 1:
        load_segments(window,login_frame)



# login page canvas
def create_canvas(window):
    window.title("Login Page")
    window.geometry("1280x600")

    login_frame = Frame(window, height=600, width=1280)
    login_frame.pack(fill='both', expand=1)

    width = 700
    height = 700
    # canvas for title
    canvas = Canvas(login_frame, width=width, height=height, bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, anchor='nw')
    label = Label(login_frame, text="Login Page", font=("Ariel 15 bold"))
    canvas.create_window(550, 40, anchor="nw", window=label)

    # canvas for username title
    user_label = Label(login_frame, text="User name:", font=("Ariel 12 bold"))
    canvas.create_window(480, 130, anchor="nw", window=user_label)

    # canvas for password title
    password_label = Label(login_frame, text="Password:", font=("Ariel 12 bold"))
    canvas.create_window(480, 210, anchor="nw", window=password_label)

    # usernmae input field display
    user_entry = Entry(login_frame, font=("Ariel 12"))
    user_entry.focus()
    selected_name = user_entry.get()
    canvas.create_window(580, 130, anchor="nw", window=user_entry)

    # password input field display
    pas = StringVar()
    password_entry = Entry(login_frame, textvar=pas, font=("Ariel 12"), show="*")
    selected_password = password_entry.get()
    canvas.create_window(580, 210, anchor="nw", window=password_entry)
    
    photo_images,canvases=new_images(login_frame)
    
    # login button display
    # calls authenticate on click with credentials as arguments
    login = custom_button.TkinterCustomButton(master=login_frame, text="Log In", height=40, corner_radius=10,
                   command=lambda: authenticate( window, login_frame, s_image[0], password_entry.get(), user_entry.get(),photo_images, canvases)).place(relx=0.5, rely=0.7, anchor=CENTER)
    
    #Go Back button
    custom_button.TkinterCustomButton(master=login_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, login_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)
    
    
    window.mainloop()

def start(window):
    create_canvas(window)