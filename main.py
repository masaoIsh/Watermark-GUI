import tkinter.constants
from tkinter import *
from tkinter import filedialog, messagebox
from tkmacosx import Button
from PIL import Image, ImageTk, ImageDraw, ImageFont
from time import sleep
import webcolors

# Global variables
pil_image = None
img_width = 0
img_height = 0


def save_image():
    global pil_image
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    pil_image.save(filename)


def upload_image():
    global pil_image, img_height, img_width
    img_path = filedialog.askopenfilename()
    pil_image = Image.open(img_path).convert("RGBA")
    img_width, img_height = pil_image.size

    if img_width > 660 or img_height > 610:
        while img_width > 660 or img_height > 610:
            img_width *= 0.99
            img_height *= 0.99
        pil_image = pil_image.resize(size=(int(img_width), int(img_height)))
        messagebox.showinfo(title='Warning!', message="The uploaded image is larger than the canvas. "
                                                      "It will be resized.")

    img = ImageTk.PhotoImage(pil_image)
    canvas.img = img
    canvas.create_image(660 / 2, 610 / 2, image=img, anchor=tkinter.CENTER)
    img_width_rounded = int(img_width)
    img_height_rounded = int(img_height)
    img_dimensions_label.config(
        text=f"The image is {img_width_rounded} x {img_height_rounded} pixels.\nCoordinates (0, 0) will "
             f"place the text in the top left corner.")


def apply_text():
    global pil_image
    the_image = pil_image

    txt = Image.new('RGBA', the_image.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype(font_var.get(), int(font_size_entry.get()))
    drawer = ImageDraw.Draw(the_image)

    text = watermark_text_entry.get()
    coordinates = (int(x_pos_entry.get()), int(y_pos_entry.get()))
    color_name = color_var.get()
    hex_code = webcolors.name_to_rgb(color_name)
    opacity_percent = int(opacity_var.get().split('%')[0])
    to_multiply = float(opacity_percent / 100)
    opacity_value = int(255 * to_multiply)
    fill_value = hex_code + (opacity_value,)

    drawer.text(coordinates, text, font=fnt, fill=fill_value)

    pil_image = Image.alpha_composite(the_image, txt)

    watermark_text_entry.delete(0, END)
    sleep(2)
    show_pic()


def show_pic():
    global pil_image
    the_img = ImageTk.PhotoImage(pil_image)
    canvas.img = the_img
    canvas.create_image(660 / 2, 610 / 2, image=the_img, anchor=tkinter.CENTER)
    watermark_text_entry.delete(0, END)


BACKGROUND_COLOR = "#222831"

window = Tk()
window.title("Watermark Adder")
window.config(padx=5, pady=30, bg=BACKGROUND_COLOR)
window.geometry("1235x760")

canvas = Canvas(window, width=660, height=610, bg="#EEEEEE")
canvas.place(x=35, y=20)

# Title Label
title_label = Label(text="Create your Watermark", bg=BACKGROUND_COLOR, fg="#00ADB5", font=("Helvetica", 26, "bold"))
title_label.place(x=820, y=50)

# Watermark Text
watermark_text_label = Label(text="Watermark Text:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
watermark_text_label.place(x=730, y=120)
watermark_text_entry = Entry(bg="#393E46", width=26, fg="#EEEEEE")
watermark_text_entry.place(x=878, y=121)

# Font
font_label = Label(text="Font:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
font_label.place(x=730, y=170)
font_options = [
    "Helvetica",
    "Times New Roman",
    "Verdana",
    "Georgia",
    "Monaco",
    "Palatino",
    "Futura"
]
font_var = StringVar()
font_var.set("Helvetica")
font_drop = OptionMenu(window, font_var, *font_options)
font_drop.config(width=12, background=BACKGROUND_COLOR, borderwidth=1)
font_drop.place(x=785, y=174)

# Color
color_label = Label(text="Color:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
color_label.place(x=730, y=220)
color_options = [
    "white",
    "black",
    "red",
    "green",
    "blue",
    "cyan",
    "yellow",
    "magenta",
    "orange"
]
color_var = StringVar()
color_var.set("white")
color_drop = OptionMenu(window, color_var, *color_options)
color_drop.config(width=10, background=BACKGROUND_COLOR, borderwidth=1)
color_drop.place(x=793, y=224)

# Font Size
font_size_label = Label(text="Font Size:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
font_size_label.place(x=730, y=270)
font_size_entry = Entry(bg="#393E46", width=8, fg="#EEEEEE", borderwidth=2)
font_size_entry.place(x=825, y=270)

# Opacity
opacity_label = Label(text="Opacity:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
opacity_label.place(x=730, y=320)
opacity_options = [
    "100%",
    "75%",
    "50%",
    "25%"
]
opacity_var = StringVar()
opacity_var.set("100%")
opacity_drop = OptionMenu(window, opacity_var, *opacity_options)
opacity_drop.config(width=10, background=BACKGROUND_COLOR, borderwidth=1)
opacity_drop.place(x=809, y=324)

# Position
x_pos_label = Label(text="Position X:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
x_pos_label.place(x=730, y=370)
x_pos_entry = Entry(bg="#393E46", width=8, fg="#EEEEEE", borderwidth=2)
x_pos_entry.place(x=830, y=370)
y_pos_label = Label(text="Position Y:", bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "bold"))
y_pos_label.place(x=730, y=420)
y_pos_entry = Entry(bg="#393E46", width=8, fg="#EEEEEE", borderwidth=2)
y_pos_entry.place(x=830, y=420)

# Buttons
upload_button = Button(window, text="Upload Image", bg="#EEEEEE", fg="#222831", borderless=1,
                       command=upload_image)
upload_button.place(x=290, y=660)
apply_button = Button(window, text='Apply', bg="#EEEEEE", fg="#393E46", borderless=1, width=100, height=35,
                      font=("Helvetica", 17, "bold"),
                      command=apply_text)
apply_button.place(x=860, y=490)
save_button = Button(window, text='Save', bg="#EEEEEE", fg="#393E46", borderless=1, width=100, height=35,
                     font=("Helvetica", 18, "bold"), command=save_image)
save_button.place(x=970, y=490)

# Image Dimensions Label
img_dimensions_label = Label(text=f"The image is {img_width} x {img_height} pixels.\nCoordinates (0, 0) will "
                                  f"place the text in the top left corner.",
                             bg=BACKGROUND_COLOR, fg="#EEEEEE", font=("Helvetica", 17, "normal"))
img_dimensions_label.place(x=745, y=560)

window.mainloop()
