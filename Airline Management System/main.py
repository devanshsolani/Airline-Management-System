from tkinter import *
from tkinter import messagebox
import re
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector as mysql

conn = mysql.connect(user="root",password="root",host='127.0.0.1',database="projectdb1")
c=conn.cursor()

def sqlcommit():
    conn.commit()

def showprice():
    messagebox.showinfo('Price','YOUR TICKET PRICE IS '+str(TICKPRICE)+'/-')
    pass
#---------------------------Ticket------------------------------#
def ticketprint():
    PID = currlogin[0]
    PNAME = currlogin[1]
    NO_PASS = varpass.get()
    DEPDATE = vardep.get()
    ARRDATE = vararr.get()
    if ARRDATE == '':
        ARRDATE = "---"
    DEPCITY = departurecityvar.get()
    ARRCITY = arrivalcityvar.get()
    FTIME = vartime.get()

    root_main.destroy()
        
    root_ticket = Tk()
    root_ticket.geometry('2000x2000+-10+0')
    root_ticket.title("E-Ticket")

    image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\dwnld2.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(root_ticket,image=photo)
    label.image = photo # keep a reference!
    label.place(x=0,y=0)

    ticket = LabelFrame(root_ticket,text="Happy Skies E-Ticket",font=('Comic Sans MS',10),width=1000,height=400,bd=5,highlightbackground="blue",highlightthickness=3,bg="white")
    ticket.place(x=300,y=210)

    Label(ticket,text="Passenger's Name: ",font=('Comic Sans MS',15),bg='white').place(x=0,y=25)
    Label(ticket,text=PNAME,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=200,y=25)

    Label(ticket,text="No. of Passenger(s): ",font=('Comic Sans MS',15),bg='white').place(x=700,y=25)
    Label(ticket,text=NO_PASS,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=900,y=25)

    Label(ticket,text="Departure Date: ",font=('Comic Sans MS',15),bg='white').place(x=0,y=75)
    Label(ticket,text=DEPDATE,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=10,y=115)

    Label(ticket,text="Return Date: ",font=('Comic Sans MS',15),bg='white').place(x=200,y=75)
    Label(ticket,text=ARRDATE,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=210,y=115)

    Label(ticket,text="From ",font=('Comic Sans MS',15),bg='white').place(x=500,y=95)
    Label(ticket,text=DEPCITY,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=520,y=125)

    Label(ticket,text="To ",font=('Comic Sans MS',15),bg='white').place(x=700,y=95)
    Label(ticket,text=ARRCITY,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=720,y=125)

    Label(ticket,text="Status: UNPAID",font=('Comic Sans MS',13),bg='white').place(x=800,y=320)
    
    Label(ticket,text="Flight Timing: ",font=('Comic Sans MS',15),bg='white').place(x=10,y=200)
    Label(ticket,text=FTIME,font=('MS Serif',17),bg='white',fg='midnightblue').place(x=150,y=200)

    Label(ticket,text="Thanks for choosing Happy Skies!!\nWishing you a safe journey :)",font=('Comic Sans MS',17),bg='white').place(x=100,y=300)

    try:
        booking = "INSERT INTO bookedflights(passid,pname,nopass,depdate,arrdate,depcity,arrcity,ftime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        booker = (PID,PNAME,NO_PASS,DEPDATE,ARRDATE,DEPCITY,ARRCITY,FTIME)
        c.execute(booking,booker)
        sqlcommit()
        messagebox.showinfo("Success","PLEASE VISIT THE NEAREST HAPPYSKIES BRANCH\nAND COLLECT YOUR TICKET")
    except:
        messagebox.showerror("SQL ENTRY ERROR", "ERROR OCCURED.\nPLEASE BOOK YOUR TICKETS AGAIN")
        main_page()
    
    root_ticket.mainloop()
