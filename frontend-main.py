from tkinter import *
from tkinter import ttk
import urllib.request
from tkinter import messagebox
import json
import ast
from PIL import Image,ImageTk
#from connection import *
newdata=""

def add():

        pname=product_entry.get()
        pid=pid_entry.get()
        mrp=mrp_entry.get()
        sp=sp_entry.get()
        quantity=quantity_entry.get()
        try:
            url="http://127.0.0.1:5000/add/"+pname+"/"+pid+"/"+mrp+"/"+sp+"/"+quantity
            print(url)
            #call the endpoint
            response=urllib.request.urlopen(url)
            print("connectivity to backendend completed******************")
            body = response.read()
            messagebox.showinfo('information',body)
        except:
            messagebox.showerror('error',"something wrong")

        
def searchbyid():
        sid=productid_entry.get()
    
        url="http://127.0.0.1:5000/searchbyid/"+sid
        response=urllib.request.urlopen(url)
        print("connectivity to backendend completed******************")
        
        body = response.read()
        
        notificationwindow=Tk()
        notificationwindow.geometry('400x250')
        body=body.decode('utf-8')
        body=body.split(",")
      
        firstvalue=(body[0])
        firstvalue=firstvalue[5:-1]
        print(firstvalue)
        secondvalue=(body[1])
        secondvalue=secondvalue[4:-1]
        print(secondvalue)
        thirdvalue=(body[2])
        thirdvalue=thirdvalue[3:]
        print(thirdvalue)
        fourthvalue=(body[3])
        fourthvalue=fourthvalue[3:]
        print(type(fourthvalue))
        print(fourthvalue)
        fifthvalue=(body[4])
        fifthvalue=fifthvalue[3:-5]
        print(fifthvalue)
        
       
        notificationframe=Frame(notificationwindow,bd=10,relief=SUNKEN,bg='blue')
        notificationframe.place(x=0,y=0,height=250,width=400)

        c1=Label(notificationframe,text="PRODUCT NAME ",font=('bold',15),bg='snow',fg='black')
        c1.place(x=10,y=10)
        c6=Label(notificationframe,text=firstvalue,font=('bold',15),bg='snow',fg='black')
        c6.place(x=200,y=10)
        
        c2=Label(notificationframe,text="   PRODUCT ID    ",font=('bold',15),bg='snow',fg='black')
        c2.place(x=10,y=50)
        c7=Label(notificationframe,text=secondvalue,font=('bold',15),bg='snow',fg='black')
        c7.place(x=200,y=50)
        
        c3=Label(notificationframe,text="         M R P         ",font=('bold',15),bg='snow',fg='black')
        c3.place(x=10,y=90)
        c8=Label(notificationframe,text=thirdvalue,font=('bold',15),bg='snow',fg='black')
        c8.place(x=200,y=90)
        
        c4=Label(notificationframe,text=" SELLING PRICE ",font=('bold',15),bg='snow',fg='black')
        c4.place(x=10,y=130)
        c9=Label(notificationframe,text=fourthvalue,font=('bold',15),bg='snow',fg='black')
        c9.place(x=200,y=130)
        
        c5=Label(notificationframe,text="     QUANTITY      ",font=('bold',15),bg='snow',fg='black')
        c5.place(x=10,y=170)
        c10=Label(notificationframe,text=fifthvalue,font=('bold',15),bg='snow',fg='black')
        c10.place(x=200,y=170)
        notificationwindow.mainloop()
        productid_entry.delete(0,END)
        
    
