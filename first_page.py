# from tkinter import *
# from tkinter import font
# import custom_button
# import main_menu
# from PIL import ImageTk, Image
# def load_main(window,menu_frame):
#     menu_frame.pack_forget()
#     main_menu.start(window)

# def start(win):
#     win.geometry("1280x600")
#     win.title("Graphical Authentication System")
#     img1 = Image.open("assets/logo.png")
#     img1 = img1.resize((50, 50))
#     img1 = ImageTk.PhotoImage(img1)

#     menu_frame = Frame(win, height=600, width=1280,bg="#F5F5DC")
#     menu_frame.pack(fill='both', expand=1)

#     label = Label(menu_frame, text="Graphical Password Authentication System \nfor Non-Human Intruder Defence", font=('Goudy Old Style', 35),bg="#F5F5DC")
#     label.pack(padx=50, pady=50)
#     btn_height = 90
#     btn_width = 450
#     btn_font = ('Footlight MT Light', 18,'bold')
#     btn1 = custom_button.TkinterCustomButton(master=menu_frame,image=img1,
#                                              height=btn_height, width=btn_width, corner_radius=10,
#                                              command=lambda: load_main(win, menu_frame)).pack(padx=100,pady=100)

# # Assuming img1 is your image file path
# # img = Image.open("assets/logo.png")
# # img = img.resize((btn_width, btn_height), Image.ANTIALIAS)
# # img = ImageTk.PhotoImage(img)

# def on_button_click():
#     load_main(win, menu_frame)

# menu_frame = tk.Frame()  # Assuming menu_frame is already defined
# label = tk.Label(menu_frame, image=img, width=btn_width, height=btn_height)
# label.image = img  # Keeping a reference to avoid garbage collection
# label.bind("<Button-1>", lambda event: on_button_click())
# label.pack(padx=100, pady=100)

# if __name__ == "__main__":
#     win = Tk()
#     start(win)
#     win.mainloop()



from tkinter import *
from tkinter import font
import custom_button
import main_menu
from PIL import ImageTk, Image

def load_main(window, menu_frame):
    menu_frame.pack_forget()
    main_menu.start(window)

def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    menu_frame = Frame(win, height=600, width=1280, bg="#F5F5DC")
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Graphical Password Authentication System \nfor Non-Human Intruder Defence", font=('Goudy Old Style', 35), bg="#F5F5DC")
    label.pack(padx=50, pady=100)

    btn_height = 250
    btn_width = 250

    # Load and resize the image
    img = Image.open("assets/logo.png")
    img = img.resize((btn_width, btn_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # Create a button with an image
    btn = Button(menu_frame, image=img, height=btn_height, width=btn_width, command=lambda: load_main(win, menu_frame), bd=0)
    btn.image = img  # Keep a reference to avoid garbage collection
    btn.pack(padx=100)

if __name__ == "__main__":
    win = Tk()
    start(win)
    win.mainloop()