#--------------------------Main page---------------------------#
def main_page():
    def validateprice():
        DEPCITY = departurecityvar.get()
        #print(DEPCITY)
        #ARRCITY = arrivalcityvar.get()
        #print(ARRCITY)
        list1 = ['Ahmedabad','Chandigarh','Chennai','Cochin','Delhi','Goa','Hyderabad','Jaipur','Kolkata','Leh']
        if DEPCITY in list1:
            DEPPRICE = 1610
            ARRPRICE = 1189
        else:
            DEPPRICE = 1209
            ARRPRICE = 1290
#elif (DEPCITY == 'Kolkata'or'Leh'or'Lucknow'or'Mumbai'or'Nagpur'or'Patna'or'Port Blair'or'Pune'or'Rajkot'or'Srinagar'or'Trivandrum'):'''
        
        global TICKPRICE
        TICKPRICE = DEPPRICE + ARRPRICE
        #print(TICKPRICE)
        if loginSkipped == 1:
            reguser = messagebox.askyesno('Continue?','WOULD YOU LIKE TO BOOK YOUR TICKET?\nCLICK YES TO REGISTER\nAND NO TO JUST VIEW THE TICKET PRICE.')
            if reguser == True:
                root_main.destroy()
                registration(event='<Button-1>')
            else:
                showprice()
        else:
            showprice()

    def validatetime():
        SUITABLETIME = vartime.get()
        if SUITABLETIME == '0':
            messagebox.showerror('Error',"Please select a suitable time for your flight")
            root_time.destroy()
            timeflight()
        else:
            confirmtick = messagebox.askyesno('Confirmation',"Are you sure you want to proceed ?\nWe will book a temporary seat for you until the payment is done.")
            if confirmtick == False:
                root_time.destroy()
                timeflight()
            else:
                ticketprint()

    def timeflight():
            global root_time
            root_time = Toplevel()
            root_time.title("Flights available")
            root_time.geometry('420x420+500+150')

            image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\airplane-logo2.png")
            photo = ImageTk.PhotoImage(image)
            label = Label(root_time,image=photo)
            label.image=photo
            label.place(x=-5,y=0)

            global vartime
            vartime=StringVar()
            vartime.set(False)

            Label(root_time,text="Choose a Flight timing suitable for you...",font=('courier',13)).grid(row=0,column=1,columnspan=2,rowspan=2)

            Radiobutton(root_time, text="1 am",padx = 20, variable=vartime, value='1:00 am',font=('system',10)).grid(row=2,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="2 am",padx = 20, variable=vartime, value='2:00 am',font=('system',10)).grid(row=3,column=1,columnspan=2,sticky=W)
            Label(root_time,text="No Flights Between 2-7 am",font=('courier',13)).grid(row=4,column=1,columnspan=2)
            Radiobutton(root_time, text="7 am",padx = 20, variable=vartime, value='7:00 am',font=('system',10)).grid(row=5,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="9 am",padx = 20, variable=vartime, value='9:00 am',font=('system',10)).grid(row=6,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="11 am",padx = 20, variable=vartime, value='11:00 am',font=('system',10)).grid(row=7,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="1 pm",padx = 20, variable=vartime, value='1:00 pm',font=('system',10)).grid(row=8,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="3 pm",padx = 20, variable=vartime, value='3:00 pm',font=('system',10)).grid(row=9,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="5 pm",padx = 20, variable=vartime, value='5:00 pm',font=('system',10)).grid(row=10,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="7 pm",padx = 20, variable=vartime, value='7:00 pm',font=('system',10)).grid(row=11,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="9 pm",padx = 20, variable=vartime, value='9:00 pm',font=('system',10)).grid(row=12,column=1,columnspan=2,sticky=W)
            Radiobutton(root_time, text="11 pm",padx = 20, variable=vartime, value='11:00 pm',font=('system',10)).grid(row=14,column=1,columnspan=2,sticky=W)

            Label(root_time,text="Bookings cannot be cancelled online once placed.\nVisit the nearest Happy Skies branch for further inquiries ").place(x=0,y=350)

            btnbook = Button(root_time,text="Book Ticket",font=('Helvetica',13),width=10,command=validatetime,bg='black',fg='white')
            if loginSkipped == 1:
                btnbook.place_forget()
            else:
                btnbook.place(x=300,y=370)
            
            Button(root_time,text="S\nh\no\nw\n\nP\nr\ni\nc\ne",font=('Helvetica',13),width=5,bg='black',fg='white',command=validateprice).place(x=370,y=70)

            root_time.mainloop()


    def validatesearch():
        DEPCITY=departurecityvar.get()
        ARRCITY=arrivalcityvar.get()
        DEPDATE=vardep.get()
        ARRDATE=vararr.get()
        PASSENGER=varpass.get()
        flag=0
    #-----------
        if (DEPCITY and ARRCITY and DEPDATE or ARRDATE and PASSENGER) == '':
             messagebox.showerror("Error", "PLEASE SELECT YOUR TYPE OF TRAVEL")
        else:
            if DEPCITY and ARRCITY == airportlst[0]:
                    flag=1
                    messagebox.showwarning("Warning", "SELECT A CITY")
            else:
                if DEPCITY == ARRCITY:
                    flag=1
                    messagebox.showwarning("Warning", "PLEASE SELECT DIFFERENT CITIES")
                else:
                    pass
                if ARRDATE != '' and DEPDATE > ARRDATE:
                    flag=1
                    messagebox.showwarning("Warning", "ARRIVAL CANNONT BE BEFORE DEPARTURE DATE")
                if flag == 0:
                    timeflight()
        

    try:
        root_login.destroy()
    except:    
        root_regist.destroy()
    global root_main
    root_main = Tk()
    root_main.geometry('2000x2000+-10+0')
    root_main.title("Happy Skies Flight Reservation")
    root_main.configure(background="floralwhite")

    image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\background_img.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(root_main,image=photo)
    label.image = photo

    #-------------\\\\\---------Defining Frames---------------------#

    Title = Frame(root_main, width=1500,height=70,bd=5)
    Title.pack(side=TOP)

    path = Frame(root_main,width=200,height=200,bd=5)
    path.place(x=100,y=150)
    label = Label(path,image=photo)
    label.image = photo
    label.place(x=-10,y=-10)

    info = Frame(root_main, width=900,height=300,bd=5)
    info.place(x=500,y=480)
    label = Label(info,image=photo)
    label.image = photo
    label.place(x=-10,y=-10)

    img1 = Frame(root_main, width=420,height=460,bd=5)
    img1.place(x=50,y=400)
    image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\logo3.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(img1,image=photo)
    label.image = photo
    label.place(x=-10,y=-10)

    img2 = Frame(root_main, width=590,height=360,bd=5)
    img2.place(x=700,y=115)
    image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\logo4.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(img2,image=photo)
    label.image = photo
    label.place(x=-10,y=-10)

    global vardep,vararr,varpass,departurecityvar,arrivalcityvar
    vardep=StringVar()
    vararr=StringVar()
    varpass=StringVar()
    departurecityvar = StringVar()
    arrivalcityvar = StringVar()

    #-----------------\\\\---------------------------------------#

    Label(Title,text="Happy Skies",font=('Comic Sans MS',34),width=900,bg='black',fg='white').pack()
    Label(Title,text="We are happy to have you here!!",font=('Helvetica',20),width=1000,bg='black',fg='white').pack()



        #--------------\\--------City--------------------------------#
    airportlst = ['Select city','Ahmedabad','Chandigarh','Chennai','Cochin','Delhi','Goa','Hyderabad','Jaipur','Kolkata','Leh','Lucknow','Mumbai','Nagpur'
    ,'Patna','Port Blair','Pune','Rajkot','Srinagar','Trivandrum']
    passengerlst = [1,2,3,4,5,6,7]
    def one_way():

        Label(info,text="From",font=('Arial',10),width=20,bg='paleturquoise').place(x=70,y=20)
        
        departurecityvar.set("Select city")
        departurecity = OptionMenu(info,departurecityvar,*airportlst)
        departurecity.place(x=170,y=50)
        departurecity.config(width=10)

        Label(info,text="To",font=('Arial',10),width=20,bg='paleturquoise').place(x=300,y=20)

        arrivalcityvar.set("Select city")
        arrivalcity = OptionMenu(info,arrivalcityvar,*airportlst)
        arrivalcity.place(x=400,y=50)
        arrivalcity.config(width=10)

        

        #---------------\\-------Date--------------------------------#
        Label(info,text="Date of Departure",font=('Arial',10),width=20,bg='paleturquoise').place(x=70,y=120)
        datedep = DateEntry(info,width=20,date_pattern='dd/mm/yyyy',textvariable=vardep).place(x=150,y=150)

        lblret=Label(info,text="Date of Return",font=('Arial',10),width=20,bg='paleturquoise')
        lblret.place(x=340,y=120)
        lblret.config(state='disabled')
        datearr = DateEntry(info,width=20,date_pattern='dd/mm/yyyy')
        datearr.place(x=420,y=150)
        datearr.config(state='disabled')

        #----------------\\------Passengers------------------------------#
        Label(info,text="Passenger(s)",width=10,bg='paleturquoise').place(x=200,y=200)
        varpass.set(1)
        passmenu = OptionMenu(info,varpass,*passengerlst).place(x=280,y=200)
        Label(info,text="~ Maximum 7 passengers allowed",font=('arial',9,'italic'),bg='paleturquoise').place(x=350,y=220)

    def round_trip():

        Label(info,text="From",font=('Arial',10),width=20,bg='paleturquoise').place(x=70,y=20)
        
        departurecityvar.set("Select city")
        departurecity = OptionMenu(info,departurecityvar,*airportlst)
        departurecity.place(x=170,y=50)
        departurecity.config(width=10)

        Label(info,text="To",font=('Arial',10),width=20,bg='paleturquoise').place(x=300,y=20)

        arrivalcityvar.set("Select city")
        arrivalcity = OptionMenu(info,arrivalcityvar,*airportlst)
        arrivalcity.place(x=400,y=50)
        arrivalcity.config(width=10)

        #---------------\\-------Date--------------------------------#
        Label(info,text="Date of Departure",font=('Arial',10),width=20,bg='paleturquoise').place(x=70,y=120)
        datedep = DateEntry(info,width=20,date_pattern='dd/mm/yyyy',textvariable=vardep).place(x=150,y=150)

        Label(info,text="Date of Return",font=('Arial',10),width=20,bg='paleturquoise').place(x=340,y=120)
        datearr = DateEntry(info,width=20,date_pattern='dd/mm/yyyy',textvariable=vararr).place(x=420,y=150)

        #----------------\\------Passengers------------------------------#
        Label(info,text="Passenger(s)",width=10,bg='paleturquoise').place(x=200,y=200)
        varpass.set(1)
        passmenu = OptionMenu(info,varpass,*passengerlst).place(x=280,y=200)
        #entpass = Entry(info,width=5,justify='right',font=('Comic Sans Ms',10),textvariable=varpass).place(x=280,y=200)
        Label(info,text="~ Maximum 7 passengers allowed",font=('arial',9,'italic'),bg='paleturquoise').place(x=350,y=220)


    #--------------------button--------------------------------------#
    Button(info,text="Search Flights",font=('Helvetica',13),width=70,command=validatesearch).place(x=120,y=260)
    #-------------------\\\\-------------------------------------#
    Button(path,text="One Way",font=('Helvetica',13),width=10,command=one_way,bd=2).place(x=40,y=25)
    Button(path,text="Round Trip",font=('Helvetica',13),width=10,command=round_trip,bd=2).place(x=40,y=105)



    root_main.mainloop()

