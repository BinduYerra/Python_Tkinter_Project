from tkinter import *
from tkinter import filedialog,messagebox
#import random
import time
#import requests

#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_dips.set('0')
    e_chicken.set('0')
    e_bavarian.set('0')
    e_pepperoni.set('0')
    e_mac.set('0')
    e_pretzel.set('0')
    e_mozzerella.set('0')
    e_spinach.set('0')

    e_singlecone.set('0')
    e_doublecone.set('0')
    e_sundae.set('0')
    e_signature.set('0')

    e_smallsoda.set('0')
    e_sodatogo.set('0')
    e_largesoda.set('0')
    e_soday.set('0')
    e_milkshake.set('0')

    textdips.config(state=DISABLED)
    textsinglecone.config(state=DISABLED)
    textbavarian.config(state=DISABLED)
    textpepperoni.config(state=DISABLED)
    textmac.config(state=DISABLED)
    textpretzel.config(state=DISABLED)
    textmozzerella.config(state=DISABLED)
    textspinach.config(state=DISABLED)

    textsinglecone.config(state=DISABLED)
    textdoublecone.config(state=DISABLED)
    textsundae.config(state=DISABLED)
    textsignature.config(state=DISABLED)

    textsmallsoda.config(state=DISABLED)
    textsodatogo.config(state=DISABLED)
    textlargesoda.config(state=DISABLED)
    textsoday.config(state=DISABLED)
    textmilkshake.config(state=DISABLED)

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

    totalcostofappetizers.set('')
    totalcostoficecreamdesserts.set('')
    totalcostofbeverages.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


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
    global date
    if totalcostofappetizers.get() != '' or totalcostoficecreamdesserts.get() != '' or totalcostofbeverages.get() != '':
        textReceipt.delete(1.0,END)
        date = time.strftime('%m/%d/%Y')
        textReceipt.insert(END,'Receipt Ref: 5\t\t\t'+ date +'\n')
        textReceipt.insert(END,'*************************************\n')
        textReceipt.insert(END,'Name of food \t\t\t\t Price\n')
        textReceipt.insert(END,'*************************************\n')

        if e_dips.get()!='0':
            quantity = int(e_dips.get())
            textReceipt.insert(END, f'Dips and Chips\t\tx{quantity}\t\t${round(float(e_dips.get())*3.00,2)}\n\n')

        if e_chicken.get()!='0':
            quantity = int(e_chicken.get())
            textReceipt.insert(END,f'Chicken Fries\t\tx{quantity}\t\t${round(float(e_chicken.get())*3.00,2)}\n\n')

        if e_bavarian.get()!='0':
            quantity = int(e_bavarian.get())
            textReceipt.insert(END,f'Bavarian Pretzel Sticks\t\tx{quantity}\t\t${round(float(e_bavarian.get())*4.00,2)}\n\n')

        if e_pepperoni.get() != '0':
            quantity = int(e_pepperoni.get())
            textReceipt.insert(END, f'Pepperoni Pizza Sticks\t\tx{quantity}\t\t${round(float(e_pepperoni.get())* 4.00,2)}\n\n')

        if e_mac.get() != '0':
            quantity = int(e_mac.get())
            textReceipt.insert(END, f'Mac & Cheese Bites\t\tx{quantity}\t\t${round(float(e_mac.get()) * 4.00,2)}\n\n')

        if e_pretzel.get() != '0':
            quantity = int(e_pretzel.get())
            textReceipt.insert(END, f'Pretzel Hot Dogs\t\tx{quantity}\t\t${round(float(e_pretzel.get())* 5.00,2)}\n\n')

        if e_mozzerella.get() != '0':
            quantity = int(e_mozzerella.get())
            textReceipt.insert(END, f'Mozzerella Sticks\t\tx{quantity}\t\t${round(float(e_mozzerella.get())* 5.00,2)}\n\n')

        if e_spinach.get() != '0':
            quantity = int(e_spinach.get())
            textReceipt.insert(END, f'Spinach & Artichoke Dip\t\tx{quantity}\t\t${round(float(e_spinach.get()) * 5.00,2)}\n\n')

        if e_singlecone.get() != '0':
            quantity = int(e_singlecone.get())
            textReceipt.insert(END, f'Single Cone/Cup\t\tx{quantity}\t\t${round(float(e_singlecone.get()) * 2.50,2)}\n\n')

        if e_doublecone.get() != '0':
            quantity = int(e_doublecone.get())
            textReceipt.insert(END, f'Double Cone/ Cup\t\tx{quantity}\t\t${round(float(e_doublecone.get())* 3.50,2)}\n\n')

        if e_sundae.get() != '0':
            quantity = int(e_sundae.get())
            textReceipt.insert(END, f'Sundae\t\tx{quantity}\t\t${round(float(e_sundae.get())* 4.00,2)}\n\n')

        if e_signature.get() != '0':
            quantity = int(e_signature.get())
            textReceipt.insert(END, f'Signature Desserts\t\tx{quantity}\t\t${round(float(e_signature.get()) * 5.00,2)}\n\n')

        if e_smallsoda.get() != '0':
            quantity = int(e_smallsoda.get())
            textReceipt.insert(END, f'Small Soda\t\tx{quantity}\t\t${round(float(e_smallsoda.get()) * 1.00,2)}\n\n')

        if e_sodatogo.get() != '0':
            quantity = int(e_sodatogo.get())
            textReceipt.insert(END, f'Soda To Go\t\tx{quantity}\t\t${round(float(e_sodatogo.get()) * 1.50,2)}\n\n')

        if e_largesoda.get() != '0':
            quantity = int(e_largesoda.get())
            textReceipt.insert(END, f'Large Soda\t\tx{quantity}\t\t${round(float(e_largesoda.get()) * 2.00,2)}\n\n')

        if e_soday.get() != '0':
            quantity = int(e_soday.get())
            textReceipt.insert(END, f'Soday StringVar\t\tx{quantity}\t\t${round(float(e_soday.get()) * 3.50,2)}\n\n')

        if e_milkshake.get() != '0':
            quantity = int(e_milkshake.get())
            textReceipt.insert(END, f'Milkshake/ Smoothie:\t\tx{quantity}\t\t${round(float(e_milkshake.get()) * 4.75,2)}\n\n')
   

        textReceipt.insert(END,'*************************************\n')

        textReceipt.insert(END, f'Sub Total\t\t\t${round(subtotalofItems,2)}\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t${round(0.0625*subtotalofItems,2)}\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t${round(subtotalofItems+(0.0625*subtotalofItems),2)}\n\n')
        textReceipt.insert(END,'*************************************\n')
        textReceipt.insert(END,f'Have a Nice Day!!Please Visit Again\n\n')
        textReceipt.insert(END,f'Order Online\nwww.areyerradrivein.com\n\n')
    else:
        messagebox.showerror('Error','No Item Is selected')


