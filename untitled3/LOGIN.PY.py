from tkinter import*
base=Tk()
f = ("Franklin Gothic",13)
h=15
base.title("New User Registration")
base.geometry("400x400")
lb1 = Label(base, text="Enter User ID:",font=f)
lb1.place(x=20,y=20)
txt1 = Entry(base)
txt1.place(x=20,y=55,width=300)

lb1 = Label(base, text="Enter Password:",font=f)
lb1.place(x=20,y=80)
txt2 = Entry(base)
txt2 = Entry(base,show="*")
txt2.place(x=20,y=120,width=300)

lb2 = Label(base, text="Confirm Password:",font=f)
lb2.place(x=20,y=150)
txt3 = Entry(base)
txt3 = Entry(base,show="*")
txt3.place(x=20,y=190,width=300)


btn1 = Button(base,text="Submit",background="Yellow",font=f)
btn1.place(x=90,y=250)

btn2 = Button(base,text="Reset",background="Sky blue",font=f)
btn2.place(x=180,y=250)

base.mainloop()