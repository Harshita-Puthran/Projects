from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox
import random
import time
import requests

#functions
def reset():
    textReceipt.delete(1.0,END)
    e_cake.set('0')
    e_roll.set('0')
    e_hroll.set('0')
    e_salad.set('0')
    e_sand.set('0')
    e_cros.set('0')
    e_froll.set('0')
    e_kebab.set('0')
    e_Puff.set('0')
    e_Fries.set('0')
    e_pizza.set('0')
    e_Tea.set('0')
    e_Peachtea.set('0')
    e_coffee.set('0')
    e_coldcof.set('0')
    e_choc.set('0')
    e_milkchoc.set('0')
    e_americo.set('0')
    e_lemon.set('0')
    e_moji.set('0')
    e_smoth.set('0')
    e_shake.set('0')

    textcake.config(state=DISABLED)
    textroll.config(state=DISABLED)
    texthroll.config(state=DISABLED)
    textsalad.config(state=DISABLED)
    textsand.config(state=DISABLED)
    textcros.config(state=DISABLED)
    textfroll.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textPuff.config(state=DISABLED)

    textFries.config(state=DISABLED)
    textpizza.config(state=DISABLED)
    textTea.config(state=DISABLED)
    textPeachtea.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textcoldcof.config(state=DISABLED)
    textchoc.config(state=DISABLED)
    textmilkchoc.config(state=DISABLED)
    textamerico.config(state=DISABLED)

    textlemon.config(state=DISABLED)
    textmoji.config(state=DISABLED)
    textsmoth.config(state=DISABLED)
    textshake.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    


    

def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:

        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='lijzt467wT8vUqxsSGDmXVBIkdnoeph9NugOfQW5YaLHcR10PrX4HIMGCFLBxW8QR2qVpvntrgi1YeTD'
            url='https://www.fast2sms.com/dev/bulk'
            #url='https://www.fast2sms.com/dashboard/dlt-intro'
            params={
                'authorization':auth,
                    'message':message,
                    'numbers':number,
                    'sender-id':'FSTSMS',
                    'route':'p',
                    'language':'english'
            }
            requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')


        

    #root2=tk.Tk()
        logoImage=tk.PhotoImage(file="C:/Users/Harshita/Downloads/sender.png")
        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='aquamarine4')
        root2.geometry('485x620+50+50')

        #logoImage=PhotoImage(file='sender.png')
        label=Label(root2,image=logoImage,bg='aquamarine4')
        label.pack(pady=5)

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='aquamarine4',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='aquamarine4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceoffood}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
            
        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                            ,command=send_msg)
        sendButton.pack(pady=5)
        
        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')




