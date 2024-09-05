import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image



def drop():
    step2 = Label(steps, text="Step 2: Select Ground", bg='white', fg='#19423c',
                  font=('Microsoft Yahei UI Light', 13, 'bold'))
    step2.place(x=150, y=240)

    ground1 = Button(steps, text="Ground 1\n\n-Outdoor\n-Turf\n-6*6 per side",
                     font=('Microsoft Yahei UI Light', 13, 'bold'), fg='white',
                     bg="grey", relief="flat", activeforeground='white', activebackground='orange',command=store)
    ground1.place(x=150, y=270)

    ground2 = Button(steps, text="Ground 2\n\n-Outdoor\n-Turf\n-6*6 per side",
                     font=('Microsoft Yahei UI Light', 13, 'bold'), fg='white',
                     bg="grey", relief="flat", activeforeground='white', activebackground='orange',command=store)
    ground2.place(x=279, y=270)



def store():
    RULES = Label(steps, text="RULES", bg='white', fg='#19423c',
                  font=('Microsoft Yahei UI Light', 13, 'bold'))
    RULES.place(x=150, y=430)

    RULES = Label(steps,
                  text="1)Use designated areas for warming up:\n2)No food or drinks on the field:\n3)Respect the field:\n4)Wear appropriate footwear:\n5)No smoking or open flames:\n6)Keep the field clean:",
                  bg='grey', fg='white',
                  font=('Microsoft Yahei UI Light', 13, 'bold'), justify=LEFT)
    RULES.place(x=150, y=470)

    time_slot_btn = Button(steps, text="Book Time Slot", font=('Open sans', 20, 'bold'), fg='white',
                      bg='dark orange', activeforeground='orange', cursor='hand2', bd=0, width=18,command=press)
    time_slot_btn.place(x='150', y='650')

def press():
    steps.destroy()
    import time1

steps=Tk()
steps.geometry('1408x792+50+0')
steps.resizable(0,0)

       # Create header frame
header_frame = Frame(steps, bg="white", height=80)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = Button(header_frame, text="Book Online",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white")
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white")
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)


        # Create footer frame
footer_frame = Frame(steps, bg="lightgrey", height=50)
footer_frame.pack(side="bottom", fill="x")

        # Add widgets to footer frame
tk.Label(footer_frame, text="Copyright © 2023").pack()

        # Create main frame
main_frame = Frame(steps, bg="black")
main_frame.pack(side="left", fill="both", expand=True)

        # Create canvas
canvas = Canvas(main_frame, bg="white")
canvas.pack(side="left", fill="both", expand=True)

        # Add scrollbar to canvas


        # Configure canvas


        # Create inner frame for widgets
inner_frame = Frame(canvas, bg="white")
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

step1 = Label(steps, text="Step 1: Select Sport",bg='white',fg='#19423c',
              font=('Microsoft Yahei UI Light',13,'bold'))
step1.place(x=150,y=130)

football_btn = Button(steps, text="Football",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
                      bg="grey", relief="flat",activeforeground='white',activebackground='orange',command=drop)
football_btn.place(x=150, y=165)

cricket_btn = Button(steps, text="Cricket",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
                     bg="grey", relief="flat",activeforeground='white',activebackground='orange',command=drop)
cricket_btn.place(x=238, y=165)

Basketball_btn = Button(steps, text="Basketball",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
                      bg="grey", relief="flat",activeforeground='white',activebackground='orange',command=drop)
Basketball_btn.place(x=315, y=165)

hockey_btn = Button(steps, text="Hockey",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
                     bg="grey", relief="flat",activeforeground='white',activebackground='orange',command=drop)
hockey_btn.place(x=419, y=165)

# step2 = Label(steps, text="Step 2: Select Ground",bg='white',fg='#19423c',
#               font=('Microsoft Yahei UI Light',13,'bold'))
# step2.place(x=150,y=240)
#
# ground1 = Button(steps, text="Ground 1\n\n-Outdoor\n-Turf\n-6*6 per side",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
#                       bg="grey", relief="flat",activeforeground='white',activebackground='orange')
# ground1.place(x=150, y=270)
#
# ground2 = Button(steps, text="Ground 2\n\n-Outdoor\n-Turf\n-6*6 per side",font=('Microsoft Yahei UI Light',13,'bold'),fg='white',
#                      bg="grey", relief="flat",activeforeground='white',activebackground='orange')
# ground2.place(x=279, y=270)
#
# RULES = Label(steps, text="RULES",bg='white',fg='#19423c',
#               font=('Microsoft Yahei UI Light',13,'bold'))
# RULES.place(x=150,y=430)
#
# RULES = Label(steps, text="1)Use designated areas for warming up:\n2)No food or drinks on the field:\n3)Respect the field:\n4)Wear appropriate footwear:\n5)No smoking or open flames:\n6)Keep the field clean:" ,bg='grey',fg='white',
#               font=('Microsoft Yahei UI Light',13,'bold'),justify=LEFT)
# RULES.place(x=150,y=470)
#
# h2=PhotoImage(file='stepppp.png')
# home = Label(steps,image=h2, relief="flat", bg="white")
# home.place(x='650',y='140')

h2 = PhotoImage(file='stepppp.png')
home = Label(steps, image=h2, relief="flat", bg="white")
home.place(x='650', y='140')

steps.mainloop()
