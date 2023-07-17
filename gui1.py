import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from csv import writer
from csv import reader
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import food





def adminops():
    
    def ADDDISH():
        def newdish():
            if(food.addingdish(nameent.get(),UNent.get())):
                messagebox.showinfo("LOGIN", "SUCCESSFULLY ADDED NEW DISH")
                
                
        root2.destroy()
        root5=Tk()
        root5.resizable(0,0)
        root5.geometry('990x660+50+50')
        bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
        bglable=Label(root5,image=bgimage)
        bglable.place(x=0,y=0)
    
        frame=Frame(root5,bg='white')
        frame.place(x=554,y=100)
        heading=Label(frame,text='ADD  DISH',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen',padx=75,pady=11)
        heading.grid(row=0,column=0)
    
        namel=Label(frame,text='NAME OF DISH',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
        namel.grid(row=1,column=0,sticky='w',padx=25,pady=(30,10))
        nameent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
        nameent.grid(row=2,column=0)
    
        UNl=Label(frame,text='PRICE',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
        UNl.grid(row=5,column=0,sticky='w',padx=25,pady=(30,10))
        UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
        UNent.grid(row=6,column=0)
        
        signupb=Button(frame,text='ADD DISH',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12,command=newdish)
        signupb.grid(row=9,column=0,pady=30)
        root5.mainloop()

    
    def VIEWORDER():
        pass
    
    def ADDADMIN():
        
        def newadmin():
            if(food.adminadding(nameent.get(),UNent.get(),passent.get())):
                messagebox.showinfo("LOGIN", "SUCCESSFULLY ADDED NEW STAFF")
                
                
        root2.destroy()
        root3=Tk()
        root3.resizable(0,0)
        root3.geometry('990x660+50+50')
        bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
        bglable=Label(root3,image=bgimage)
        bglable.place(x=0,y=0)
    
        frame=Frame(root3,bg='white')
        frame.place(x=554,y=100)
        heading=Label(frame,text='ADDADMIN',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen',padx=75,pady=11)
        heading.grid(row=0,column=0)
    
        namel=Label(frame,text='Name',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
        namel.grid(row=1,column=0,sticky='w',padx=25,pady=10)
        nameent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
        nameent.grid(row=2,column=0)
    
        UNl=Label(frame,text='Username',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
        UNl.grid(row=5,column=0,sticky='w',padx=25,pady=10)
        UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
        UNent.grid(row=6,column=0)
    
    
        passl=Label(frame,text='Password',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
        passl.grid(row=7,column=0,sticky='w',padx=25,pady=10)
        passent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen',show='*')
        passent.grid(row=8,column=0)
    
        signupb=Button(frame,text='ADD STAFF',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12,command=newadmin)
        signupb.grid(row=9,column=0,pady=30)
        root.mainloop()

    
    
    root2=Tk()
    root2.resizable(0,0)
    root2.geometry('990x660+50+50')
    bg1image=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable1=Label(root2,image=bg1image)
    bglable1.place(x=0,y=0)
    heading=Label(root2,text='ADMIN PAGE',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='lightseagreen')
    heading.place(x=600,y=140)
    userb=Button(root2,text='ADD ADMIN',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=ADDADMIN)
    userb.place(x=600,y=240)
    adminb=Button(root2,text='ADD DISH',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=ADDDISH)
    adminb.place(x=600,y=340)
    adminb=Button(root2,text='VIEW ORDER',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=VIEWORDER)
    adminb.place(x=600,y=440)
    root2.mainloop()

def addadmin():
    root4=Tk()
    root4.resizable(0,0)
    root4.geometry('990x660+50+50')
    bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable=Label(root4,image=bgimage)
    bglable.place(x=0,y=0)

    frame=Frame(root4,bg='white')
    frame.place(x=554,y=100)
    heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen',padx=12,pady=11)
    heading.grid(row=0,column=0)

    namel=Label(frame,text='Name',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    namel.grid(row=1,column=0,sticky='w',padx=25,pady=10)
    nameent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    nameent.grid(row=2,column=0)

    UNl=Label(frame,text='Username',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    UNl.grid(row=5,column=0,sticky='w',padx=25,pady=10)
    UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    UNent.grid(row=6,column=0)


    passl=Label(frame,text='Password',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    passl.grid(row=7,column=0,sticky='w',padx=25,pady=10)
    passent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen', show='*')
    passent.grid(row=8,column=0)

    signupb=Button(frame,text='SIGNUP',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12)
    signupb.grid(row=9,column=0,pady=50)
    root4.mainloop()



def login():
    def adminlog1():
        root2.destroy()
        adminlogpage()
        
    def userlog1():
        root2.destroy()
        userlogpage()
    
    root.destroy()
    root2=Tk()
    root2.resizable(0,0)
    root2.geometry('990x660+50+50')
    bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable=Label(root2,image=bgimage)
    bglable.place(x=0,y=0)
    heading=Label(root2,text='LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='lightseagreen')
    heading.place(x=660,y=140)
    userb=Button(root2,text='USER',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=userlog1)
    userb.place(x=610,y=240)
    adminb=Button(root2,text='ADMIN',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=adminlog1)
    adminb.place(x=610,y=340)
    root2.mainloop()


def signup():
    
    def adduser():
        if(food.useersignup(nameent.get(),emailent.get(),UNent.get(),passent.get()))==True:
            messagebox.showinfo("LOGIN", "SUCCESSFULLY SIGNED UP")
            root3.destroy()
            import menu1
    
    root.destroy()
    root3=Tk()
    root3.resizable(0,0)
    root3.geometry('990x660+50+50')
    bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable=Label(root3,image=bgimage)
    bglable.place(x=0,y=0)

    frame=Frame(root3,bg='white')
    frame.place(x=554,y=100)
    heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen',padx=12,pady=11)
    heading.grid(row=0,column=0)

    namel=Label(frame,text='Name',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    namel.grid(row=1,column=0,sticky='w',padx=25,pady=10)
    nameent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    nameent.grid(row=2,column=0)

    emaill=Label(frame,text='Email',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    emaill.grid(row=3,column=0,sticky='w',padx=25,pady=10)
    emailent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    emailent.grid(row=4,column=0)

    UNl=Label(frame,text='Username',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    UNl.grid(row=5,column=0,sticky='w',padx=25,pady=10)
    UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    UNent.grid(row=6,column=0)


    passl=Label(frame,text='Password',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    passl.grid(row=7,column=0,sticky='w',padx=25,pady=10)
    passent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen', show='*')
    passent.grid(row=8,column=0)

    signupb=Button(frame,text='SIGNUP',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12,command=adduser)
    signupb.grid(row=9,column=0,pady=30)
    root.mainloop()



def adminlogpage():
    
    def adminlogin():
        if(food.adminuser(str(UNent.get()),str(passent.get()))==True):
            messagebox.showinfo("LOGIN", "YOU'RE LOGGED IN")
            root4.destroy()
            adminops()
        else:
            messagebox.showwarning("LOGIN", "USER NOT FOUND")

    
    root4=Tk()
    root4.resizable(0,0)
    root4.geometry('990x660+50+50')
    bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable=Label(root4,image=bgimage)
    bglable.place(x=0,y=0)

    frame=Frame(root4,bg='white')
    frame.place(x=554,y=100)
    heading=Label(frame,text='ADMIN LOGIN',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen')
    heading.grid(row=0,column=0,padx=55,pady=50)

    UNl=Label(frame,text='Username',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    UNl.grid(row=1,column=0,sticky='w',padx=25,pady=10)
    UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    UNent.grid(row=2,column=0)


    passl=Label(frame,text='Password',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    passl.grid(row=3,column=0,sticky='w',padx=25,pady=10)
    passent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen',show='*')
    passent.grid(row=4,column=0)

    loginb=Button(frame,text='LOGIN',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12,command=adminlogin)
    loginb.grid(row=9,column=0,pady=30)
    root.mainloop()
    
def userlogpage():
    def userlogin():
        if(food.loginuser(str(UNent.get()),str(passent.get()))==True):
            
            messagebox.showinfo("LOGIN", "YOU'RE LOGGED IN")
            root6.destroy()
            import menu1
        else:
            messagebox.showwarning("LOGIN", "USER NOT FOUND")

    root6=Tk()
    root6.resizable(0,0)
    root6.geometry('990x660+50+50')
    bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable=Label(root6,image=bgimage)
    bglable.place(x=0,y=0)

    frame=Frame(root6,bg='white')
    frame.place(x=554,y=100)
    heading=Label(frame,text='USER LOGIN',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='lightseagreen')
    heading.grid(row=0,column=0,padx=72,pady=50)

    UNl=Label(frame,text='Username',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    UNl.grid(row=1,column=0,sticky='w',padx=25,pady=10)
    UNent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen')
    UNent.grid(row=2,column=0)


    passl=Label(frame,text='Password',font=('Microsoft Yahei UI light',10,'bold'),bg='white',fg='lightseagreen')
    passl.grid(row=3,column=0,sticky='w',padx=25,pady=10)
    passent=Entry(frame,width=25,font=('Microsoft Yahei UI light',10,'bold'),fg='white',bg='lightseagreen', show='*')
    passent.grid(row=4,column=0)

    loginb=Button(frame,text='LOGIN',font=('Open Sans',16),fg='white',bg='lightseagreen',width=12,command=userlogin)
    loginb.grid(row=5,column=0,pady=30)
    root6.mainloop()
    
    
root=Tk()
root.resizable(0,0)
root.geometry('990x660+50+50')

bgimage=ImageTk.PhotoImage(file='img\\bg.jpg')
bglable=Label(root,image=bgimage)
bglable.place(x=0,y=0)

heading=Label(root,text='WELOCOME',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='lightseagreen')
heading.place(x=610,y=140)
loginb=Button(root,text='LOGIN',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=login)
loginb.place(x=610,y=240)
signupb=Button(root,text='SIGNUP',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=signup)
signupb.place(x=610,y=340)
root.mainloop()