def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_cake.get()!='0':
            textReceipt.insert(END,f'Dark Cherry Cheesecake:\t\t\t{int(e_cake.get()) * 200}\n\n')
        if e_roll.get()!='0':
            textReceipt.insert(END,f'Strawberry Cream Roll :\t\t\t{int(e_roll.get()) * 120}\n\n')
        if e_hroll.get()!='0':
            textReceipt.insert(END,f'Hotdog Roll :\t\t\t{int(e_hroll.get()) * 150}\n\n')
        if e_salad.get()!='0':
            textReceipt.insert(END,f'Salad :\t\t\t{int(e_salad.get()) * 100}\n\n')
        if e_sand.get()!='0':
            textReceipt.insert(END,f'Chutney Sandwhich :\t\t\t{int(e_sand.get()) * 90}\n\n')  
        if e_cros.get()!='0':
            textReceipt.insert(END,f'Crossaint Sandwhich :\t\t\t{int(e_cros.get()) * 60}\n\n')
        if e_froll.get()!='0':
            textReceipt.insert(END,f'Falafel Roll :\t\t\t{int(e_froll.get()) * 180}\n\n')
        if e_kebab.get()!='0':
            textReceipt.insert(END,f'Veg Kebab :\t\t\t{int(e_kebab.get()) * 100}\n\n')
        if e_Puff.get()!='0':
            textReceipt.insert(END,f'Puff :\t\t\t{int(e_Puff.get()) * 50}\n\n')
        if e_Fries.get()!='0':
            textReceipt.insert(END,f'Peri-Peri Fries :\t\t\t{int(e_Fries.get()) * 70}\n\n')
        if e_pizza.get()!='0':
            textReceipt.insert(END,f'Farmhouse pizza :\t\t\t{int(e_pizza.get()) * 180}\n\n')

        if e_Tea.get()!='0':
            textReceipt.insert(END,f'Tea :\t\t\t{int(e_Tea.get()) * 50}\n\n')
        if e_Peachtea.get()!='0':
            textReceipt.insert(END,f'Peach Iced Tea :\t\t\t{int(e_Peachtea.get()) * 80}\n\n')
        if e_coffee.get()!='0':
            textReceipt.insert(END,f'Coffee :\t\t\t{int(e_roll.get()) * 60}\n\n')
        if e_coldcof.get()!='0':
            textReceipt.insert(END,f'Cold Coffee :\t\t\t{int(e_coldcof.get()) * 65}\n\n')
        if e_choc.get()!='0':
            textReceipt.insert(END,f'Hot Chocolate :\t\t\t{int(e_choc.get()) * 70}\n\n') 
        if e_milkchoc.get()!='0':
            textReceipt.insert(END,f'Chocolate Milkshake :\t\t\t{int(e_milkchoc.get()) * 80}\n\n')
        if e_americo.get()!='0':
            textReceipt.insert(END,f'Americano:\t\t\t{int(e_roll.get()) * 90}\n\n')
        if e_lemon.get()!='0':
            textReceipt.insert(END,f'Lemonade :\t\t\t{int(e_lemon.get()) * 70}\n\n') 
        if e_moji.get()!='0':
            textReceipt.insert(END,f'Mojito :\t\t\t{int(e_moji.get()) * 100}\n\n') 
        if e_smoth.get()!='0':
            textReceipt.insert(END,f'Mango Smoothie :\t\t\t{int(e_smoth.get()) * 90}\n\n')
        if e_shake.get()!='0':
            textReceipt.insert(END,f'Vanilla Milkshake :\t\t\t{int(e_shake.get()) * 80}\n\n')  

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost of food:\t\t\t{priceoffood}Rs\n\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost of Drinks:\t\t\t{priceofDrinks}Rs\n\n')

        textReceipt.insert(END,f'Sub Total:\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END,f'Service Tax:\t\t\t{50}Rs\n\n')
        textReceipt.insert(END,f'Total Cost:\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')
    else:
        messagebox.showerror('Error','No item is selected')    


    

                  

def totalcost():
    global priceoffood,priceofDrinks,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0:

        item1=int(e_cake.get())
        item2=int(e_roll.get())
        item3=int(e_hroll.get())
        item4=int(e_salad.get())
        item5=int(e_sand.get()) 
        item6=int(e_cros.get()) 
        item7=int(e_froll.get()) 
        item8=int(e_kebab.get()) 
        item9=int(e_Puff.get()) 
        item10=int(e_Fries.get()) 
        item11=int(e_pizza.get()) 
        item12=int(e_Tea.get()) 
        item13=int(e_Peachtea.get()) 
        item14=int(e_coffee.get())
        item15=int(e_coldcof.get())
        item16=int(e_choc.get()) 
        item17=int(e_milkchoc.get())
        item18=int(e_americo.get())  
        item19=int(e_lemon.get()) 
        item20=int(e_moji.get()) 
        item21=int(e_smoth.get())
        item22=int(e_shake.get())  

        priceoffood=(item1*200)+(item2*120)+(item3*150)+(item4*100)+(item5*90)+(item6*60)+(item7*180)\
        +(item8*100)+(item9*50)+(item10*70)+(item11*180)

        priceofDrinks=(item12*50)+(item13*80)+(item14*60)+(item15*65)+(item16*70)+(item17*80)+(item18*90)\
        +(item19*70)+(item20*100)+(item21*90)+(item22*80)

        costoffoodvar.set(str(priceoffood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')

        subtotalofItems=priceoffood+priceofDrinks
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set(str('50 Rs'))

        totalcost=subtotalofItems+50
        totalcostvar.set(str(totalcost)+' Rs')
    else:
        messagebox.showerror('Error','No Item is selected')

      
 






def cake():
    if var1.get()==1:
        textcake.config(state=NORMAL)
        textcake.delete(0,END)
        textcake.focus()
    else:
        textcake.config(state=DISABLED)
        e_cake.set('0')

def roll():
    if var2.get()==1:
        textroll.config(state=NORMAL)
        textroll.delete(0,END)
        textroll.focus()
    else:
        textroll.config(state=DISABLED)
        e_roll.set('0')

def hroll():
    if var3.get()==1:
        texthroll.config(state=NORMAL)
        texthroll.delete(0,END)
        texthroll.focus()
    else:
        texthroll.config(state=DISABLED)
        e_hroll.set('0')

def salad():
    if var4.get()==1:
        textsalad.config(state=NORMAL)
        textsalad.delete(0,END)
        textsalad.focus()
    else:
        textsalad.config(state=DISABLED)
        e_salad.set('0')

def sand():
    if var5.get()==1:
        textsand.config(state=NORMAL)
        textsand.delete(0,END)
        textsand.focus()
    else:
        textsand.config(state=DISABLED)
        e_sand.set('0')

def cros():
    if var6.get()==1:
        textcros.config(state=NORMAL)
        textcros.delete(0,END)
        textcros.focus()
    else:
        textcros.config(state=DISABLED)
        e_cros.set('0')

def froll():
    if var7.get()==1:
        textfroll.config(state=NORMAL)
        textfroll.delete(0,END)
        textfroll.focus()
    else:
        textfroll.config(state=DISABLED)
        e_froll.set('0')

def kebab():
    if var8.get()==1:
        textkebab.config(state=NORMAL)
        textkebab.delete(0,END)
        textkebab.focus()
    else:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')

def Puff():
    if var9.get()==1:
        textPuff.config(state=NORMAL)
        textPuff.delete(0,END)
        textPuff.focus()
    else:
        textPuff.config(state=DISABLED)
        e_Puff.set('0')

def Fries():
    if var10.get()==1:
        textFries.config(state=NORMAL)
        textFries.delete(0,END)
        textFries.focus()
    else:
        textFries.config(state=DISABLED)
        e_Fries.set('0')

def pizza():
    if var11.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete(0,END)
        textpizza.focus()
    else:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')

def Tea():
    if var12.get()==1:
        textTea.config(state=NORMAL)
        textTea.delete(0,END)
        textPeachtea.focus()
    else:
        textTea.config(state=DISABLED)
        e_Tea.set('0')

def Peachtea():
    if var13.get()==1:
        textPeachtea.config(state=NORMAL)
        textPeachtea.delete(0,END)
        textPeachtea.focus()
    else:
        textPeachtea.config(state=DISABLED)
        e_Peachtea.set('0')

def coffee():
    if var14.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def coldcof():
    if var15.get()==1:
        textcoldcof.config(state=NORMAL)
        textcoldcof.delete(0,END)
        textcoldcof.focus()
    else:
        textcoldcof.config(state=DISABLED)
        e_coldcof.set('0')

def choc():
    if var16.get()==1:
        textchoc.config(state=NORMAL)
        textchoc.delete(0,END)
        textchoc.focus()
    else:
        textchoc.config(state=DISABLED)
        e_choc.set('0')

def milkchoc():
    if var17.get()==1:
        textmilkchoc.config(state=NORMAL)
        textmilkchoc.delete(0,END)
        textmilkchoc.focus()
    else:
        textmilkchoc.config(state=DISABLED)
        e_milkchoc.set('0')

def americo():
    if var18.get()==1:
        textamerico.config(state=NORMAL)
        textamerico.delete(0,END)
        textamerico.focus()
    else:
        textamerico.config(state=DISABLED)
        e_americo.set('0')

def lemon():
    if var19.get()==1:
        textlemon.config(state=NORMAL)
        textlemon.delete(0,END)
        textlemon.focus()
    else:
        textlemon.config(state=DISABLED)
        e_lemon.set('0')

def moji():
    if var20.get()==1:
        textmoji.config(state=NORMAL)
        textmoji.delete(0,END)
        textmoji.focus()
    else:
        textmoji.config(state=DISABLED)
        e_moji.set('0')

def smoth():
    if var21.get()==1:
        textsmoth.config(state=NORMAL)
        textsmoth.delete(0,END)
        textsmoth.focus()
    else:
        textsmoth.config(state=DISABLED)
        e_smoth.set('0')

def shake():
    if var22.get()==1:
        textshake.config(state=NORMAL)
        textshake.delete(0,END)
        textshake.focus()
    else:
        textshake.config(state=DISABLED)
        e_shake.set('0')





root=Tk()
root.geometry('1350x750+0+0')
root.resizable(0,0)
root.title('Restaurant Management System')
root.config(bg='aquamarine3')
topFrame=Frame(root,bd=10,relief=RIDGE)
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='CAFE MANAGEMENT SYSTEM',font=('arial',30,'bold'),
                 fg='azure1',bd=9,bg='aquamarine4',width=51)
labelTitle.grid(row=0,column=0)
#frames
menuFrame=Frame(root,bd=10,relief=RIDGE)
menuFrame.pack(side=LEFT)
costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='aquamarine4')
costFrame.pack(side=BOTTOM)
foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='black')
foodFrame.pack(side=LEFT)
drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE)
drinksFrame.pack(side=LEFT)
occupFrame=LabelFrame(menuFrame,text='Occupancy',font=('arial',19,'bold'),bd=10,relief=RIDGE)
occupFrame.pack(side=LEFT)
rightFrame=Frame(root,bd=15,relief=RIDGE,bg='aquamarine4')
rightFrame.pack(side=RIGHT)
calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='aquamarine4')
calculatorFrame.pack()
receiptFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='aquamarine4')
receiptFrame.pack()
buttonFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='aquamarine4')
buttonFrame.pack()
#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()

