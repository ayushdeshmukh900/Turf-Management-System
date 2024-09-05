import webbrowser
from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import pymysql
from PIL import ImageTk, Image

def clear():
    usernameEntry.delete(0,END)
    passwEntry.delete(0,END)

def data():
    if usernameEntry.get() == '' or passwEntry.get() == '':
        messagebox.showerror('Error','All fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password="",database='turf',cursorclass=pymysql.cursors.DictCursor)
            cur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Issue')
            return
        query = 'use turf'
        cur.execute(query)
        query='select * from username' \
              '' \
              ' where user_name=%s and user_password=%s'
        cur.execute(query,(usernameEntry.get(),passwEntry.get()))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
            userlogin.destroy()
            import login
        else:
            userlogin.destroy()
            import home

# FUNCTIONALITY PART

def hide():
    openeye.config(file='closeye.png')
    passwEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwEntry.config(show='')
    eyeButton.config(command=hide)

def On_enter(event):
    if usernameEntry.get()=='Enter First name & Last name':
        usernameEntry.delete(0,END)

def passw_enter(event):
    if passwEntry.get() == 'Enter Password':
        passwEntry.delete(0, END)

def sign_in():
    userlogin.destroy()
    import signup

# GUI PART
userlogin=Tk()
# a=userlogin.winfo_height()
# b=userlogin.winfo_width()

userlogin.geometry('1408x792+50+0') #(sizing of the page)

#a=userlogin.winfo_height()
#b=userlogin.winfo_width()

#print(a,b)
userlogin.resizable(0,0)
userlogin.title('login Page')

#bgImage=Image.open("login(1).jpg")

#bgImage=bgImage.resize((100,100))
bgImage=ImageTk.PhotoImage(file='1.jpg')

#bgImage=bgImage.resize((0,0))

bgLabel=Label(userlogin,image=bgImage)
#bgLabel.grid(row=0,column=0)
#bgLabel.place(x=100,y=120) #(sizing of the page)
bgLabel.pack(side = LEFT, expand =TRUE, fill = BOTH)
heading=Label(userlogin,text='LOGIN' , font=('Microsoft Yahei UI Light',23,'bold'),bg='#19423c',fg='light cyan')
heading.place(x=1060,y=200) # for placing the labels
bgLabel.pack()

user=Label(userlogin,text='Username' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
user.place(x=990,y=270)
usernameEntry=Entry(userlogin,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
usernameEntry.place(x=990,y=300)
usernameEntry.insert(0,'Enter First name & Last name')

usernameEntry.bind('<FocusIn>',On_enter)
#frame1=Frame(userlogin,width=235,height=2,bg='darkslategray')
#frame1.place(x=1040,y=322)

user=Label(userlogin,text='Password' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
user.place(x=990,y=370)
passwEntry=Entry(userlogin,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
passwEntry.place(x=990,y=400)
passwEntry.insert(0,'Enter Password')

passwEntry.bind('<FocusIn>',passw_enter)
#frame2=Frame(userlogin,width=235,height=2,bg='darkslategray')
#frame2.place(x=1040,y=371)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(userlogin,image=openeye,bd=1,bg='darkslategray',activebackground='darkslategray',cursor='hand2',command=hide)
eyeButton.place(x=1241,y=402)


forgetButton=Button(userlogin,text='Forgot Password?',bd=0,bg='#19423c',
                    cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='light cyan',
    activeforeground='darkslategray')
forgetButton.place(x=1143,y=431)

loginbutton=Button(userlogin,text='Login',font=('Open sans',15,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='darkslategray',cursor='hand2',bd=0,width=18,command=data)
loginbutton.place(x=1010,y=500)


#orLabel=Label(userlogin,text='------------OR-------------',font=('Open Sans',16),fg='light cyan',bg='darkslategray')
#orLabel.place(x=1060,y=520)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(userlogin,image=facebook_logo,cursor='hand2',bg='#19423c')
fbLabel.place(x=1040,y=600)
fbLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.facebook.com/"))
google_logo=PhotoImage(file='google.png')
gLabel=Label(userlogin,image=google_logo,cursor='hand2',bg='#19423c')
gLabel.place(x=1100,y=600)
gLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.xavier.ac.in"))
twitter_logo=PhotoImage(file='twitter.png')
tLabel=Label(userlogin,image=twitter_logo,cursor='hand2',bg='#19423c')
tLabel.place(x=1160,y=600)
tLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://twitter.com"))
signupLabel=Label(userlogin,text='Dont have account?',font=('Open Sans',11,'bold'),fg='light cyan',bg='#173c35')
signupLabel.place(x=970,y=700)

newaccbutton=Button(userlogin,text='Create new account',font=('Open sans',11,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='light cyan',cursor='hand2',bd=0,command=sign_in)
newaccbutton.place(x=1140,y=700)



userlogin.mainloop()