from tkinter import *
from PIL import ImageTk, Image
import webbrowser
from tkinter import messagebox
def on_enter():
    mira_road.destroy()
    import sixturf


def mumbai():
    mum=Button(mira_road,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(mira_road, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(mira_road, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    mira_road.destroy()
    import forpass

def mk():
    mira_road.destroy()
    import login

def hm():
    mira_road.destroy()
    import home



#GUI
mira_road=Tk()
mira_road.geometry('1408x792+50+0')
mira_road.resizable(0,0)

mira_road.title('mira_road')
       # Create header frame
header_frame = Frame(mira_road, bg="white", height=80,bd=2)
header_frame.pack(side="top", fill="x")

h1=PhotoImage(file='panther.png')
home = Label(header_frame,image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = Button(header_frame, text="HOME",font=('Open sans',20,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18,command=hm)
book_btn.pack(side="right", padx=10)

sign_in_btn = Button(header_frame, text="Setting",font=('Open sans',15,'bold'),fg='green' ,relief="flat",bg="white",command=om)
sign_in_btn.pack(side="right", padx=10)

location_btn = Button(header_frame, text="Location",font=('Open sans',15,'bold'),fg='green' , relief="flat", bg="white",command=mumbai)
location_btn.pack(side="right", padx=0)

loc=PhotoImage(file='loc new.png')
location = Label(header_frame, image=loc,cursor='hand2',bg='white')
location.pack(side="right", padx=0)

scrollbar = Scrollbar(mira_road)
scrollbar.pack( side = RIGHT,fill=Y)



#frame

turf=Label(mira_road,bg='white')
turf.pack(side = LEFT, expand =TRUE, fill = BOTH)


user=Label(mira_road,text="Sector1,MiraRoad" , font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='#19423c')
user.place(x=250,y=150)

mira_roadlogo=PhotoImage(file='mira_logo.png')
xlabel=Label(mira_road,image=mira_roadlogo,cursor='hand2',bd=0)

xlabel.place(x=250,y=200)


address=Label(mira_road,text=' Bhayandar Flyover, Chandan Shanti, Mira Road East,\n Mira Bhayandar, Maharashtra 401105',justify=LEFT, font=('Microsoft Yahei UI Light',15),bg='white')
address.place(x=700,y=200)

map=PhotoImage(file='map.png')
mapbtn=Button(mira_road,image=map,cursor='hand2',bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/TrickShot+Soccer+and+cricket+turf/@19.2900035,72.7834487,12z/data=!4m19!1m12!4m11!1m3!2m2!1d72.8538299!2d19.2900035!1m6!1m2!1s0x3be7b046c96ee519:0x2f2f10dfbfb38408!2s7VR3%2B295,+Bhayandar+Flyover,+Chandan+Shanti,+Mira+Road+East,+Mira+Bhayandar,+Maharashtra+401105!2m2!1d72.8534892!2d19.2900168!3m5!1s0x3be7b046c96ee519:0x2f2f10dfbfb38408!8m2!3d19.2900168!4d72.8534892!16s%2Fg%2F11f120tllx"))

mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(mira_road,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=Button(mira_road,text='Review /', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
revbtn.place(x=700,y=310)

wrevbtn=Button(mira_road,text='Write Review', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
wrevbtn.place(x=755,y=310)

ambi=Label(mira_road,text='Amenities:', font=('Microsoft Yahei UI Light',10),bg='forestgreen',fg='white')
ambi.place(x=700,y=340)

foot=Label(mira_road,text='Footballs', font=('Microsoft Yahei UI Light',8),bg='grey92')
foot.place(x=700,y=370)

cric=Label(mira_road,text='Floodlights', font=('Microsoft Yahei UI Light',8),bg='grey92')
cric.place(x=760,y=370)

bat=Label(mira_road,text='Bats', font=('Microsoft Yahei UI Light',8),bg='grey92')
bat.place(x=828,y=370)

stump=Label(mira_road,text='Stumps', font=('Microsoft Yahei UI Light',8),bg='grey92')
stump.place(x=862,y=370)



cr=Label(mira_road,text='Changing Rooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
cr.place(x=700,y=400)

wash=Label(mira_road,text='Washrooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
wash.place(x=800,y=400)


bookbutton=Button(mira_road,text='Book Now',font=('Open sans',15,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
bookbutton.place(x=700,y=460)



# step=Label(mira_road,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(mira_road,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(mira_road,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(mira_road,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(mira_road,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)



mirm=PhotoImage(file="mira1.png")
mirm1=Label(mira_road,image=mirm)
mirm1.place(x=250,y=580)



mirm2=PhotoImage(file="mira2.png")
mirm3=Label(mira_road,image=mirm2)
mirm3.place(x=500,y=580)

mirm6=PhotoImage(file="mira4.png")
mirm7=Label(mira_road,image=mirm6)
mirm7.place(x=655,y=580)

mirm4=PhotoImage(file="m3.png")
mirm5=Label(mira_road,image=mirm4)
mirm5.place(x=770,y=580)

mira_road.mainloop()