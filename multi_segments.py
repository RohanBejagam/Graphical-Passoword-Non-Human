import os
import tkinter
from tkinter import *
import custom_button
import main_menu

import utils
from PIL import ImageTk, Image
import random
import multi_login
import multi_obscured

def load_menu(window, frame):
    frame.pack_forget()
    multi_login.start(window)

def load_multi_obs(window,frame):
    frame.pack_forget()
    multi_obscured.start(window)

def start(window):
    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    segments_frame = Frame(window, height=600, width=1280,bg='#F5F5DC')
    segments_frame.pack(fill='both', expand=1)

    canvas = Canvas(segments_frame, width=250, height=250,bg='#F5F5DC')
    canvas.bind("<Button-1>", utils.callback)
    img = (Image.open("segmentedImages/order.jpg"))
    img = img.resize((250, 250)) #Image.ANTIALIAS
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.place(x=320,y=80)
    
    all_items= os.listdir("segmentedImages")
    folders = [item for item in all_items if os.path.isdir(os.path.join("segmentedImages", item))]
    selected_set = folders[random.randint(0,len(folders)-1)]
    print(selected_set)
    dir= os.listdir("segmentedImages/"+selected_set)
    for file in dir:
        if file.endswith(('.png','.jpg','.jpeg')):
            selected_set_image=file
    
    canvas1 = Canvas(segments_frame, width=260, height=260,bg='#F5F5DC')
    canvas1.bind("<Button-1>", utils.callback)
    img1 = (Image.open("segmentedImages/"+selected_set+"/"+selected_set_image))
    img1 = img1.resize((250, 250)) #Image.ANTIALIAS
    img1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(10, 10, anchor=NW, image=img1)
    canvas1.place(x=670,y=80)

    
    imgList = utils.getSegmentedImages(selected_set+"/parts")
    random.shuffle(imgList)
    imgClickData = []

    for imgPath in imgList:
        var = utils.imageClick(imgPath)
        imgClickData.append(var)

    def highlight0(event):
        imgClickData[0].clicked(event)
        canvas2.config(highlightthickness=1, highlightbackground="black")
    
    def highlight1(event):
        imgClickData[1].clicked(event)
        canvas3.config(highlightthickness=1, highlightbackground="black")
    
    def highlight2(event):
        imgClickData[2].clicked(event)
        canvas4.config(highlightthickness=1, highlightbackground="black")
    
    def highlight3(event):
        imgClickData[3].clicked(event)
        canvas5.config(highlightthickness=1, highlightbackground="black")
        
    # Draw shuffled segments
    label = Label(segments_frame, text="Please select below pictures in correct order", font=('Calibri', 20),bg='#F5F5DC')
    label.place(x=400, y=350)


    canvas2 = Canvas(segments_frame, width=200, height=150,bg='#F5F5DC')
    canvas2.bind("<Button-1>", highlight0)
    # canvas.config(highlightthickness=1, highlightbackground="black")
    canvas2.place(x=100, y=400)
    img2 = (Image.open(imgList[0]))
    img2 = img2.resize((200, 150)) #Image.ANTIALIAS
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor=NW, image=img2)

        
    canvas3 = Canvas(segments_frame, width=200, height=150,bg='#F5F5DC')
    canvas3.bind("<Button-1>", highlight1)
    canvas3.place(x=400, y=400)
    img3 = (Image.open(imgList[1]))
    img3 = img3.resize((200, 150)) #Image.ANTIALIAS
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(10, 10, anchor=NW, image=img3)

    canvas4 = Canvas(segments_frame, width=200, height=150,bg='#F5F5DC')
    canvas4.bind("<Button-1>", highlight2)
    canvas4.place(x=700, y=400)
    img4 = (Image.open(imgList[2]))
    img4 = img4.resize((200, 150)) #Image.ANTIALIAS
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(10, 10, anchor=NW, image=img4)

    canvas5 = Canvas(segments_frame, width=200, height=150,bg='#F5F5DC')
    canvas5.bind("<Button-1>", highlight3)
    canvas5.place(x=1000, y=400)
    img5 = (Image.open(imgList[3]))
    img5 = img5.resize((200, 150)) #Image.ANTIALIAS
    img5 = ImageTk.PhotoImage(img5)
    canvas5.create_image(10, 10, anchor=NW, image=img5)

    custom_button.TkinterCustomButton(master=segments_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, segments_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    while True:
        window.update_idletasks()
        window.update()

        if utils.checkAllClicked(imgClickData):
            # print(imgClickData)
            # for i in imgClickData:
            #     print(i.id, end=" ")
            # print()
            sortedClickList = sorted(imgClickData)
            # for i in sortedClickList:
            #     print(i.id, end=" ")
            # print()
            # # print(sortedClickList)

            if (sortedClickList[0].id == 1) and (sortedClickList[1].id == 2) and (sortedClickList[2].id == 3) and (
                    sortedClickList[3].id == 4):
                utils.create_popup(msg="Loading next method...", font="Gabriola 28 bold")
                # load_menu(window, segments_frame)
                load_multi_obs(window,segments_frame)
            else:
                utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")
                
                

            utils.setAllUnclicked(imgClickData)