def searchbyname():
        sname=p1_name.get()
        print(sname)
        
        url="http://127.0.0.1:5000/searchbyname/"+sname
        print(url)
        response=urllib.request.urlopen(url)
        print("connectivity to backendend completed******************")
        body = response.read()
        
    
        notification2window=Tk()
        notification2window.geometry('400x250')
        body=body.decode('utf-8')
        body=body.split(",")
      
        firstvalue=(body[0])
        firstvalue=firstvalue[5:-1]
        print(firstvalue)
        secondvalue=(body[1])
        secondvalue=secondvalue[4:-1]
        print(secondvalue)
        thirdvalue=(body[2])
        thirdvalue=thirdvalue[3:]
        print(thirdvalue)
        fourthvalue=(body[3])
        fourthvalue=fourthvalue[3:]
        print(type(fourthvalue))
        print(fourthvalue)
        fifthvalue=(body[4])
        fifthvalue=fifthvalue[3:-5]
        print(fifthvalue)
        
       
        notification2frame=Frame(notification2window,bd=10,relief=SUNKEN,bg='blue')
        notification2frame.place(x=0,y=0,height=250,width=400)

        c1=Label(notification2frame,text="PRODUCT NAME ",font=('bold',15),bg='snow',fg='black')
        c1.place(x=10,y=10)
        c6=Label(notification2frame,text=firstvalue,font=('bold',15),bg='snow',fg='black')
        c6.place(x=200,y=10)
        
        c2=Label(notification2frame,text="   PRODUCT ID    ",font=('bold',15),bg='snow',fg='black')
        c2.place(x=10,y=50)
        c7=Label(notification2frame,text=secondvalue,font=('bold',15),bg='snow',fg='black')
        c7.place(x=200,y=50)
        
        c3=Label(notification2frame,text="         M R P         ",font=('bold',15),bg='snow',fg='black')
        c3.place(x=10,y=90)
        c8=Label(notification2frame,text=thirdvalue,font=('bold',15),bg='snow',fg='black')
        c8.place(x=200,y=90)
        
        c4=Label(notification2frame,text=" SELLING PRICE ",font=('bold',15),bg='snow',fg='black')
        c4.place(x=10,y=130)
        c9=Label(notification2frame,text=fourthvalue,font=('bold',15),bg='snow',fg='black')
        c9.place(x=200,y=130)
        
        c5=Label(notification2frame,text="     QUANTITY      ",font=('bold',15),bg='snow',fg='black')
        c5.place(x=10,y=170)
        c10=Label(notification2frame,text=fifthvalue,font=('bold',15),bg='snow',fg='black')
        c10.place(x=200,y=170)
        notification2window.mainloop()
        p1_name.delete(0,END)
    
    
def fetch():
    id5=p4_name.get()

    url="http://127.0.0.1:5000/ciddetails/"+id5
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    
    body = response.read()
    dict_str = body.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    
    fetchwindow=Tk()
    fetchwindow.geometry('400x250')
    
  
    firstvalue=(body[0])
    firstvalue=mydata["productname"]
    print(firstvalue)
    secondvalue=mydata["mrp"]
    print(secondvalue)
    thirdvalue=mydata["sp"]
    print(thirdvalue)
    fourthvalue=mydata["quantity"]
    print(type(fourthvalue))
    print(fourthvalue)
    fifthvalue=mydata["discount"]
    print(fifthvalue)
    sixthvalue=mydata["discountpercentage"]
    print(sixthvalue)
    seventhvalue=mydata["totalproduct"]
    print(seventhvalue)
    
   
    fetchframe=Frame(fetchwindow,bd=10,relief=SUNKEN,bg='blue')
    fetchframe.place(x=0,y=0,height=1000,width=1000)

    c1=Label(fetchframe,text="PRODUCT NAME ",font=('bold',15),bg='snow',fg='black')
    c1.place(x=10,y=10)
    c6=Label(fetchframe,text=firstvalue,font=('bold',15),bg='snow',fg='black')
    c6.place(x=300,y=10)
    
    c2=Label(fetchframe,text=" M R P     ",font=('bold',15),bg='snow',fg='black')
    c2.place(x=10,y=50)
    c7=Label(fetchframe,text=secondvalue,font=('bold',15),bg='snow',fg='black')
    c7.place(x=300,y=50)
    
    c3=Label(fetchframe,text="     SELLING PRICE   ",font=('bold',15),bg='snow',fg='black')
    c3.place(x=10,y=90)
    c8=Label(fetchframe,text=thirdvalue,font=('bold',15),bg='snow',fg='black')
    c8.place(x=300,y=90)
    
    c4=Label(fetchframe,text="  QUANTITY  ",font=('bold',15),bg='snow',fg='black')
    c4.place(x=10,y=130)
    c9=Label(fetchframe,text=fourthvalue,font=('bold',15),bg='snow',fg='black')
    c9.place(x=300,y=130)
    
    c5=Label(fetchframe,text="   DISCOUNT      ",font=('bold',15),bg='snow',fg='black')
    c5.place(x=10,y=170)
    c10=Label(fetchframe,text=fifthvalue,font=('bold',15),bg='snow',fg='black')
    c10.place(x=300,y=170)
    
    c11=Label(fetchframe,text=" DISCOUNT PERCENTAGE  ",font=('bold',15),bg='snow',fg='black')
    c11.place(x=10,y=210)
    c12=Label(fetchframe,text=sixthvalue,font=('bold',15),bg='snow',fg='black')
    c12.place(x=300,y=210)
    
    c13=Label(fetchframe,text=" TOTAL PRODUCT  ",font=('bold',15),bg='snow',fg='black')
    c13.place(x=10,y=250)
    c14=Label(fetchframe,text=seventhvalue,font=('bold',15),bg='snow',fg='black')
    c14.place(x=300,y=250)
    
    
    
    fetchwindow.mainloop()
    
    
        
        
