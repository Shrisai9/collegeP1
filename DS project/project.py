import tkinter as tk
from tkinter import messagebox, ttk

class ClinicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinic Patient Queue System")
        self.root.geometry("600x600")
        self.root.config(bg="#d7f0f5")

        # Patient data storage
        self.patients = []

        # Frame for input fields
        input_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief=tk.RIDGE)
        input_frame.place(x=20, y=20, width=560, height=200)

        # Labels and entries for patient details
        tk.Label(input_frame, text="Patient Name", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Age", font=("Arial", 12), bg="#ffffff").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.entry_age = tk.Entry(input_frame, font=("Arial", 12), width=5)
        self.entry_age.grid(row=0, column=3, padx=10, pady=10)

        tk.Label(input_frame, text="Contact", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_contact = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.entry_contact.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Symptoms", font=("Arial", 12), bg="#ffffff").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.entry_symptoms = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.entry_symptoms.grid(row=1, column=3, padx=10, pady=10)

        tk.Label(input_frame, text="Appointment Time", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_time = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.entry_time.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # AM/PM dropdown
        self.time_format = tk.StringVar(value="AM")
        self.am_pm_selector = ttk.Combobox(input_frame, textvariable=self.time_format, font=("Arial", 12), width=5)
        self.am_pm_selector['values'] = ("AM", "PM")
        self.am_pm_selector.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.am_pm_selector.current(0)

        # Buttons for actions
        self.button_add = tk.Button(self.root, text="Add Patient", font=("Arial", 12), bg="#43a047", fg="white", command=self.add_patient)
        self.button_add.place(x=50, y=230, width=120, height=40)

        self.button_view = tk.Button(self.root, text="View Queue", font=("Arial", 12), bg="#1e88e5", fg="white", command=self.view_queue)
        self.button_view.place(x=180, y=230, width=120, height=40)

        self.button_consult = tk.Button(self.root, text="Select Patient", font=("Arial", 12), bg="#f4511e", fg="white", command=self.select_patient)
        self.button_consult.place(x=310, y=230, width=150, height=40)

        # Treeview to display patient queue (hidden by default)
        self.tree = ttk.Treeview(self.root, columns=("Queue No", "Name", "Age", "Contact", "Symptoms", "Time"), show="headings", height=10)
        self.tree.column("Queue No", width=70, anchor="center")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Age", width=50, anchor="center")
        self.tree.column("Contact", width=100, anchor="center")
        self.tree.column("Symptoms", width=100, anchor="center")
        self.tree.column("Time", width=80, anchor="center")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.place(x=20, y=300, width=560, height=250)
        self.tree.place_forget()

    def add_patient(self):
        """Adds a patient to the queue."""
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        contact = self.entry_contact.get().strip()
        symptoms = self.entry_symptoms.get().strip()
        time = self.entry_time.get().strip() + " " + self.time_format.get()

        if name and age and contact and symptoms and time:
            queue_no = len(self.patients) + 1
            self.patients.append((queue_no, name, age, contact, symptoms, time))
            messagebox.showinfo("Success", f"Patient '{name}' added to queue.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all patient details.")

    def view_queue(self):
        """Displays the patient queue."""
        if self.patients:
            self.tree.place(x=20, y=300, width=560, height=250)
            self.update_tree()
        else:
            messagebox.showinfo("Empty Queue", "No patients in the queue.")

    def select_patient(self):
        """Selects a patient for the next consultation."""
        selected_item = self.tree.selection()
        if selected_item:
            patient_data = self.tree.item(selected_item)["values"]
            patient_name = patient_data[1]
            messagebox.showinfo("Consultation", f"Consulting {patient_name}")
            self.patients = [p for p in self.patients if p[0] != patient_data[0]]  # Remove selected patient
            self.update_tree()
        else:
            messagebox.showinfo("Error", "Please select a patient from the queue.")

    def update_tree(self):
        """Refreshes the TreeView to display the current queue."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for patient in self.patients:
            self.tree.insert("", tk.END, values=patient)

    def clear_entries(self):
        """Clears input fields after adding a patient."""
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.entry_symptoms.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.time_format.set("AM")

# Run the application
root = tk.Tk()
app = ClinicApp(root)
root.mainloop()
