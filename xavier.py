import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser

def on_enter():
    xavier.destroy()
    import sixturf


def mumbai():
    mum=tkinter.Button(xavier, text='Mumbai', font=('Open sans', 10), bg='#19423c', fg='white', bd=1, command=on_enter)
    mum.place(x=880,y=70)


def om():
    mum1 = tkinter.Button(xavier, text='Change Password', font=('Open sans', 10), bg='#19423c', fg="white", bd=1, width=14, command=pk)
    mum1.place(x=965, y=70)

    mum2 = tkinter.Button(xavier, text='Logout', font=('Open sans', 10), bg='#19423c', fg='white', bd=1, width=14, command=mk)
    mum2.place(x=965, y=95)

def pk():
    messagebox.showinfo('Redirect',"You would be logged out after changing the password ")
    xavier.destroy()
    import forpass

def mk():
    xavier.destroy()
    import login




def step1():
    xavier.destroy()
    import step
def home1():
    xavier.destroy()
    import home

#GUI
xavier=tkinter.Tk()
xavier.geometry('1408x792+50+0')
xavier.resizable(0,0)

xavier.title('Xavier')
       # Create header frame
header_frame = tkinter.Frame(xavier, bg="white", height=80, bd=2)
header_frame.pack(side="top", fill="x")

h1=tkinter.PhotoImage(file='panther.png')
home = tkinter.Label(header_frame, image=h1, relief="flat", bg="white")
home.pack(side="left", padx=0)


        # Create buttons in header frame
book_btn = tkinter.Button(header_frame, text="HOME", font=('Open sans', 20, 'bold'), fg='white',
                          bg='dark orange', activeforeground='orange', cursor='hand2', bd=0, width=18, command=home1)
book_btn.pack(side="right", padx=10)

sign_in_btn = tkinter.Button(header_frame, text="Setting", font=('Open sans', 15, 'bold'), fg='green', relief="flat", bg="white", command=om)
sign_in_btn.pack(side="right", padx=10)

location_btn = tkinter.Button(header_frame, text="Location", font=('Open sans', 15, 'bold'), fg='green', relief="flat", bg="white", command=mumbai)
location_btn.pack(side="right", padx=0)

loc=tkinter.PhotoImage(file='loc new.png')
location = tkinter.Label(header_frame, image=loc, cursor='hand2', bg='white')
location.pack(side="right", padx=0)

scrollbar = tkinter.Scrollbar(xavier)
scrollbar.pack(side = tkinter.RIGHT, fill=tkinter.Y)



#frame

turf=tkinter.Label(xavier, bg='white')
turf.pack(side = tkinter.LEFT, expand =tkinter.TRUE, fill = tkinter.BOTH)


user=tkinter.Label(xavier, text="XAVIER,MAHIM", font=('Microsoft Yahei UI Light', 20, 'bold'), bg='white', fg='#19423c')
user.place(x=250,y=150)

xavierlogo=tkinter.PhotoImage(file='xavier_logo.png')
xlabel=tkinter.Label(xavier, image=xavierlogo, cursor='hand2')

xlabel.place(x=250,y=200)


address=tkinter.Label(xavier, text='ST. XAVIERS COLLEGE,Mahapalika Marg,\nMumbai , Maharashtra 400001', font=('Microsoft Yahei UI Light', 15), bg='white')
address.place(x=700,y=200)

map=tkinter.PhotoImage(file='map.png')
mapbtn=tkinter.Button(xavier, image=map, cursor='hand2', bd=0)
mapbtn.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.google.com/maps/place/Xavier+Institute+of+Engineering/@19.0452429,72.8391121,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7c92fb093d785:0x38854a716f0ca945!8m2!3d19.0452429!4d72.841687!16s%2Fm%2F0dgny57"))

mapbtn.place(x=700,y=270)

# re=PhotoImage(file='review.png')
# rebtn=Button(xavier,image=re,cursor='hand2',bd=0)
# rebtn.place(x=600,y=310)

revbtn=tkinter.Button(xavier, text='Review /', font=('Microsoft Yahei UI Light', 10), cursor='hand2', bd=0, bg='white')
revbtn.place(x=700,y=310)

wrevbtn=tkinter.Button(xavier, text='Write Review', font=('Microsoft Yahei UI Light', 10), cursor='hand2', bd=0, bg='white')
wrevbtn.place(x=755,y=310)

ambi=tkinter.Label(xavier, text='Amenities:', font=('Microsoft Yahei UI Light', 10), bg='forestgreen', fg='white')
ambi.place(x=700,y=340)

foot=tkinter.Label(xavier, text='Footballs', font=('Microsoft Yahei UI Light', 8), bg='grey92')
foot.place(x=700,y=370)

cric=tkinter.Label(xavier, text='Floodlights', font=('Microsoft Yahei UI Light', 8), bg='grey92')
cric.place(x=760,y=370)

bat=tkinter.Label(xavier, text='Bats', font=('Microsoft Yahei UI Light', 8), bg='grey92')
bat.place(x=828,y=370)

stump=tkinter.Label(xavier, text='Stumps', font=('Microsoft Yahei UI Light', 8), bg='grey92')
stump.place(x=862,y=370)



cr=tkinter.Label(xavier, text='Changing Rooms', font=('Microsoft Yahei UI Light', 8), bg='grey92')
cr.place(x=700,y=400)

wash=tkinter.Label(xavier, text='Washrooms', font=('Microsoft Yahei UI Light', 8), bg='grey92')
wash.place(x=800,y=400)


bookbutton=tkinter.Button(xavier, text='Book Now', font=('Open sans', 15, 'bold'), fg='white',
                          bg='dark orange', activeforeground='orange', cursor='hand2', bd=0, width=18, command=step1)
bookbutton.place(x=700,y=460)



# step=Label(xavier,text='Step 1: Select Sport',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# step.place(x=250,y=550)
#
# cri=Button(xavier,text='Cricket', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# cri.place(x=250,y=600)
#
# ft=Button(xavier,text='Football', font=('Microsoft Yahei UI Light',15),bg='azure4',bd=0)
# ft.place(x=330,y=600)
#
# rule=Label(xavier,text='Rules',font=('Microsoft Yahei UI Light',20,'bold'),fg='darkred')
# rule.place(x=250,y=650)
#
#
# rule_name=Label(xavier,text='''
# - NO SMOKING
# - NO ALCOHOL CONSUMPTION
# - Book Ground 1 & Ground 2 for full ground
# - NO MORE THAN 25 PEOPLE PER BOOKING
# - NO OUTSIDE FOOD & EATABLES ALLOWED
# - FOR EVENT BOOKINGS PLEASE DROP A WHATSAPP MESSAGE BY CLICKING: 8169729906'''
#                 ,font=('Microsoft Yahei UI Light',10,'bold'),fg='black')
# rule_name.place(x=100,y=700)




xie=tkinter.PhotoImage(file="xav1.png")
xie1=tkinter.Label(xavier, image=xie)
xie1.place(x=250,y=580)


#
# xie2=PhotoImage(file="xav2.png")
# xie3=Label(xavier,image=xie2)
# xie3.place(x=480,y=580)

xie6=tkinter.PhotoImage(file="xav3.png")
xie7=tkinter.Label(xavier, image=xie6)
xie7.place(x=520,y=580)

xie4=tkinter.PhotoImage(file="xav4.png")
xie5=tkinter.Label(xavier, image=xie4)
xie5.place(x=790,y=580)
















xavier.mainloop()