def search():
    if(productid_entry.get()==""):
        searchbyname()
    else:
        searchbyid()
        
        
def getstockbyname():
    getname=p2_name.get()

    url="http://127.0.0.1:5000/getstockbyname/"+getname
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    
    body = response.read()
    messagebox.showinfo('information',body)
    p2_name.delete(0,END)
 
    
def getstockbyid():
    getid=productid2_entry.get()

    url="http://127.0.0.1:5000/getstockbyid/"+getid
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    
    body = response.read()
    messagebox.showinfo('information',body)
    productid2_entry.delete(0,END)
        
def productsearch():
    if(productid2_entry.get()==""):
        getstockbyname()
    else:
        getstockbyid()
    
    
def addbill():
    idd=productid3_entry.get()
    quantity=quantity2_entry.get()

    url="http://127.0.0.1:5000/generatebill/"+idd+"/"+quantity
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    
    body = response.read()
  
    dict_str = body.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    pname=(mydata['product'])
    pname=(list(pname))
    newdata=""
    for i in pname:
        newdata=newdata+i+'\n'
        
    print(newdata)
    #messagebox.showinfo('information',body)
    p_label.configure(text=newdata)
    quantity2_entry.delete(0,END)
    productid3_entry.delete(0,END)
    print("ready for next")
    
    
def checkout():
    url="http://127.0.0.1:5000/checkout"
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    global Button38,Button39
    Button38.place(x=10,y=400)
    Button39.place(x=200,y=400)
    body = response.read()
    
    messagebox.showinfo('information',body)
    
def updatebyname():
    newname=productname4_entry.get()
    newmrp=newmrp_entry.get()
    newsp=newsp_entry.get()
    newquantity=newquantity_entry.get()
    
    url="http://127.0.0.1:5000/updateByname/"+newname+"/"+newmrp+"/"+newsp+"/"+newquantity
    print(url)
    #call the endpoint
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    body = response.read()
    messagebox.showinfo('information',body)
    productname4_entry.delete(0,END)
    newmrp_entry.delete(0,END)
    newsp_entry.delete(0,END)
    newquantity_entry.delete(0,END)
    

def updatebyid():
    idd=productid4_entry.get()
    newmrp=newmrp2_entry.get()
    newsp=newsp2_entry.get()
    newquantity=newquantity2_entry.get()
    
    url="http://127.0.0.1:5000/updateByID/"+idd+"/"+newmrp+"/"+newsp+"/"+newquantity
    print(url)
    #call the endpoint
    response=urllib.request.urlopen(url)
    print("connectivity to backendend completed******************")
    body = response.read()
    messagebox.showinfo('information',body)
    productid4_entry.delete(0,END)
    newmrp2_entry.delete(0,END)
    newsp2_entry.delete(0,END)
    newquantity2_entry.delete(0,END)
    
    
