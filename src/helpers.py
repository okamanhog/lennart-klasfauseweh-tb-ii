from PIL import Image,ImageTk
import tkinter as tk


def set_background(root, image_file_path):
    """This function was inspired by Robin Paul and sets the background image

    You need to specify the variable that creates the gui frame and the file path of the image
    """

    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.lower() # places it a layer lower so it does not overlap with the xp counter


def clear_widgets(root, exclude=[]):
    """This function will destroy any widgets you created

    You need to specify the variable that creates the gui frame
    """
    for i in root.winfo_children():
        # this deletes everything except one widget (in my case xp, because it should be permanently visible), Reference: https://stackoverflow.com/a/52844255
        if i not in exclude:
            i.destroy()