def totalcost():
    global priceofappetizers,priceofdesserts,priceofbeverages,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0:

        item1 = int(e_dips.get())
        item2 = int(e_chicken.get())
        item3 = int(e_bavarian.get())
        item4 = int(e_pepperoni.get())
        item5 = int(e_mac.get())
        item6 = int(e_pretzel.get())
        item7 = int(e_mozzerella.get())
        item8 = int(e_spinach.get())

        item9 = int(e_singlecone.get())
        item10 = int(e_doublecone.get())
        item11 = int(e_sundae.get())
        item12 = int(e_signature.get())

        item13 = int(e_smallsoda.get())
        item14 = int(e_sodatogo.get())
        item15 = int(e_largesoda.get())
        item16 = int(e_soday.get())
        item17 = int(e_milkshake.get())

        priceofappetizers=(float(item1)*3.00)+(float(item2)*3.00)+(float(item3)*4.00)+(float(item4)*4.00)+ (float(item5)*4.00) + (float(item6) * 5.00) + (float(item7) * 5.00) + (float(item8) * 5.00) 

        priceofdesserts = (float(item9) * 2.50) + (float(item10) *3.50)+(float(item11) *4.00)+ (float(item12) * 5.00) 

        priceofbeverages = (float(item13) * 1.00) + (float(item14) * 1.50) + (float(item15) * 2.00)  + (float(item16 * 2.5)) + (float(item17) * 4.75) 

        totalcostofappetizers.set(str(priceofappetizers)+ '$')
        totalcostoficecreamdesserts.set(str(priceofdesserts)+ '$')
        totalcostofbeverages.set(str(priceofbeverages)+ '$')

        subtotalofItems = round(priceofappetizers + priceofdesserts + priceofbeverages,2)
        subtotalvar.set(str(subtotalofItems)+'$')

        servicetaxvar.set(str(round(0.0625 * float(subtotalofItems), 2))+ '$')

        tottalcost = round(subtotalofItems + (0.0625*float(subtotalofItems)),2)
        totalcostvar.set(str(tottalcost)+'$')

    else:
        messagebox.showerror('Error','No Item Is selected')