def continuepayment():
    url="http://127.0.0.1:5000/continuepayment"
    response=urllib.request.urlopen(url)
    body = response.read()
    print("connectivity to backendend completed******************")
    messagebox.showinfo('information',body)
    cancel_bill()

def paylater():
    url="http://127.0.0.1:5000/paylater"
    response=urllib.request.urlopen(url)
    body = response.read()
    print("connectivity to backendend completed******************")
    messagebox.showinfo('information',body)
    
    cancel_bill()
    mainwindow.destroy()
    import main
    
    
def paynow():  
     idd=p4_name.get()
     url="http://127.0.0.1:5000/confirmdetails/"+idd
     response=urllib.request.urlopen(url)
     body = response.read()
     print("connectivity to backendend completed******************")
     body=body.decode('utf-8')
     print(body)
     if(body=="ok"):
         messagebox.showinfo('successful',"payment completed")
     else:
         messagebox.showerror('unsuccessful',"something wrong")
         
         
     

            
        
        
def addproduct():
    billframe.place_forget()
    searchframe.place_forget()
    infoframe.place_forget()
    updateframe.place_forget()
    checkframe.place_forget()
    paylaterframe.place_forget()
    productframe.place(x=100,y=300,height=450,width=1200)

def addcustomerbill():
    productframe.place_forget()
    searchframe.place_forget()
    infoframe.place_forget()
    updateframe.place_forget()
    paylaterframe.place_forget()
    billframe.place(x=100,y=300,height=450,width=900)
    checkframe.place(x=1000,y=300,height=450,width=450)

def searchproduct():
    billframe.place_forget()
    productframe.place_forget()
    infoframe.place_forget()
    checkframe.place_forget()
    updateframe.place_forget()
    paylaterframe.place_forget()
    searchframe.place(x=100,y=300,height=450,width=1200)
    
def productinfo():
    billframe.place_forget()
    productframe.place_forget()
    searchframe.place_forget()
    checkframe.place_forget()
    updateframe.place_forget()
    paylaterframe.place_forget()
    infoframe.place(x=100,y=300,height=450,width=1200)
    

def updateproduct():
    billframe.place_forget()
    productframe.place_forget()
    searchframe.place_forget()
    checkframe.place_forget()
    infoframe.place_forget()
    paylaterframe.place_forget()
    updateframe.place(x=100,y=300,height=450,width=1200)
    
def update2():
    update2frame.place(x=20,y=20,height=350,width=1140)
    
def update3():
    update3frame.place(x=20,y=20,height=350,width=1140)
    
def paylater2():
    billframe.place_forget()
    productframe.place_forget()
    searchframe.place_forget()
    checkframe.place_forget()
    infoframe.place_forget()
    updateframe.place_forget()
    paylaterframe.place(x=100,y=300,height=450,width=550)
    


def customerdetails():
    customerdetailframe.place(x=640,y=300,height=450,width=850)


    
    
    
    
    



def cancel():
    productframe.place_forget()
    
def cancel_search():
    searchframe.place_forget()
    
def cancel_productsearch():
    infoframe.place_forget()
    
def cancel_bill():
    p_label.configure(text="")
    newdata=""
    Button38.place_forget()
    Button39.place_forget()
    billframe.place_forget()
    checkframe.place_forget()
    
    
    
def cancel_update():
    updateframe.place_forget()
    
def cancel_update2():
    update2frame.place_forget()
    
def cancel_update3():
    update3frame.place_forget()
    
def cancel_paylater():
    paylaterframe.place_forget()
    customerdetailframe.place_forget()
    