e_cake=StringVar()
e_roll=StringVar()
e_hroll=StringVar()
e_salad=StringVar()
e_sand=StringVar()
e_cros=StringVar()
e_froll=StringVar()
e_kebab=StringVar()
e_Puff=StringVar()
e_Fries=StringVar()
e_pizza=StringVar()
e_Tea=StringVar()
e_Peachtea=StringVar()
e_coffee=StringVar()
e_coldcof=StringVar()
e_choc=StringVar()
e_milkchoc=StringVar()
e_americo=StringVar()
e_lemon=StringVar()
e_moji=StringVar()
e_smoth=StringVar()
e_shake=StringVar()

e_cake.set('0')
e_roll.set('0')
e_hroll.set('0')
e_salad.set('0')
e_sand.set('0')
e_cros.set('0')
e_froll.set('0')
e_kebab.set('0')
e_Puff.set('0')
e_Fries.set('0')
e_pizza.set('0')
e_Tea.set('0')
e_Peachtea.set('0')
e_coffee.set('0')
e_coldcof.set('0')
e_choc.set('0')
e_milkchoc.set('0')
e_americo.set('0')
e_lemon.set('0')
e_moji.set('0')
e_smoth.set('0')
e_shake.set('0')

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()




#food
cake=Checkbutton(foodFrame,text='Dark Cherry Cheesecake',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var1,command=cake)
cake.grid(row=0,column=0,sticky=W)

