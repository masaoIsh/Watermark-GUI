from tkinter import *
from tkinter import filedialog
from tkmacosx import Button
from PIL import Image, ImageTk

def UploadImage():
    filename = filedialog.askopenfilename()
    user_image = PhotoImage(file=filename)
    img_label = Label(window, image=user_image)
    img_label.image = user_image
    img_label.place(x=35, y=60)
    initial_img_label.destroy()
    print('Selected:', filename)


BACKGROUND_COLOR = "#222831"

window = Tk()
window.title("Watermark Adder")
window.config(padx=10, pady=30, bg=BACKGROUND_COLOR)
window.geometry("1235x760")

sample_img = PhotoImage(file="images/sample_img.png")
initial_img_label = Label(window, image=sample_img)
initial_img_label.place(x=35, y=60)

# Labels
title_label = Label(text="Create your Watermark", bg=BACKGROUND_COLOR, fg="#00ADB5", font=("Helvetica", 26, "bold"))
title_label.place(x=810, y=50)
watermark_text_label = Label(text="Watermark Text:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
watermark_text_label.place(x=720, y=120)
font_label = Label(text="Font:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
font_label.place(x=720, y=160)
color_label = Label(text="Color:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
color_label.place(x=720, y=200)
font_size_label = Label(text="Font Size:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
font_size_label.place(x=720, y=240)
opacity_label = Label(text="Opacity:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
opacity_label.place(x=720, y=280)
rotation_label = Label(text="Rotation:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
rotation_label.place(x=720, y=320)
position_label = Label(text="Position:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
position_label.place(x=720, y=360)

# Entries
watermark_text_entry = Entry(bg="#393E46", width=30)
watermark_text_entry.place(x=868, y=121)

# Buttons
upload_button = Button(text="Upload Image", bg="#EEEEEE", fg="#222831", borderless=1, command=UploadImage)
upload_button.place(x=290, y=460)

window.mainloop()
