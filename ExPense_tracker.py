import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import sqlite3

conn = sqlite3.connect('modif.db')
cursor = conn.cursor()

# Create an 'expenses' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exprt (
        datee varchar(50),
        name TEXT,
        description TEXT,
        amount int(40)
     )
''')

def getVal(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['datee'])
    e2.insert(0,select['name'])
    e3.insert(0,select['description'])
    e4.insert(0,select['amount'])


def Add():
    datee= e1.get()
    name= e2.get()
    description = e3.get()
    amount = e4.get()

    conn = sqlite3.connect('modif.db')
    cursor = conn.cursor()

    try:
       sql = "INSERT INTO  exprt (datee,name,description,amount) VALUES (?, ?, ?, ?)"
       val = (datee,name,description,amount)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "Details inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       conn.rollback()
       conn.close()


def update():
    datee = e1.get()
    name = e2.get()
    description = e3.get()
    amount = e4.get()
    conn = sqlite3.connect('modif.db')
    cursor = conn.cursor()

    try:
       sql = "Update  exprt set  name= ?,description= ?,amount= ? where datee= ?"
       val = (name,description,amount,datee)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       conn.rollback()
       conn.close()


def delete():
    datee = e1.get()
    conn = sqlite3.connect('modif.db')
    cursor = conn.cursor()
   
    try:
       sql = "delete from exprt where datee = ?"
       val = (datee,)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       conn.rollback()
       conn.close()

def show():
        conn = sqlite3.connect('modif.db')
        cursor = conn.cursor()
        cursor.execute("Select datee,name,description,amount FROM exprt")
        records =cursor.fetchall()
        print(records)

        for i, (datee,name,description,amount) in enumerate(records, start=1):
            listBox.insert("", "end", values=(datee,name,description,amount))
            conn.close()
            
def total():
        conn = sqlite3.connect('modif.db')
        cursor = conn.cursor()
   
       
        cursor.execute("SELECT sum(amount) FROM exprt")
        f = cursor.fetchall()
        for i in f:
            for j in i:
                messagebox.showinfo( 'View: ', f"Total Expense:  {j}  ")


      
        

    
root = Tk()
root.title("Display")
root["bg"]="lightblue1"
root.geometry("825x500")
global e1
global e2
global e3
global e4



tk.Label(root, text="Personal Expense Tracker",bg="lightgoldenrod1" ,fg="Dark Blue", font=('Bold', 30)).place(x=300, y=15)

tk.Label(root, text="Date",fg="Dark Blue",bg="lightblue1",font=(None,13)).place(x=10, y=12)
Label(root, text="Name",fg="Dark Blue",bg="lightblue1",font=(None,13)).place(x=10, y=47)
Label(root, text="Description",fg="Dark Blue",bg="lightblue1",font=(None,13)).place(x=10, y=82)
Label(root, text="Amount",fg="Dark Blue",bg="lightblue1",font=(None,13)).place(x=10, y=120)


e1 = Entry(root)
e1.place(x=140, y=16)

e2 = Entry(root)
e2.place(x=140, y=50)

e3 = Entry(root)
e3.place(x=140, y=85)

e4 = Entry(root)
e4.place(x=140, y=122)

Button(root, text="Add",command = Add,height=2, width= 10,bg="Brown",fg="white",font="Bold").place(x=25, y=180)
Button(root, text="Update",command = update,height=2, width= 10,bg="Blue",fg="white",font="Bold").place(x=145, y=180)
Button(root, text="Delete",command = delete,height=2, width= 10,bg="Dark Grey",fg="white",font="Bold").place(x=265, y=180)
Button(root,text="Total",command=total,height=2,width=10,bg="purple",fg="white",font="Bold").place(x=380,y=180)
Button(root, text="Exit",command=root.destroy,height=2,width=10,bg="firebrick1",fg="white",font="Bold").place(x=500,y=180)


cols = ('datee','name','description','amount')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=250)

show()
listBox.bind('<Double-Button-1>',getVal)
root.mainloop()
