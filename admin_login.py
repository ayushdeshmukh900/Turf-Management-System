import webbrowser
from tkinter import *
from tkinter import messagebox
import pymysql.cursors


import mysql.connector
import pymysql
from PIL import ImageTk, Image

def clear():
    adminnameEntry.delete(0,END)
    passwEntry.delete(0,END)

def data():
    if adminnameEntry.get()=='' or passwEntry.get()=='':
        messagebox.showerror('Error','All fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root',database='turf',cursorclass=pymysql.cursors.DictCursor)
            cursor = con.cursor()
        except Exception as e:
            messagebox.showerror('Error', e)
            return

        cursor.execute('use turf')
        query = "select admin_name from admin where admin_name=%s"
        cursor.execute(query, (adminnameEntry.get()))
        row = cursor.fetchone()
        print(row)
        query1 = "select admin_password from admin where admin_password=%s"
        cursor.execute(query1, (passwEntry.get()))
        row1 = cursor.fetchone()
        print(row1)
        con.commit()
        con.close()
        adminlogin.destroy()
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
    if adminnameEntry.get()=='Enter First name & Last name':
        adminnameEntry.delete(0,END)

def passw_enter(event):
    if passwEntry.get() == 'Enter Password':
        passwEntry.delete(0, END)

def sign_in():
    adminlogin.destroy()
    import signup

# GUI PART
adminlogin=Tk()

adminlogin.geometry('1408x792+50+0') #(sizing of the page)


adminlogin.resizable(0,0)
adminlogin.title('Admin login Page')


bgImage=ImageTk.PhotoImage(file='1admin.jpeg')


bgLabel=Label(adminlogin,image=bgImage)
bgLabel.pack(side = LEFT, expand =TRUE, fill = BOTH)
heading=Label(adminlogin,text='ADMIN LOGIN' , font=('Microsoft Yahei UI Light',23,'bold'),bg='#19423c',fg='light cyan')
heading.place(x=1025,y=200) # for placing the labels
bgLabel.pack()

admin=Label(adminlogin,text='Admin name' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
admin.place(x=990,y=270)
adminnameEntry=Entry(adminlogin,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
adminnameEntry.place(x=990,y=300)
adminnameEntry.insert(0,'Enter First name & Last name')

adminnameEntry.bind('<FocusIn>',On_enter)

admin=Label(adminlogin,text='Password' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
admin.place(x=990,y=370)
passwEntry=Entry(adminlogin,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
passwEntry.place(x=990,y=400)
passwEntry.insert(0,'Enter Password')

passwEntry.bind('<FocusIn>',passw_enter)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(adminlogin,image=openeye,bd=1,bg='darkslategray',activebackground='darkslategray',cursor='hand2',command=hide)
eyeButton.place(x=1241,y=402)


forgetButton=Button(adminlogin,text='Forgot Password?',bd=0,bg='#19423c',
                    cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='light cyan',
    activeforeground='darkslategray')
forgetButton.place(x=1143,y=431)

loginbutton=Button(adminlogin,text='Login',font=('Open sans',15,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='darkslategray',cursor='hand2',bd=0,width=18,command=data)
loginbutton.place(x=1010,y=500)


#orLabel=Label(adminlogin,text='------------OR-------------',font=('Open Sans',16),fg='light cyan',bg='darkslategray')
#orLabel.place(x=1060,y=520)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(adminlogin,image=facebook_logo,cursor='hand2',bg='#19423c')
fbLabel.place(x=1040,y=600)
fbLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.facebook.com/"))
google_logo=PhotoImage(file='google.png')
gLabel=Label(adminlogin,image=google_logo,cursor='hand2',bg='#19423c')
gLabel.place(x=1100,y=600)
gLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://www.xavier.ac.in"))
twitter_logo=PhotoImage(file='twitter.png')
tLabel=Label(adminlogin,image=twitter_logo,cursor='hand2',bg='#19423c')
tLabel.place(x=1160,y=600)
tLabel.bind('<Button-1>',
             lambda  x:webbrowser.open_new("https://twitter.com"))
signupLabel=Label(adminlogin,text='Dont have account?',font=('Open Sans',11,'bold'),fg='light cyan',bg='#173c35')
signupLabel.place(x=970,y=700)

newaccbutton=Button(adminlogin,text='Create new account',font=('Open sans',11,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='light cyan',cursor='hand2',bd=0,command=sign_in)
newaccbutton.place(x=1140,y=700)



adminlogin.mainloop()