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
import multi_segments
import multi_garbled

original_text = []


def load_menu(window, frame):
    frame.pack_forget()
    multi_segments.start(window)
    
def load_garbled(window,frame):
    frame.pack_forget()
    multi_garbled.start(window)

# res=0
def start(window):
    obscuredImages = utils.getObscuredImages()
    num = random.randint(1, len(obscuredImages) - 1)
    filename = obscuredImages[num]
    # filepath = "obscuredImages/original_obscure.txt"
    global original_text

    # f = open(filepath, "r")

    # while True:
    #     string = f.readline()
    #     s1 = string.split(' ')[0]
    #     if s1 == filename[0:len(filename) - 4]:
    #         break
    # # print(string)
    # string = string.split(' ')
    # string.pop(0)
    # string=' '.join(string)
    # string = string.replace(' ', '-')
    # string = string
    # original_text.append(string.rstrip())
    # f.close()
    def fetcher():
        base_name, extension = os.path.splitext(filename)
        conn = sqlite3.connect('obscuredImages/obscure_db.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT original_obscured from obscured_table where filename=?',(base_name,))
        return cursor.fetchone()[0]
    
    original_text=fetcher().rstrip()

    obscure_frame = Frame(window, height=600, width=1280,bg='#F5F5DC')
    obscure_frame.pack(fill='both', expand=1)

    window.title("Graphical Authentication System")
    window.geometry("1280x600")
    heading_label = Label(obscure_frame, text="Obscure Image Authentication System", font=('Goudy Old Style', 40),bg='#F5F5DC')
    heading_label.pack(pady=20)
    label = Label(obscure_frame, text="Click on the microphone and speak the words in the following image", font=('Calibri', 20),bg='#F5F5DC')
    label.pack(pady=10)
    tag_line = Label(obscure_frame, text="Say 'STOP' in order to stop recording", font=('Calibri', 15),bg='#F5F5DC')
    tag_line.pack(pady=20)
    canvas = Canvas(obscure_frame, width=420, height=220,bg='#F5F5DC')
    img = (Image.open("obscuredImages/" + filename))
    img = img.resize((420, 220))
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,anchor=NW, image=img)
    canvas.place(relx=0.8, rely=0.35, anchor=CENTER)
    canvas.pack(pady=10)

    canvas2 = Canvas(obscure_frame, width=120, height=100,bg='#F5F5DC')
    def toggle(event):
        input_text = None

        while True:
            e = sr.Recognizer()
            with sr.Microphone() as source:
                try:
                    utils.create_popup1(msg="Speak now", font="Gabriola 28 bold")
                    print("Say Something. Say 'stop' inorder to stop ")
                    audio = e.listen(source)
                    input_text = e.recognize_google(audio)
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
            print("Going to garbled")
            utils.create_popup(msg="Loading next method...", font="Gabriola 28 bold")
            load_garbled(window,obscure_frame)
            # utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
        else:
            print("Authentication Failed")
            utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")
    
    canvas2.bind("<Button-1>", toggle)
    img2 = (Image.open("assets/mic.jpg"))
    img2 = img2.resize((120, 100))
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(0, 0, anchor=NW, image=img2)
    canvas2.place(relx=0.5, rely=0.6, anchor=CENTER)  # Place at the center vertically
    canvas2.pack(pady=20)

    custom_button.TkinterCustomButton(master=obscure_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, obscure_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)
    # # Add timer of 30 seconds
    # timer_label = Label(obscure_frame, text="Time left: 30 seconds", font=('Calibri', 16))
    # timer_label.pack(pady=10)

    # def update_timer(seconds_left):
    #     timer_label.config(text=f"Time left: {seconds_left} seconds")

    # def reload_window():
    #     window.destroy()
    #     new_window = Tk()
    #     start(new_window)

    # # Countdown timer function
    # def countdown_timer(seconds_left):
    #     if seconds_left > 0:
    #         update_timer(seconds_left)
    #         window.after(1000, countdown_timer, seconds_left - 1)
    #     else:
    #         timer_label.config(text="Time's up!")
    #         reload_window()

    # # Start the countdown timer
    # countdown_timer(30)

    # Periodically check for updates
    # window.after(100, lambda: window.update_idletasks())
    # window.after(100, lambda: window.update())
    
    

    # Periodically check for updates
    window.after(100, lambda: window.update_idletasks())
    window.after(100, lambda: window.update())
    
    window.mainloop()


if __name__ == "__main__":
    root = Tk()
    start(root)
