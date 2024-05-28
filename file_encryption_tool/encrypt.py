import customtkinter
import sqlite3
from CTkMessagebox import CTkMessagebox 
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import bcrypt
import random
import smtplib
from subprocess import call
from tkinter.messagebox import askyesno
from tkinter import Tk
import re

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
#style = ttk.Style(self.master)
#root =customtkinter.CTk()
#root.geometry("500*350")
app=customtkinter.CTk()
app.title=('login')
app.geometry('500x550')

font1 = ('Helvetica',25,'bold')
font2 = ('Arial',17,'bold')
font3 = ('Arial',13,'bold','underline')
font4 = ('Arial',13, 'bold','underline')

#######################################################
conn = sqlite3.connect("newdata.db")
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS newdata (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
            )
            """)
def signup():
    username = entry1.get()
    password = entry2.get()
    is_valid = False

    if username != '' and password != '':
        cur.execute("SELECT username FROM newdata where username=? ",[username])
        if cur.fetchone() is not None:
            messagebox.showerror('Error','Username already exists.')
        else:    
            if len(entry2.get()) <6:
              refuse2_label = customtkinter.CTkLabel(frame1, font=font1, text='Password must be : \n > 6 characters',text_color='red')
              refuse2_label.pack(pady=12,padx=10)
            else:
             
             encoded_password = password.encode('Utf-8')
             hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
             cur.execute('INSERT INTO newdata(username,password) VALUES (?, ?)',[username, hashed_password])           
             conn.commit()
             messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error','Enter all data !')

def login_account():
    username = entry1.get()
    password = entry2.get()
    if username !='' and password !='':
        cur.execute('SELECT password FROM newdata WHERE username=?', [username])
        result = cur.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'),result[0]):
                frame2.destroy()
                messagebox.showinfo('Success','Logged in successfully.')
                app.destroy()
                call(["python","main.py"])
            else:
                messagebox.showerror('Error', 'Invalid Password')
        else:
            messagebox.showerror('Error','Username does not Exist.')
    else:
        messagebox.showerror('Error','Enter all data')


def login():
    frame0.destroy()
    global frame2
    frame2 = customtkinter.CTkFrame(app, bg_color='#001220',fg_color='#001220',width=470,height=360)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    login_label=customtkinter.CTkLabel(frame2,font=font3,text='Already have an account?', text_color='#fff', bg_color='#001220')
    login_label.pack(pady=12,padx=10)

    global entry1
    global entry2

    entry1 = customtkinter.CTkEntry (master=frame2, placeholder_text="username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry (master=frame2, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    login_button2 = customtkinter.CTkButton (master=frame2, text="Login", command=login_account)
    login_button2.pack(pady=12,padx=10)

def confirm():
    ans = askyesno(title='Exit', message='Do you want To Exit ?')
    if ans:
        app.destroy()

app.protocol("WM_DELETEWINDOW",confirm)
##############################################################################
#--------------------------------FRAME FOR REQUESTING OTP--------------------#
def frame_otp():
    frame0.destroy()
    global frameotp
    frameotp=customtkinter.CTkFrame(master=app)
    frameotp.pack(pady=20, padx=60,fill="both", expand=True)

    global codeEntry
    admin_verify = customtkinter.CTkLabel(master=frameotp, text="IN ODER TO CREATE ACCOUNT:\n\n 1.Click on the RED button\n\n  2.Contact ICT Admin for Code\n\n 3.Enter The Code Given by ICT Admin\n\n 4.Verify and Proceed Creating Account",font=("Roboto", 16))
    admin_verify.pack(pady=12, padx=50,fill="both", expand=True)

    sendOTP = Button(master=frameotp, text="send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="red", fg="white", command=connectingSender)
    sendOTP.pack(pady=12, padx=10,fill="both", expand=True)

    otpMsg = customtkinter.CTkLabel(master=frameotp, text="OTP", font=('Roboto', 16))
    otpMsg.pack(pady=12, padx=10,fill="both", expand=True)

    codeEntry = Entry(master=frameotp, width=6, font=("Arial", 20), borderwidth=0, show="*")
    codeEntry.pack(pady=12, padx=10,fill="both", expand=True)

    verify = Button(master=frameotp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="green", fg="white",command=checkOTP)
    verify.pack(pady=12, padx=10,fill="both", expand=True)

def back_frame0():
    frame1.destroy()
    global frame0
    frame0=customtkinter.CTkFrame(master=app)
    frame0.pack(pady=20, padx=60,fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame0,text="Encryption and Decryption Tool", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    signup_label=customtkinter.CTkLabel(frame0, font=font1, text='Sign up',text_color='#001220')
    signup_label.pack(pady=12,padx=10)

    signup_button = customtkinter.CTkButton (master=frame0, text="Sign up", cursor='hand2', command= frame_otp)
    signup_button.pack(pady=12,padx=10)

    login_label=customtkinter.CTkLabel(frame0,font=font3,text='Already have an account?', text_color='#fff', bg_color='#001220')
    login_label.pack(pady=12,padx=10)

    login_button = customtkinter.CTkButton (master=frame0, text="Login", command=login)
    login_button.pack(pady=12,padx=10)

def frame_1():
    global frame1
    frame1=customtkinter.CTkFrame(master=app)
    frame1.pack(pady=20, padx=60,fill="both", expand=True)
    #frame1.place(x=40,y=40)

    label = customtkinter.CTkLabel(master=frame1,text="Encryption and Decryption Tool", font=("Roboto", 24))
    label.pack(pady=12, padx=10)
    
    global entry1
    global entry2
    entry1 = customtkinter.CTkEntry (master=frame1, placeholder_text="username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry (master=frame1, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    signup_label=customtkinter.CTkLabel(frame1, font=font1, text='Sign up',text_color='#001220')
    signup_label.pack(pady=12,padx=10)

    signup_button = customtkinter.CTkButton (master=frame1, text="Sign up", cursor='hand2', command=signup)
    signup_button.pack(pady=12,padx=10)

    login_label=customtkinter.CTkLabel(frame1,font=font3,text='Already have an account?', text_color='#fff', bg_color='#001220')
    login_label.pack(pady=12,padx=10)

    login_button = customtkinter.CTkButton (master=frame1, text="back", command=back_frame0)
    login_button.pack(pady=12,padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame1, text="Remember Me")
    checkbox.pack(pady=12,padx=10)

###########################################################################
frame0=customtkinter.CTkFrame(master=app)
frame0.pack(pady=20, padx=60,fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame0,text="Encryption and Decryption Tool", font=("Roboto", 24))
label.pack(pady=12, padx=10)

signup_label=customtkinter.CTkLabel(frame0, font=font1, text='Sign up',text_color='#001220')
signup_label.pack(pady=12,padx=10)

signup_button = customtkinter.CTkButton (master=frame0, text="Sign up", cursor='hand2', command= frame_otp)
signup_button.pack(pady=12,padx=10)

login_label=customtkinter.CTkLabel(frame0,font=font3,text='Already have an account?', text_color='#fff', bg_color='#001220')
login_label.pack(pady=12,padx=10)

login_button = customtkinter.CTkButton (master=frame0, text="Login", command=login)
login_button.pack(pady=12,padx=10)

#########################################################################
#-------GENERATING OTP CODE---------#
def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
    return randomCode


sender = 'alvinokiya7@gmail.com'
password = 'zllv keln aubi wubj'
code = generateOTP()


def connectingSender():
    receiver = 'okiyaalvin@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    sendingMail(receiver, server)


def sendingMail(receiver, server):
    msg = 'Hello! \n This is your OTP  ' + code
    server.sendmail(sender, receiver, msg)
    server.quit()


def checkOTP():
    if code == codeEntry.get():
        messagebox.showinfo('Successful Verification')
        frameotp.destroy()
        return frame_1()
    else:
        messagebox.showerror('Verification Unsuccesful ! \n Kindly enter the correct code \n or contact ICT support')


#############################################################################
app.mainloop()