roll=Checkbutton(foodFrame,text='Strawberry Cream Roll',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var2,command=roll)
roll.grid(row=1,column=0,sticky=W)

hroll=Checkbutton(foodFrame,text='Hotdog Roll',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var3,command=hroll)
hroll.grid(row=2,column=0,sticky=W)

salad=Checkbutton(foodFrame,text='Fruit Salad',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var4,command=salad)
salad.grid(row=3,column=0,sticky=W)

sand=Checkbutton(foodFrame,text='Chutney Sandwhich',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var5,command=sand)
sand.grid(row=4,column=0,sticky=W)

cros=Checkbutton(foodFrame,text='Crossaint Sandwhich',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var6,command=cros)
cros.grid(row=5,column=0,sticky=W)

froll=Checkbutton(foodFrame,text='Falafel Roll',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var7,command=froll)
froll.grid(row=6,column=0,sticky=W)

kebab=Checkbutton(foodFrame,text='Veg Kebab',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var8,command=kebab)
kebab.grid(row=7,column=0,sticky=W)

Puff=Checkbutton(foodFrame,text='Paneer Puff',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var9,command=Puff)
Puff.grid(row=8,column=0,sticky=W)

Fries=Checkbutton(foodFrame,text='Peri Peri Fries',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var10,command=Fries)
Fries.grid(row=9,column=0,sticky=W)

pizza=Checkbutton(foodFrame,text='Farmhouse Pizza',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var11,command=pizza)
pizza.grid(row=10,column=0,sticky=W)

#Entry fidgets for food items
textcake=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cake)
textcake.grid(row=0,column=1)
textroll=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roll)
textroll.grid(row=1,column=1)
texthroll=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_hroll)
texthroll.grid(row=2,column=1)
textsalad=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_salad)
textsalad.grid(row=3,column=1)
textsand=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sand)
textsand.grid(row=4,column=1)
textcros=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cros)
textcros.grid(row=5,column=1)
textfroll=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_froll)
textfroll.grid(row=6,column=1)
textkebab=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kebab)
textkebab.grid(row=7,column=1)
textPuff=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Puff)
textPuff.grid(row=8,column=1)
textFries=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Fries)
textFries.grid(row=9,column=1)
textpizza=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizza)
textpizza.grid(row=10,column=1)
#DRINKS
Tea=Checkbutton(drinksFrame,text='Tea',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var12,command=Tea)
Tea.grid(row=0,column=1,sticky=W)

Peachtea=Checkbutton(drinksFrame,text='Peach Iced Tea',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var13,command=Peachtea)
Peachtea.grid(row=1,column=1,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var14,command=coffee)
coffee.grid(row=2,column=1,sticky=W)

