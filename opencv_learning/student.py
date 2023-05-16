from tkinter import *
import tkinter as tkinter
import psycopg2

root=Tk()
# def clear_all():
#     name.delete(0,END)
#     age.delete(0,END)

def get_search_result(id):
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="Chintu@1234567890",host="localhost",port="5432")
    cur=conn.cursor()
    query='''SELECT * from student WHERE id=%s;'''
    cur.execute(query,(id))
    row=cur.fetchone()
    # print("data searched")
    # print(row)
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox=Listbox(frame,width=20,height=1)
    listbox.grid(row=6,column=1)
    listbox.insert(END,row)

def display_all():
     conn=psycopg2.connect(dbname="postgres",user="postgres",password="Chintu@1234567890",host="localhost",port="5432")
     cur=conn.cursor()
     query='''SELECT * from student ;'''
     cur.execute(query)
     row=cur.fetchall()
     listbox=Listbox(frame,width=20,height=5)
     listbox.grid(row=10,column=1)
     for x in row:
         listbox.insert(END,x)


def get_value(name,age):
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="Chintu@1234567890",host="localhost",port="5432")
    cur=conn.cursor()
    query='''INSERT INTO student(name,age) VALUES(%s,%s);'''
    cur.execute(query,(name,age))
    print("data inserted")
    display_all()
    
    conn.commit()
    conn.close()


canvas=Canvas(root,height=480,width=900)
canvas.pack()
frame=Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)
label=Label(frame,text="Add data")
label.grid(row=0,column=1 )

label=Label(frame,text="Name")
label.grid(row=1,column=0 )
entry_name=Entry(frame)
entry_name.grid(row=1,column=1)

label=Label(frame,text="Age")
label.grid(row=2,column=0 )
entry_age=Entry(frame)
entry_age.grid(row=2,column=1)

button=Button(frame, text="submit",command=lambda: get_value(entry_name.get(),entry_age.get()))
button.grid(row=4,column=1)

label=Label(frame,text="Search by id")
label.grid(row=5,column=0 )
entry_id=Entry(frame)
entry_id.grid(row=5,column=1)
button=Button(frame, text="search",command=lambda: get_search_result(entry_id.get()))
button.grid(row=5,column=2)
display_all()


root.mainloop()