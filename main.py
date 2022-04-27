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
reps=0
checkboxes=""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  global checkboxes, reps
  reps = 0
  checkboxes = ""
  title_txt.config(text="Timer",fg=GREEN)
  canvas.itemconfig(timer_txt,text="00:00")
  reset_checksign()
  
  window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  work_sec = WORK_MIN*60
  short_break_sec = SHORT_BREAK_MIN*60
  long_break_sec = LONG_BREAK_MIN*60
  
  if reps==1 or reps==3 or reps==5 or reps==7:
    title_txt.config(text="WORK",fg= GREEN)
    arg = work_sec
    
  elif reps==8:
    make_checksign()
    title_txt.config(text="BREAK",fg=RED)
    reps = 0
    arg = long_break_sec
    
  else:
    make_checksign()
    title_txt.config(text="BREAK",fg=PINK)
    arg = short_break_sec

  
  count_down(arg)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
  
def count_down(count):
  global timer
  count_min = math.floor(count/60)
  count_sec = count%60
  if count_sec <10:
    count_sec = f"0{count_sec}"
  
  
  canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}" )
  
  timer = window.after(1000, count_down, count-1)
  if count_min==0 and count_sec=="00":
    start_timer()
  
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100,pady=50,bg=YELLOW)

title_txt = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
title_txt.grid(column=2,row=1)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_txt = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=1,row=3)

restart_button = Button(text="Restart",command=reset)
restart_button.grid(column=3,row=3)

def make_checksign():
  global checkboxes
  checkboxes += "✔"
  check_label = Label(text=checkboxes,bg=YELLOW,fg=GREEN, font=(FONT_NAME,30,"bold"))
  check_label.grid(column=2,row=3)

def reset_checksign():
  global checkboxes
  check_label = Label(text=checkboxes,bg=YELLOW,fg=GREEN, font=(FONT_NAME,30,"bold"))
  check_label.grid(column=2,row=3)



window.mainloop()