def dips():
    if var1.get()==1:
        textdips.config(state=NORMAL)
        textdips.delete(0,END)
        textdips.focus()
    elif var1.get() == 0:
        textdips.config(state=DISABLED)
        e_dips.set('0')

def chicken():
    if var2.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    elif var2.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def bavarian():
    if var3.get()==1:
        textbavarian.config(state=NORMAL)
        textbavarian.delete(0,END)
        textbavarian.focus()

    elif var3.get() == 0:
        textbavarian.config(state=DISABLED)
        e_bavarian.set('0')

def pepperoni():
    if var4.get() == 1:
        textpepperoni.config(state=NORMAL)
        textpepperoni.focus()
        textpepperoni.delete(0, END)
    elif var4.get() == 0:
        textpepperoni.config(state=DISABLED)
        e_pepperoni.set('0')


def mac():
    if var5.get() == 1:
        textmac.config(state=NORMAL)
        textmac.focus()
        textmac.delete(0, END)
    elif var5.get() == 0:
        textmac.config(state=DISABLED)
        e_mac.set('0')


def pretzel():
    if var6.get() == 1:
        textpretzel.config(state=NORMAL)
        textpretzel.focus()
        textpretzel.delete(0, END)
    elif var6.get() == 0:
        textpretzel.config(state=DISABLED)
        e_pretzel.set('0')


def mozzerella():
    if var7.get() == 1:
        textmozzerella.config(state=NORMAL)
        textmozzerella.focus()
        textmozzerella.delete(0, END)
    elif var7.get() == 0:
        textmozzerella.config(state=DISABLED)
        e_mozzerella.set('0')


def spinach():
    if var8.get() == 1:
        textspinach.config(state=NORMAL)
        textspinach.focus()
        textspinach.delete(0, END)
    elif var8.get() == 0:
        textspinach.config(state=DISABLED)
        e_spinach.set('0')


def singlecone():
    if var9.get() == 1:
        textsinglecone.config(state=NORMAL)
        textsinglecone.focus()
        textsinglecone.delete(0, END)
    elif var9.get() == 0:
        textsinglecone.config(state=DISABLED)
        e_singlecone.set('0')


def doublecone():
    if var10.get() == 1:
        textdoublecone.config(state=NORMAL)
        textdoublecone.focus()
        textdoublecone.delete(0, END)
    elif var10.get() == 0:
        textdoublecone.config(state=DISABLED)
        e_doublecone.set('0')


def sundae():
    if var11.get() == 1:
        textsundae.config(state=NORMAL)
        textsundae.focus()
        textsundae.delete(0, END)
    elif var11.get() == 0:
        textsundae.config(state=DISABLED)
        e_sundae.set('0')


