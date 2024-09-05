from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser


def on_enter():
    malad.destroy()
    import sixturf


def mumbai():
    mum=Button(malad,text='Mumbai',font=('Open sans',10),bg='#19423c',fg='white',bd=1,command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = Button(malad, text='Change Password', font=('Open sans', 10), bg='#19423c',fg="white", bd=1,width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = Button(malad, text='Logout', font=('Open sans', 10), bg='#19423c',fg='white', bd=1,width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    malad.destroy()
    import forpass

def mk():
    malad.destroy()
    import login

def hm():
    malad.destroy()
    import home



#GUI
malad=Tk()
malad.geometry('1408x792+50+0')
malad.resizable(0,0)

malad.title('malad')
       # Create header frame
header_frame = Frame(malad, bg="white", height=80,bd=2)
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

scrollbar = Scrollbar(malad)
scrollbar.pack( side = RIGHT,fill=Y)



#frame

turf=Label(malad,bg='white')
turf.pack(side = LEFT, expand =TRUE, fill = BOTH)


user=Label(malad,text="Inorbit,Malad" , font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='#19423c')
user.place(x=250,y=150)

maladlogo=PhotoImage(file='malad_logo.png')
xlabel=Label(malad,image=maladlogo,cursor='hand2')

xlabel.place(x=250,y=200)


address=Label(malad,text=' Inorbit Rd, Malad, Mindspace, Malad West,\n Mumbai, Maharashtra 400064',justify=LEFT, font=('Microsoft Yahei UI Light',15),bg='white')
address.place(x=700,y=200)

map=PhotoImage(file='map.png')
mapbtn=Button(malad,image=map,cursor='hand2',bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/Dream+Sports+Fields+-+Inorbit+Malad+-+Football+%26+Cricket+Turf/@19.1762433,72.7564177,12.63z/data=!4m19!1m12!4m11!1m3!2m2!1d72.8347654!2d19.1728053!1m6!1m2!1s0x3be7b658a52f9ae7:0x74ef1bf70fe422d3!2s5RCM%2BXQV,+Inorbit+Rd,+Malad,+Mindspace,+Malad+West,+Mumbai,+Maharashtra+400064!2m2!1d72.8343237!2d19.1725048!3m5!1s0x3be7b658a52f9ae7:0x74ef1bf70fe422d3!8m2!3d19.1724943!4d72.8344247!16s%2Fg%2F11c1qbccqp"))

mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(malad,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=Button(malad,text='Review /', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
revbtn.place(x=700,y=310)

wrevbtn=Button(malad,text='Write Review', font=('Microsoft Yahei UI Light',10),cursor='hand2',bd=0,bg='white')
wrevbtn.place(x=755,y=310)

ambi=Label(malad,text='Amenities:', font=('Microsoft Yahei UI Light',10),bg='forestgreen',fg='white')
ambi.place(x=700,y=340)

foot=Label(malad,text='Footballs', font=('Microsoft Yahei UI Light',8),bg='grey92')
foot.place(x=700,y=370)

cric=Label(malad,text='Floodlights', font=('Microsoft Yahei UI Light',8),bg='grey92')
cric.place(x=760,y=370)

bat=Label(malad,text='Bats', font=('Microsoft Yahei UI Light',8),bg='grey92')
bat.place(x=828,y=370)

stump=Label(malad,text='Stumps', font=('Microsoft Yahei UI Light',8),bg='grey92')
stump.place(x=862,y=370)



cr=Label(malad,text='Changing Rooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
cr.place(x=700,y=400)

wash=Label(malad,text='Washrooms', font=('Microsoft Yahei UI Light',8),bg='grey92')
wash.place(x=800,y=400)


bookbutton=Button(malad,text='Book Now',font=('Open sans',15,'bold'),fg='white',
                   bg='dark orange',activeforeground='orange',cursor='hand2',bd=0,width=18)
bookbutton.place(x=700,y=460)



# step=Label(malad,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(malad,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(malad,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(malad,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(malad,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)


mim=PhotoImage(file="m1.png")
mim1=Label(malad,image=mim)
mim1.place(x=250,y=580)


mim2=PhotoImage(file="m2.png")
mim3=Label(malad,image=mim2)
mim3.place(x=600,y=580)

mim4=PhotoImage(file="m3.png")
mim5=Label(malad,image=mim4)
mim5.place(x=830,y=580)














malad.mainloop()