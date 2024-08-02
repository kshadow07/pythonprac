
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep =0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    tick_button.config(text="")
    timer_label.config(text="Timer",fg=GREEN)
    global rep
    rep=0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_min_sec= WORK_MIN*60
    short_break_min_sec=SHORT_BREAK_MIN*60
    long_break_min_sec=LONG_BREAK_MIN*60
    global rep
    if rep<8:
        rep+=1
        if rep%8==0:
         count_down(long_break_min_sec)
         timer_label.config(text="LONG-Break",fg=RED)
        elif rep%2==0:
            count_down(short_break_min_sec)
            timer_label.config(text="Break",fg=PINK)
        else:
            count_down(work_min_sec)
            timer_label.config(text="Work",fg=GREEN)
        
    else:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text,text='00:00')
        tick_button.config(text="")
        timer_label.config(text="COMPLETED") 
        
        
   
           
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec= count%60
    
    if count_sec <10:
        count_sec=f"0{count_sec}"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
        
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(rep/2)
        for _ in range(work_sessions):
            marks+="✔"
        tick_button.config(text=marks)    
        
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=150,pady=75,bg=YELLOW)

#CANVAs
canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="C:/Python/tkinter/pomodora/tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#label 
timer_label= Label(window,text="Timer",fg=GREEN,font=(FONT_NAME,36,"bold"),bg=YELLOW,)
timer_label.grid(column=1,row=0)

#buttons

#start 
start_button= Button(text="Start",font=(FONT_NAME,15,"bold"),command=start_timer)
start_button.grid(row=2,column=0)

#stop
stop_button= Button(text="Reset",font=(FONT_NAME,15,"bold"),command=reset)
stop_button.grid(row=2,column=2)


#tick label
tick_button= Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,23,"bold"))
tick_button.grid(row=2,column=1)
tick_button.config(padx=10,pady=10)


window.mainloop()