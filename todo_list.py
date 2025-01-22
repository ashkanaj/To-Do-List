import re
import tkinter as ttk
import tkinter.ttk
import tkinter.messagebox as msg
from tkinter.ttk import Label

def task_validator(task):
    if re.match(r"^[a-zA-Z\s]{2,30}$", task):
        return True
    else:
        return False

def add_click():
    task = entey_entry.get()
    if task_validator(task):
        table.insert('', 'end', values=(task,), tags=('lightblue',))
        entey_entry.delete(0, 'end')
        msg.showinfo('Added', 'Task added successfully!')
    else:
        msg.showerror('Error', 'Please enter a valid task')

def delete_selected():
    selected_item = table.selection()
    if selected_item:
        for item in selected_item:
            table.delete(item)
        msg.showinfo('Deleted', 'Selected tasks deleted successfully!')
    else:
        msg.showwarning('No Selection', 'Please select a task to delete!')

def delete_all():
    if table.get_children():
        confirm = msg.askyesno('Confirm Delete All', 'Are you sure you want to delete all tasks?')
        if confirm:
            for item in table.get_children():
                table.delete(item)
            msg.showinfo('Deleted All', 'All tasks deleted successfully!')
    else:
        msg.showwarning('No Tasks', 'There are no tasks to delete!')

def exit_app():
    confirm = msg.askyesno('Confirm Exit', 'Are you sure you want to exit?')
    if confirm:
        win.destroy()

#main window
win = ttk.Tk()
win.geometry('500x250')
win.title('To-Do List')

#main lable
window_lable = Label(win, text='To-Do List', font=('Arial', 16), foreground='black', borderwidth=2)
window_lable.pack()

#entry lable
entry_lable = ttk.Label(win, text='Enter The Task :')
entry_lable.place(x=85, y=50)

#entry
entey_entry = ttk.Entry(win)
entey_entry.place(x=20, y=80, width=220)

#buttons
add_btn = ttk.Button(win, text='Add', command=add_click)
add_btn.place(x=20, y=110, width=220)

delete_btn = ttk.Button(win, text='Delete', command=delete_selected)
delete_btn.place(x=20, y=140, width=220)

delete_all_btn = ttk.Button(win, text='Delete All', command=delete_all)
delete_all_btn.place(x=20, y=170, width=220)

exit_btn = ttk.Button(win, text='Exit', command=exit_app)
exit_btn.place(x=20, y=200, width=220)

#table
table = tkinter.ttk.Treeview(win, columns=['Tasks'], show='headings')
table.heading('Tasks', text='Tasks')
table.place(x=250, y=80, width=220, height=145)
table.tag_configure('lightblue', background='lightblue')

win.mainloop()