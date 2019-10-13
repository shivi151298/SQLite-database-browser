from tkinter import *
from tkinter import filedialog
import sqlite3 as s
import os
scr=Tk()
def opens():
    global cu
    global client
    name=filedialog.askopenfilename()
    if name.endswith('.db'):
        client=s.connect("d:/database1.db")
        cu=client.cursor()
        cu.execute('''SELECT 
    name
 FROM 
     sqlite_master 
WHERE 
    type ='table' AND 
    name NOT LIKE "sqlite_%"''')
        l=[]
        for i in cu.fetchall():
            l.append(i[0])
        for i,j in enumerate(l):
            listbox.insert(i,j)
def create_(dbname):
    if str(dbname.endswith('.db')):
        global client
        global cu
        client=s.connect(dbname)
        cu=client.cursor()

def create():
    w=Toplevel(scr,bg='cyan',bd=4)
    e=Entry(w,bg='lightpink',bd=4,width=4,relief=SUNKEN)
    e.pack()
    b5=Button(w,bd=4,bg='lightpink',width=4,font=('times',20,"bold"),text='create',relief=SUNKEN,command=lambda:create_(e.get()))
    b5.pack()
def delete_(dbname):
    os.remove(dbname)

def delete():
    w=Toplevel(scr,bg='cyan',bd=4)
    e=Entry(w,bg='lightpink',bd=4,width=4,relief=SUNKEN)
    e.pack()
    b5=Button(w,bd=4,bg='lightpink',width=4,font=('times',20,"bold"),text='delete',relief=SUNKEN,command=lambda:delete_(e.get()))
    b5.pack()

def fun():
    global result
    fo.delete('1.0',END)
    sel(listbox)
    l=[','.join([str(j) for j in i]) for i in list(result)]
    print(l)
    fo.insert('1.0',"\n".join(l))

scr.geometry('1350x750+0+0')
b1=Button(scr,text='open',bd=4,bg='lightpink',width=4,font=('times',20,'bold'),command=opens)
b1.grid(row=0,column=0)
b2=Button(scr,text='create',bd=4,bg='lightpink',width=4,font=('times',20,'bold'),command=create)
b2.grid(row=0,column=1)
b3=Button(scr,text='delete',bd=4,bg='lightpink',width=4,font=('times',20,'bold'),command=delete)
b3.grid(row=0,column=2)
f=Frame(scr,bg='white',bd=4,height=600,width=300,relief=GROOVE)
f.place(x=0,y=50)
fo=Text(scr,bg='white',bd=4,height=500,width=600,relief=GROOVE)
fo.place(x=350,y=10)
l=Label(scr,bg='lightpink',bd=4,fg='black',relief=SUNKEN,text='enter the query',width=15,font=('times',20,'bold'))
l.place(x=400,y=550)
def sql(q):
    result=cu.execute('{}'.format(q.get()))
    client.commit()
    q.delete(0,END)
    fun()      
e=Entry(scr,bg='lightpink',bd=4,fg='black',relief=SUNKEN,width=40,font=("times",20,"bold"))
e.place(x=720,y=550)
bu=Button(scr,text='save',bg='lightpink',relief=SUNKEN,width=4,font=('times',20,'bold'),command=lambda:sql(e))
bu.place(x=750,y=600)
listbox = Listbox(f,selectmode='single',font=('aerial',20,'bold'))
listbox.pack()
def sel(listbox):
    global result
    table=listbox.get(listbox.curselection())
    result=cu.execute('SELECT * FROM {}'.format(table))
b4=Button(f,text='enter',bg='lightpink',width=4,font=('times',20,'bold'),command=fun)
b4.place(x=90,y=270)
scr.mainloop()

