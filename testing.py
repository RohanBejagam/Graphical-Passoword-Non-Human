import pyautogui
import time
import random

# Function to register a new user
def register(username, password, reenter_password):
    # Click on the Register button
    pyautogui.click(640, 520)  # Adjust the coordinates based on your screen resolution

    # Type the username
    pyautogui.write(username)

    # Type the password
    pyautogui.press('tab')  # Move to the next field
    pyautogui.write(password)

    # Type the re-entered password
    pyautogui.press('tab')  # Move to the next field
    pyautogui.write(reenter_password)

    # Click on a random image canvas
    select_image()

    # Click on the Register button
    pyautogui.press('enter')  # Submit the form

# Function to select a random image canvas
def select_image():
    # Calculate the number of image canvases
    num_canvases = 3  # Assuming there are 3 image canvases
    # Generate a random index to select a canvas
    canvas_index = random.randint(0, num_canvases - 1)
    # Calculate the coordinates of the canvas based on its index
    canvas_x = 50 + canvas_index * 150  # Adjust these values based on your canvas positions
    canvas_y = 320

    # Click on the canvas
    pyautogui.click(canvas_x, canvas_y)  # Adjust the coordinates based on your screen resolution

# Function to login with existing credentials
def login(username, password):
    # Click on the Login button
    pyautogui.click(640, 600)  # Adjust the coordinates based on your screen resolution

    # Type the username
    pyautogui.write(username)

    # Type the password
    pyautogui.press('tab')  # Move to the next field
    pyautogui.write(password)

    # Click on the Login button
    pyautogui.press('enter')  # Submit the form

# Example usage:
# Assuming the Tkinter application is open and visible on the screen
time.sleep(2)  # Add a delay to ensure the application is fully loaded

# Register a new user
register("new_user", "password123", "password123")

# Wait for registration process to complete (adjust sleep time accordingly)
time.sleep(5)

# Alternatively, you can directly login with existing credentials
login("existing_user", "password123")

# Wait for login process to complete (adjust sleep time accordingly)
time.sleep(5)