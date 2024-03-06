
# import tkinter
# from tkinter import *
# import custom_button
# import main_menu

# import utils
# from PIL import ImageTk, Image
# from tkinter import Entry
# import random


# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)


# def start(window):
#     filepath = "garbledImages/original_garbled.txt"  # File Path
#     garbledImages = utils.getGarbledImages()
#     num = random.randint(0, len(garbledImages) - 1)
#     filename = garbledImages[num]

#     f = open(filepath, "r")

#     while True:
#         string = f.readline()  # Reading file line by line
#         s1 = string.split(' ')[0]  # Getting first word (filename) of line
#         if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
#             break
#     string = string.split(' ')
#     string.pop(0)
#     original_text = string[0]
#     original_text = original_text.rstrip()  # Removing 
#     f.close()

#     print(original_text)
#     print(filename)

#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     garbled_frame = Frame(window, height=600, width=1280)
#     garbled_frame.pack(fill='both', expand=1)

#     label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20))
#     label.pack(padx=40, pady=10)

#     canvas = Canvas(garbled_frame, width=450, height=300)
#     img = (Image.open("garbledImages/" + filename))
#     img = img.resize((450, 300)) #resample=Image.ANTIALIAS
#     img = ImageTk.PhotoImage(img)
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.place(relx=0.45, rely=0.5, anchor=E)

#     def check():
#         entered_text = input.get()
#         if entered_text == original_text:
#             print("Authenticated")
#             utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#         else:
#             print("Authentication Failed")
#             utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

#     input = StringVar()
#     Label(garbled_frame, text="Enter word", font="ariel 16 bold").place(relx=0.7, rely=0.40, anchor=CENTER)
#     Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(
#         relx=0.7,
#         rely=0.5,
#         anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
#                                       command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

#     while True:
#         window.update_idletasks()
#         window.update()

# import hashlib
# import os
# import tkinter
# from tkinter import *
# import custom_button
# import main_menu
# import utils
# from PIL import ImageTk, Image
# import random
# import sqlite3 


# def load_menu(window, frame):
#     frame.pack_forget()
#     main_menu.start(window)

# def start(window):
#     def update_timer():
#         nonlocal timer
#         timer -= 1
#         timer_label.config(text=f"Time left: {timer} seconds")
#         if timer <= 0:
#             reset_timer()
#         window.after(1000, update_timer)

#     def reset_timer():
#         # print('reset loki ochina')
#         nonlocal timer
#         timer = 30
#         # update_timer()
#         load_new_image()

#     def load_new_image():
#         nonlocal timer
#         timer=30
#         nonlocal filename, original_text, img
#         num = random.randint(0, len(garbledImages) - 1)
#         filename = garbledImages[num]

#         # Fetch hashed original text in the image
#         original_text=fetcher() 
        
#         img = (Image.open("garbledImages/" + filename))
#         img = img.resize((200, 200))
#         img = ImageTk.PhotoImage(img)
#         canvas.itemconfig(image_on_canvas, image=img)

#     garbledImages = utils.getGarbledImages()
#     # filepath = "garbledImages/original_garbled.txt"
#     num = random.randint(0, len(garbledImages) - 1)
#     filename = garbledImages[num]
    
#     # def fetcher():
#     #     base_name, extension = os.path.splitext(filename)
#     #     h=hashlib.new('sha512_256')
#     #     h.update(base_name.encode())
#     #     base_name=h.hexdigest()
#     #     conn = sqlite3.connect('./garbledImages/garbled_db.db')
#     #     cursor = conn.cursor()

#     #     cursor.execute('SELECT original_text from garbled_table WHERE original_text=?',[base_name,])
#     #     return cursor.fetchone()[0]

#     def fetcher():
#         base_name, extension = os.path.splitext(filename)
#         h = hashlib.new('sha512_256')
#         h.update(base_name.encode())
#         base_name_hash = h.hexdigest()

#         conn = sqlite3.connect('./garbledImages/garbled_db.db')
#         cursor = conn.cursor()

#         cursor.execute('SELECT original_text FROM garbled_table WHERE original_text = ?', [base_name_hash])
#         result = cursor.fetchone()
#         if result is not None:
#             return result[0]
#         else:
#             # Handle the case when no rows are returned from the query
#             return None  # or any default value you prefer

    
    
#     original_text=fetcher()    
    
#     window.title("Graphical Authentication System")
#     window.geometry("1280x600")

#     garbled_frame = Frame(window, height=600, width=1280,bg='#F5F5DC')
#     garbled_frame.pack(fill='both', expand=1)

