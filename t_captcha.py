from tkinter import*
from tkinter import messagebox
import tkinter
import datetime
import time
import socket
import random
top=tkinter.Tk()
import sqlite3
var_time=time.time()
def data_entry():
     global conn,cursor
     cap_db=sqlite3.connect('Access.db')
     cursor=cap_db.cursor()
     cursor.execute('CREATE TABLE IF NOT EXISTS Entry(Registration_no int,Time text,IP_Address text)')
     cursor.execute('INSERT INTO Entry VALUES(?,?,?)',(Reg_ent.get(),str(datetime.datetime.fromtimestamp(var_time).strftime('%Y-%m-%d %H:%M:%S')),socket.gethostbyname(socket.gethostname())))
     cap_db.commit()
     cursor.close()
     cursor.close() 
code=''
def gen_cap():
  n=''
  for i in range(0,6):
      cap=random.randint(1,3)
      if(cap==1):
          value=random.randint(97,122)
          n+=chr(value)
      elif(cap==2):
          value=random.randint(65,90)
          n+=chr(value)
      else:
          value=random.randint(48,57)
          n+=chr(value)
  return n
def check():
      ck=ent_cap.get()
      ent_cap.delete(0,END)
      global code
      r=Reg_ent.get()
      if(r.isdigit() and (len(r)==8 or len(r)==5)):
            Rgn=Reg_ent.get()
      else:
            messagebox.showinfo("ERROR","Reg no. Not valid")
            Reg_ent.delete(0,END)
            return 0
      if(ck==code):
            messagebox.showinfo("ACCESS","Registation no. : %s \n Accessed Successfully"%Rgn)
            data_entry()
      else :
            messagebox.showinfo("ERROR","Wrong captcha")
            g=gen_cap()
            code=g
            display()
            c.create_text(160,40,text=g,font='Calibri 28 bold')
            c.grid(row=3,column=10)
            see=tkinter.Label(top,text='re-enter : ',font='Times 10')
            see.grid(row=6,column=10)
def display():
      c.create_rectangle(80,10,240,70,fill='white')
      c.create_line(80,20,230,50)
      c.create_line(85,55,180,25)
      c.create_line(150,10,170,70)
      c.create_line(100,65,240,40)
def valid():
    r=Reg_ent.get()
    if(r.isdigit() and len(r)==8):
        conitnue
    else:
        messagebox.showinfo("ERROR","Reg no. Not valid")
        Reg_ent.delete(0,END)
def reset1():
      ent_cap.delete(0,END)
      global code
      g=gen_cap()
      code=g
      display()
      c.create_text(160,40,text=g,font='Calibri 28 bold')
      c.grid(row=3,column=10)
code=gen_cap()
Reg=tkinter.Label(top,text='Registration Number : ',font='Times 13')
Reg.grid(row=1,column=10,sticky=E)
Reg_ent=Entry(top)
Reg_ent.grid(row=1,column=11)
top.geometry('450x220')
top.title("PASSWORD REMINDER")
c=Canvas(top,height=80,width=240)
display()
c.create_text(160,40,text=code,font='Calibri 28 bold')
c.grid(row=3,column=10)
see=tkinter.Label(top,text='Type the code you see above : ',font='Times 10')
see.grid(row=4,column=10)
ent_cap=Entry(top)
ent_cap.grid(row=5,column=10)
submit=tkinter.Button(top,text='Submit',relief=GROOVE,command=check,height=2,width=15,bg='lightblue')
submit.grid(row=7,column=10)
img=PhotoImage(file="reload.png")
reset=tkinter.Button(top,text='Reload',relief=GROOVE,height=20,width=30,bg='blue',image=img,command=reset1)
reset.grid(row=3,column=11)
top.mainloop()
