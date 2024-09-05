import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def data():
    root.destroy()
    import home
def mahim():
    root.destroy()
    import xavier

def malad():
    root.destroy()
    import Malad

def miraroad():
    root.destroy()
    import Mira_road

def dadar():
    root.destroy()
    import dadar

def borivali():
    root.destroy()
    import borivali

def palghar():
    root.destroy()
    import Palghar

def on_enter():
    root.destroy()
    import sixturf


def mumbai():
    mum=Button(root,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(root, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(root, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    root.destroy()
    import forpass

def mk():
    root.destroy()
    import login























root=Tk()
root.geometry('1408x792+50+0')
root.resizable(0,0)

header_frame = Frame(root, bg="white", height=80)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = Button(header_frame, text="HOME",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18,command=data)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white",command=om)
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white",command=mumbai)
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)



fea=Label(root,text="Feature Listing",font=('Open sans',20,'bold'),fg='green')
fea.place(x=200,y=140)

des=Label(root,text="See & book your ground from the list of most popular grounds in your city",font=('Open sans',12,'bold'),fg='green')
des.place(x=200,y=175)


t1=Frame(root,bg='white',height=250,width=300)
t1.place(x=200,y=200)

t12=PhotoImage(file='My project.png')
t121=Button(t1,image=t12,cursor='hand2',bd=0,bg='white',command=mahim)
t121.place(x=60,y=0)

t123=Button(t1,text='Xavier,Mahim',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=mahim)
t123.place(x=10,y=140)

t124=Button(t1,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t124.place(x=14,y=174)

t125=Button(t1,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=mahim)
t125.place(x=10,y=195)




t2=Frame(root,bg='white',height=250,width=300)
t2.place(x=550,y=200)


t21=PhotoImage(file='malad_logo1.png')
t211=Button(t2,image=t21,cursor='hand2',bd=0,bg='white',command=malad)
t211.place(x=80,y=10)

t223=Button(t2,text='Inorbit,Malad',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=malad)
t223.place(x=10,y=140)

t224=Button(t2,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t224.place(x=14,y=174)

t225=Button(t2,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=malad)
t225.place(x=10,y=195)




t3=Frame(root,bg='white',height=250,width=300)
t3.place(x=900,y=200)


t31=PhotoImage(file='mira_logo1.png')
t311=Button(t3,image=t31,cursor='hand2',bd=0,bg='white',command=miraroad)
t311.place(x=80,y=10)

t323=Button(t3,text='Sector1,MiraRoad',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=miraroad)
t323.place(x=10,y=140)

t324=Button(t3,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t324.place(x=14,y=174)

t325=Button(t3,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=miraroad)
t325.place(x=10,y=195)


t4=Frame(root,bg='white',height=250,width=300)
t4.place(x=200,y=500)

t41=PhotoImage(file='dadar_logo1.png')
t411=Button(t4,image=t41,cursor='hand2',bd=0,bg='white',command=dadar)
t411.place(x=80,y=10)

t423=Button(t4,text='Astro Park,Dadar',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=dadar)
t423.place(x=10,y=141)

t424=Button(t4,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t424.place(x=14,y=174)

t425=Button(t4,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=dadar)
t425.place(x=10,y=195)


t5=Frame(root,bg='white',height=250,width=300)
t5.place(x=550,y=500)

t51=PhotoImage(file='borivali_logo1.png')
t511=Button(t5,image=t51,cursor='hand2',bd=0,bg='white',command=borivali)
t511.place(x=80,y=10)

t523=Button(t5,text='Footcric,Borivali',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=borivali)
t523.place(x=10,y=140)

t524=Button(t5,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t524.place(x=14,y=174)

t525=Button(t5,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=borivali)
t525.place(x=10,y=195)




t6=Frame(root,bg='white',height=250,width=300)
t6.place(x=900,y=500)

t61=PhotoImage(file='palghar_logo1.png')
t611=Button(t6,image=t61,cursor='hand2',bd=0,bg='white',command=palghar)
t611.place(x=80,y=10)

t623=Button(t6,text='Spartan,Palghar',font=('Open sans',15,'bold'),fg='green',bg="white",bd=0,command=palghar)
t623.place(x=10,y=140)

t624=Button(t6,text='Mumbai',font=('Open sans',8),bg="white",bd=0)
t624.place(x=14,y=174)

t625=Button(t6,text='Book Now',font=('Open sans',15,'bold'),fg='orange',bg="white",bd=0,command=palghar)
t625.place(x=10,y=195)


root.mainloop()