mainwindow=Tk()
'''
status,sheet=config.doConnectionread()
row=sheet.nrows
print(row)
#step 4 -retrieve the product details
productfound=0
prod_list=[]
for i in range(row):
    pname=sheet.cell_value(i,0)
    prod_list.append(pname)
    prod_list.sort()
print(prod_list)
'''
mainwindow.state('zoomed')
mainwindow.configure(background='black')
img=Image.open('mart.jpg')
img.thumbnail((2000,2000),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)
Label(mainwindow,image=photo).place(x=500,y=300)





dashboardframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
dashboardframe.place(x=20,y=100,height=170,width=1450)
b11=Button(dashboardframe,text="ADD PRODUCT",font=('bold',15),bg='yellow',fg='purple',command=addproduct)
b11.place(x=10,y=40)

b22=Button(dashboardframe,text="ADD CUSTOMER BILL",font=('bold',15),bg='yellow',fg='purple',command=addcustomerbill)
b22.place(x=250,y=40)

b33=Button(dashboardframe,text="SEARCH PRODUCT",font=('bold',15),bg='yellow',fg='purple',command=searchproduct)
b33.place(x=540,y=40)

b44=Button(dashboardframe,text="UPDATE PRODUCT",font=('bold',15),bg='yellow',fg='purple',command=updateproduct)
b44.place(x=1040,y=40)

b55=Button(dashboardframe,text="PRODUCT INFO",font=('bold',15),bg='yellow',fg='purple',command=productinfo)
b55.place(x=810,y=40)

b66=Button(dashboardframe,text="PAY LATER",font=('bold',15),bg='yellow',fg='purple',command=paylater2)
b66.place(x=1280,y=40)



productframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
productframe.place(x=100,y=300,height=450,width=1200)

b1=Label(productframe,text="PRODUCT NAME",font=('bold',25),bg='snow',fg='black')
b1.place(x=20,y=20)
product_entry=Entry(productframe,font=('bold',25),bg='white',fg='black')
product_entry.place(x=400,y=20)

b2=Label(productframe,text="   PRODUCT ID    ",font=('bold',25),bg='snow',fg='black')
b2.place(x=20,y=90)
pid_entry=Entry(productframe,font=('bold',25),bg='white',fg='black')
pid_entry.place(x=400,y=90)

b3=Label(productframe,text="         M R P           ",font=('bold',25),bg='snow',fg='black')
b3.place(x=20,y=170)
mrp_entry=Entry(productframe,font=('bold',25),bg='white',fg='black')
mrp_entry.place(x=400,y=170)

b4=Label(productframe,text=" SELLING PRICE ",font=('bold',25),bg='snow',fg='black')
b4.place(x=20,y=250)
sp_entry=Entry(productframe,font=('bold',25),bg='white',fg='black')
sp_entry.place(x=400,y=250)

b5=Label(productframe,text="     QUANTITY      ",font=('bold',25),bg='snow',fg='black')
b5.place(x=20,y=330)
quantity_entry=Entry(productframe,font=('bold',25),bg='white',fg='black')
quantity_entry.place(x=400,y=340)

b6=Button(productframe,text="ADD",font=('bold',30),bg='light green',fg='black',command=add)
b6.place(x=900,y=150)

b7=Button(productframe,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel)
b7.place(x=900,y=20)

productframe.place_forget()



searchframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
searchframe.place(x=100,y=300,height=450,width=1200)
b8=Label(searchframe,text="   PRODUCT ID   ",font=('bold',25),bg='snow',fg='black')
b8.place(x=20,y=20)
productid_entry=Entry(searchframe,font=('bold',30),bg='white',fg='black')
productid_entry.place(x=400,y=20)

b9=Label(searchframe,text="PRODUCT NAME",font=('bold',25),bg='snow',fg='black')
b9.place(x=20,y=150)
p1_name=StringVar()
b10=ttk.Combobox(searchframe,font=('bold',30),textvariable=p1_name) 
'''b10['values']=tuple(prod_list[:])
b10.current(0)'''
b10.place(x=400,y=150)

