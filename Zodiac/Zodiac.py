from tkinter import *
import datetime
from datetime import*
import tkinter.messagebox as tkMessageBox


def main():
    get_date = num1.get()

    if (get_date == ""):
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        string_date = str(num1.get())
        string_date = string_date+" 2020"
        date_format = '%b %d %Y'

        convert_date = datetime.strptime(string_date,date_format)

        if convert_date <= datetime(2020,12,19) and convert_date <= datetime(2020,1,19) or convert_date >= datetime(2020,12,20) :
        	sa = PhotoImage(file='img\\sa.png')
        	lbl = Label(root, image=sa)
        	lbl.img = sa
        	lbl.place(x=540, y=45)
        	print("Your Zodiac Sign is Sagittarius")

        elif convert_date >= datetime(2020,1,20) and convert_date <= datetime(2020,2,16) :
            cap = PhotoImage(file='img\\cap.png')
            lbl = Label(root, image=cap)
            lbl.img = cap
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Capricornus")
     
        elif convert_date <= datetime(2020,3,12) :
            aq = PhotoImage(file='img\\aq.png')
            lbl = Label(root, image=aq)
            lbl.img = aq
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is aquarius")

        elif convert_date <= datetime(2020,4,19):
            pi = PhotoImage(file='img\\pi.png')
            lbl = Label(root, image=pi)
            lbl.img = pi
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Pisces")

        elif convert_date <= datetime(2020,5,14):
            ar = PhotoImage(file='img\\ar.png')
            lbl = Label(root, image=ar)
            lbl.img = ar
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Aries")

        elif convert_date <= datetime(2020,6,21):
            ta = PhotoImage(file='img\\ta.png')
            lbl = Label(root, image=ta)
            lbl.img = ta
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Taurus")

        elif convert_date <= datetime(2020,7,21):
            ge = PhotoImage(file='img\\ge.png')
            lbl = Label(root, image=ge)
            lbl.img = ge
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Gemini")

        elif convert_date <= datetime(2020,8,11):
            ca = PhotoImage(file='img\\ca.png')
            lbl = Label(root, image=ca)
            lbl.img = ca
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Cancer")

        elif convert_date <= datetime(2020,9,17):
            le = PhotoImage(file='img\\le.png')
            lbl = Label(root, image=le)
            lbl.img = le
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Leo")

        
        elif convert_date <= datetime(2020,10,31):
            vi = PhotoImage(file='img\\vi.png')
            lbl = Label(root, image=vi)
            lbl.img = vi
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Virgo")



        elif convert_date <= datetime(2020,11,22):
            li = PhotoImage(file='img\\li.png')
            lbl = Label(root, image=li)
            lbl.img = li
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Libra")

        elif convert_date <= datetime(2020,11,30):
            sc = PhotoImage(file='img\\sc.png')
            lbl = Label(root, image=sc)
            lbl.img = sc
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Scorpius")

        elif convert_date <= datetime(2020,12,18):
            op = PhotoImage(file='img\\op.png')
            lbl = Label(root, image=op)
            lbl.img = op
            lbl.place(x=540, y=45)
            print("Your Zodiac Sign is Ophiuchus")

        else:
            print("Incorrect Birthday and BirthMonth")


def reset():
    num1.set("")


root = Tk()
root.geometry('900x300')
root.resizable(height=False,width=False)
root.title("")

num1 = StringVar()

Label(root,text="Zodiac Sign",bg='black',fg="white",font='Monospace 20 bold').pack(fill=X)

lmonth = Label(root, text="Birth Date : " ,font = "Monospace 20 bold")
lmonth.place(x= 40,y= 130)

month = Entry(root,font="Monospace 15",textvariable=num1)
month.place(x=220,y=130)


btn = Button(root,text="Enter",padx=5,font="Monospace 15 bold",bg="Green",width=5,command= main)
btn.place(x=220,y=180)

btn1 = Button(root,text="Reset",padx=5,font="Monospace 15 bold",bg="Green",width=5,command= reset)
btn1.place(x=370,y=180)




root.mainloop()