#--------------------------Login--------------------------------#
def destroot():
    try:
        root.destroy()
    except:
        root_regist.destroy()
    finally:
        login()
def login():
        def valloginclick():
            global loginSkipped
            loginSkipped = 1
            main_page()
        def validatelogin():
                global loginSkipped
                loginSkipped = 0
                USERNAME = unamevar.get().upper()
                PASSWORD = psswdvar.get()
                flag=0

                if (USERNAME and PASSWORD) == '':
                        messagebox.showerror("Error","PLEASE FILL IN THE EMPTY BOXES")
                else:
                        try:
                                getname = ("SELECT * from happyusers where pname=%s")
                                c.execute(getname,(USERNAME, ))
                                global currlogin
                                currlogin = c.fetchone()
                                getpaswd = ("SELECT psswd from happyusers where pname=%s")
                                c.execute(getpaswd,(USERNAME, ))
                                paswd = str(c.fetchone()[0])
                                if PASSWORD != paswd:
                                    messagebox.showerror("Error","INVALID CREDENTIALS")
                                else:
                                    main_page()
                        except:
                                print("Error")
        
        global root_login
        root_login=Tk()
        root_login.geometry('1000x1000+300+10')
        root_login.title("Login")
        
        image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\dwnld1.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.place(x=0,y=0)

        Label(root_login, text="Planning to go somewhere??",font=('Times', 25)).place(x=300,y=33)

        Label(root_login, text="Please login to proceed!!",font=('Helvetica',16)).place(x=355,y=100)

        unamevar = StringVar()
        psswdvar = StringVar()
        Label(root_login,text='Name:',width=30,bg='black',fg='white',font=('Times', 15)).place(x=320,y=250)
        Entry(root_login,font=(12),textvariable=unamevar).place(x=370,y=290)

        Label(root_login,text='Password:',width=30,bg='black',fg='white',font=('Times', 15)).place(x=320,y=370)
        Entry(root_login,show='*',font=(12),textvariable=psswdvar).place(x=370,y=410)


        Button(root_login, text='Login',width=10,height=1,bg='SeaGreen1',font=('Helvetica',15),command=validatelogin).place(x=430,y=480)
        Button(root_login, text='Skip Login',width=10,height=1,bg='SeaGreen1',font=('Helvetica',15),command=valloginclick).place(x=430,y=520)


        regi = Label(root_login,text="Don't have an account? Register here.")
        regi.place(x=700,y=700)
        regi.bind("<Button-1>",registration)
        root_login.mainloop()