coldcof=Checkbutton(drinksFrame,text='Cold Coffee',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var15,command=coldcof)
coldcof.grid(row=3,column=1,sticky=W)

choc=Checkbutton(drinksFrame,text='Hot Choclate',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var16,command=choc)
choc.grid(row=4,column=1,sticky=W)

milkchoc=Checkbutton(drinksFrame,text='Chocolate Milkshake',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var17,command=milkchoc)
milkchoc.grid(row=5,column=1,sticky=W)

americo=Checkbutton(drinksFrame,text='Americano',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var18,command=americo)
americo.grid(row=6,column=1,sticky=W)

lemon=Checkbutton(drinksFrame,text='Lemonade',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var19,command=lemon)
lemon.grid(row=7,column=1,sticky=W)

moji=Checkbutton(drinksFrame,text='Mojito',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var20,command=moji)
moji.grid(row=8,column=1,sticky=W)

smoth=Checkbutton(drinksFrame,text='Mango Smoothie',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var21,command=smoth)
smoth.grid(row=9,column=1,sticky=W)

shake=Checkbutton(drinksFrame,text='Vanilla Milkshake',font=('Italic',10,'bold'),onvalue=1,
offvalue=0,variable=var22,command=shake)
shake.grid(row=10,column=1,sticky=W)

#TEXT
textTea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Tea)
textTea.grid(row=0,column=2)
textPeachtea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Peachtea)
textPeachtea.grid(row=1,column=2)
textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=2,column=2)
textcoldcof=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coldcof)
textcoldcof.grid(row=3,column=2)
textchoc=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choc)
textchoc.grid(row=4,column=2)
textmilkchoc=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_milkchoc)
textmilkchoc.grid(row=5,column=2)
textamerico=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_americo)
textamerico.grid(row=6,column=2)
textlemon=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lemon)
textlemon.grid(row=7,column=2)
textmoji=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_moji)
textmoji.grid(row=8,column=2)
textsmoth=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_smoth)
textsmoth.grid(row=9,column=2)
textshake=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shake)
textshake.grid(row=10,column=2)

#occup
#occup
#occup
class TableOccupancyGUI:
    def __init__(self, master):
        self.master = master
        #self.master.title("Table Occupancy")
       
        self.tables = {}
       
        # Create buttons for tables
        for table_num in range(1, 21):  # Assuming 10 tables
            self.tables[table_num] = tk.Button(master, text=f"Table {table_num}\nVacant",
                                               command=lambda num=table_num: self.toggle_occupancy(num))
            self.tables[table_num].grid(row=(table_num-1)//3, column=(table_num-1)%3, padx=5, pady=5)

    def toggle_occupancy(self, table_num):
        # Toggle the occupancy of the selected table
        if self.tables[table_num]['text'] == f"Table {table_num}\nVacant":
            self.tables[table_num]['text'] = f"Table {table_num}\nOccupied"
            self.tables[table_num].config(bg="red")  # Change button color
        else:
            self.tables[table_num]['text'] = f"Table {table_num}\nVacant"
            self.tables[table_num].config(bg="SystemButtonFace")  # Restore button color


def main():
    #root = Tk()
    #app = TableOccupancyGUI(root)
    app = LabelFrame(menuFrame, text='Occupancy', font=('arial', 19, 'bold'),bd=10, relief=RIDGE)
    app.pack(side=tk.LEFT)
    occupancy_gui = TableOccupancyGUI(app)

if __name__ == "__main__":
    main()

#costlabels and entry field
labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='aquamarine4',fg='white')
labelCostofFood.grid(row=0, column=0)
textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1)
 
labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='aquamarine4',fg='white')
labelCostofDrinks.grid(row=1, column=0)
textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='aquamarine4',fg='white')
labelSubTotal.grid(row=0, column=2)
textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='aquamarine4',fg='white')
labelServiceTax.grid(row=1, column=2)
textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='aquamarine4',fg='white')
labelTotalCost.grid(row=2, column=2)
textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3,padx=41)

#buttons
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='aquamarine4',bd=3
                   ,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='aquamarine4',bd=3,
                     padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='aquamarine4',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='aquamarine4',bd=3,padx=5
                   ,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='aquamarine4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

#text 
textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0,)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                  bd=6,width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='aquamarine4',bg='white',
               bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='aquamarine4',bg='white',
               bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                   bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='aquamarine4',bg='white',
               bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='aquamarine4',bg='white',
               bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                  bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                   bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                 bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
               bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='aquamarine4',
                 bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)




















        










root.mainloop()
