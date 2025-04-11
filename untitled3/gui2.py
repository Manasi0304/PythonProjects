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
from tkinter import*
base = Tk()
base.geometry("400x250")
base.title("create new account")
f = ("bold",15)
lb1 = Label(base,text="enter user id",font=f,bg="red")
txt1 = Entry(base,Font=f)
txt1.place (x=230 , y=180)
base.mainloop()