def signature():
    if var12.get() == 1:
        textsignature.config(state=NORMAL)
        textsignature.focus()
        textsignature.delete(0, END)
    elif var12.get() == 0:
        textsignature.config(state=DISABLED)
        e_signature.set('0')


def smallsoda():
    if var13.get() == 1:
        textsmallsoda.config(state=NORMAL)
        textsmallsoda.focus()
        textsmallsoda.delete(0, END)
    elif var13.get() == 0:
        textsmallsoda.config(state=DISABLED)
        e_smallsoda.set('0')


def sodatogo():
    if var14.get() == 1:
        textsodatogo.config(state=NORMAL)
        textsodatogo.focus()
        textsodatogo.delete(0, END)
    elif var14.get() == 0:
        textsodatogo.config(state=DISABLED)
        e_sodatogo.set('0')

def largesoda():
    if var15.get() == 1:
        textlargesoda.config(state=NORMAL)
        textlargesoda.focus()
        textlargesoda.delete(0, END)
    elif var15.get() == 0:
        textlargesoda.config(state=DISABLED)
        e_largesoda.set('0')

def soday():
    if var16.get() == 1:
        textsoday.config(state=NORMAL)
        textsoday.focus()
        textsoday.delete(0, END)
    elif var16.get() == 0:
        textsoday.config(state=DISABLED)
        e_soday.set('0')


def milkshake():
    if var17.get() == 1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.focus()
        textmilkshake.delete(0, END)
    elif var17.get() == 0:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set('0')


root=Tk()

root.geometry('1500x700+0+0')

root.resizable(0,0)

root.title('Are Yerra Date Patel Restaurant')

root.config(bg='grey17')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='grey17')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Are Yerra Drive In',font=('Loma',30,'bold', 'italic'),fg='midnight blue',bd=9, bg='orange',width=61)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='grey17')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=10,relief=RIDGE,bg='grey17')
costFrame.pack(side=BOTTOM)

appetizerFrame=LabelFrame(menuFrame,text='Appetizers',font=('Perpetua',19,'bold'),bd=10,relief=RIDGE,fg='orange',bg='grey17')
appetizerFrame.pack(side=LEFT)

dessertFrame=LabelFrame(menuFrame,text='Icecream & Desserts',font=('Perpetua',19,'bold'),bd=10,relief=RIDGE,fg='orange',bg='grey17',pady=80)
dessertFrame.pack(side=LEFT)

beverageFrame=LabelFrame(menuFrame,text='Beverages',font=('Perpetua',19,'bold'),bd=10,relief=RIDGE,fg='orange',bg='grey17',pady=60)
beverageFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='burlywood3',pady=60)
rightFrame.pack(side= RIGHT)

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='burlywood3',pady=5)
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='burlywood3')
buttonFrame.pack()


#Variables

var1 = IntVar()
var2 = IntVar()
var3 =IntVar()
var4 =IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()

e_dips=StringVar()
e_chicken=StringVar()
e_bavarian= StringVar()
e_pepperoni = StringVar()
e_mac = StringVar()
e_pretzel = StringVar()
e_mozzerella = StringVar()
e_spinach = StringVar()


e_singlecone = StringVar()
e_doublecone = StringVar()
e_sundae = StringVar()
e_signature = StringVar()

e_smallsoda = StringVar()
e_sodatogo = StringVar()
e_largesoda = StringVar()
e_soday = StringVar()
e_milkshake = StringVar()

totalcostofappetizers = StringVar()
totalcostoficecreamdesserts = StringVar()
totalcostofbeverages = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_dips.set('0')
e_chicken.set('0')
e_bavarian.set('0')
e_pepperoni.set('0')
e_mac.set('0')
e_pretzel.set('0')
e_mozzerella.set('0')
e_spinach.set('0')

