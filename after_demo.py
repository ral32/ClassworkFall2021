import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("after demo")

my_label = tk.Label(root, text="this is a placeholder label")
my_label.grid(column=0, row=3)

def show_time():
    curative = datetime.now().time()
    msg = "The current time is {}".format(curative)
    my_label.configure(text=msg)


root.after(2000, show_time) #after certain amount of time has passed run the code, after 2000 ms, run the show_time function

root.mainloop()
