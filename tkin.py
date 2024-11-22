import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import ttk
win=tkinter.Tk()
win.title('workin?')
win.geometry('900x500+10+20')
say=ttk.Frame(win,padding=10)
say.grid()
ttk.Label(say,text="store.txt").grid(column=0,row=0)
intake="intake"
ttk.Label(say,text=(open('store.txt').read)).grid(column=3,row=0)
ttk.Button(say, text="self destruct", command=win.destroy).grid(column=1,row=2)
win.mainloop()
print("BOOOOOOOOM \n pow")
