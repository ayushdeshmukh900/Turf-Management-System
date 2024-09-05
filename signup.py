import webbrowser
from tkinter import *

import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
# FUNCTIONALITY PART

def clear():
    phonenoEntry.delete(0,END)
    usernameEntry.delete(0,END)
    npass.delete(0,END)
    cpass.delete(0,END)


def data():
    if phonenoEntry.get()=='' or usernameEntry.get()=='' or npass.get()=='' or cpass.get()=='':
        messagebox.showerror('Error','All fields Are Required')
    elif npass.get() != cpass.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password="",database='turf',cursorclass=pymysql.cursors.DictCursor)

            cursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Issue')
            return

        cursor.execute('use turf')
        query='insert into username(user_password,user_name,user_phone_no) values(%s,%s,%s)'
        cursor.execute(query,(npass.get(),usernameEntry.get(),phonenoEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','registered')
        clear()
        usersignup.destroy()
        import login


def On_enter(event):
    if usernameEntry.get()=='Enter First name & Last name':
        usernameEntry.delete(0,END)


def phoneNo(event):
    if phonenoEntry.get()=='Enter Phone Number':
        phonenoEntry.delete(0,END)

def newPass(event):
    if npass.get()=='Enter Password':
        npass.delete(0,END)

def cPass(event):
    if cpass.get()=='Re-Enter Password':
        cpass.delete(0,END)

def Log_in():
    usersignup.destroy()
    import login

# GUI PART
usersignup=Tk()
usersignup.geometry('1408x792+50+0') #(sizing of the page)
usersignup.resizable(0,0)
usersignup.title('Signup Page')


bgImage=ImageTk.PhotoImage(file='1sign.png')



bgLabel=Label(usersignup,image=bgImage)

bgLabel.pack(side = LEFT, expand =TRUE, fill = BOTH)
heading=Label(usersignup,text='SIGNUP' , font=('Microsoft Yahei UI Light',23,'bold'),bg='#19423c',fg='light cyan')
heading.place(x=1060,y=200) # for placing the labels
bgLabel.pack()

user=Label(usersignup,text='Username' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
user.place(x=990,y=270)
usernameEntry=Entry(usersignup,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
usernameEntry.place(x=990,y=300)
usernameEntry.insert(0,'Enter First name & Last name')

usernameEntry.bind('<FocusIn>',On_enter)

user=Label(usersignup,text='Phone Number' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
user.place(x=990,y=350)
phonenoEntry=Entry(usersignup,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
phonenoEntry.place(x=990,y=380)
phonenoEntry.insert(0,'Enter Phone Number')

phonenoEntry.bind('<FocusIn>',phoneNo)



npassword=Label(usersignup,text='New Password' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
npassword.place(x=990,y=430)
npass=Entry(usersignup,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
npass.place(x=990,y=460)
npass.insert(0,'Enter Password')

npass.bind('<FocusIn>',newPass)

cpassword=Label(usersignup,text='Confirm Password' , font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
cpassword.place(x=990,y=510)
cpass=Entry(usersignup,width=30,font=('Microsoft Yahei UI Light',12),bg='darkslategray',fg='light cyan',bd=2)
cpass.place(x=990,y=540)
cpass.insert(0,'Re-Enter Password')

cpass.bind('<FocusIn>',cPass)


confirm=Button(usersignup,text="Submit",width=10,font=('Microsoft Yahei UI Light',17,'bold'),bg='darkslategray',fg='light cyan',bd=0,cursor="hand2",
               activeforeground="Light cyan",command=data)
confirm.place(x=1060,y=620)


alraedyhaveanaccount=Label(usersignup,text='Already have an Account?',font=('Open Sans',11,'bold'),fg='light cyan',bg='#173c35')
alraedyhaveanaccount.place(x=970,y=700)

loginbutton=Button(usersignup,text='Log in',font=('Open sans',11,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='light cyan',cursor='hand2',bd=0,command=Log_in)
loginbutton.place(x=1180,y=700)


usersignup.mainloop()


