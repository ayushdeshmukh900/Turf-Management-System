import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def On_enter(event):
    if searchEntry.get() == 'SEARCH TURF':
        searchEntry.delete(0,END)

def on_search():
    a=searchEntry.get()
    if a.lower()== 'xavier' or a.lower()=="mahim":
        app.destroy()
        import xavier
    elif a.lower()== 'inorbit' or a.lower()=="malad":
        app.destroy()
        import Malad
    elif a.lower()=='sector1' or a.lower()=='miraroad':
        app.destroy()
        import Mira_road
    elif a.lower() == 'astro' or a.lower() == 'dadar':
        app.destroy()
        import dadar
    elif a.lower()=='footcric' or a.lower()=='borivali':
        app.destroy()
        import borivali
    elif a.lower()=='spartan' or a.lower()=='palghar':
        app.destroy()
        import Palghar
    else:
        messagebox.showerror('Not available','No such Turf available')


def on_enter():
    app.destroy()
    import sixturf

def mumbai():
    mum=Button(app,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(app, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(app, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    app.destroy()
    import forpass

def mk():
    app.destroy()
    import login



app = Tk()
app.geometry('1408x792+50+0')
app.resizable(0,0)


# menu=Menu(app)
#
# m1=Menu(menu)
#
# m1.add_command(label='new project')
# app.config(menu=menu)
# menu.add_cascade(label="Location",menu=m1)




       # Create header frame
header_frame = Frame(app, bg="white", height=80)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = Button(header_frame, text="Book Online",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18,command=on_enter)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white",command=om)
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white",
                      command=mumbai)
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)


        # Create footer frame
footer_frame = Frame(app, bg="lightgrey", height=50)
footer_frame.pack(side="bottom", fill="x")

        # Add widgets to footer frame
tk.Label(footer_frame, text="Copyright © 2023").pack()

        # Create main frame
main_frame = Frame(app, bg="black")
main_frame.pack(side="left", fill="both", expand=True)

        # Create canvas
canvas = Canvas(main_frame, bg="white")
canvas.pack(side="left", fill="both", expand=True)

        # Add scrollbar to canvas


        # Configure canvas


        # Create inner frame for widgets
inner_frame = Frame(canvas, bg="white")
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # # Create first frame
        # frame1 = tk.Frame(inner_frame, bg="white")
        # frame1.pack(side="top",fill='both',expand= True)
        #
        # all_sports_btn = tk.Button(frame1, text="All Sports", bg="white", relief="flat")
        # # all_sports_btn.place(x=0,y=500)
        # all_sports_btn.pack(side="left",padx=250,pady=100)
        #
        # # all_sports_lbl = tk.Label(frame1, text="View all sports")
        # # all_sports_lbl.grid(row=1, column=0)
        #
        # football_btn = tk.Button(frame1, text="Football", bg="white", relief="flat")
        # football_btn.pack(side="left",padx=20)
        #
        # # football_lbl = tk.Label(frame1, text="View football games")
        # # football_lbl.grid(row=1, column=1)
        #
        # cricket_btn = tk.Button(frame1, text="Cricket", bg="white", relief="flat")
        # cricket_btn.pack(side="left",padx=30)
        #
        # # cricket_lbl = tk.Label(frame1, text="View cricket games")
        # # cricket_lbl.grid(row=1, column=2)
        #
        # fitness_events_btn = tk.Button(frame1, text="Fitness & Events", bg="white", relief="flat")
        # fitness_events_btn.pack(side="left", padx=10)
        #
        # # fitness_events_lbl = tk.Label(frame1, text="View fitness events")
        # # fitness_events_lbl.grid(row=1, column=3)
        #
        # offers_btn = tk.Button(frame1, text="Offers", bg="white", relief="flat")
        # offers_btn.pack(side="left", padx=80)
        #
        # # offers_lbl = tk.Label(frame1, text="View special offers")
        # # offers_lbl.grid(row=1, column=4)
        #
        # # Create search bar in 1st frame
        # search_label = tk.Label(header_frame, text="Search:")
        # search_label.pack(side="left", padx=10)
        #
        # search_entry = tk.Entry(header_frame)
        # search_entry.pack(side="left", padx=10)
        #
        # search_btn = tk.Button(header_frame, text="Search", relief="flat", bg="white")
        # search_btn.pack(side="left", padx=10)
        #
        # '''# Create second frame
        # frame2 = tk.Frame(inner_frame, bg="white")
        # frame2.pack(side="top", pady=10)
        #
        # search_label = tk.Label(frame2, text="Search", bg="white")
        # search_label.pack(side="left", padx=10)
        #
        # search_entry = tk.Entry(frame2, bg="white")
        # search_entry.pack(side="left", padx=10)'''
        #
        # frame3 = tk.Frame(inner_frame, bg="white")
        # frame3.pack(side="top",fill='both')
        #
        # offers_lbl = tk.Label(frame3, text="View special offers")
        # offers_lbl.grid(padx=0,pady=0)


all_sports_btn = Button(app, text="All Sports",font=('Microsoft Yahei UI Light',15,'bold') ,
                        bg="white", relief="flat",activebackground='white',bd=0,command=on_enter)
all_sports_btn.place(x=190,y=120)

football_btn = Button(app, text="Football",font=('Microsoft Yahei UI Light',15,'bold'),
                      bg="white", relief="flat",activebackground='white',bd=0,command=on_enter)
football_btn.place(x=410, y=120)

cricket_btn = Button(app, text="Cricket",font=('Microsoft Yahei UI Light',15,'bold'),activebackground='white',bd=0,
                     bg="white", relief="flat",command=on_enter)
cricket_btn.place(x=630, y=120)

fit_btn = Button(app, text="Fitness and event",font=('Microsoft Yahei UI Light',15,'bold'),activebackground='white',bd=0,
                 bg="white", relief="flat",command=on_enter)
fit_btn.place(x=830, y=120)

offer_btn = Button(app, text="Offer",font=('Microsoft Yahei UI Light',15,'bold'),activebackground='white',bd=0,
                   bg="white", relief="flat",command=on_enter)
offer_btn.place(x=1110, y=120)

all_sports_lbl = Label(app, text="See all sports ground of\n your city",bg='white')
all_sports_lbl.place(x=198,y=165)

football_lbl = Label(app, text="Book turf ground &\ngymkhana grounds",bg='white')
football_lbl.place(x=410,y=165)

cricket_lbl = Label(app, text="Book indoor & outdoor\ncricket grounds",bg='white')
cricket_lbl.place(x=630,y=165)

fitness_events_lbl = Label(app, text="Register for Gym &\nEvents",bg='white')
fitness_events_lbl.place(x=860,y=165)

offers_lbl = Label(app, text="Offers & Discounts",bg='white')
offers_lbl.place(x=1110,y=165)

cricket_logo = PhotoImage(file='cricketball_for_logo.png')
clLabel = Label(app, image=cricket_logo, cursor='hand2')
clLabel.place(x=600, y=140)

football_logo = PhotoImage(file='football_image_for_logo.png')
flLabel = Label(app, image=football_logo, cursor='hand2')
flLabel.place(x=380, y=140)

fitness_logo = PhotoImage(file='callendar_for_logo.png')
ftlLabel = Label(app, image=fitness_logo, cursor='hand2')
ftlLabel.place(x=800, y=140)


ban = PhotoImage(file='bnew1.png')
bLabel = Label(app, image=ban, cursor='hand2')
bLabel.place(x=15, y=300)

# search_label = tk.Label(app, text="Search:", font=('Microsoft Yahei UI Light', 13, 'bold'))
# search_label.place(x=280, y=600)

se=Label(app,text='Search for the best turf grounds,indoor courts & gymkhana grounds in your city',font=('Microsoft Yahei UI Light', 12,'bold'), bg='white',fg='green')
se.place(x=360,y=610)



searchEntry = Entry(app, width=50, font=('Microsoft Yahei UI Light', 14,'bold'), bg='#19423c',
                    fg='white', bd=0)
searchEntry.place(x=400, y=650)
searchEntry.insert(0,'SEARCH TURF')

searchEntry.bind('<FocusIn>',On_enter)
search_button = PhotoImage(file='search.png')
flLabel1 = Button(app, image=search_button, cursor='hand2',command=on_search)
flLabel1.place(x=980, y=650)

# tk.Label(app, text="Select the Turf :",
#     font=("Times New Roman", 10)).grid(column=0,
#                                              row=5, padx=10, pady=25)
#
# # Combobox creation
# n = tk.StringVar()
# monthchoosen = tk.Combobox(app, width=27, textvariable=n)
#
# # Adding combobox drop down list
# monthchoosen['values'] = (' Mahim',
#                           ' Mira Road',
#                           ' Malad',
#                           ' Borivali',
#                           ' Dadar',
#                           ' Palghar')
#
# monthchoosen.grid(column=1, row=5)
# monthchoosen.current()



app.mainloop()