b12=Button(searchframe,text="SEARCH",font=('bold',30),bg='light green',fg='black',command=search)
b12.place(x=500,y=250)
b13=Button(searchframe,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_search)
b13.place(x=1000,y=20)
searchframe.place_forget()



infoframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
infoframe.place(x=100,y=300,height=450,width=1200)
b14=Label(infoframe,text="   PRODUCT ID   ",font=('bold',25),bg='snow',fg='black')
b14.place(x=20,y=20)
productid2_entry=Entry(infoframe,font=('bold',30),bg='white',fg='black')
productid2_entry.place(x=400,y=20)

b15=Label(infoframe,text="PRODUCT NAME",font=('bold',25),bg='snow',fg='black')
b15.place(x=20,y=150)

p2_name=StringVar()
b15=ttk.Combobox(infoframe,font=('bold',30),textvariable=p2_name) 
'''b10['values']=tuple(prod_list[:])
b10.current(0)'''
b15.place(x=400,y=150)

b16=Button(infoframe,text="SEARCH",font=('bold',30),bg='light green',fg='black',command=productsearch)
b16.place(x=950,y=140)
b17=Button(infoframe,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_productsearch)
b17.place(x=1000,y=20)
infoframe.place_forget()


billframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
billframe.place(x=100,y=300,height=450,width=900)
b18=Label(billframe,text="   PRODUCT ID   ",font=('bold',25),bg='snow',fg='black')
b18.place(x=20,y=20)
productid3_entry=Entry(billframe,font=('bold',30),bg='white',fg='black')
productid3_entry.place(x=400,y=20)
b19=Button(billframe,text="ADD",font=('bold',30),bg='light green',fg='black',command=addbill)
b19.place(x=500,y=250)
b20=Button(billframe,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_bill)
b20.place(x=700,y=250)
b21=Label(billframe,text="     QUANTITY      ",font=('bold',25),bg='snow',fg='black')
b21.place(x=20,y=150)
quantity2_entry=Entry(billframe,font=('bold',30),bg='white',fg='black')
quantity2_entry.place(x=400,y=150)
b23=Button(billframe,text="CHECKOUT",font=('bold',25),bg='blue',fg='snow',command=checkout)
b23.place(x=100,y=250)
billframe.place_forget()


updateframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
updateframe.place(x=100,y=300,height=450,width=1200)
b24=Button(updateframe,text="UPDATE BY NAME",font=('bold',30),bg='yellow',fg='black',command=update2)
b24.place(x=60,y=150)
b25=Button(updateframe,text=" UPDATE BY ID ",font=('bold',30),bg='yellow',fg='black',command=update3)
b25.place(x=600,y=150)
b26=Button(updateframe,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_update)
b26.place(x=1000,y=20)
updateframe.place_forget()


update2frame=Frame(updateframe,bd=10,relief=SUNKEN,bg='royal blue')
update2frame.place(x=20,y=20,height=350,width=1140)
b24=Label(update2frame,text=" PRODUCT NAME  ",font=('bold',25),bg='snow',fg='black')
b24.place(x=20,y=20)
productname4_entry=Entry(update2frame,font=('bold',30),bg='white',fg='black')
productname4_entry.place(x=400,y=20)
b25=Label(update2frame,text="   NEW M R P     ",font=('bold',25),bg='snow',fg='black')
b25.place(x=20,y=90)
newmrp_entry=Entry(update2frame,font=('bold',30),bg='white',fg='black')
newmrp_entry.place(x=400,y=90)
b26=Label(update2frame,text="   NEW SP  ",font=('bold',25),bg='snow',fg='black')
b26.place(x=20,y=150)
newsp_entry=Entry(update2frame,font=('bold',30),bg='white',fg='black')
newsp_entry.place(x=400,y=150)
b27=Label(update2frame,text="   QUANTITY   ",font=('bold',25),bg='snow',fg='black')
b27.place(x=20,y=220)
newquantity_entry=Entry(update2frame,font=('bold',30),bg='white',fg='black')
newquantity_entry.place(x=400,y=220)
b32=Button(update2frame,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_update2)
b32.place(x=900,y=40)
b35=Button(update2frame,text="UPDATE",font=('bold',25),bg='light green',fg='black',command=updatebyname)
b35.place(x=900,y=150)
update2frame.place_forget()


