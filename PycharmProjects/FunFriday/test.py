# importing everything from tkinter
from tkinter import *
import tkinter as tk
from Name_Picker import display_name, display_task
from tkinter.ttk import Frame, Label, Style

# creating the tkinter window
Main_window = tk.Tk()
Main_window.title("Fun Friday!!")
#Main_window.attributes('-fullscreen',True)

bg = PhotoImage(file="back.png")
label1 = Label(Main_window, image=bg)
label1.place(x=0, y=0)

label = tk.Label(Main_window, text="Yeah!! Today is Fun Friday!!", fg="black",
                 font=("Showcard Gothic", 30))
label.pack(pady=25)


def pick_name():
    name_label.config(text=display_name())


frame1 = tk.Frame(master=Main_window, width = 1500 ,height=100)
name_label = Label(master=frame1, text="", font=("Snap ITC", 30))
name_label.place(x=0.5, y=0.5)
name_label.pack(pady=20)
pickup_name = Button(master=frame1, text="Search Name", command=pick_name, width=25, font=("Snap ITC", 15))
pickup_name.pack(pady=20)
frame1.pack(pady=20, fill=X)


def pick_task():
    task_label.config(text=display_task())


frame2 = tk.Frame(master=Main_window, width = 1500, height=500)
task_label = Label(master=frame2, text="", font=("Snap ITC", 15))
task_label.place(x=0.5, y=0.5)
task_label.pack(pady=20)
pickup_task = Button(master=frame2, text="Search Task", command=pick_task, width=25, font=("Snap ITC", 15))
pickup_task.pack(pady=20)
frame2.pack(pady=20, fill=X)

# Start the GUI
Main_window.mainloop()
