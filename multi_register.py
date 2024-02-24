from tkinter import messagebox
import copy
import hashlib
import random 
import sqlite3
import tkinter
from tkinter import *
import custom_button
import os
import utils
from PIL import ImageTk, Image
from tkinter import Entry
import password
import multi_level
import multi_login



s_image = []
s_image.append("")

def load_menu(window, frame):
    frame.pack_forget()
    multi_level.start(window)
def load_login(window,frame):
    frame.pack_forget()
    multi_login.start(window)

# saves image selected by user
def clicked(canvas, img_name, event):
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

#register
global auth
def register(window,registration_frame,selected_image,selected_password, selected_name,selected_reenter_password):
    # checks if there is no empty entry
    auth=0
    if selected_name == "" and selected_password == "":
        messagebox.showinfo("Registration System", "Please enter the Username and Password")
    elif selected_name == "":
        messagebox.showinfo("Registration System", "Please enter the Username")
    elif selected_password == "":
        messagebox.showinfo("Registration System", "Please enter the Password")
    elif selected_reenter_password == "":
        messagebox.showinfo("Registration System", "Please re-enter the Password")
    elif selected_password != selected_reenter_password:
        messagebox.showinfo("Registration System", "Passwords do not match")
    else:
    # taking hash of password entered as its hash stored in backend
        h = hashlib.new('sha512_256')
        h.update(selected_password.encode())
        selected_password = h.hexdigest()
        # filepath = "credentialImages/orig_credentials.txt"  # File Path
        # f = open(filepath, "r")
        
        username = ""
        # isUser = 0
        
        cursor.execute("SELECT * from credentials_table where username=?",[selected_name])
        username=cursor.fetchone()
        if not username:  #username does not exist then
            cursor.execute("INSERT INTO credentials_table (username,password,image_category) VALUES (?, ?, ?)",(selected_name,selected_password,selected_image))
            conn.commit()
            messagebox.showinfo("Registration System","User Registered Successfully!")
            auth=1
        else:
            # print("Username already exists!!")
            messagebox.showinfo("Registration System", "Username already exists!!")
    if auth==1:
        load_login(window,registration_frame)
    
    # file reading to get original credentials
    # while True:
    #     string = f.readline()  # Reading file line by line
    #     if string == "":
    #         break
    #     info = string.split(" ")
    #     username = info[0].rstrip()
        # password = copy.deepcopy(info[1])
        # image = copy.deepcopy(info[2])
        # name = name.rstrip()
        # password = password.rstrip()
        # image = image.rstrip()

        # checks the credentials by somparing with original one
        # if username == selected_name:
        #     print("Username already exists!!")
        #     messagebox.showinfo("Registration System", "Username already exists!!")
        #     isUser=1
        #     break
    # f.close()
    
    # if isUser==0:
        # f=open(filepath,'a')
        # f.write(f'\n{selected_name} {selected_password} {selected_image}')
        # f.close()
        

#register canvas
def create_registration_canvas(window):
    window.title("Registration Page")
    
    registration_frame=Frame(window, height=600, width=1280)
    registration_frame.pack(fill='both', expand=1)
    
    width = 700
    height = 700
    
    canvas = Canvas(registration_frame, width=width, height=height, bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0,0,anchor='nw')
    label = Label(registration_frame, text="Registration Page", font=("Arial 15 bold"))
    canvas.create_window(550,40,anchor="nw",window=label)
    
    # Registration form labels
    user_label = Label(registration_frame, text="User name:", font=("Arial 12 bold"))
    canvas.create_window(480, 130, anchor="nw", window=user_label)

    password_label = Label(registration_frame, text="Password:", font=("Arial 12 bold"))
    canvas.create_window(480, 180, anchor="nw", window=password_label)

    reenter_label = Label(registration_frame, text="Re-enter Password:", font=("Arial 12 bold"))
    canvas.create_window(480, 230, anchor="nw", window=reenter_label)

    image_label = Label(registration_frame, text="Choose an Image", font=("Arial 12 bold"))
    canvas.create_window(580, 280, anchor="nw", window=image_label)
    
    # Registration form entry fields
    user_entry = Entry(registration_frame, font=("Arial 12"))
    user_entry.focus()
    canvas.create_window(640, 130, anchor="nw", window=user_entry)

    pas = StringVar()
    password_entry = Entry(registration_frame, textvar=pas, font=("Arial 12"), show="*")
    canvas.create_window(640, 180, anchor="nw", window=password_entry)

    reenter_pas = StringVar()
    reenter_password_entry = Entry(registration_frame, textvar=reenter_pas, font=("Arial 12"), show="*")
    canvas.create_window(640, 230, anchor="nw", window=reenter_password_entry)

    # You may need to adjust the image selection mechanism based on your requirements
    # image class names
    categories = ["cat", "mouse", "flower"]
    num_images_per_category = 1
    photo_images = []
    canvases = []
    selected_image = ""
    total_width=0
    # Iterate over categories to create canvases with images
    for i, category in enumerate(categories):
        # Get random images for the current category
        selected_images = get_images_from_directory(category, num_images_per_category)

        for j, img_name in enumerate(selected_images):
            canvas = Canvas(registration_frame, width=110, height=70)
            
            canvas.bind("<Button-1>", lambda event, canvas=canvas, img_name=img_name: clicked(canvas, img_name, event))
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
    start_x = (registration_frame.winfo_reqwidth() - total_width-150) // 2
    
    # Shuffle the order of canvases
    random.shuffle(canvases)
    for i, canvas in enumerate(canvases):
        canvas.place(x=start_x+150 * i + 50, y=320)
        
    # image_entry = Entry(registration_frame, font=("Arial 12"))
    # canvas.create_window(580, 280, anchor="nw", window=image_entry)

    # Registration button
    custom_button.TkinterCustomButton(master=registration_frame, text="Register", height=40, corner_radius=10,
                                      command=lambda: register(window,registration_frame,s_image[0], password_entry.get(), user_entry.get(), reenter_password_entry.get())).place(relx=0.5, rely=0.8, anchor=CENTER)
    
    # Back Button
    custom_button.TkinterCustomButton(master=registration_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, registration_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)
    window.mainloop()
def start(window):
    global cursor,conn
    conn = sqlite3.connect("credentialImages/credentials_db.db")
    cursor = conn.cursor()
    print('Database created')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            image_category TEXT
        )
    ''')
    conn.commit()
    print('Table exists/created')
    create_registration_canvas(window)
    conn.close()