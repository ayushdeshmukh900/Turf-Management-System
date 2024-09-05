
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

time1=Tk()
time1.geometry('1408x792+50+0')
time1.resizable(0,0)
header_frame = Frame(time1, bg="white", height=80,bd=2)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


# Create buttons in header frame
book_btn = Button(header_frame, text="HOME",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white")
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white")
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)

time1.title("time1 Slots")
a7_0 = Label(time1, text="Confirm booking",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=30)
a7_0.place(x=550, y=150)

h3=PhotoImage(file='qrcodee.png')
home = Label(time1,image=h3, relief="flat", bg="white")
home.place(x='565', y='200')


time1.mainloop()