"""
Blah Blah
"""

from tkinter import *
from backend import Database

database = Database('books.db')

def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def update_comm():
    database.update(selected_tuple[0],e1_title.get(),e2_year.get(),e3_author.get(),e4_isbn.get())
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)


def view_comm():
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)

def search_comm():
    listbox.delete(0,END)
    for row in database.search(e1_title.get(),e3_author.get(),e2_year.get(),e4_isbn.get()):
        listbox.insert(END,row)

def insert_comm():
    database.insert(e1_title.get(),e2_year.get(),e3_author.get(),e4_isbn.get())
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)


def delete_comm():
    database.delete(selected_tuple[0])
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)

def clear_comm():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


window = Tk()

window.wm_title("BookStore")

w=len('Update Selected')

#  LABELS
l1 = Label(window,text = 'Title:')
l1.grid(row=0,column=0)

l2 = Label(window,text = 'Author:')
l2.grid(row=1,column=0)

l3 = Label(window,text = 'Year:')
l3.grid(row=0,column=2)

l4 = Label(window,text = 'ISBN:')
l4.grid(row=1,column=2)

#  BUTTONS
b1 = Button(window, text="View All",width=w,command=view_comm)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search Entry",width=w,command=search_comm)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add Entry",width=w,command=insert_comm)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update Selected",width=w,command=update_comm)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete Selected",width=w,command=delete_comm)
b5.grid(row=6,column=3)

b6 = Button(window, text="Clear",width=w,command=clear_comm)
b6.grid(row=7,column=3)

b7 = Button(window, text="Close",width=w,command=window.destroy)
b7.grid(row=8,column=3)

#Entries

e1_title = StringVar()
e1 = Entry(window,textvariable=e1_title)
e1.grid(row=0,column=1)

e2_year = StringVar()
e2 = Entry(window,textvariable=e2_year)
e2.grid(row=1,column=1)

e3_author = StringVar()
e3 = Entry(window,textvariable=e3_author)
e3.grid(row=0,column=3)

e4_isbn = StringVar()
e4 = Entry(window,textvariable=e4_isbn)
e4.grid(row=1,column=3)

#Listbox

listbox = Listbox(window,height=6,width=35)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

# e1_value = StringVar()
# e1 = Entry(window,textvariable=e1_value)
# e1.grid(row=0,column=2)
#
# t1 = Text(window,height=1,width=20)
# t1.grid(row=1,column=1)
#
# t2 = Text(window,height=1,width=20)
# t2.grid(row=1,column=2)
#
# t3 = Text(window,height=1,width=20)
# t3.grid(row=1,column=3)

window.mainloop()
