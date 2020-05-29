from tkinter import *
from tkinter import ttk
from random import *
from tkinter.messagebox import showinfo
from tkcalendar import *
from captcha.image import ImageCaptcha
import sqlite3
image = ImageCaptcha()
data = image.generate('Uzumpuk')
image.write("Uzumpuk","1.png")
root = Tk()
root.title("Recharge System")
root.geometry("795x500+120+120")
#root.resizable(0,0)
global noentry
global otpentry

#global sims
#CREATE DATABASE
conn = sqlite3.connect('Recharge Records.db')
#CREATE CURSOR
c = conn.cursor()

#create table
#c.execute("""CREATE TABLE recharge(sim_card text,prize integer,mobile_no text)""")





#---------Second Page--------
def next():
    if (userentry.get()==""and passentry.get()==""):
        showinfo("Error","Please fill the all details")
    elif (userentry.get()=='Sumit'and passentry.get()=='sumit123'):

        top = Toplevel()
        top.configure(bg="Sky Blue")
        top.wm_iconbitmap("Mobile.ico")
        top.geometry("795x500+120+120")
        top.title("Networks")
        Label(top, text="Select Your NetWork:", font=("courier 13 bold"), bg="Sky Blue").grid(row=0, column=1)
        simcard = ["Airtel", "idea", "Vodafone", "Aircel", "jio"]
        sims = ttk.Combobox(top, width=27, values=simcard, font=("lucida 12"))
        sims.grid(row=0, column=2)
        Label(top, text="Select Your Plan:", font=("courier 13 bold"), pady=30, bg="Sky Blue").grid(row=1, column=1)
        plans = ["100", "175", "199", "249", "399", "449", "499", "999"]
        prize = ttk.Combobox(top, width=27, values=plans, font="lucida 12")
        prize.grid(row=1, column=2)
        Label(top,text="Enter Mobile Number:", font=("courier 13 bold"), pady="20", bg="Sky Blue").grid(row=2,
                                                                                                         column=1)
        mobileentry = StringVar()
        mobile_no = Entry(top,textvariable = mobileentry, font=("lucida 12"), width=25, insertborderwidth=10)
        mobile_no.grid(row=2, column=2)

        def show():
            # sims.delete(0,END)
            # prize.delete(0,END)
            # mobile_no.delete(0,END)

            # CREATE DATABASE
            conn1 = sqlite3.connect('Mobile Recharge.db')
            # CREATE CURSOR
            c1 = conn1.cursor()

            # c1.execute("""CREATE TABLE details(sim_card text,prize integer,mobile_no text)""")

            c1.execute("SELECT *, oid FROM details")
            record = c1.fetchall()
            print(record)
            # c1.execute("DELETE *,oid FROM records")
            conn1.commit()
            conn1.close()

        def pay():
            if(sims.get()==""and prize.get()==""and mobile_no.get()=="" ):
                showinfo("Error","Please fill the all details")

            else:

                # CREATE DATABASE
                conn1 = sqlite3.connect('Mobile Recharge.db')
                # CREATE CURSOR
                c1 = conn1.cursor()

                # c1.execute("""CREATE TABLE details(sim_card text,prize integer,mobile_no text)""")
                c1.execute("INSERT INTO details VALUES(:sim_card, :prize, :mobile_no)",
                           {
                               'sim_card': sims.get(),
                               'prize': prize.get(),
                               'mobile_no': mobile_no.get()
                           })
                conn1.commit()

