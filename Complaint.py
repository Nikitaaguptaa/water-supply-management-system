import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

class ComplaintManagementPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Complaint Management")
        self.root.geometry("900x500")

        title = tk.Label(self.root, text="Complaint Management", font=("Arial", 20, "bold"))
        title.pack(side=tk.TOP, pady=10)

        # Complaint Form Frame
        form_frame = tk.Frame(self.root)
        form_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

        tk.Label(form_frame, text="Consumer ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.consumer_id_entry = tk.Entry(form_frame)
        self.consumer_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Description").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.description_entry = tk.Entry(form_frame, width=40)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Status").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.status_combo = ttk.Combobox(form_frame, values=["Pending", "Resolved"], state="readonly")
        self.status_combo.set("Pending")
        self.status_combo.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Add Complaint", command=self.add_complaint).grid(row=3, column=1, pady=10)

        # Table Frame
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.complaint_table = ttk.Treeview(table_frame, columns=("complaint_id", "consumer_id", "description", "date", "status"), show="headings")

        self.complaint_table.heading("complaint_id", text="Complaint ID")
        self.complaint_table.heading("consumer_id", text="Consumer ID")
        self.complaint_table.heading("description", text="Description")
        self.complaint_table.heading("date", text="Date")
        self.complaint_table.heading("status", text="Status")

        self.complaint_table.column("complaint_id", width=100, anchor=tk.CENTER)
        self.complaint_table.column("consumer_id", width=100, anchor=tk.CENTER)
        self.complaint_table.column("description", width=250, anchor=tk.W)
        self.complaint_table.column("date", width=100, anchor=tk.CENTER)
        self.complaint_table.column("status", width=100, anchor=tk.CENTER)

        self.complaint_table.pack(fill=tk.BOTH, expand=True)

        self.load_complaints()

    def add_complaint(self):
        consumer_id = self.consumer_id_entry.get()
        description = self.description_entry.get()
        status = self.status_combo.get()

        if not consumer_id or not description:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
            cursor = conn.cursor()
            today = datetime.now().strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO complaints (consumer_id, description, date, status) VALUES (%s, %s, %s, %s)",
                           (consumer_id, description, today, status))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Complaint added successfully.")
            self.load_complaints()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_complaints(self):
        for row in self.complaint_table.get_children():
            self.complaint_table.delete(row)

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM complaints")
            rows = cursor.fetchall()
            for row in rows:
                self.complaint_table.insert("", tk.END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def clear_fields(self):
        self.consumer_id_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.status_combo.set("Pending")
