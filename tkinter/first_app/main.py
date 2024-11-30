import tkinter as tk

# Window
window = tk.Tk()
window.title("GAME ON")
window.minsize(height=100, width=200)
window.config(padx=50,pady=50)



# function to convert km into miles
def miles_to_km(miles):
    km = round(miles /  0.621371,2)
    return str(km)

# function to handle button click
def convert_miles_to_km():
    try:
        miles = float(entry.get())
        km = miles_to_km(miles)
        label2.config(text=km)
        entry.delete(0, tk.END)
    except ValueError:
        label2.config(text="Invalid input")



# entry
entry = tk.Entry(width=10)
entry.grid(column=1,row=0)

#miles label
label= tk.Label(window,text="Convert")
label.grid(column=0,row=0)



#miles label
miles_label= tk.Label(window,text="miles")
miles_label.grid(column=2,row=0)

#km label
km_label= tk.Label(window,text="km")
km_label.grid(column=2,row=1)

# button
button = tk.Button(text="Convert", command=convert_miles_to_km)
button.grid(column=1,row=2)

# label to display result
label2 = tk.Label(window, text="0",)
label2.grid(column=1,row=1)

window.mainloop()