from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Bill_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Supply Bill Management")
        self.root.geometry("1200x600+100+50")

        # Variables
        self.var_bill_id = StringVar()
        self.var_consumer_id = StringVar()
        self.var_amount = StringVar()
        self.var_due_date = StringVar()
        self.var_status = StringVar(value="Unpaid")
        self.search_var = StringVar()
        self.txt_search = StringVar()

        # Title
        title = Label(self.root, text="BILL MANAGEMENT", font=("Arial", 20, "bold"),
                      bg="#0066cc", fg="white", bd=4, relief=RIDGE)
        title.pack(fill=X)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightgray")
        main_frame.pack(fill=BOTH, expand=True)

        # Left Frame
        left_frame = LabelFrame(main_frame, text="Bill Details", font=("Arial", 12, "bold"),
                                bg="lightgray", bd=2, relief=RIDGE)
        left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

        # Consumer ID
        Label(left_frame, text="Consumer ID:", font=("Arial", 12, "bold"), bg="lightgray").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_consumer_id, font=("Arial", 12), width=25).grid(row=0, column=1, padx=10, pady=5)

        # Amount
        Label(left_frame, text="Amount:", font=("Arial", 12, "bold"), bg="lightgray").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_amount, font=("Arial", 12), width=25).grid(row=1, column=1, padx=10, pady=5)

        # Due Date
        Label(left_frame, text="Due Date (YYYY-MM-DD):", font=("Arial", 12, "bold"), bg="lightgray").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_due_date, font=("Arial", 12), width=25).grid(row=2, column=1, padx=10, pady=5)

        # Status
        Label(left_frame, text="Status:", font=("Arial", 12, "bold"), bg="lightgray").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        combo_status = ttk.Combobox(left_frame, textvariable=self.var_status, font=("Arial", 12), state="readonly", width=23)
        combo_status['values'] = ("Paid", "Unpaid")
        combo_status.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="lightgray")
        btn_frame.place(x=10, y=180, width=340, height=40)

        Button(btn_frame, text="Add", command=self.add_data, width=8, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update", command=self.update_data, width=8, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete", command=self.delete_data, width=8, bg="#f44336", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset", command=self.reset_data, width=8, bg="#607D8B", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=5)

        # Right Frame
        right_frame = LabelFrame(main_frame, text="View Bills", font=("Arial", 12, "bold"),
                                 bg="lightgray", bd=2, relief=RIDGE)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        # Search Frame
        search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
        search_frame.pack(fill=X, padx=5, pady=5)

        Label(search_frame, text="Search By:", font=("Arial", 12, "bold"), bg="lightgray").grid(row=0, column=0, padx=10, pady=5)
        combo_search = ttk.Combobox(search_frame, textvariable=self.search_var, font=("Arial", 12), state="readonly", width=15)
        combo_search['values'] = ("Consumer ID", "Status")
        combo_search.grid(row=0, column=1, padx=10, pady=5)
        combo_search.current(0)

        Entry(search_frame, textvariable=self.txt_search, font=("Arial", 12), width=20).grid(row=0, column=2, padx=10, pady=5)
        Button(search_frame, text="Search", command=self.search_data, font=("Arial", 10, "bold"), bg="#009688", fg="white", width=8).grid(row=0, column=3, padx=10)
        Button(search_frame, text="Show All", command=self.fetch_data, font=("Arial", 10, "bold"), bg="#795548", fg="white", width=8).grid(row=0, column=4, padx=10)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
        table_frame.pack(fill=BOTH, expand=True)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.bill_table = ttk.Treeview(table_frame, columns=("bill_id", "consumer_id", "amount", "due_date", "status"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.bill_table.xview)
        scroll_y.config(command=self.bill_table.yview)

        self.bill_table.heading("bill_id", text="Bill ID")
        self.bill_table.heading("consumer_id", text="Consumer ID")
        self.bill_table.heading("amount", text="Amount")
        self.bill_table.heading("due_date", text="Due Date")
        self.bill_table.heading("status", text="Status")

        self.bill_table["show"] = "headings"

        self.bill_table.column("bill_id", width=80)
        self.bill_table.column("consumer_id", width=100)
        self.bill_table.column("amount", width=100)
        self.bill_table.column("due_date", width=100)
        self.bill_table.column("status", width=100)

        self.bill_table.pack(fill=BOTH, expand=1)
        self.bill_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # Functions
    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bills (consumer_id, amount, due_date, status) VALUES (%s, %s, %s, %s)", (
                self.var_consumer_id.get(), self.var_amount.get(), self.var_due_date.get(), self.var_status.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Bill Added Successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bills")
        rows = cursor.fetchall()
        self.bill_table.delete(*self.bill_table.get_children())
        for row in rows:
            self.bill_table.insert("", END, values=row)
        conn.close()

    def get_cursor(self, event=""):
        row_id = self.bill_table.focus()
        row = self.bill_table.item(row_id)["values"]
        if row:
            self.var_bill_id.set(row[0])
            self.var_consumer_id.set(row[1])
            self.var_amount.set(row[2])
            self.var_due_date.set(row[3])
            self.var_status.set(row[4])

    def update_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
            cursor = conn.cursor()
            cursor.execute("UPDATE bills SET consumer_id=%s, amount=%s, due_date=%s, status=%s WHERE bill_id=%s", (
                self.var_consumer_id.get(), self.var_amount.get(), self.var_due_date.get(), self.var_status.get(), self.var_bill_id.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Updated", "Bill updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def delete_data(self):
        if self.var_bill_id.get() == "":
            messagebox.showerror("Error", "Please select a bill to delete", parent=self.root)
        else:
            if messagebox.askyesno("Confirm", "Are you sure to delete this bill?", parent=self.root):
                conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM bills WHERE bill_id=%s", (self.var_bill_id.get(),))
                conn.commit()
                conn.close()
                self.fetch_data()
                self.reset_data()
                messagebox.showinfo("Deleted", "Bill deleted successfully", parent=self.root)

    def reset_data(self):
        self.var_bill_id.set("")
        self.var_consumer_id.set("")
        self.var_amount.set("")
        self.var_due_date.set("")
        self.var_status.set("Unpaid")

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="water_supply_system")
        cursor = conn.cursor()
        if self.search_var.get() == "Consumer ID":
            cursor.execute("SELECT * FROM bills WHERE consumer_id LIKE %s", ("%" + self.txt_search.get() + "%",))
        else:
            cursor.execute("SELECT * FROM bills WHERE status LIKE %s", ("%" + self.txt_search.get() + "%",))
        rows = cursor.fetchall()
        self.bill_table.delete(*self.bill_table.get_children())
        for row in rows:
            self.bill_table.insert("", END, values=row)
        conn.close()

if __name__ == "__main__":
    root = Tk()
    app = Bill_Win(root)
    root.mainloop()
