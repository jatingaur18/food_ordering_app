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

def payment(arr,price):
    
    food.addorder(arr,price)
    
    def cash():
        messagebox.showinfo("LOGIN", "ORDER PLACED")
    
    def creditcard():
        messagebox.showinfo("LOGIN", "PROCEEDING TO PAYMENT GATEWAY")
    
    def debitcard():
        messagebox.showinfo("LOGIN", "PROCEEDING TO PAYMENT GATEWAY")
    
    root.destroy()
    root2=Tk()
    root2.resizable(0,0)
    root2.geometry('990x660+50+50')
    
    bg1image=ImageTk.PhotoImage(file='img\\bg.jpg')
    bglable1=Label(root2,image=bg1image)
    bglable1.place(x=0,y=0)
    
    heading=Label(root2,text='PAYMENT',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='lightseagreen')
    heading.place(x=610,y=140)
    userb=Button(root2,text='CASH',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=cash)
    userb.place(x=573,y=240)
    adminb=Button(root2,text='CREDIT CARD',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=creditcard)
    adminb.place(x=573,y=340)
    adminb=Button(root2,text='DEBIT CARD',font=('Open Sans',16),fg='white',bg='lightseagreen',width=16,command=debitcard)
    adminb.place(x=573,y=440)
    root2.mainloop()

root =tb.Window(themename="superhero")
root.title("MENU")
root.geometry('990x660+50+50')

frame=Frame(root,bg='#266681')
frame.pack(side=LEFT,fill=BOTH,expand=1)

label=tb.Label(frame,text='PLACE YOUR ORDER',font=('Microsoft Yahei UI Light',18,'bold') ,bootstyle="warning" )
label.pack(pady=1)

my_canvas=tb.Canvas(frame,bg='#8155BA',width=10000, height=1000)
my_canvas.place(x=-1,y=79 )

frames=tb.Frame(my_canvas,width=990, height=600)

my_canvas.create_window((0,2), window=frames, anchor="nw")

tp=0
amt=[]
listitem=[]
dic={}
price=[]
order=[]
amt_var=StringVar()
with open('dataset\\dish1.csv', mode ='r')as file:
    csvFile = reader(file)
    for lines in csvFile:
        listitem.append(lines[0])
        price.append(lines[1])
        dic[lines[0]]=IntVar()

def totalprice():
    global dic,tp
    global label2
    i=0
    tp=0
    check=0
    for l in dic:
        quant=dic[l].get()
        tp+=(dic[l].get())*int(price[i])
        amt.append(dic[l])
        if(tp!=check):
            string=l+"-"+str(quant)
            order.append(string)
        i+=1
        check=tp
    label2.pack_forget()

    label2=tb.Label(frames,text=tp,font=('Microsoft Yahei UI Light',18,'bold'),bootstyle="warning")
    label2.grid(row=i,column=2,columnspan=6)

i=0
bgimage=[]
for k in dic:
    k=str(k)
    cur_enterybox='amount' + str(k)
    
    label1=tb.Label(frames,text=i+1,font=('Microsoft Yahei UI Light',18,'bold'),bootstyle="warning")
    label1.grid(row=i,column=0,padx=10,pady=10)

    bgimage.append(ImageTk.PhotoImage(file=f'img\\{k}.jpg'))
    bglable=Label(frames,image=bgimage[i],height=105,width=175)
    bglable.grid(row=i,column=1,pady=70,padx=100)
    
    label2=tb.Label(frames,text=k,font=('Microsoft Yahei UI Light',18,'bold '),bootstyle="warning")
    label2.grid(row=i,column=2,padx=100,pady=0)
    
    
    label3=tb.Label(frames,text=price[i],font=('Microsoft Yahei UI Light',18,'bold'),bootstyle="warning")
    label3.grid(row=i,column=3,padx=100,pady=0)
    amt.append(0)
    
    cur_enterybox = tb.Entry(frames , width =8 , textvariable=dic[k])
    cur_enterybox.grid(row=i,column=4,padx=100,pady=0)
    i+=1

scroll=ttk.Scrollbar(root,orient=VERTICAL, command=my_canvas.yview,bootstyle="danger round")
scroll.pack(side="right" ,fill="y")
my_canvas.config(yscrollcommand=scroll.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=(0,0,990,2000)))


but=tb.Button(frames, text="TOTAL PRICE" ,width=20 ,command=totalprice)
but.grid(row=i,column=0,columnspan=6)
label2=tb.Label(frames,text=tp,font=('Microsoft Yahei UI Light',18,'bold'),bootstyle="warning")
label2.grid(row=i,column=2,columnspan=6)

but=tb.Button(frames, text="PAY" ,width=20 ,command=lambda: payment(order,price))
but.grid(row=i,column=6,columnspan=6)

root.mainloop()