#-----------------------------Registration--------------------------#

def registration(event):
    def validateregist():
        pattern=re.compile(r'@' and r'.com')
        FULLNAME=varfname.get().upper()
        PHONENO=varphnno.get()
        EMAIL=varemail.get()
        GENDER=vargend.get()
        PASSWORD=varpsswd.get()
        PASSWORD1=varpsswdre.get()
        ADDRESS=varaddress.get()
        flag=0
#-----------       
        if (FULLNAME and PHONENO and EMAIL and GENDER and PASSWORD and PASSWORD1 and ADDRESS) == '':
             messagebox.showerror("Error", "PLEASE FILL ALL THE FIELDS")
        else:
            try:
                assert len(PHONENO)==10 and type(int(PHONENO)) == int
            except:
                flag=1
                messagebox.showerror("Error", "ENTER A VALID CONTACT NUMBER")
            
            if pattern.search(EMAIL):
                pass
            else:
                flag=1
                messagebox.showerror("Error", "ENTER A VALID EMAIL")
            if PASSWORD != PASSWORD1:
                flag=1
                messagebox.showerror("Error", "BOTH PASSWORDS DO NOT MATCH")
            else:
                try:
                    assert len(PASSWORD)>=8
                except:
                    flag=1
                    messagebox.showerror("Error", "ENTER A VALID PASSWORD ")

            if flag == 0:
                try:
                    registering = "INSERT INTO happyusers(pname,phno,email,gender,psswd,addr) VALUES(%s,%s,%s,%s,%s,%s)"
                    registerer = (FULLNAME,PHONENO,EMAIL,GENDER,PASSWORD,ADDRESS)
                    c.execute(registering,registerer)
                    sqlcommit()
                    messagebox.showinfo("Success","YOU ARE NOW A HAPPYUSER\nLUCKY TO HAVE YOU!!")
                    main_page()
                except:
                    messagebox.showerror("SQL ENTRY ERROR", "RE-CHECK THE ENTRIES MADE.")

    try:
        root_login.destroy()
    except:
        pass
    finally:
        global root_regist
        root_regist = Tk()
        root_regist.geometry('1080x1080+290+10')
        root_regist.title("Registration")


        image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\plane_4.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(root_regist,image=photo)
        label.image = photo # keep a reference!
        label.place(x=0,y=0)

        Label(root_regist, text="Registration",width=10,font=('Times', 25)).place(x=420,y=33)

        Label(root_regist, text="Hello, New user...Make sure you register here before starting.",font=('Helvetica',10)).place(x=323,y=100)

        varfname=StringVar()
        varphnno=StringVar()
        varemail=StringVar()
        vargend=StringVar()
        vargend.set(False)
        varpsswd=StringVar()
        varpsswdre=StringVar()
        varaddress=StringVar()

        Label(root_regist, text="Full Name",width=20,font=('Times', 15)).place(x=290,y=150)

        entry_1 = Entry(root_regist,font=('Comic Sans MS',12),textvariable=varfname)
        entry_1.place(x=520,y=150)

        Label(root_regist, text="Phone No.",width=20,font=('Times', 15)).place(x=290,y=200)

        entr_1 = Entry(root_regist,font=('Comic Sans MS',12),textvariable=varphnno)
        entr_1.place(x=520,y=200)

        Label(root_regist, text="E-mail",width=20,font=('Times', 15)).place(x=290,y=250)

        entry_2 = Entry(root_regist,font=('Comic Sans MS',12),textvariable=varemail)
        entry_2.place(x=520,y=250)

        Label(root_regist, text="Gender",width=20,font=('Times', 15)).place(x=290,y=300)

        Radiobutton(root_regist, text="Male",padx = 5, variable=vargend, value='male',font=('Helvetica',10)).place(x=520,y=300)
        Radiobutton(root_regist, text="Female",padx = 20, variable=vargend, value='female',font=('Helvetica',10)).place(x=590,y=300)
        Radiobutton(root_regist, text="Others",padx = 35, variable=vargend, value='others',font=('Helvetica',10)).place(x=705,y=300)

        Label(root_regist, text="New Password",width=20,font=('Times', 15)).place(x=290,y=350)
        
        Entry(root_regist,font=('Comic Sans MS',12),textvariable=varpsswd,show='*').place(x=520,y=350)

        Label(root_regist, text="~ Minimum 8 characters",width=20,font=('Times',12,'italic')).place(x=750,y=370)

        Label(root_regist, text="Re-Enter Password",width=20,font=('Times', 15)).place(x=290,y=390)
        
        Entry(root_regist,font=('Comic Sans MS',12),textvariable=varpsswdre,show='*').place(x=520,y=390)

        Label(root_regist, text="Address",width=20,font=('Times', 15)).place(x=290,y=440)
        
        Entry(root_regist,font=('Comic Sans MS',12),textvariable=varaddress).place(x=520,y=440)


        Button(root_regist, text='Register',width=20,bg='brown',fg='white',font=('Helvetica',11),command=validateregist).place(x=420,y=520)
        
        Button(root_regist, text='<= Back to Login',width=15,bg='brown',fg='white',font=('Verdana',11),command=destroot).place(x=20,y=20)

        Label(root_regist,text="By joining you agree to our Terms & Conditions").place(x=400,y=720)

        
        root_regist.mainloop()

#----------------------------Opening page-----------------------#

root=Tk()
root.geometry('530x500+500+150')
root.title("Happy Skies")
root.configure(background='white')
#root.after(5000,destroot)

image = Image.open("F:\\SEM-2\\PP\\PP_project_final\\images\\start_page.png")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image=photo
label.place(x=10,y=15)

Button(root,text="Skip >>",width=10,bg='turquoise',command=destroot).place(x=420,y=450)


Label(root,text="Happy Skies Pvt. Ltd is an award winning Airline and one of the India's largest tour operator\nhelping travel enthusiasts across the country dicover India's most amazing destinations.\nOur team of 250+ travel consultants help you handcraft holiday of a lifetime.\nWe are a one-stop travel solution and have planned vacations\nsuccessfully for more than 1,55,000 families.",font=('Comic Sans MS',9),width=75,height=8,bg='white').place(x=0,y=0)


root.mainloop()
conn.close()