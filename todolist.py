import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        
        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)
        
        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=20)
        
        self.mark_done_btn = tk.Button(root, text="Mark Task as Done", command=self.mark_done)
        self.mark_done_btn.pack(pady=5)
        
        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(pady=5)
    
    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.update_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You need to enter a task.")
    
    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_index = selected[0]
            self.tasks[task_index]["done"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")
    
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_index = selected[0]
            del self.tasks[task_index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[X]" if task["done"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
