
from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
 website= website_entry.get()
 email=email_entry.get()
 password=password_entry.get()
 
 new_data={
        website:{
                "email": email,
                "password":password
            }
        }
 
 if website=="" or email=="" or password=="":
     messagebox.showerror("Error", "Please fill out all fields")
 else:
    is_ok= messagebox.askokcancel(title=website,message=" Is it ok to save?")
    if is_ok:
     
        try:
            with open("data.json", "r") as data:
                load_data=json.load(data)
                
        except json.JSONDecodeError:
            with open("data.json","w") as data:
                json.dump(new_data, data,indent=4)
                
        except FileNotFoundError:
            with open("data.json","w") as data:
                json.dump(new_data, data,indent=4)
        else:
            load_data.update(new_data)
            with open("data.json","w") as data:
                json.dump(load_data,data,indent=4)     
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        
     
 

 #----------------------------USER FINDER-----------------------------#

def search():
    website=website_entry.get()
    try:
        with open("data.json","r") as data:
            data=json.load(data)
            try:
                messagebox.showinfo(title="User info",message=f"email:{data[website]['email']}\n password:{data[website]['password']}")
            except KeyError:
                messagebox.showerror("Error","No Data Avaialable")    
    except json.JSONDecodeError:
        messagebox.showerror("Error", "No data available")
    
    except FileNotFoundError:
        messagebox.showerror("Error", "No data available")
            

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)

canvas= Canvas(height=180,width=180)
img= PhotoImage(file="tkinter/password_manager/logo.png")
canvas.create_image(90,90,image=img)
canvas.grid(column=1,row=0)

#labels

website_label=Label(window,text="Website:",font=(28))
website_label.grid(column=0,row=1)
website_label.config(padx=3,pady=5)

email_label=Label(window,text="Email/Username",font=(28))
email_label.grid(column=0,row=2)
email_label.config(padx=3,pady=5)

password_label=Label(window,text="Password",font=(28))
password_label.grid(column=0,row=3)
password_label.config(padx=3,pady=5)

#Entrys
website_entry=Entry(width=25,font=(28))
website_entry.grid(column=1,row=1,columnspan=1)
website_entry.focus()

email_entry=Entry(width=45,font=(28))
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"example@gmail.com")

password_entry=Entry(width=26,font=(28))
password_entry.grid(column=1,row=3)

#buttons
generate_password_button=Button(text="Generate Password" ,font=(28),command=generate_password)
generate_password_button.grid(column=2,row=3)

add_password_button=Button(text="Add",width=42,command=save,font=(21))
add_password_button.grid(column=1,row=4,columnspan=2)

search_button= Button(text="Search",width=12,font=(12),command=search)
search_button.grid(column=2,row=1,columnspan=1)








window.mainloop()
