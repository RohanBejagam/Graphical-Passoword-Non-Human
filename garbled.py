import hashlib
import os
import tkinter
from tkinter import *
import custom_button
import main_menu
import utils
from PIL import ImageTk, Image
import random
import sqlite3 


def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

def start(window):
    def update_timer():
        nonlocal timer
        timer -= 1
        timer_label.config(text=f"Time left: {timer} seconds")
        if timer <= 0:
            reset_timer()
        window.after(1000, update_timer)

    def reset_timer():
        # print('reset loki ochina')
        nonlocal timer
        timer = 30
        # update_timer()
        load_new_image()

    def load_new_image():
        nonlocal timer
        timer=30
        nonlocal filename, original_text, img
        num = random.randint(0, len(garbledImages) - 1)
        filename = garbledImages[num]

        # Fetch hashed original text in the image
        original_text=fetcher() 
        
        img = (Image.open("garbledImages/" + filename))
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        canvas.itemconfig(image_on_canvas, image=img)

    garbledImages = utils.getGarbledImages()
    # filepath = "garbledImages/original_garbled.txt"
    num = random.randint(0, len(garbledImages) - 1)
    filename = garbledImages[num]
    
    def fetcher():
        base_name, extension = os.path.splitext(filename)
        h=hashlib.new('sha512_256')
        h.update(base_name.encode())
        base_name=h.hexdigest()
        conn = sqlite3.connect('./garbledImages/garbled_db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT original_text from garbled_table WHERE original_text=?',[base_name,])
        return cursor.fetchone()[0]
    
    
    original_text=fetcher()    
    
    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    garbled_frame = Frame(window, height=600, width=1280,bg='#F5F5DC')
    garbled_frame.pack(fill='both', expand=1)

    label = Label(garbled_frame, text="Garbled Image Authentication", font=('Goudy Old Style', 40),bg='#F5F5DC')
    label.pack(padx=40, pady=20)

    label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20),bg='#F5F5DC')
    label.pack(padx=40, pady=20)

    canvas = Canvas(garbled_frame, width=300, height=250,bg='#F5F5DC')
    img = (Image.open("garbledImages/" + filename))
    img = img.resize((300, 250))
    img = ImageTk.PhotoImage(img)
    image_on_canvas = canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.place(relx=0.40, rely=0.53, anchor=E)

    timer = 30
    timer_label = Label(garbled_frame, text=f"Time left: {timer} seconds", font=('Calibri', 16),bg='#F5F5DC')
    timer_label.place(relx=0.5, rely=0.9, anchor=CENTER)

    def check():
        hasher=hashlib.new('sha512_256')
        entered_text = input.get()
        hasher.update(entered_text.encode())
        entered_text=hasher.hexdigest()
        # print('o_t: ',original_text)
        # print('entered:',entered_text)
        if entered_text == original_text:
            # print("Authenticated")
            utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
            load_menu(window,garbled_frame)
            # print("Nenu execute aithunna")
            # reset_timer()
        else:
            print("Authentication Failed")
            utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")
            reset_timer()

    input = StringVar()
    Label(garbled_frame, text="Enter word", font="ariel 16 bold",bg='#F5F5DC').place(relx=0.7, rely=0.40, anchor=CENTER)
    Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(relx=0.7,rely=0.5,anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
                                      command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

    update_timer()
