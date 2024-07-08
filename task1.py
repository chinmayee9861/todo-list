from tkinter import *
from tkinter import messagebox

NUMBER = 0


def add_task():
    global NUMBER
    new_task = task_entry.get().capitalize()
    if new_task != "":
        NUMBER += 1
        list_box.insert(END, f"{NUMBER}. {new_task}")
        task_entry.delete(0, END)
        update_num()
    else:
        messagebox.showwarning(title="Warning", message="Please don't leave entry field empty!")


def delete_task():
    global NUMBER
    selected_task_index = list_box.curselection()
    if selected_task_index:
        list_box.delete(selected_task_index)
        update_num()


def update_num():
    global NUMBER
    NUMBER = 0
    tasks = list_box.get(0, END)
    list_box.delete(0, END)
    for task in tasks:
        NUMBER += 1
        task_text = task.split('. ', 1)[1]
        list_box.insert(END, f"{NUMBER}. {task_text}")


window = Tk()
window.title("TO-DO LIST")
window.geometry("350x300")
window.config(bg="#223441", padx=30, pady=20)
window.resizable(width=False, height=False)

sv_bar = Scrollbar(orient=VERTICAL)
sv_bar.grid(row=0, column=2, sticky="ns")

list_box = Listbox(width=32, height=10, bd=0, cursor="dot", font=("Times", 12, "bold"), highlightthickness=0,
                   selectbackground="#a6a6a6", fg="#464646", activestyle="none", yscrollcommand=sv_bar.set)
list_box.grid(row=0, column=0, columnspan=2)
sv_bar.config(command=list_box.yview)

task_entry = Entry(width=32)
task_entry.grid(row=1, column=0, columnspan=2, pady=5)

add_button = Button(text="Add task", padx=37, bg="#008000", command=add_task)
add_button.grid(row=2, column=0, pady=5)
delete_button = Button(text="Delete task", padx=33, bg="#008080", command=delete_task)
delete_button.grid(row=2, column=1, pady=5)

window.mainloop()