e_singlecone.set('0')
e_doublecone.set('0')
e_sundae.set('0')
e_signature.set('0')

e_smallsoda.set('0')
e_sodatogo.set('0')
e_largesoda.set('0')
e_soday.set('0')
e_milkshake.set('0')

#Appetizers

dips = Checkbutton(appetizerFrame,text='Dips and Chips',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var1,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                 ,command=dips)
dips.grid(row=0,column=0,sticky=W)

chicken = Checkbutton(appetizerFrame,text='Chicken Fries',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var2,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                 ,command=chicken)
chicken.grid(row=1,column=0,sticky=W)

bavarian = Checkbutton(appetizerFrame,text='Bavarian Pretzel Sticks',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var3,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                 ,command=bavarian)
bavarian.grid(row=2,column=0,sticky=W)

pepperoni = Checkbutton(appetizerFrame,text='Pepperoni Pizza Sticks',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var4,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                  ,command=pepperoni)
pepperoni.grid(row=3,column=0,sticky=W)

mac=Checkbutton(appetizerFrame,text='Mac & Cheese Bites',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var5,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                  ,command=mac)
mac.grid(row=4,column=0,sticky=W)

pretzel = Checkbutton(appetizerFrame,text='Pretzel Hot Dogs',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var6,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                  ,command=pretzel)
pretzel.grid(row=5,column=0,sticky=W)

mozzerella = Checkbutton(appetizerFrame,text='Mozzerella Sticks',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var7,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                   ,command=mozzerella)
mozzerella.grid(row=6,column=0,sticky=W)

spinach=Checkbutton(appetizerFrame,text='Spinach & Artichoke Dip',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var8,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                   ,command=spinach)
spinach.grid(row=7,column=0,sticky=W)

