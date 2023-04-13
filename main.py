from tkinter import*

window= Tk()
window.geometry("500x500")
window.title("simple calculator")

lbl1 = Label(window,text="enter 1st number:")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="enter 2nd number:")
lbl2.place(x=50,y=100)

t1 = Entry()
t1.place(x=200,y=50)

t2 = Entry()
t2.place(x=200,y=100)

lbl3 = Label(window,text="Result:")
lbl3.place(x=70,y=150)

t3 = Entry()
t3.place(x=200,y=150)

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1+num2
  t3.insert(END,str(sum))

def sub():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1-num2
  t3.insert(END,str(sum))

def mul():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1*num2
  t3.insert(END,str(sum))

def div():
  num1=int(t1.get())
  num2=int(t2.get())
  sum=num1/num2
  t3.insert(END,str(sum))

def clear():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,END)


b1=Button(window, text="Add",command=add)
b1.place(x=50,y=200)

b2=Button(window, text="Sub",command=sub)
b2.place(x=110,y=200)

b3=Button(window, text="mul",command=mul)
b3.place(x=170,y=200)

b4=Button(window, text="div",command=div)
b4.place(x=230,y=200)

b5=Button(window, text="clear",command=clear)
b5.place(x=140,y=250)

