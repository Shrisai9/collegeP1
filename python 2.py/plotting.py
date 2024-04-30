import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TaskDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Dashboard")
        
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.start_date_entry = tk.Entry(master, width=15)
        self.start_date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.start_time_entry = tk.Entry(master, width=15)
        self.start_time_entry.grid(row=0, column=2, padx=5, pady=5)

        self.end_date_entry = tk.Entry(master, width=15)
        self.end_date_entry.grid(row=0, column=3, padx=5, pady=5)

        self.end_time_entry = tk.Entry(master, width=15)
        self.end_time_entry.grid(row=0, column=4, padx=5, pady=5)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=5, padx=5, pady=5)
        
        self.task_listbox = tk.Listbox(master, width=60)
        self.task_listbox.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
        
        self.complete_button = tk.Button(master, text="Complete", command=self.complete_task ) 
        self.complete_button.grid(row=2, column=0, columnspan=6, padx=5, pady=5 )
        
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_task , bg= "red")
        self.delete_button.grid(row=2, column=1, columnspan=6, padx=5, pady=5)
        
        self.plot_button = tk.Button(master, text="Plot Tasks", command=self.plot_tasks, bg= "lightgreen")
        self.plot_button.grid(row=3, column=0, columnspan=6, padx=5, pady=5,)
        
        # Initialize plot window
        self.fig, self.ax = plt.subplots(figsize=(10, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=6, padx=5, pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        start_date_str = self.start_date_entry.get()
        start_time_str = self.start_time_entry.get()
        end_date_str = self.end_date_entry.get()
        end_time_str = self.end_time_entry.get()
        
        if task and start_date_str and start_time_str and end_date_str and end_time_str:
            start_datetime = datetime.strptime(start_date_str + " " + start_time_str, "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(end_date_str + " " + end_time_str, "%Y-%m-%d %H:%M")
            self.tasks.append((task, start_datetime, end_datetime))
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.start_date_entry.delete(0, tk.END)
            self.start_time_entry.delete(0, tk.END)
            self.end_date_entry.delete(0, tk.END)
            self.end_time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter all details.")

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
        
        # Plotting
        dates = sorted(completion_counts.keys())
        counts = [completion_counts[date] for date in dates]
        
        self.ax.clear()
        self.ax.plot_date(dates, counts, linestyle='solid')
        self.ax.set_title('Tasks Over Time')
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Number of Tasks')

        # Customize x-axis and y-axis ticks
        self.ax.set_xticks([datetime(2024, 1, 1), datetime(2024, 6, 1), datetime(2024, 12, 31)])
        self.ax.set_xticklabels(['Jan', 'Jun', 'Dec'])
        self.ax.set_yticks(range(1, max(counts) + 1))

        self.ax.grid(True)
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = TaskDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
