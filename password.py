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

import password_register
import password_login

def load_menu(window,frame):
    frame.pack_forget()
    main_menu.start(window)

def start(window):
    window.title("Password Image Authentication System")
    password_selector = Frame(window, height=600, width=1280)
    password_selector.pack(fill='both', expand=1)
    def login():
        password_selector.pack_forget()
        password_login.start(window)
    
    def register():
        password_selector.pack_forget()
        password_register.start(window)
        
    custom_button.TkinterCustomButton(master=window, text="Registration", height=50, corner_radius=10,
                                      command=register).place(relx=0.4, rely=0.5, anchor=CENTER)

    # Button to switch to the login page
    custom_button.TkinterCustomButton(master=window, text="Login", height=50, corner_radius=10,
                                      command=login).place(relx=0.5, rely=0.5, anchor=CENTER)
    custom_button.TkinterCustomButton(master=window, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window,password_selector)).place(relx=0.08, rely=0.08, anchor=CENTER)
    
    
    
