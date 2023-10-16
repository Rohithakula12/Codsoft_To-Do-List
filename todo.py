import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List App")
tasks = []
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = int(selected_task_index[0])
        del tasks[index]
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
entry = tk.Entry(root)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root)
listbox.pack()
root.mainloop()
