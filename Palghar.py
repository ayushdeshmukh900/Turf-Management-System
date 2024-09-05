from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser

def on_enter():
    palghar.destroy()
    import sixturf


def mumbai():
    mum=Button(palghar,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(palghar, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(palghar, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    palghar.destroy()
    import forpass

def mk():
    palghar.destroy()
    import login


def hm():
    palghar.destroy()
    import home



#GUI
palghar=Tk()
palghar.geometry('1408x792+50+0')
palghar.resizable(0,0)

palghar.title('palghar')
 # Create header frame
header_frame = Frame(palghar, bg="white", height=80,bd=2)
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

scrollbar = Scrollbar(palghar)
scrollbar.pack( side = RIGHT,fill=Y)



#frame

turf=Label(palghar,bg='white')
turf.pack(side = LEFT, expand =TRUE, fill = BOTH)


user=Label(palghar,text="Spartan,Palghar" , font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='#19423c')
user.place(x=250,y=150)

palgharlogo=PhotoImage(file='palghar_logo.png')
xlabel=Label(palghar,image=palgharlogo,cursor='hand2')

xlabel.place(x=250,y=200)


address=Label(palghar,text='Spartan The Sports Club Near Palm Springs,\nPalghar, Maharashtra 401404',justify=LEFT, font=('Microsoft Yahei UI Light',15),bg='white')
address.place(x=700,y=200)

map=PhotoImage(file='map.png')
mapbtn=Button(palghar,image=map,cursor='hand2',bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/Spartan+The+Sports+Club/@19.6857223,72.6827953,12z/data=!4m19!1m12!4m11!1m3!2m2!1d72.7542064!2d19.6853991!1m6!1m2!1s0x3be71dfee20e0bb3:0xd85e6736ba9f392e!2sSpartan+The+Sports+Club+Near+Palm+Springs,+Valan+Naka+Mahim+Road,+West,+Palghar,+Maharashtra+401404!2m2!1d72.7528357!2d19.6857359!3m5!1s0x3be71dfee20e0bb3:0xd85e6736ba9f392e!8m2!3d19.6857359!4d72.7528357!16s%2Fg%2F11t9c964qm"))

mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(palghar,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=Button(palghar,text='Review /', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
revbtn.place(x=700,y=310)

wrevbtn=Button(palghar,text='Write Review', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
wrevbtn.place(x=755,y=310)

ambi=Label(palghar,text='Amenities:', font=('Microsoft Yahei UI Light',10),bg='forestgreen',fg='white')
ambi.place(x=700,y=340)

foot=Label(palghar,text='Footballs', font=('Microsoft Yahei UI Light',8),bg='grey92')
foot.place(x=700,y=370)

cric=Label(palghar,text='Floodlights', font=('Microsoft Yahei UI Light',8),bg='grey92')
cric.place(x=760,y=370)

bat=Label(palghar,text='Bats', font=('Microsoft Yahei UI Light',8),bg='grey92')
bat.place(x=828,y=370)

stump=Label(palghar,text='Stumps', font=('Microsoft Yahei UI Light',8),bg='grey92')
stump.place(x=862,y=370)



cr=Label(palghar,text='Changing Rooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
cr.place(x=700,y=400)

wash=Label(palghar,text='Washrooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
wash.place(x=800,y=400)


bookbutton=Button(palghar,text='Book Now',font=('Open sans',15,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
bookbutton.place(x=700,y=460)



# step=Label(palghar,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(palghar,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(palghar,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(palghar,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(palghar,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)


pg=PhotoImage(file="pal1.png")
pg1=Label(palghar,image=pg)
pg1.place(x=250,y=580)



pg2=PhotoImage(file="pal2.png")
pg3=Label(palghar,image=pg2)
pg3.place(x=480,y=580)

pg6=PhotoImage(file="pal3.png")
pg7=Label(palghar,image=pg6)
pg7.place(x=725,y=580)

# pg4=PhotoImage(file="m3.png")
# pg5=Label(mira_road,image=pg4)
# pg5.place(x=770,y=580)


















palghar.mainloop()