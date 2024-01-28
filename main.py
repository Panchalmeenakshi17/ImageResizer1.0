import cv2
import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(title="Select Source Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

# Create the main window
root = tk.Tk()

# Create a button
button = tk.Button(root, text="Click Me to select your Image!", command=select_file)

# Pack the button into the window
button.pack()

# Keep the window open
root.mainloop()

# Get the source file path from the user
source = select_file()

if not source:
    print("No file Selected!")
else:
    try:
        print(f"Your file named - {source} has been uploaded!")
        # destination = "newimage.jpg"
        scale_percent = 50

        src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
        # cv2.imshow("meenakshi",src)

        newWidth = int(src.shape[1]*scale_percent/100)
        newHeight = int(src.shape[0]*scale_percent/100)

        output = cv2.resize(src, (newWidth, newHeight))

        destination = input("\n\nEnter the name for the newly generated image with your desired extension!: ")

        newImage = cv2.imwrite(destination, output)

        if destination == newImage or destination == source:
            print("New Image name already taken!")
        else:
            print(f"\n\nA new Image with the name {destination} has been Generated!")

    except Exception as e:
        print(f"An error occurred: {e}")
