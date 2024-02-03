from tkinter import *
from PIL import Image, ImageTk
import random
import os

def clicked(canvas, img_name, event):
    print(f"Canvas {canvas} with image {img_name} clicked!")

def get_images_from_directory(category, num_images):
    directory = "credentialImages"
    file_list = [file for file in os.listdir(directory) if file.startswith(category)]
    selected_images = random.sample(file_list, min(num_images, len(file_list)))
    return selected_images

# List of categories
categories = ["cat", "mouse", "flower"]

# Number of images to display for each category
num_images_per_category = 1

# Create a Tkinter window
root = Tk()

# List to store PhotoImage objects to prevent garbage collection
photo_images = []

# List to store canvases for shuffling
canvases = []

# Iterate over categories to create canvases with images
for i, category in enumerate(categories):
    # Get random images for the current category
    selected_images = get_images_from_directory(category, num_images_per_category)

    for j, img_name in enumerate(selected_images):
        canvas = Canvas(root, width=110, height=70)
        canvas.bind("<Button-1>", lambda event, canvas=canvas, img_name=img_name: clicked(canvas, img_name, event))
        img_path = os.path.join("credentialImages", img_name)
        img = Image.open(img_path)
        img = img.resize((90, 60))
        photo_img = ImageTk.PhotoImage(img)
        photo_images.append(photo_img)  # Retain a reference to prevent garbage collection
        canvas.create_image(10, 10, anchor="nw", image=photo_img)
        canvases.append(canvas)

# Shuffle the order of canvases
random.shuffle(canvases)

# Place the shuffled canvases on the window
for i, canvas in enumerate(canvases):
    canvas.place(x=150 * i + 50, y=290)

# Start the Tkinter event loop
root.mainloop()
