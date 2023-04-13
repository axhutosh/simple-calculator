from tkinter import*

window= Tk()
window.geometry("500x500")
window.title("simple calculator")

lbl1 = Label(window,text="enter 1st number:")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="enter 2nd number:")
lbl2.place(x=50,y=100)