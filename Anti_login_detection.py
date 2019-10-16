# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:47:45 2019
lets code
@author: Anson
"""
import tkinter
import cv2
import PIL.ImageTk, PIL.Image 
def but1():
    global label1
    global e
    global b3
    b1.destroy()
    label1=tkinter.Label(window,text="Enter Your Password",font=("Aerospace",'15'))
    label1.pack(pady=12,padx=0)
    v=tkinter.StringVar()
    e=tkinter.Entry(window,textvariable=v)
    e.pack()
    b3=tkinter.Button(window,text="OK",fg="red",bg="black",height=1,width=2,font=("Aerospace",'15'))
    b3.pack()
    b3.configure(command=but2)

def but2():
    global c
    c=e.get()
    print(c)
    b='qwerty'
    label1.destroy()
    b3.destroy()
    e.destroy()
    if(b==c):
        new=tkinter.Label(window,text="Access Granted",fg="green",font=("Aerospace",'30'))
        new.pack(pady=12,padx=0)
    else:
        news=tkinter.Label(window,text="Access Denied",fg="red",font=("Aerospace",'30'))
        news.pack(pady=12,padx=0)
        cap=cv2.VideoCapture(0)
        while True:
            d,frame=cap.read()
            cv2.imshow("video",frame)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray video",gray)
            k=cv2.waitKey(0)
            if(k==27):
                cv2.imwrite(r'C:\Users\Anson\Desktop\python\anzz.jpg',frame)
                cv2.destroyAllWindows()
                cap.release()
                break
            
def quit():
     window.destroy()

window=tkinter.Tk()
window.geometry("19280x1080")
window.title("Welcome")
img=cv2.imread("D:\IMG_20190404_211256_220w.jpg")
img=cv2.resize(img,(200,350))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
height,width,no_channels=img.shape
canvas=tkinter.Canvas(window,width=width,height=height)
canvas.pack()
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
label=tkinter.Label(window,text="Anson",font=("7th Service Italic",'20'))
label.pack()
b1=tkinter.Button(window,text="Login",bg="red",font=("Aerospace",'15'))
b1.config(height=1,width=5)
b1.configure(command=but1)
b1.pack(pady=10)
b2=tkinter.Button(window,text="ShutDown",fg="red",bg="black",height=1,width=9,font=("Aerospace",'15'),command=quit)
b2.pack(side=tkinter.RIGHT,padx=100,pady=100)
window.mainloop()



import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
fromaddr = "sender mail"
toaddr = "mariaansona@gmail.com"
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Security Breach"
body = "Someone is trying to inflitrate your system. The person's picture is as follows"
msg.attach(MIMEText(body, 'plain')) 
filename = "anzz.jpg"
attachment = open(r"C:\Users\Anson\Desktop\python\anzz.jpg", "rb") 
p = MIMEBase('image', 'plain') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "password") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 
