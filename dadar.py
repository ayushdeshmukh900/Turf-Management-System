from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import  webbrowser


def on_enter():
    dadar.destroy()
    import sixturf


def mumbai():
    mum=Button(dadar,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(dadar, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(dadar, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    dadar.destroy()
    import forpass

def mk():
    dadar.destroy()
    import login

def hm():
    dadar.destroy()
    import home



#GUI
dadar=Tk()
dadar.geometry('1408x792+50+0')
dadar.resizable(0,0)

dadar.title('dadar')
       # Create header frame
header_frame = Frame(dadar, bg="white", height=80,bd=2)
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

scrollbar = Scrollbar(dadar)
scrollbar.pack( side = RIGHT,fill=Y)



#frame

turf=Label(dadar,bg='white')
turf.pack(side = LEFT, expand =TRUE, fill = BOTH)


user=Label(dadar,text="Astro,Dadar" , font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='#19423c')
user.place(x=250,y=150)

dadarlogo=PhotoImage(file='dadar_logo.png')
xlabel=Label(dadar,image=dadarlogo,cursor='hand2')

xlabel.place(x=250,y=200)


address=Label(dadar,text='  Astro Park, near Portuguese Church, Dadar West,\n Mumbai, Maharashtra 400028',justify=LEFT, font=('Microsoft Yahei UI Light',15),bg='white')
address.place(x=700,y=200)

map=PhotoImage(file='map.png')
mapbtn=Button(dadar,image=map,cursor='hand2',bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/Astro+Park+-+Salvation+School+Dadar/@19.0175104,72.8325604,17z/data=!3m1!4b1!4m16!1m9!4m8!1m0!1m6!1m2!1s0x3be7cec38cece1d7:0xc5068c32b3bf61e3!2sAstro+Park,+Inside+Our+Lady+Salvation+School+Ghokale+Road,+near+Portuguese+Church,+Dadar+West,+Mumbai,+Maharashtra+400028!2m2!1d72.8351407!2d19.0175104!3m5!1s0x3be7cec38cece1d7:0xc5068c32b3bf61e3!8m2!3d19.0175104!4d72.8351407!16s%2Fg%2F11bzwpj_qy"))
mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(dadar,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=Button(dadar,text='Review /', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
revbtn.place(x=700,y=310)

wrevbtn=Button(dadar,text='Write Review', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
wrevbtn.place(x=755,y=310)

ambi=Label(dadar,text='Amenities:', font=('Microsoft Yahei UI Light',10),bg='forestgreen',fg='white')
ambi.place(x=700,y=340)

foot=Label(dadar,text='Footballs', font=('Microsoft Yahei UI Light',8),bg='grey92')
foot.place(x=700,y=370)

cric=Label(dadar,text='Floodlights', font=('Microsoft Yahei UI Light',8),bg='grey92')
cric.place(x=760,y=370)

bat=Label(dadar,text='Bats', font=('Microsoft Yahei UI Light',8),bg='grey92')
bat.place(x=828,y=370)

stump=Label(dadar,text='Stumps', font=('Microsoft Yahei UI Light',8),bg='grey92')
stump.place(x=862,y=370)



cr=Label(dadar,text='Changing Rooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
cr.place(x=700,y=400)

wash=Label(dadar,text='Washrooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
wash.place(x=800,y=400)


bookbutton=Button(dadar,text='Book Now',font=('Open sans',15,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
bookbutton.place(x=700,y=460)



# step=Label(dadar,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(dadar,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(dadar,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(dadar,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(dadar,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)

ddr=PhotoImage(file="dd1.png")
ddr1=Label(dadar,image=ddr)
ddr1.place(x=250,y=580)



ddr2=PhotoImage(file="dd2.png")
ddr3=Label(dadar,image=ddr2)
ddr3.place(x=498,y=580)

ddr6=PhotoImage(file="dd3.png")
ddr7=Label(dadar,image=ddr6)
ddr7.place(x=705,y=580)

ddr4=PhotoImage(file="dd5.png")
ddr5=Label(dadar,image=ddr4)
ddr5.place(x=910,y=580)



















dadar.mainloop()