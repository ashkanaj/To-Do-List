import re
import tkinter as ttk
import tkinter.ttk
from tkinter.ttk import Label


def task_validator(task):
    if re.match(r"^[a-zA-Z/s],{2,30}$", task):
        return True
    else:
        return False

def add_click():
    pass

win = ttk.Tk()

win.geometry('500x250')
win.title('To-Do List')
window_lable=Label(win, text='To-Do List', font=('Arial', 16), foreground='black', borderwidth=2)
window_lable.pack()
#lable
entry_lable=ttk.Label(win, text='Enter The Task :')
entry_lable.place(x=85, y=50)
#entry
entey_entry=ttk.Entry(win)
entey_entry.place(x=20, y=80,width=220)
#button
add_btn=ttk.Button(win, text='Add')
add_btn.place(x=20, y=110,width=220)

delete_btn=ttk.Button(win, text='Delete')
delete_btn.place(x=20, y=140,width=220)

delete_all_btn=ttk.Button(win, text='Delete All')
delete_all_btn.place(x=20, y=170,width=220)

exit_btn=ttk.Button(win, text='Exit')
exit_btn.place(x=20, y=200,width=220)

#table
table=tkinter.ttk.Treeview(win, columns=['Tasks'], show='headings')
table.heading('Tasks', text='Tasks')
table.place(x=250, y=80, width=220, height=145)



win.mainloop()