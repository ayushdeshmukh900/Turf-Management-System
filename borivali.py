from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser

def on_enter():
    borivali.destroy()
    import sixturf


def mumbai():
    mum=Button(borivali,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(borivali, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(borivali, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    borivali.destroy()
    import forpass

def mk():
    borivali.destroy()
    import login


def hm():
    borivali.destroy()
    import home




#GUI
borivali=Tk()
borivali.geometry('1408x792+50+0')
borivali.resizable(0,0)

borivali.title('borivali')
       # Create header frame
header_frame = Frame(borivali, bg="white", height=80,bd=2)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = Button(header_frame, text="HOME",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white",command=om)
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white",command=mumbai)
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)

scrollbar = Scrollbar(borivali)
scrollbar.pack( side = RIGHT,fill=Y)



#frame

turf=Label(borivali,bg='white')
turf.pack(side = LEFT, expand =TRUE, fill = BOTH)


user=Label(borivali,text="Footcric,Borivali" , font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='#19423c')
user.place(x=250,y=150)

borivalilogo=PhotoImage(file='borivali_logo.png')
xlabel=Label(borivali,image=borivalilogo,cursor='hand2')

xlabel.place(x=250,y=200)


address=Label(borivali,text='Nalanda Academy,near Mangal Murti Hospital Road,\n Borivali W, Maharashtra 400091',justify=LEFT, font=('Microsoft Yahei UI Light',15),bg='white')
address.place(x=700,y=200)

map=PhotoImage(file='map.png')
mapbtn=Button(borivali,image=map,cursor='hand2',bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/FootCric+Turf,+Borivali/@19.2266613,72.7905829,13z/data=!4m19!1m12!4m11!1m3!2m2!1d72.8231985!2d19.2323343!1m6!1m2!1s0x3be7b185f84ff97b:0xc25432813b9b1112!2sNalanda+Academy,+RSC+Rd+Number+34,+near+Mangal+Murti+Hospital+Road,+Gorai+2,+Borivali,+W,+Maharashtra+400091!2m2!1d72.8252611!2d19.2261884!3m5!1s0x3be7b185f84ff97b:0xc25432813b9b1112!8m2!3d19.2261884!4d72.8252611!16s%2Fg%2F11j94rdk8s"))

mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(borivali,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=Button(borivali,text='Review /', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
revbtn.place(x=700,y=310)

wrevbtn=Button(borivali,text='Write Review', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
wrevbtn.place(x=755,y=310)

ambi=Label(borivali,text='Amenities:', font=('Microsoft Yahei UI Light',10),bg='forestgreen',fg='white')
ambi.place(x=700,y=340)

foot=Label(borivali,text='Footballs', font=('Microsoft Yahei UI Light',8),bg='grey92')
foot.place(x=700,y=370)

cric=Label(borivali,text='Floodlights', font=('Microsoft Yahei UI Light',8),bg='grey92')
cric.place(x=760,y=370)

bat=Label(borivali,text='Bats', font=('Microsoft Yahei UI Light',8),bg='grey92')
bat.place(x=828,y=370)

stump=Label(borivali,text='Stumps', font=('Microsoft Yahei UI Light',8),bg='grey92')
stump.place(x=862,y=370)



cr=Label(borivali,text='Changing Rooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
cr.place(x=700,y=400)

wash=Label(borivali,text='Washrooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
wash.place(x=800,y=400)


bookbutton=Button(borivali,text='Book Now',font=('Open sans',15,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
bookbutton.place(x=700,y=460)



# step=Label(borivali,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(borivali,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(borivali,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(borivali,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(borivali,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)




bor=PhotoImage(file="dd4.png")
bor1=Label(borivali,image=bor)
bor1.place(x=250,y=580)



bor2=PhotoImage(file="bor1.png")
bor3=Label(borivali,image=bor2)
bor3.place(x=480,y=580)

bor6=PhotoImage(file="bor2.png")
bor7=Label(borivali,image=bor6)
bor7.place(x=753,y=580)

# bor4=PhotoImage(file="m3.png")
# bor5=Label(mira_road,image=bor4)
# bor5.place(x=770,y=580)
















borivali.mainloop()