update3frame=Frame(updateframe,bd=10,relief=SUNKEN,bg='royal blue')
update3frame.place(x=20,y=20,height=350,width=1140)
b28=Label(update3frame,text="   PRODUCT ID    ",font=('bold',25),bg='snow',fg='black')
b28.place(x=20,y=20)
productid4_entry=Entry(update3frame,font=('bold',30),bg='white',fg='black')
productid4_entry.place(x=400,y=20)
b29=Label(update3frame,text="   NEW M R P     ",font=('bold',25),bg='snow',fg='black')
b29.place(x=20,y=90)
newmrp2_entry=Entry(update3frame,font=('bold',30),bg='white',fg='black')
newmrp2_entry.place(x=400,y=90)
b30=Label(update3frame,text="   NEW SP   ",font=('bold',25),bg='snow',fg='black')
b30.place(x=20,y=150)
newsp2_entry=Entry(update3frame,font=('bold',30),bg='white',fg='black')
newsp2_entry.place(x=400,y=150)
b31=Label(update3frame,text="   QUANTITY      ",font=('bold',25),bg='snow',fg='black')
b31.place(x=20,y=220)
newquantity2_entry=Entry(update3frame,font=('bold',30),bg='white',fg='black')
newquantity2_entry.place(x=400,y=220)
b34=Button(update3frame,text="CANCEL",font=('bold',20),bg='red',fg='snow',command=cancel_update3)
b34.place(x=900,y=40)
b36=Button(update3frame,text="UPDATE",font=('bold',25),bg='light green',fg='black',command=updatebyid)
b36.place(x=900,y=150)
update3frame.place_forget()


checkframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
checkframe.place(x=1000,y=300,height=450,width=450)
Button38=Button(checkframe,text="PAY NOW",command=continuepayment)
Button39=Button(checkframe,text="PAY LATER",command=paylater)
p_label=Label(checkframe,bg='royal blue',fg='white')
p_label.place(x=10,y=20)
checkframe.place_forget()

paylaterframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
paylaterframe.place(x=50,y=300,height=450,width=550)

b38=Button(paylaterframe,text=" CUSTOMER DETAILS",font=('bold',20),bg='yellow',fg='black',command=customerdetails)
b38.place(x=100,y=150)

b41=Button(paylaterframe,text="CANCEL",font=('bold',10),bg='red',fg='snow',command=cancel_paylater)
b41.place(x=450,y=20)



paylaterframe.place_forget()

customerdetailframe=Frame(mainwindow,bd=10,relief=SUNKEN,bg='royal blue')
customerdetailframe.place(x=600,y=300,height=450,width=850)
b37=Label(customerdetailframe,text="CUSTOMER ID ",font=('bold',25),bg='snow',fg='black')
b37.place(x=20,y=40)
url="http://127.0.0.1:5000/pendingid"
print(url)
#call the endpoint
response=urllib.request.urlopen(url)
print("connectivity to backendend completed******************")
body = response.read()
body=tuple(json.loads(body))
p4_name=StringVar()
try:
    b38=ttk.Combobox(customerdetailframe,font=('bold',30),textvariable=p4_name) 
    b38['values']=body
    b38.current(0)
except:
    pass

b38.place(x=350,y=40)


b42=Button(customerdetailframe,text=" FETCH ",font=('bold',20),bg='yellow',fg='black',command=fetch)
b42.place(x=350,y=160)
b40=Button(customerdetailframe,text="PAY NOW",font=('bold',22),bg='light green',fg='black',command=paynow)
b40.place(x=600,y=160)
customerdetailframe.place_forget()

mainwindow.mainloop()

