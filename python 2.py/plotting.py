import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from collections import Counter

class TaskDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Dashboard")
        
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.task_listbox = tk.Listbox(master, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.complete_button = tk.Button(master, text="Complete", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_task , bg= "red")
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.plot_button = tk.Button(master, text="Plot Tasks", command=self.plot_tasks, bg= "lightgreen")
        self.plot_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5,)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, datetime.now()))
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
            
    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")
            
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def plot_tasks(self):
        completion_dates = [task[1].date() for task in self.tasks]
        completion_counts = Counter(completion_dates)
        
        for date, count in completion_counts.items():
            print(f"{date}: {count} tasks completed")

def main():
    root = tk.Tk()
    app = TaskDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
