from tkinter import *
root=Tk()
root.geometry("500x800")
root.resizable(False,False)
root.title("Calculator")
c0="black"
c="#0A0B0B"
c2="#211E1E"
c3="#524dd6"
c4="#3a35db"
c5="white"
#functions for interaction with the gui.
def insertb(a):
    current=e2.get()
    e2.delete(0,END)
    e2.insert(0,str(current)+str(a))
def inserta(o):
    s=e2.get()
    e1.insert(0,s)
    e2.delete(0,END)    
    e3.delete(0,END)
    e3.insert(0,o)
def oper():
    o=str(e3.get())
    x=e1.get()
    y=e2.get()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e3.insert(0," =")
    if(o==" +"):
        e2.insert(0,float(x)+float(y))
    if(o==" -"):
        e2.insert(0,float(x)-float(y))
    if(o==" x"):
        e2.insert(0,float(x)*float(y))
    if(o==" /"):
          e2.insert(0,float(x)/float(y))
def clr():
    e1.delete(0,END)            
    e2.delete(0,END)    
    e3.delete(0,END)    

        
#a section
e1=Entry(root,bg=c,fg="white",font=("Ariel",30),justify=RIGHT,border=0)
e1.place(x=100,y=0,width=400,height=124)
#b section
e2=Entry(root ,bg=c,fg="white",font=("Ariel",30),justify=RIGHT,border=0)
e2.place(x=100,y=120,width=400,height=124)
# operator section
e3=Entry(root,bg=c,fg=c4,border=0,font=("Ariel",40))
e3.place(x=0,y=0,width=100,height=244)
root.configure(bg=c0)
#  number buttons 
b1=Button(root,text="1",font=("Ariel",20,"bold"),bg=c2,fg=c5,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(1))
b1.place(x=0,y=245)
b2=Button(root,text="2",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(2))
b2.place(x=126,y=245)

b3=Button(root,text="3",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(3))
b3.place(x=252,y=245)
b4=Button(root,text="4",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(4))
b4.place(x=0,y=390)
b5=Button(root,text="5",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(5))
b5.place(x=126,y=390)
b6=Button(root,text="6",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(6))
b6.place(x=252,y=390)

b7=Button(root,text="7",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(7))
b7.place(x=0,y=535)
b8=Button(root,text="8",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(8))
b8.place(x=126,y=535)
b9=Button(root,text="9",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(9))
b9.place(x=252,y=535)
b0=Button(root,text="0",font=("Ariel",20,"bold"),fg=c5,bg=c2,padx=44,pady=45,border=0,activebackground=c4,command=lambda:insertb(0))
b0.place(x=0,y=680)
#equals button.
be=Button(root,text="=",font=("Ariel",20,"bold"),fg=c5,bg=c4,padx=107,pady=43,border=0,activebackground="black",activeforeground="white",command=oper)
be.place(x=126,y=680)
#operation buttons
ba=Button(root,text="+",font=("Ariel",20,"bold"),fg="black",bg=c3,padx=45,pady=45,border=0,activebackground=c4,command=lambda:inserta(" +"))
ba.place(x=252+126,y=245)
bs=Button(root,text="_",font=("Ariel",20,"bold"),fg="black",bg=c3,padx=48,pady=45,border=0,activebackground=c4,command=lambda:inserta(" -"))
bs.place(x=252+126,y=390)
bm=Button(root,text="x",font=("Ariel",20,"bold"),fg="black",bg=c3,padx=48,pady=45,border=0,activebackground=c4,command=lambda:inserta(" x"))
bm.place(x=252+126,y=535)
bd=Button(root,text="/",font=("Ariel",20,"bold"),fg="black",bg=c3,padx=48,pady=45,border=0,activebackground=c4,command=lambda:inserta(" /"))
bd.place(x=252+126,y=680)
#clear button
bc=Button(e3,text="X",font=("Ariel",15,"bold"),fg=c5,bg=c4,padx=5,pady=5,border=0,activebackground="red",command=clr)
bc.place(x=2,y=2)
root.mainloop()


