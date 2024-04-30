import tkinter as tk
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define a list to store the tasks
tasks = []

# Define a list to store the tasks by date
tasks_by_date = pd.DataFrame(columns=["date", "count"])

def add_task():
    # Get the task description from the user
    task_text = task_entry.get()
    if task_text:
        task_date = datetime.date.today()
        task = {"text": task_text, "completed": False, "date": task_date.strftime("%Y-%m-%d")}
        tasks.append(task)

        # Update the tasks by date
        tasks_by_date = update_tasks_by_date(tasks_by_date, tasks)

        # Display the tasks
        display_tasks(tasks_listbox, tasks)

        # Clear the task entry field
        task_entry.delete(0, tk.END)

def delete_task():
    # Get the selected task index
    selected_index = tasks_listbox.curselection()
    if selected_index:
        # Remove the task from the tasks list
        tasks.pop(selected_index[0])

        # Update the tasks by date
        tasks_by_date = update_tasks_by_date(tasks_by_date, tasks)

        # Display the tasks
        display_tasks(tasks_listbox, tasks)

def complete_task():
    # Get the selected task index
    selected_index = tasks_listbox.curselection()
    if selected_index:
        # Toggle the completed status of the task
        task = tasks[selected_index[0]]
        task["completed"] = not task["completed"]

        # Update the tasks by date
        tasks_by_date = update_tasks_by_date(tasks_by_date, tasks)

        # Display the tasks
        display_tasks(tasks_listbox, tasks)

def update_tasks_by_date(tasks_by_date, tasks):
    # Get the current date
    today = datetime.date.today()

    # Get the tasks for the current date
    tasks_today = [task for task in tasks if task["completed"] or today == task["date"]]

    # Create a DataFrame of tasks by date
    tasks_by_date_new = pd.DataFrame(columns=["date", "count"])
    for task in tasks_today:
        task_date = task["date"] if "date" in task else today
        task_count = tasks_by_date_new[tasks_by_date_new["date"] == task_date]["count"].sum() + 1
        tasks_by_date_new = tasks_by_date_new.append({"date": task_date, "count": task_count}, ignore_index=True)

    # Sort the DataFrame by date
    tasks_by_date_new = tasks_by_date_new.sort_values(by=["date"])

    # Update the tasks by date DataFrame
    tasks_by_date = tasks_by_date.append(tasks_by_date_new[tasks_by_date_new["count"] > 0])

    return tasks_by_date

def display_tasks(tasks_listbox, tasks):
    # Clear the listbox
    tasks_listbox.delete(0, tk.END)

    # Display the tasks
    for task in tasks:
        task_text = task["text"]
        if task["completed"]:
            task_text = f"~~{task_text}~~"
        tasks_listbox.insert(tk.END, task_text)

def display_pie_chart():
        # Create a pie chart of tasks by date
        labels = tasks_by_date["date"].tolist()
        sizes = tasks_by_date["count"].tolist()
        colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(len(labels))]

        plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
        plt.axis('equal')
        plt.title("Tasks by date")

        # Create a new Figure and Tkinter canvas for the pie chart
        fig = plt.Figure(figsize=(6, 6))
        pie_chart = fig.add_subplot(111)
        pie_chart.axis('equal')

        # Draw the pie chart
        pie_chart.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
        pie_chart.set_title("Tasks by date")

        # Create a Tkinter canvas for the pie chart
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()

        # Pack the Tkinter canvas into the GUI
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    # Create the Tkinter root window
    root = tk.Tk()

    # Create a frame to hold the task entry and button
    entry_frame = tk.Frame(root)
    entry_frame.pack(fill=tk.X, pady=10)

    # Create a label and entry for the task description
    tk.Label(entry_frame, text="Task description:").pack(side=tk.LEFT)
    task_entry = tk.Entry(entry_frame)
    task_entry.pack(fill=tk.X, expand=True)

    # Create a button toadd a task
    add_task_button = tk.Button(entry_frame, text="Add task", command=add_task)
    add_task_button.pack(side=tk.RIGHT)

    # Create a listbox to display the tasks
    tasks_listbox = tk.Listbox(root)
    tasks_listbox.pack(fill=tk.BOTH, expand=True)

    # Create a button to delete the selected task
    delete_task_button = tk.Button(root, text="Delete task", command=delete_task)
    delete_task_button.pack(fill=tk.X, pady=10)

    # Create a button to complete the selected task
    complete_task_button = tk.Button(root, text="Complete task", command=complete_task)
    complete_task_button.pack(fill=tk.X)

    # Create a button to display the pie chart
    display_pie_chart_button = tk.Button(root, text="View tasks by date", command=display_pie_chart)
    display_pie_chart_button.pack(pady=20)

    # Display the initial tasks
    display_tasks(tasks_listbox, tasks)

    # Run the Tkinter event loop
    root.mainloop()