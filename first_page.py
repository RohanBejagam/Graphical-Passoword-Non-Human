from tkinter import *
from tkinter import font
import custom_button
import main_menu
def load_main(window,menu_frame):
    menu_frame.pack_forget()
    main_menu.start(window)

def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    menu_frame = Frame(win, height=600, width=1280,bg="#F5F5DC")
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Graphical Password Authentication System \nfor Non-Human Intruder Defence", font=('Goudy Old Style', 35),bg="#F5F5DC")
    label.pack(padx=40, pady=30)
    btn_height = 90
    btn_width = 450
    btn_font = ('Footlight MT Light', 18,'bold')
    btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Main Menu", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_main(win, menu_frame)).pack()

if __name__ == "__main__":
    win = Tk()
    start(win)
    win.mainloop()