"""
from tkinter import *

base = Tk()
base.title("My First Frame")
base.geometry("400x250")

btn1 = Button(base, text="Submit", width=10, font=("Arial Black", 15))
btn1.pack()  # is to add/appear/place 'btn' into 'base'

btn2 = Button(base, text="Copy", width=15)
btn2.pack()

txt1 = Entry(base,  font=("Arial Black", 15), show="#")
txt1.pack()

base.mainloop()
"""
""" 
from tkinter import *

base = Tk()
base.geometry("400x250")
base.title("Demonstrating First GUI")
f = ("Arial Black", 15)

btn1 = Button(base, text="Submit", bg="red", font=f)
btn1.pack()

btn2 = Button(base, text="Copy", bg="green", fg="white")
btn2.pack()

txt1 = Entry(base)
txt1.pack()

txt2 = Text(base)
txt2.pack()

base.mainloop()

"""
from tkinter import *

base = Tk()
base.geometry("400x250")
base.title("Demonstrating First GUI")
f = ("Arial Black", 15)

btn1 = Button(base, text="Submit", bg="red", font=f)
btn1.place(x=50, y=100)

btn2 = Button(base, text="Copy", bg="green", fg="white")
btn2.place(x=50, y=200)

lb1 = Label(base, text="Enter Use ID here", font=f)
lb1.place(x=100,y=180)

txt1 = Entry(base, font=f)
txt1.place(x=230,y=180)

base.mainloop()

=======================
=======================

* If we use grid() method, then we can arrange 
component/widget objects in grid (rows x columns)
To use grid(), we have to specify row-index and 
column-index.
* We have to use attributes "row=" and "column="
"""

from tkinter import *

base = Tk()
base.geometry("400x250")
base.title("Demonstrating First GUI")
f = ("Arial Black", 15)

btn1 = Button(base, text="Submit", bg="red", font=f)
btn1.grid(row=0, column=0)

btn2 = Button(base, text="Copy", bg="green", fg="white")
btn2.grid(row=0, column=1)

lb1 = Label(base, text="Enter Use ID here", font=f)
lb1.grid(row=1, column=0)

txt1 = Entry(base, font=f)
txt1.grid(row=1, column=1)


base.mainloop()

"""
from tkinter import*
base = Tk()
base.geometry("400x250")
base.title("create new account")
f = ("bold",15)
lb1 = Label(base,text="enter user id",font=f,bg="red")
txt1 = Entry(base,Font=f)
txt1.place (x=230 , y=180)
base.mainloop()