#     label = Label(garbled_frame, text="Garbled Image Authentication", font=('Goudy Old Style', 40),bg='#F5F5DC')
#     label.pack(padx=40, pady=20)

#     label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20),bg='#F5F5DC')
#     label.pack(padx=40, pady=20)

#     canvas = Canvas(garbled_frame, width=300, height=250,bg='#F5F5DC')
#     img = (Image.open("garbledImages/" + filename))
#     img = img.resize((300, 250))
#     img = ImageTk.PhotoImage(img)
#     image_on_canvas = canvas.create_image(10, 10, anchor=NW, image=img)
#     canvas.place(relx=0.40, rely=0.53, anchor=E)

#     timer = 30
#     timer_label = Label(garbled_frame, text=f"Time left: {timer} seconds", font=('Calibri', 16),bg='#F5F5DC')
#     timer_label.place(relx=0.5, rely=0.9, anchor=CENTER)

#     def check():
#         hasher=hashlib.new('sha512_256')
#         entered_text = input.get()
#         hasher.update(entered_text.encode())
#         entered_text=hasher.hexdigest()
#         print('o_t: ',original_text)
#         print('entered:',entered_text)
#         if entered_text == original_text:
#             # print("Authenticated")
#             utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
#             load_menu(window,garbled_frame)
#             # print("Nenu execute aithunna")
#             # reset_timer()
#         else:
#             print("Authentication Failed")
#             utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")
#             reset_timer()

#     input = StringVar()
#     Label(garbled_frame, text="Enter word", font="ariel 16 bold",bg='#F5F5DC').place(relx=0.7, rely=0.40, anchor=CENTER)
#     Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(relx=0.7,rely=0.5,anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
#                                       command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

#     custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
#                                       command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

#     update_timer()

#     # window.mainloop()



# garbled.py

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
        nonlocal timer
        timer = 30
        load_new_image()

    def load_new_image():
        timer = 30  # Assigning timer without nonlocal keyword
        filename = garbledImages[num]

        # Fetch hashed original text in the image
        original_text = fetcher() 
        if original_text is None:
            print("Original text not found for image:", filename)
            # Handle the case when original text is not found
            # For now, simply skip this image
            load_new_image()  # Reload new image
            return
            
        img = (Image.open("garbledImages/" + filename))
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        canvas.itemconfig(image_on_canvas, image=img)


    garbledImages = utils.getGarbledImages()
    num = random.randint(0, len(garbledImages) - 1)
    filename = garbledImages[num]

    def fetcher():
        base_name, extension = os.path.splitext(filename)
        h = hashlib.new('sha512_256')
        h.update(base_name.encode())
        base_name_hash = h.hexdigest()

        conn = sqlite3.connect('./garbledImages/garbled_db.db')
        cursor = conn.cursor()

        cursor.execute('SELECT original_text FROM garbled_table WHERE original_text = ?', [base_name_hash])
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None  # Return None if original text is not found

    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    garbled_frame = Frame(window, height=600, width=1280, bg='#F5F5DC')
    garbled_frame.pack(fill='both', expand=1)

    label = Label(garbled_frame, text="Garbled Image Authentication", font=('Goudy Old Style', 40), bg='#F5F5DC')
    label.pack(padx=40, pady=20)

    label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20), bg='#F5F5DC')
    label.pack(padx=40, pady=20)

    canvas = Canvas(garbled_frame, width=300, height=250, bg='#F5F5DC')
    img = (Image.open("garbledImages/" + filename))
    img = img.resize((300, 250))
    img = ImageTk.PhotoImage(img)
    image_on_canvas = canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.place(relx=0.40, rely=0.53, anchor=E)

    timer = 30
    timer_label = Label(garbled_frame, text=f"Time left: {timer} seconds", font=('Calibri', 16), bg='#F5F5DC')
    timer_label.place(relx=0.5, rely=0.9, anchor=CENTER)

    def check():
        hasher = hashlib.new('sha512_256')
        entered_text = input.get()
        hasher.update(entered_text.encode())
        entered_text = hasher.hexdigest()

        if entered_text == original_text:
            utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
            load_menu(window, garbled_frame)
        else:
            print("Authentication Failed")
            utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")
            reset_timer()

    input = StringVar()
    Label(garbled_frame, text="Enter word", font="ariel 16 bold", bg='#F5F5DC').place(relx=0.7, rely=0.40, anchor=CENTER)
    Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(relx=0.7, rely=0.5, anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10, command=check).place(relx=0.7, rely=0.6, anchor=CENTER)
    custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10, command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

    update_timer()
