import os
import sqlite3
import tkinter
from tkinter import *
import custom_button
import main_menu
import speech_recognition as sr
import utils
from PIL import ImageTk, Image
import random

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

def toggle(event):
    input_text = None
    while True:
        e = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("Say Something. Say 'stop' inorder to stop")
                audio = e.listen(source)
                input_text = e.recognize_google(audio)
                # input_text = e.recognize_sphinx(audio)
                print(input_text)
                if input_text == "stop":
                    break
            except:
                print("Exception occurred when trying to record")
        break

    input_text = input_text[:-5]
    input_text = input_text.rstrip()
    input_text = input_text.lower()
    input_text = input_text.replace(' ', '-')

    print("Original Text = ", original_text)
    print("Input Text = ", input_text)

    if original_text == input_text:
        print("Authenticated")
        utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
    else:
        print("Authentication Failed")
        utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

def start(window):
    obscuredImages = utils.getObscuredImages()
    num = random.randint(0, len(obscuredImages) - 1)
    filename = obscuredImages[num]
    global original_text

    def fetcher():
        base_name, extension = os.path.splitext(filename)
        conn = sqlite3.connect('obscuredImages/obscure_db.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT original_obscured from obscured_table where filename=?',[base_name,])
        return cursor.fetchone()[0]
    
    original_text=fetcher().rstrip()
  
    obscure_frame = Frame(window, height=600, width=1280,bg='#F5F5DC')
    obscure_frame.pack(fill='both', expand=True)  # Make the frame expand to fill its container

    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    # Heading
    heading_label = Label(obscure_frame, text="Obscure Image Authentication System", font=('Goudy Old Style', 40),bg='#F5F5DC')
    heading_label.pack(pady=20)

    # Label
    label = Label(obscure_frame, text="Click on the microphone and speak the words in the following image", font=('Calibri', 20),bg='#F5F5DC')
    label.pack(pady=10)

    # Tag Line
    tag_line = Label(obscure_frame, text="Say 'STOP' in order to stop recording", font=('Calibri', 15),bg='#F5F5DC')
    tag_line.pack(pady=20)

    # Image
    canvas = Canvas(obscure_frame, width=420, height=220,bg='#F5F5DC')
    img = (Image.open("obscuredImages/" + filename))
    img = img.resize((420, 220))
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=img)  # Use (0, 0) coordinates for image placement
    canvas.place(relx=0.8, rely=0.35, anchor=CENTER)  # Place at the center vertically
    canvas.pack(pady=10)

    # Microphone Image
    canvas2 = Canvas(obscure_frame, width=120, height=100,bg='#F5F5DC')
    canvas2.bind("<Button-1>", toggle)
    img2 = (Image.open("assets/mic.jpg"))
    img2 = img2.resize((120, 100))
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(0, 0, anchor=NW, image=img2)  # Use (0, 0) coordinates for image placement
    canvas2.place(relx=0.5, rely=0.6, anchor=CENTER)  # Place at the center vertically
    canvas2.pack(pady=20)

    # Go Back Button
    custom_button.TkinterCustomButton(master=obscure_frame, text="Go Back", height=40, corner_radius=10,command=lambda: load_menu(window, obscure_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    window.mainloop()

if __name__ == "_main_":
    root = Tk()
    start(root)