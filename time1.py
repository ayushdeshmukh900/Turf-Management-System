import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def red():
    messagebox.showerror('Bookes','This slot is not Avaliable')

def green():
    time1.destroy()
    import afterbooking


time1=Tk()
time1.geometry('1408x792+50+0')
time1.resizable(0,0)
time1.title("time1 Slots")


header_frame = Frame(time1, bg="white", height=80)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


# Create buttons in header frame
book_btn = Button(header_frame, text="Go To Home Page",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white")
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white")
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)

step3 = Label(time1, text="Select Time Slot",bg='#19423c',fg='white',
              font=('Microsoft Yahei UI Light',15,'bold'))
step3.place(x=600,y=700)


a0_1 = Label(time1, text="7am",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7,height=1)
a0_1.place(x=215, y=145)

a0_2 = Label(time1, text="8am",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_2.place(x=215, y=177)

a0_3 = Label(time1, text="9am",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_3.place(x=215, y=209)

a0_4 = Label(time1, text="10am",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_4.place(x=215, y=241)

a0_5 = Label(time1, text="11am",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_5.place(x=215, y=273)

a0_6 = Label(time1, text="12pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_6.place(x=215, y=305)

a0_7 = Label(time1, text="1pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_7.place(x=215, y=337)

a0_8 = Label(time1, text="2pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_8.place(x=215, y=369)

a0_9 = Label(time1, text="3pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_9.place(x=215, y=401)

a0_10 = Label(time1, text="4pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_10.place(x=215, y=433)

a0_11 = Label(time1, text="5pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_11.place(x=215, y=465)

a0_12 = Label(time1, text="6pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_12.place(x=215, y=497)

a0_13 = Label(time1, text="7pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_13.place(x=215, y=529)

a0_14 = Label(time1, text="8pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_14.place(x=215, y=561)

a0_15 = Label(time1, text="9pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_15.place(x=215, y=593)

a0_16 = Label(time1, text="10pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_16.place(x=215, y=625)

a0_17 = Label(time1, text="11pm",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=7)
a0_17.place(x=215, y=657)

a1_0 = Label(time1, text="Sun",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a1_0.place(x=300, y=113)

a2_0 = Label(time1, text="Mon",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a2_0.place(x=420, y=113)

a3_0 = Label(time1, text="Tue",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a3_0.place(x=540, y=113)

a4_0 = Label(time1, text="Wed",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a4_0.place(x=660, y=113)

a5_0 = Label(time1, text="Thu",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a5_0.place(x=780, y=113)

a6_0 = Label(time1, text="Fri",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a6_0.place(x=900, y=113)

a7_0 = Label(time1, text="Sat",font=('Microsoft Yahei UI Light',13,'bold'),fg='#19423c', bg="white",width=10)
a7_0.place(x=1020, y=113)

#Sunday
a1_1 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_1.place(x=302, y=145)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=145)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=145)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=145)

a1_5 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_5.place(x=782, y=145)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=145)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=145)

#monday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=177)

a1_2 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_2.place(x=422, y=177)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=177)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=177)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=177)

a1_6 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_6.place(x=902, y=177)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=177)

#tuesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=209)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=209)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=209)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=209)

a1_5 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_5.place(x=782, y=209)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=209)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=209)

#wednesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=241)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=241)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=241)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=241)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=241)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=241)

a1_7 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=241)

#thursday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=273)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=273)

a1_3 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_3.place(x=542, y=273)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=273)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=273)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=273)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=273)

#friday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=305)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=305)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=305)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=305)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=305)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=305)

a1_7 = Button(time1,text="1500",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=305)

#saturday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=337)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=337)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=337)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=337)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=337)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=337)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=337)

#Sunday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=369)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=369)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=369)

a1_4 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_4.place(x=662, y=369)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=369)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=369)

a1_7 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=369)

#monday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=401)

a1_2 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_2.place(x=422, y=401)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=401)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=401)

a1_5 = Button(time1,text="1500",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_5.place(x=782, y=401)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=401)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=401)

#tuesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=433)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=433)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=433)

a1_4 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_4.place(x=662, y=433)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=433)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=433)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=433)

#wednesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=465)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=465)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=465)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=465)

a1_5 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_5.place(x=782, y=465)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=465)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=465)

#thursday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=273)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=273)

a1_3 = Button(time1,text="1500",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_3.place(x=542, y=273)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=273)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=273)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=273)

a1_7 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=273)

#friday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=305)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=305)

a1_3 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_3.place(x=542, y=305)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=305)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=305)

a1_6 = Button(time1,text="1500",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_6.place(x=902, y=305)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=305)

#saturday
a1_1 = Button(time1,text="1500",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_1.place(x=302, y=337)

a1_2 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_2.place(x=422, y=337)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=337)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=337)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=337)

a1_6 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_6.place(x=902, y=337)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=337)

#Sunday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=369)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=369)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=369)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=369)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=369)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=369)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=369)

#monday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=433)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=433)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=433)

a1_4 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_4.place(x=662, y=433)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=433)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=433)

a1_7 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=433)

#tuesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=465)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=465)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=465)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=465)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=465)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=465)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=465)

#wednesday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=497)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=497)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=497)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=497)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=497)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=497)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=497)

#thursday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=529)

a1_2 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_2.place(x=422, y=529)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=529)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=529)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=529)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=529)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=529)

#friday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=561)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=561)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=561)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=561)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=561)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=561)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=561)

#saturday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=593)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=593)

a1_3 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_3.place(x=542, y=593)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=593)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=593)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=593)

a1_7 = Button(time1,text="1000",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="lightgreen",width=12,bd=0,command=green)
a1_7.place(x=1022, y=593)

#friday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=625)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=625)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=625)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=625)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=625)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=625)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=625)

#saturday
a1_1 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_1.place(x=302, y=657)

a1_2 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_2.place(x=422, y=657)

a1_3 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_3.place(x=542, y=657)

a1_4 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_4.place(x=662, y=657)

a1_5 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_5.place(x=782, y=657)

a1_6 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_6.place(x=902, y=657)

a1_7 = Button(time1,text="-",font=('Microsoft Yahei UI Light',10,'bold'),fg='#19423c', bg="firebrick1",width=12,bd=0,command=red)
a1_7.place(x=1022, y=657)


time1.mainloop()