#--------------------Online Payment Page-------------------------------------#
                top1 = Toplevel()
                top1.geometry("795x500+120+120")
                top1.title("Online Payment")
                top1.configure(bg="Orange")
                top1.wm_iconbitmap("Mobile.ico")
                Label(top1, text="Card Number:", font=("Century 15 bold"), bg="Orange").grid(row=0, column=0)
                cardentry = IntVar()
                card = Entry(top1, text=cardentry, width=20, font=("Arial 14"))
                card.grid(row=0, column=1)
                Label(top1, text="First Name:", font=("Century 15 bold"), pady=20, bg="Orange").grid(row=1, column=0)
                nameentry = StringVar()
                f_name = Entry(top1, text=nameentry, width=20, font=("Georgia 14"))
                f_name.grid(row=1, column=1)
                Label(top1, text="Last Name:", font=("Century 15 bold"), padx=10, bg="Orange").grid(row=1, column=2)
                lastnamenetry = StringVar()
                l_name = Entry(top1, text=lastnamenetry, width=20, font=("Georgia 14"))
                l_name.grid(row=1, column=3)
                Label(top1, text="CVV:", font=("Century 15 bold"), pady=30, bg="Orange").grid(row=2, column=0)
                cvventry = IntVar()
                cvv = Entry(top1, text=cvventry, width=10, font=("Arial 14"))
                cvv.grid(row=2, column=1)

                Label(top1, text="Expiry Date:", font=("Century 15 bold"), bg="Orange").grid(row=2, column=2)
                date = DateEntry(top1, width=10, background="Black", foreground="green", borderwidth=3,
                      font=("Arial 10 bold"))
                date.grid(row=2,column=3)

                def paynow():
                    if(card.get()==""and f_name.get()==""and l_name.get()==""and cvv.get()==""and date.get()==""):
                        showinfo("Error", "Please fill the all details")
                    else:
                        showinfo("Message", "Your Recharge has been successfully credited")


                Button(top1, text="Pay now", bg="Yellow", fg="black", width=10, height=1, font=("Arial 10 bold"),
                   command=paynow).grid(row=3, column=1)
                Button(top1,text = "Cancel",bg = "sky blue",fg = "blue",width = 10,height = 1,font = ("Arial 10 bold"),command = top1.destroy).grid(row = 3,column = 2)

        def reset():
            sims.delete(0,END)
            prize.delete(0,END)
            mobile_no.delete(0,END)
        Button(top, text="Confirm & Pay", width=10, height=1, font=("Arial 10"), bg="light green", command=pay).grid(
            row=3, column=1)

        Button(top, text="Reset", width=10, height=1, font=("Arial 10"), bg="light green",command = reset).grid(row=3, column=3)



#-----------------------Get OTP Page---------------------------#
        def otp1():
            # CREATE DATABASE
            conn1 = sqlite3.connect('Mobile Recharge.db')
            # CREATE CURSOR
            c1 = conn1.cursor()

            # c1.execute("""CREATE TABLE details(sim_card text,prize integer,mobile_no text)""")
            c1.execute("INSERT INTO details VALUES(:sim_card, :prize, :mobile_no)",
                       {
                           'sim_card': sims.get(),
                           'prize': prize.get(),
                           'mobile_no': mobile_no.get()
                       })
            conn1.commit()
            top2 = Toplevel()
            top2.title("OTP Page")
            top2.geometry("795x500+120+120")
            top2.configure(bg="orange")
            top2.wm_iconbitmap("Mobile.ico")
            Label(top2, text="Enter Valid OTP:", font=("TimesNewRoman 15 bold"), pady=20, bg="orange").grid(row=0,
                                                                                                            column=1)
            otpentry = StringVar()
            e1 = Entry(top2, textvariable=otpentry, width=20, font=("Arial 12 bold"))
            e1.grid(row=0, column=2, padx=20)

            def otp():
                otp4 = ""
                for i in range(4):
                    otp4 += str(randint(1, 9))
                print("Your One Time PassWord is")
                print(otp4)

                def submit_otp():
                    if (e1.get() == otp4):
                        e1.delete(0,END)

                        showinfo("Recharge", "Your Recharge Is Successfull")
                    else:
                        e1.delete(0, END)
                        showinfo("Error", "Please Enter a Valid OTP")

                Button(top2, text="Submit", width=10, font=("lucida 14 bold"), command=submit_otp, bg="red",
                       fg="black").grid(row=1, column=2,
                                        pady=20)

            otp()
        Button(top, text="Show Records", width=10, height=1, font=("Arial 10"), bg="light green",
                   command=show).grid(
                row=4, column=2, pady=20)

        Button(top, text="Get OTP", width=10, height=1, font=("Arial 10"), bg="light green", command=otp1).grid(row=3,column=2)
    else:
        showinfo("Error","Please Enter a Correct Username or password")


#--------First Page--------#
user = Label(root,text = "Username:",font = "TimesNewRoman 17 bold",fg = "Green",bg = "black").grid(row = 4,column = 3)
password = Label(root,text = "Password:",font = "TimesNewRoman 17 bold",fg = "Green",bg = "black").grid(row = 5,column = 3)
userentry = StringVar()
passentry = StringVar()
Entry(root,textvariable = userentry,width = 25,fg = "red",bg = "White",font = ("Arial 14")).grid(row =4,column=5,padx = 20)
Entry(root,textvariable = passentry,width = 25,fg = "black",bg = "White",font = ("Arial 14"),show = "*").grid(row = 5,column = 5,padx = 20)

Button(root,text = "Login",width = 15,height = 1,font = ("courier 13 bold"),fg = "dark red",bg = "grey",command = next).grid(row = 6,column = 5,pady = 20)
root.configure(bg = "Black")
root.wm_iconbitmap("Mobile.ico")
photo = PhotoImage(file = "images.png")
w = Label(root,image = photo).grid(row = 7,column = 7)

root.mainloop()