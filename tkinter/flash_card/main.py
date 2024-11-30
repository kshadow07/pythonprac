# Importing necessary modules

from email.mime import image
import random
from tkinter import *
import pandas
import json

# Setting background color
BACKGROUND_COLOR = "#B1DDC6"
data=pandas.read_csv("tkinter/flash_card/data/french_words.csv")
data_dic=data.to_dict(orient="records")
currnt_card={}
learned_words=[]


def next_data_correct():
    global current_card
    is_know()
    window.after_cancel(count_down)
    current_card=random.choice(data_dic)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(title_word,text=current_card["French"],fill="black")
    canvas.itemconfigure(canvas_image,image=old_img)
    

def next_data_incorrect():
    global current_card
    window.after_cancel(count_down)
    current_card=random.choice(data_dic)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(title_word,text=current_card["French"],fill="black")
    canvas.itemconfigure(canvas_image,image=old_img)
    count_down()
    
def is_know():
    global learned_words
    learned_words.append(current_card)
    data_dic.remove(current_card)
    data=pandas.DataFrame(learned_words)
    data.to_csv("tkinter/flash_card/data/learned_french_words.csv")
    count_down()

# Creating the main window
window =Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvas and images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
old_img = PhotoImage(file="tkinter/flash_card/images/card_front.png")
new_img = PhotoImage(file="tkinter/flash_card/images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=old_img)
title=canvas.create_text(400, 150, text="FRENCH", font=("Ariel", 40, "italic"))
title_word=converted_language=canvas.create_text(400, 263, text="FRENCH", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Creating buttons
cross_image = PhotoImage(file="tkinter/flash_card/images/wrong.png")
button_x =Button(image=cross_image, highlightthickness=0, borderwidth=0,command=next_data_incorrect)
button_x.grid(column=0, row=1)

right_image = PhotoImage(file="tkinter/flash_card/images/right.png")
button_right = Button(image=right_image, highlightthickness=0, borderwidth=0,command=next_data_correct)
button_right.grid(column=1, row=1)

#countdown update
def update_image():
    canvas.itemconfig(canvas_image, image=new_img)

def update_text():
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    canvas.itemconfig(title_word, text=current_card["English"], fill="white")

def count_down():
    window.after(3000, lambda: [update_image(), update_text()])
    
    
# Starting the countdown
next_data_incorrect()
count_down()

# Running the main loop
window.mainloop()