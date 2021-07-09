import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root = Tk()



textv=StringVar()


root.title("Speech To Text")
root.geometry("500x200")
root.resizable(False, False)
obj = LabelFrame(root, text="Text To Speech", font=30, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)


lbl= Label(obj,text="Insert Text Here -", font="30")
lbl.pack(side=tk.LEFT,padx=5)


text_insert_box=Entry(obj, textvariable=textv, font=30, width=25,bd=5)
text_insert_box.pack(side=tk.LEFT, padx=10)


btn1=Button(obj,text="speak", font=20, bg="grey", fg="black", command=speaknow)
btn1.pack(side=tk.LEFT, padx=10)



root.mainloop()
