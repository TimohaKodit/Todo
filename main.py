from tkinter import *


root = Tk()
root.title("ToDo") #Заголовок программы
list = Listbox(root, width = 45)
list.pack()

task_entry = Entry(root,width=45) #Создание списка задач
task_entry.pack()
root['bg'] = '#fcfcfc'
#Создание основного интерфейса
def add():
    task = task_entry.get()
    list.insert(END, task)
def delete_task():
    list.delete(ANCHOR)

button_add = Button( text='Добавить задачу', width = 40, height = 2,bg = 'red', command = add)
button_add.pack()
button_delete = Button(text = 'Удалить задачу', width = 40, height = 2, bg = 'green', command=delete_task )
button_delete.pack()


root.mainloop()