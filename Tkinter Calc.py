from tkinter import *
x=0
check=0
def add():
    f_num=e.get()
    global x
    global check
    check=0
    x=int(f_num)
    e.delete(0,END)
def sub():
    f_num=e.get()
    global x
    global check
    check=1
    x=int(f_num)
    e.delete(0,END)
def mul():
    f_num=e.get()
    global x
    global check
    check=2
    x=int(f_num)
    e.delete(0,END)
def div():
    f_num=e.get()
    global x
    global check
    check=3
    x=int(f_num)
    e.delete(0,END)   
def clear():
    e.delete(0,END)
        
def equal():
    s_num=int(e.get())
    e.delete(0,END)
    if check==0:
       e.insert(0,x+s_num)
    elif check==1:
        e.insert(0,x-s_num)
    elif check==2:
        e.insert(0,x*s_num)
    else:
        e.insert(0,x/s_num)
def buttonclick(n):
    current =e.get()
    e.insert(0,str(current)+str(n))
def backspace():
    cur=int(e.get())
    cur=cur//10
    e.delete(0,END)
    e.insert(0,cur)    
root=Tk()
root.title("Calculator")
root.iconbitmap('E:\download.ico')
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)
button_9=Button(root,text="9",command=lambda: buttonclick(9),padx=50,pady=20).grid(row=1,column=0)
button_8=Button(root,text="8",command=lambda: buttonclick(8),padx=50,pady=20).grid(row=1,column=1)
button_7=Button(root,text="7",command=lambda: buttonclick(7),padx=50,pady=20).grid(row=1,column=2)
button_6=Button(root,text="6",command=lambda: buttonclick(6),padx=50,pady=20).grid(row=2,column=0)
button_5=Button(root,text="5",command=lambda: buttonclick(5),padx=50,pady=20).grid(row=2,column=1)
button_4=Button(root,text="4",command=lambda: buttonclick(4),padx=50,pady=20).grid(row=2,column=2)
button_3=Button(root,text="3",command=lambda: buttonclick(3),padx=50,pady=20).grid(row=3,column=0)
button_2=Button(root,text="2",command=lambda: buttonclick(2),padx=50,pady=20).grid(row=3,column=1)
button_1=Button(root,text="1",command=lambda: buttonclick(1),padx=50,pady=20).grid(row=3,column=2)
button_0=Button(root,text="0",command=lambda: buttonclick(0),padx=50,pady=20).grid(row=4,column=0)
button_add = Button(root, text="+", command=add, padx=49,pady=20).grid(row=4, column=1)
button_equal = Button(root, text="=", command=equal, padx=49,pady=20).grid(row=6, column=0)
button_clear = Button(root, text="Clear", command=clear, padx=95,pady=20).grid(row=6, column=1,columnspan=2)
button_mul = Button(root, text="*", command=mul, padx=49,pady=20).grid(row=5, column=1)
button_sub = Button(root, text="-", command=sub, padx=50,pady=20).grid(row=5, column=2)
button_div = Button(root, text="/", command=div, padx=49,pady=20).grid(row=4, column=2)
button_backspace = Button(root, text="Back",command=backspace, padx=45,pady=20).grid(row=5, column=0)
root.mainloop()
