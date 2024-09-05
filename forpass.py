from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox

#FUNCTION PART
def submit():
    if usernameEntry.get()=='' or npasswEntry.get()=='' or cpasswEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required')
        forpassword.destroy()
        import forpass
    elif npasswEntry.get()!=cpasswEntry.get():
         messagebox.showerror('Error','Password and confirm Password are not matching')
    else:
        con = pymysql.connect(host='localhost', user='root',password='root',database='turf')
        mycursor = con.cursor()
        query= ' select * from user where user_name=%s'
        mycursor.execute(query, usernameEntry.get())
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect username')
        else:
            query='Update user set user_password=%s where user_name=%s'
            mycursor.execute(query,(npasswEntry.get(),usernameEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Password is reset, please login with new password')
            forpassword.destroy()
            import login


def On_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def npassw_enter(event):
    if npasswEntry.get() == 'New Password':
        npasswEntry.delete(0, END)

def cpassw_enter(event):
    if cpasswEntry.get() == 'Confirm Password':
        cpasswEntry.delete(0, END)







#GUI PART

forpassword=Tk()
forpassword.geometry('1408x792+50+0') #(sizing of the page)
forpassword.resizable(0,0)
forpassword.title('login Page')

#bgImage=Image.open("login(1).jpg")

#bgImage=bgImage.resize((100,100))
bgImage=ImageTk.PhotoImage(file='1.jpg')

#bgImage=bgImage.resize((100,100))

bgLabel=Label(forpassword,image=bgImage)
#bgLabel.grid(row=0,column=0)
#bgLabel.place(x=100,y=120) #(sizing of the page)
bgLabel.pack(side = LEFT, expand =TRUE, fill = BOTH)
heading=Label(forpassword,text='RESET PASSWORD', font=('Microsoft Yahei UI Light',23,'bold'),bg='darkslategray',fg='light cyan')
heading.place(x=1020,y=200) # for placing the labels
bgLabel.pack()


username=Label(forpassword,text='Username', font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
username.place(x=1040,y=280)
usernameEntry=Entry(forpassword,width=30,font=('Microsoft Yahei UI Light',11),bg='darkslategray',fg='light cyan',bd=2)
usernameEntry.place(x=1040,y=310)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',On_enter)
#frame1=Frame(forpassword,width=235,height=2,bg='darkslategray')
#frame1.place(x=1040,y=322)



newpass=Label(forpassword,text='New Password', font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
newpass.place(x=1040,y=350)
npasswEntry=Entry(forpassword,width=30,font=('Microsoft Yahei UI Light',11),bg='darkslategray',fg='light cyan',bd=2)
npasswEntry.place(x=1040,y=380)
npasswEntry.insert(0,'New Password')
npasswEntry.bind('<FocusIn>',npassw_enter)

compass=Label(forpassword,text='Confirm Password', font=('Microsoft Yahei UI Light',13,'bold'),bg='#19423c',fg='light cyan')
compass.place(x=1040,y=420)
cpasswEntry=Entry(forpassword,width=30,font=('Microsoft Yahei UI Light',11),bg='darkslategray',fg='light cyan',bd=2)
cpasswEntry.place(x=1040,y=450)
cpasswEntry.insert(0,'Confirm Password')

cpasswEntry.bind('<FocusIn>',cpassw_enter)
#frame2=Frame(forpassword,width=235,height=2,bg='darkslategray')
#frame2.place(x=1040,y=371)




submitbutton=Button(forpassword,text='Submit',font=('Open sans',15,'bold'),fg='light cyan',
                   bg='darkslategray',activeforeground='darkslategray',cursor='hand2',bd=0,width=18,command=submit)
submitbutton.place(x=1055,y=530)



forpassword.mainloop()