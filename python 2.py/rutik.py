import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class TaskDashboard:
    def _init_(self, master):
        self.master = master
        self.master.title("Task Dashboard")
        
        # Task List
        self.tasks = []
        
        # GUI Elements
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.task_listbox = tk.Listbox(master, width=60)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.view_button = tk.Button(master, text="View Task", command=self.view_task)
        self.view_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.alert_button = tk.Button(master, text="Send Alert", command=self.send_alert)
        self.alert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def view_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            messagebox.showinfo("Task", f"Task: {task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to view.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def send_alert(self):
        if self.tasks:
            sender_email = "your_email@example.com"
            sender_password = "your_email_password"
            receiver_email = "recipient_email@example.com"
            subject = "Task Alert"
            body = "\n".join(self.tasks)
            
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            
            try:
                with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                messagebox.showinfo("Success", "Task alert sent successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send task alert: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No tasks to send as alert.")

def main():
    root = tk.Tk()
    task_dashboard = TaskDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()