#price
Label(appetizerFrame, text="$3.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=0,column=1)
Label(appetizerFrame, text="$3.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=1,column=1)
Label(appetizerFrame, text="$4.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=2,column=1)
Label(appetizerFrame, text="$4.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=3,column=1)
Label(appetizerFrame, text="$4.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=4,column=1)
Label(appetizerFrame, text="$5.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=5,column=1)
Label(appetizerFrame, text="$5.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=6,column=1)
Label(appetizerFrame, text="$5.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=7,column=1)
#Entry Fields for Food Appetizers

textdips = Entry(appetizerFrame,font=('Perpetua',16,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dips)
textdips.grid(row=0,column=2)

textchicken = Entry(appetizerFrame,font=('Perpetua',16,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=1,column=2)

textbavarian = Entry(appetizerFrame,font=('Perpetua',16,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bavarian)
textbavarian.grid(row=2,column=2)

textpepperoni = Entry(appetizerFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pepperoni)
textpepperoni.grid(row=3, column=2)

textmac = Entry(appetizerFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mac)
textmac.grid(row=4, column=2)

textpretzel = Entry(appetizerFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pretzel)
textpretzel.grid(row=5, column=2)

textmozzerella = Entry(appetizerFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mozzerella)
textmozzerella.grid(row=6, column=2)

textspinach = Entry(appetizerFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_spinach)
textspinach.grid(row=7, column=2)

#Icecreams & Desserts

singlecone = Checkbutton(dessertFrame,text='Singlecone/Cup',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var9,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                  ,command=singlecone)
singlecone.grid(row=0,column=0,sticky=W)

doublecone=Checkbutton(dessertFrame,text='Doublecone/Cup',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var10,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                   ,command=doublecone)
doublecone.grid(row=1,column=0,sticky=W)

sundae = Checkbutton(dessertFrame,text='Sundae',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var11,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                   ,command=sundae)
sundae.grid(row=2,column=0,sticky=W)

signature = Checkbutton(dessertFrame,text='Signature Desserts',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var12,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                     ,command=signature)
signature.grid(row=3,column=0,sticky=W)

#price
Label(dessertFrame, text="$2.50", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=0,column=1)
Label(dessertFrame, text="$3.50", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=1,column=1)
Label(dessertFrame, text="$4.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=2,column=1)
Label(dessertFrame, text="$5.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=3,column=1)

#entry fields for Icecream & desserts

textsinglecone = Entry(dessertFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_singlecone)
textsinglecone.grid(row=0, column=2)

textdoublecone = Entry(dessertFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_doublecone)
textdoublecone.grid(row=1, column=2)

textsundae = Entry(dessertFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sundae)
textsundae.grid(row=2, column=2)

textsignature = Entry(dessertFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_signature)
textsignature.grid(row=3, column=2)

#Beverages

smallsoda = Checkbutton(beverageFrame,text='Small Soda',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var13,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                     ,command=smallsoda)
smallsoda.grid(row=0,column=0,sticky=W)

sodatogo = Checkbutton(beverageFrame,text='Soda To Go',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var14,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                      ,command=sodatogo)
sodatogo.grid(row=1,column=0,sticky=W)

largesoda = Checkbutton(beverageFrame,text='Large Soda(Free Refills)',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var15,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                       ,command=largesoda)
largesoda.grid(row=2,column=0,sticky=W)

soday = Checkbutton(beverageFrame,text='Soday Float',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var16,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                        ,command=soday)
soday.grid(row=3,column=0,sticky=W)

milkshake = Checkbutton(beverageFrame,text='Milkshake/Smoothie',font=('Perpetua',13,'bold'),onvalue=1,offvalue=0,variable=var17,bg='grey17',fg='white', activeforeground='white', selectcolor='black'
                       ,command= milkshake)
milkshake.grid(row=4,column=0,sticky=W)

#price
Label(beverageFrame, text="$1.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=0,column=1)
Label(beverageFrame, text="$1.50", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=1,column=1)
Label(beverageFrame, text="$2.00", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=2,column=1)
Label(beverageFrame, text="$3.50", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=3,column=1)
Label(beverageFrame, text="$4.75", font=('Perpetua',13,'bold'),bd=7,width=6,bg='grey17',fg='white').grid(row=4,column=1)

#entry fields for beverages

textsmallsoda = Entry(beverageFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_smallsoda)
textsmallsoda.grid(row=0, column=2)

textsodatogo = Entry(beverageFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sodatogo)
textsodatogo.grid(row=1, column=2)

textlargesoda = Entry(beverageFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_largesoda)
textlargesoda.grid(row=2, column=2)

textsoday = Entry(beverageFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_soday)
textsoday.grid(row=3, column=2)

textmilkshake = Entry(beverageFrame, font=('Perpetua', 16, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milkshake)
textmilkshake.grid(row=4, column=2)

#costlabels & entry fields

labelCostofappetizers=Label(costFrame,text='Cost of Appetizers',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelCostofappetizers.grid(row=0,column=0)

textCostofappetizers=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostofappetizers)
textCostofappetizers.grid(row=0,column=1,padx=41)

labelCostoficecreamdesserts=Label(costFrame,text='Cost of Icecream and Desserts',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelCostoficecreamdesserts.grid(row=1,column=0)

textCostoficecreamdesserts=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostoficecreamdesserts)
textCostoficecreamdesserts.grid(row=1,column=1,padx=41)

labelCostofbeverages=Label(costFrame,text='Cost of Beverages',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelCostofbeverages.grid(row=2,column=0)

textCostofbeverages=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostofbeverages)
textCostofbeverages.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('Perpetua',13,'bold'),bg='grey17',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('Perpetua',13,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('Perpetua',13,'bold'),fg='black',bg='burlywood3',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('Perpetua',13,'bold'),fg='black',bg='burlywood3',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('Perpetua',13,'bold'),fg='black',bg='burlywood3',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text='Reset',font=('Perpetua',13,'bold'),fg='black',bg='burlywood3',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('Perpetua',13,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

root.mainloop()