# from tkinter import*
# from PIL import Image, ImageTk
# from tkinter import ttk
# import random
# # import mysql.connector
# from tkinter import messagebox

# class Cust_Win:
#     def __init__(self, root):  # Fixed constructor name
#         self.root = root
#         self.root.title("Hotel Management System")
#         self.root.geometry("1300x820+230+100")

#     #     # ========== Variables ==========
#     #     self.var_ref = StringVar()
#     #     x = random.randint(1000, 9999)
#     #     self.var_ref.set(str(x))

#     #     self.var_cust_id = StringVar()
#     #     self.var_name = StringVar()
#     #     self.var_mobile = StringVar()
#     #     self.var_address = StringVar()
#     #     self.var_connectiondate = StringVar()
       

#         # ========== Title ==========
#         lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 40, "bold"),
#                          bg="black", fg="white", bd=4, relief=RIDGE)
#         lbl_title.place(x=0, y=0, width=1695, height=70)


#         # ========== Left Frame ==========
#         labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
#                                    font=("arial", 18, "bold"), padx=2)
#         labelframeleft.place(x=3, y=70, width=540, height=680)

#         # ========== Labels and Entries ==========
#         # Customer Ref
#         lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 18, "bold"), padx=2, pady=6)
#         lbl_cust_ref.grid(row=0, column=0, sticky=W)
#         entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 15, "bold"),
#                              width=29, state="readonly")
#         entry_ref.grid(row=0, column=1)

#         # Customer Name
#         cname = Label(labelframeleft, font=("arial", 18, "bold"), text="Customer Name:", padx=2, pady=6)
#         cname.grid(row=1, column=0, sticky=W)
#         txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=("arial", 15, "bold"), width=29)
#         txtcname.grid(row=1, column=1)

#         # Mother Name
#         lblname = Label(labelframeleft, font=("arial", 18, "bold"), text="Mother Name:", padx=2, pady=6)
#         lblname.grid(row=2, column=0, sticky=W)
#         txtname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 15, "bold"), width=29)
#         txtname.grid(row=2, column=1)

#         # Gender Combobox
#         label_gender = Label(labelframeleft, font=("arial", 18, "bold"), text="Gender:", padx=2, pady=6)
#         label_gender.grid(row=3, column=0, sticky=W)
#         combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 15, "bold"),
#                                    width=27, state="readonly")
#         combo_gender["values"] = ("Male", "Female", "Other")
#         combo_gender.current(0)
#         combo_gender.grid(row=3, column=1)

#         # Postcode
#         lblPostCode = Label(labelframeleft, font=("arial", 18, "bold"), text="PostCode:", padx=2, pady=6)
#         lblPostCode.grid(row=4, column=0, sticky=W)
#         txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 15, "bold"), width=29)
#         txtPostCode.grid(row=4, column=1)

#         # Mobile Number
#         lblMobile = Label(labelframeleft, font=("arial", 18, "bold"), text="Mobile:", padx=2, pady=6)
#         lblMobile.grid(row=5, column=0, sticky=W)
#         txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 15, "bold"), width=29)
#         txtMobile.grid(row=5, column=1)

#         # Email
#         lblEmail = Label(labelframeleft, font=("arial", 18, "bold"), text="Email:", padx=2, pady=6)
#         lblEmail.grid(row=6, column=0, sticky=W)
#         txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 15, "bold"), width=29)
#         txtEmail.grid(row=6, column=1)

#         # Nationality
#         lblNationality = Label(labelframeleft, font=("arial", 18, "bold"), text="Nationality:", padx=2, pady=6)
#         lblNationality.grid(row=7, column=0, sticky=W)
#         combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,
#                                        font=("arial", 15, "bold"), width=27, state="readonly")
#         combo_Nationality["values"] = ("Indian", "Foreigner")
#         combo_Nationality.current(0)
#         combo_Nationality.grid(row=7, column=1)

#         # ID Proof Type
#         lblIdProof = Label(labelframeleft, font=("arial", 18, "bold"), text="Id Proof Type:", padx=2, pady=6)
#         lblIdProof.grid(row=8, column=0, sticky=W)
#         combo_IdProof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 15, "bold"),
#                                     width=27, state="readonly")
#         combo_IdProof["values"] = ("AdharCard", "DrivingLicence", "Passport", "Other Valid Proof")
#         combo_IdProof.current(0)
#         combo_IdProof.grid(row=8, column=1)

#         # ID Number
#         lblIdNumber = Label(labelframeleft, font=("arial", 18, "bold"), text="Id Number:", padx=2, pady=6)
#         lblIdNumber.grid(row=9, column=0, sticky=W)
#         txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=("arial", 15, "bold"), width=29)
#         txtIdNumber.grid(row=9, column=1)

#         # Address
#         lblAddress = Label(labelframeleft, font=("arial", 18, "bold"), text="Address:", padx=2, pady=6)
#         lblAddress.grid(row=10, column=0, sticky=W)
#         txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 15, "bold"), width=29)
#         txtAddress.grid(row=10, column=1)

#         # ========== Buttons ==========
#         btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
#         btn_frame.place(x=0, y=580, width=535, height=60)
        
#         btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 16, "bold"),
#                        bg="black", fg="white", width=9)
#         btnAdd.grid(row=0, column=0, padx=6, pady=1)

#         btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 16, "bold"),
#                           bg="black", fg="white", width=9)
#         btnUpdate.grid(row=0, column=1, padx=2)

#         btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 16, "bold"),
#                           bg="black", fg="white", width=9)
#         btnDelete.grid(row=0, column=2, padx=2)

#         btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 16, "bold"),
#                          bg="black", fg="white", width=9)
#         btnReset.grid(row=0, column=3, padx=2)

#         # ========== Right Frame ==========
#         Tabel_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
#                                 font=("arial", 18, "bold"), padx=2)
#         Tabel_Frame.place(x=550, y=75, width=1110, height=680)

#         # Search System
#         lblSearchBy = Label(Tabel_Frame, font=("arial", 18, "bold"), text="Search By:", bg="red", fg="white")
#         lblSearchBy.grid(row=0, column=0, sticky=W, padx=3)

#         self.search_var = StringVar()
#         combo_Search = ttk.Combobox(Tabel_Frame, textvariable=self.search_var, 
#                                    font=("arial", 18, "bold"), width=23, state="readonly")
#         combo_Search["values"] = ("Mobile", "Ref")
#         combo_Search.current(0)
#         combo_Search.grid(row=0, column=1, padx=3)

#         self.txt_search = StringVar()
#         txtSearch = ttk.Entry(Tabel_Frame, textvariable=self.txt_search, font=("arial", 18, "bold"), width=23)
#         txtSearch.grid(row=0, column=2, padx=3)

#         btnSearch = Button(Tabel_Frame, text="Search", command=self.search_data,
#                           font=("arial", 18, "bold"), bg="black", fg="white", width=9)
#         btnSearch.grid(row=0, column=3, padx=2)

#         btnShowAll = Button(Tabel_Frame, text="Show All", command=self.fetch_data,
#                            font=("arial", 18, "bold"), bg="black", fg="white", width=9)
#         btnShowAll.grid(row=0, column=4, padx=2)

#         # ========== Data Table ==========
#         details_table = Frame(Tabel_Frame, bd=10, relief=RIDGE)
#         details_table.place(x=0, y=50, width=1100, height=600)

#         scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

#         self.Cust_Details_Table = ttk.Treeview(details_table, columns=(
#             "ref", "name", "mother", "gender", "post", "mobile", "email",
#             "nationality", "idproof", "idnumber", "address"),
#                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.Cust_Details_Table.xview)
#         scroll_y.config(command=self.Cust_Details_Table.yview)

#         self.Cust_Details_Table.heading("ref", text="Refer No")
#         self.Cust_Details_Table.heading("name", text="Name")
#         self.Cust_Details_Table.heading("mother", text="Mother")
#         self.Cust_Details_Table.heading("gender", text="Gender")
#         self.Cust_Details_Table.heading("post", text="PostCode")
#         self.Cust_Details_Table.heading("mobile", text="Mobile")
#         self.Cust_Details_Table.heading("email", text="Email")
#         self.Cust_Details_Table.heading("nationality", text="Nationality")
#         self.Cust_Details_Table.heading("idproof", text="Id Proof")
#         self.Cust_Details_Table.heading("idnumber", text="Id Number")
#         self.Cust_Details_Table.heading("address", text="Address")

#         self.Cust_Details_Table["show"] = "headings"
#         self.Cust_Details_Table.pack(fill=BOTH, expand=1)
#         self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
#         self.fetch_data()

#     # ========== Database Methods ==========
#     def add_data(self):
#         if self.var_mobile.get() == "" or self.var_mother.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     user="root",
#                     password="12345678",
#                     database="management"
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
#                     self.var_ref.get(),
#                     self.var_cust_name.get(),
#                     self.var_mother.get(),
#                     self.var_gender.get(),
#                     self.var_post.get(),
#                     self.var_mobile.get(),
#                     self.var_email.get(),
#                     self.var_nationality.get(),
#                     self.var_id_proof.get(),
#                     self.var_id_number.get(),
#                     self.var_address.get()
#                 ))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Success", "Customer has been added", parent=self.root)
#             except Exception as es:
#                 messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

#     def fetch_data(self):
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="12345678",
#             database="management"
#         )
#         my_cursor = conn.cursor()
#         my_cursor.execute("SELECT * FROM customer")
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
#             for i in rows:
#                 self.Cust_Details_Table.insert("", END, values=i)
#         conn.close()

#     def get_cursor(self, event=""):
#         cursor_row = self.Cust_Details_Table.focus()
#         content = self.Cust_Details_Table.item(cursor_row)
#         row = content["values"]
        
#         self.var_ref.set(row[0]),
#         self.var_cust_name.set(row[1]),
#         self.var_mother.set(row[2]),
#         self.var_gender.set(row[3]),
#         self.var_post.set(row[4]),
#         self.var_mobile.set(row[5]),
#         self.var_email.set(row[6]),
#         self.var_nationality.set(row[7]),
#         self.var_id_proof.set(row[8]),
#         self.var_id_number.set(row[9]),
#         self.var_address.set(row[10])

#     def update_data(self):
#         if self.var_mobile.get() == "":
#             messagebox.showerror("Error", "Mobile number is required", parent=self.root)
#         else:
#             conn = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="12345678",
#                 database="management"
#             )
#             my_cursor = conn.cursor()
#             my_cursor.execute("UPDATE customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s WHERE Ref=%s", (
#                 self.var_cust_name.get(),
#                 self.var_mother.get(),
#                 self.var_gender.get(),
#                 self.var_post.get(),
#                 self.var_mobile.get(),
#                 self.var_email.get(),
#                 self.var_nationality.get(),
#                 self.var_id_proof.get(),
#                 self.var_id_number.get(),
#                 self.var_address.get(),
#                 self.var_ref.get()
#             ))
#             conn.commit()
#             self.fetch_data()
#             conn.close()
#             messagebox.showinfo("Update", "Customer details updated successfully", parent=self.root)

#     def delete_data(self):
#         delete = messagebox.askyesno("Delete", "Are you sure you want to delete this customer?", parent=self.root)
#         if delete:
#             conn = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="12345678",
#                 database="management"
#             )
#             my_cursor = conn.cursor()
#             query = "DELETE FROM customer WHERE Ref=%s"
#             value = (self.var_ref.get(),)
#             my_cursor.execute(query, value)
#             conn.commit()
#             conn.close()
#             self.fetch_data()
#             self.reset_data()
#             messagebox.showinfo("Delete", "Customer deleted successfully", parent=self.root)

#     def reset_data(self):
#         x = random.randint(1000, 9999)
#         self.var_ref.set(str(x))
#         self.var_cust_name.set(""),
#         self.var_mother.set(""),
#         self.var_gender.set("Male"),
#         self.var_post.set(""),
#         self.var_mobile.set(""),
#         self.var_email.set(""),
#         self.var_nationality.set("Indian"),
#         self.var_id_proof.set("AdharCard"),
#         self.var_id_number.set(""),
#         self.var_address.set("")

#     def search_data(self):
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="12345678",
#             database="management"
#         )
#         my_cursor = conn.cursor()
        
#         if self.search_var.get() == "Mobile":
#             my_cursor.execute("SELECT * FROM customer WHERE Mobile LIKE %s", ("%"+self.txt_search.get()+"%",))
#         else:
#             my_cursor.execute("SELECT * FROM customer WHERE Ref LIKE %s", ("%"+self.txt_search.get()+"%",))
            
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
#             for i in rows:
#                 self.Cust_Details_Table.insert("", END, values=i)
#         conn.close()

# if __name__ == "__main__":  # Fixed main guard
#     root = Tk()
#     obj = Cust_Win(root)
#     root.mainloop()
# from tkinter import *
# from tkinter import ttk, messagebox
# import mysql.connector
# import random

# class Cust_Win:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Water Supply Management System")
#         self.root.geometry("1300x700+100+50")
        
#         # ========== Variables ==========
#         self.var_consumer_id = StringVar()
#         x = random.randint(1000, 9999)
#         self.var_consumer_id.set(str(x))
        
#         self.var_name = StringVar()
#         self.var_address = StringVar()
#         self.var_contact = StringVar()
#         self.var_connection_date = StringVar()
#         self.search_var = StringVar()
#         self.txt_search = StringVar()
        
#         # ========== Title ==========
#         lbl_title = Label(self.root, text="WATER SUPPLY CONSUMER MANAGEMENT", 
#                          font=("Times New Roman", 25, "bold"), 
#                          bg="#0066cc", fg="white", bd=4, relief=RIDGE)
#         lbl_title.pack(fill=X)

#         # ========== Main Frame ==========
#         main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightgray")
#         main_frame.pack(fill=BOTH, expand=True)

#         # ========== Left Frame (Form) ==========
#         left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Consumer Details",
#                               font=("Arial", 12, "bold"), bg="lightgray")
#         left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

#         # Consumer ID
#         lbl_id = Label(left_frame, text="Consumer ID:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
#         txt_id = Entry(left_frame, textvariable=self.var_consumer_id, font=("Arial", 12), 
#                       width=25, state='readonly')
#         txt_id.grid(row=0, column=1, padx=5, pady=5)

#         # Name
#         lbl_name = Label(left_frame, text="Name:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_name.grid(row=1, column=0, padx=5, pady=5, sticky=W)
#         txt_name = Entry(left_frame, textvariable=self.var_name, font=("Arial", 12), width=25)
#         txt_name.grid(row=1, column=1, padx=5, pady=5)

#         # Address
#         lbl_address = Label(left_frame, text="Address:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_address.grid(row=2, column=0, padx=5, pady=5, sticky=W)
#         txt_address = Entry(left_frame, textvariable=self.var_address, font=("Arial", 12), width=25)
#         txt_address.grid(row=2, column=1, padx=5, pady=5)

#         # Contact
#         lbl_contact = Label(left_frame, text="Contact:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_contact.grid(row=3, column=0, padx=5, pady=5, sticky=W)
#         txt_contact = Entry(left_frame, textvariable=self.var_contact, font=("Arial", 12), width=25)
#         txt_contact.grid(row=3, column=1, padx=5, pady=5)

#         # Connection Date
#         lbl_date = Label(left_frame, text="Connection Date:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_date.grid(row=4, column=0, padx=5, pady=5, sticky=W)
#         txt_date = Entry(left_frame, textvariable=self.var_connection_date, font=("Arial", 12), width=25)
#         txt_date.grid(row=4, column=1, padx=5, pady=5)

#         # Buttons Frame
#         btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="lightgray")
#         btn_frame.place(x=5, y=200, width=350, height=40)

#         btn_add = Button(btn_frame, text="Add", command=self.add_data, 
#                         font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=8)
#         btn_add.grid(row=0, column=0, padx=2)

#         btn_update = Button(btn_frame, text="Update", command=self.update_data, 
#                            font=("Arial", 10, "bold"), bg="#2196F3", fg="white", width=8)
#         btn_update.grid(row=0, column=1, padx=2)

#         btn_delete = Button(btn_frame, text="Delete", command=self.delete_data, 
#                            font=("Arial", 10, "bold"), bg="#f44336", fg="white", width=8)
#         btn_delete.grid(row=0, column=2, padx=2)

#         btn_reset = Button(btn_frame, text="Reset", command=self.reset_data, 
#                           font=("Arial", 10, "bold"), bg="#607D8B", fg="white", width=8)
#         btn_reset.grid(row=0, column=3, padx=2)

#         # ========== Right Frame (Table) ==========
#         right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Consumer Details",
#                                font=("Arial", 12, "bold"), bg="lightgray")
#         right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

#         # Search Frame
#         search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
#         search_frame.pack(fill=X, padx=5, pady=5)

#         lbl_search = Label(search_frame, text="Search By:", font=("Arial", 12, "bold"), bg="lightgray")
#         lbl_search.grid(row=0, column=0, padx=5, pady=5)

#         combo_search = ttk.Combobox(search_frame, textvariable=self.search_var, 
#                                   font=("Arial", 12), width=15, state="readonly")
#         combo_search['values'] = ("Name", "Contact", "Consumer ID")
#         combo_search.current(0)
#         combo_search.grid(row=0, column=1, padx=5, pady=5)

#         txt_search = Entry(search_frame, textvariable=self.txt_search, font=("Arial", 12), width=20)
#         txt_search.grid(row=0, column=2, padx=5, pady=5)

#         btn_search = Button(search_frame, text="Search", command=self.search_data,
#                           font=("Arial", 10, "bold"), bg="#009688", fg="white", width=8)
#         btn_search.grid(row=0, column=3, padx=5, pady=5)

#         btn_show_all = Button(search_frame, text="Show All", command=self.fetch_data,
#                             font=("Arial", 10, "bold"), bg="#795548", fg="white", width=8)
#         btn_show_all.grid(row=0, column=4, padx=5, pady=5)

#         # Table Frame
#         table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
#         table_frame.pack(fill=BOTH, expand=True)

#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.consumer_table = ttk.Treeview(table_frame, columns=(
#             "consumer_id", "name", "address", "contact", "connection_date"),
#             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.consumer_table.xview)
#         scroll_y.config(command=self.consumer_table.yview)

#         self.consumer_table.heading("consumer_id", text="Consumer ID")
#         self.consumer_table.heading("name", text="Name")
#         self.consumer_table.heading("address", text="Address")
#         self.consumer_table.heading("contact", text="Contact")
#         self.consumer_table.heading("connection_date", text="Connection Date")

#         self.consumer_table["show"] = "headings"

#         self.consumer_table.column("consumer_id", width=100, anchor=CENTER)
#         self.consumer_table.column("name", width=150)
#         self.consumer_table.column("address", width=200)
#         self.consumer_table.column("contact", width=100, anchor=CENTER)
#         self.consumer_table.column("connection_date", width=100, anchor=CENTER)

#         self.consumer_table.pack(fill=BOTH, expand=1)
#         self.consumer_table.bind("<ButtonRelease-1>", self.get_cursor)

#         self.fetch_data()

#     # ========== Database Methods ==========
#     def add_data(self):
#         if self.var_name.get() == "" or self.var_contact.get() == "":
#             messagebox.showerror("Error", "Name and Contact fields are required", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     user="root",
#                     password="12345678",
#                     database="water_supply_system"
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("INSERT INTO consumers (name, address, contact, connection_date) VALUES (%s, %s, %s, %s)", 
#                                 (self.var_name.get(),
#                                  self.var_address.get(),
#                                  self.var_contact.get(),
#                                  self.var_connection_date.get()))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Success", "Consumer added successfully", parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#     def fetch_data(self):
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="12345678",
#             database="water_supply_system"
#         )
#         my_cursor = conn.cursor()
#         my_cursor.execute("SELECT * FROM consumers")
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#             self.consumer_table.delete(*self.consumer_table.get_children())
#             for row in rows:
#                 self.consumer_table.insert("", END, values=row)
#         conn.close()

#     def get_cursor(self, event=""):
#         cursor_row = self.consumer_table.focus()
#         content = self.consumer_table.item(cursor_row)
#         row = content["values"]
        
#         if row:
#             self.var_consumer_id.set(row[0])
#             self.var_name.set(row[1])
#             self.var_address.set(row[2])
#             self.var_contact.set(row[3])
#             self.var_connection_date.set(row[4])

#     def update_data(self):
#         if self.var_consumer_id.get() == "":
#             messagebox.showerror("Error", "Please select a consumer to update", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     user="root",
#                     password="12345678",
#                     database="water_supply_system"
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("UPDATE consumers SET name=%s, address=%s, contact=%s, connection_date=%s WHERE consumer_id=%s", 
#                                 (self.var_name.get(),
#                                  self.var_address.get(),
#                                  self.var_contact.get(),
#                                  self.var_connection_date.get(),
#                                  self.var_consumer_id.get()))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Success", "Consumer updated successfully", parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#     def delete_data(self):
#         if self.var_consumer_id.get() == "":
#             messagebox.showerror("Error", "Please select a consumer to delete", parent=self.root)
#         else:
#             if messagebox.askyesno("Confirm", "Are you sure you want to delete this consumer?", parent=self.root):
#                 try:
#                     conn = mysql.connector.connect(
#                         host="localhost",
#                         user="root",
#                         password="12345678",
#                         database="water_supply_system"
#                     )
#                     my_cursor = conn.cursor()
#                     my_cursor.execute("DELETE FROM consumers WHERE consumer_id=%s", (self.var_consumer_id.get(),))
#                     conn.commit()
#                     self.fetch_data()
#                     conn.close()
#                     self.reset_data()
#                     messagebox.showinfo("Success", "Consumer deleted successfully", parent=self.root)
#                 except Exception as es:
#                     messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#     def reset_data(self):
#         x = random.randint(1000, 9999)
#         self.var_consumer_id.set(str(x))
#         self.var_name.set("")
#         self.var_address.set("")
#         self.var_contact.set("")
#         self.var_connection_date.set("")

#     def search_data(self):
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="12345678",
#             database="water_supply_system"
#         )
#         my_cursor = conn.cursor()
        
#         if self.search_var.get() == "Name":
#             my_cursor.execute("SELECT * FROM consumers WHERE name LIKE %s", ("%" + self.txt_search.get() + "%",))
#         elif self.search_var.get() == "Contact":
#             my_cursor.execute("SELECT * FROM consumers WHERE contact LIKE %s", ("%" + self.txt_search.get() + "%",))
#         else:
#             my_cursor.execute("SELECT * FROM consumers WHERE consumer_id LIKE %s", ("%" + self.txt_search.get() + "%",))
            
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#             self.consumer_table.delete(*self.consumer_table.get_children())
#             for row in rows:
#                 self.consumer_table.insert("", END, values=row)
#         else:
#             messagebox.showinfo("Info", "No matching records found", parent=self.root)
#         conn.close()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Cust_Win(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import random
from datetime import datetime

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Supply Management System")
        self.root.geometry("1300x700+100+50")
        
        # Initialize database first
        self.initialize_database()
        
        # Variables
        self.var_consumer_id = StringVar()
        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()
        self.var_connection_date = StringVar()
        self.var_connection_date.set(datetime.now().strftime("%Y-%m-%d"))
        self.search_var = StringVar()
        self.txt_search = StringVar()
        
        # Generate random consumer ID
        x = random.randint(1000, 9999)
        self.var_consumer_id.set(str(x))
        
        # GUI Setup
        self.setup_ui()
        
        # Fetch initial data
        self.fetch_data()

    def setup_ui(self):
        # Title
        lbl_title = Label(self.root, text="WATER SUPPLY CONSUMER MANAGEMENT", 
                         font=("Times New Roman", 25, "bold"), 
                         bg="#0066cc", fg="white", bd=4, relief=RIDGE)
        lbl_title.pack(fill=X)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightgray")
        main_frame.pack(fill=BOTH, expand=True)

        # Left Frame (Form)
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Consumer Details",
                              font=("Arial", 12, "bold"), bg="lightgray")
        left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

        # Form Fields
        fields = [
            ("Consumer ID:", self.var_consumer_id, True),
            ("Name:", self.var_name, False),
            ("Address:", self.var_address, False),
            ("Contact:", self.var_contact, False),
            ("Connection Date:", self.var_connection_date, False)
        ]

        for i, (text, var, readonly) in enumerate(fields):
            Label(left_frame, text=text, font=("Arial", 12, "bold"), bg="lightgray")\
                .grid(row=i, column=0, padx=5, pady=5, sticky=W)
            Entry(left_frame, textvariable=var, font=("Arial", 12), 
                  width=25, state='readonly' if readonly else NORMAL)\
                .grid(row=i, column=1, padx=5, pady=5)

        # Buttons
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="lightgray")
        btn_frame.place(x=5, y=200, width=350, height=40)

        buttons = [
            ("Add", "#4CAF50", self.add_data),
            ("Update", "#2196F3", self.update_data),
            ("Delete", "#f44336", self.delete_data),
            ("Reset", "#607D8B", self.reset_data)
        ]

        for i, (text, color, command) in enumerate(buttons):
            Button(btn_frame, text=text, command=command, 
                  font=("Arial", 10, "bold"), bg=color, fg="white", width=8)\
                .grid(row=0, column=i, padx=2)

        # Right Frame (Table)
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Consumer Details",
                               font=("Arial", 12, "bold"), bg="lightgray")
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        # Search Frame
        search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
        search_frame.pack(fill=X, padx=5, pady=5)

        Label(search_frame, text="Search By:", font=("Arial", 12, "bold"), bg="lightgray")\
            .grid(row=0, column=0, padx=5, pady=5)

        self.combo_search = ttk.Combobox(search_frame, textvariable=self.search_var, 
                                      font=("Arial", 12), width=15, state="readonly")
        self.combo_search['values'] = ("Name", "Contact", "Consumer ID")
        self.combo_search.current(0)
        self.combo_search.grid(row=0, column=1, padx=5, pady=5)

        Entry(search_frame, textvariable=self.txt_search, font=("Arial", 12), width=20)\
            .grid(row=0, column=2, padx=5, pady=5)

        Button(search_frame, text="Search", command=self.search_data,
              font=("Arial", 10, "bold"), bg="#009688", fg="white", width=8)\
            .grid(row=0, column=3, padx=5, pady=5)

        Button(search_frame, text="Show All", command=self.fetch_data,
              font=("Arial", 10, "bold"), bg="#795548", fg="white", width=8)\
            .grid(row=0, column=4, padx=5, pady=5)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="lightgray")
        table_frame.pack(fill=BOTH, expand=True)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.consumer_table = ttk.Treeview(table_frame, columns=(
            "consumer_id", "name", "address", "contact", "connection_date"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.consumer_table.xview)
        scroll_y.config(command=self.consumer_table.yview)

        # Configure columns
        columns = [
            ("consumer_id", "Consumer ID", 100),
            ("name", "Name", 150),
            ("address", "Address", 200),
            ("contact", "Contact", 100),
            ("connection_date", "Connection Date", 100)
        ]

        for col, heading, width in columns:
            self.consumer_table.heading(col, text=heading)
            self.consumer_table.column(col, width=width, anchor=CENTER if col in ["consumer_id", "contact", "connection_date"] else W)

        self.consumer_table["show"] = "headings"
        self.consumer_table.pack(fill=BOTH, expand=1)
        self.consumer_table.bind("<ButtonRelease-1>", self.get_cursor)

    def initialize_database(self):
        """Initialize the database and create table if not exists"""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678"
            )
            my_cursor = conn.cursor()
            
            my_cursor.execute("CREATE DATABASE IF NOT EXISTS water_supply_system")
            my_cursor.execute("USE water_supply_system")
            
            my_cursor.execute("""
                CREATE TABLE IF NOT EXISTS consumers (
                    consumer_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    address VARCHAR(200),
                    contact VARCHAR(20),
                    connection_date DATE
                )
            """)
            
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to initialize database: {str(e)}")

    def safe_date_conversion(self, date_value):
        """Safely convert date values to string"""
        if date_value is None:
            return ""
        if isinstance(date_value, str):
            return date_value
        if hasattr(date_value, 'strftime'):
            return date_value.strftime("%Y-%m-%d")
        return str(date_value)

    def fetch_data(self):
        """Fetch data from database and display in table"""
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM consumers")
            rows = my_cursor.fetchall()
            
            self.consumer_table.delete(*self.consumer_table.get_children())
            for row in rows:
                # Convert date to string safely
                row = list(row)
                if len(row) > 4:  # Ensure we have the connection_date column
                    row[4] = self.safe_date_conversion(row[4])
                self.consumer_table.insert("", END, values=row)
                
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", 
                               f"Error fetching data:\nCode: {err.errno}\nMessage: {err.msg}", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

    def get_cursor(self, event):
        """Get selected row data and populate form fields"""
        cursor_row = self.consumer_table.focus()
        content = self.consumer_table.item(cursor_row)
        row = content["values"]
        
        if row:
            self.var_consumer_id.set(row[0])
            self.var_name.set(row[1])
            self.var_address.set(row[2])
            self.var_contact.set(row[3])
            self.var_connection_date.set(row[4])

    def add_data(self):
        """Add new consumer to database"""
        if not self.var_name.get() or not self.var_contact.get():
            messagebox.showerror("Error", "Name and Contact are required fields", parent=self.root)
            return
            
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            my_cursor = conn.cursor()
            
            query = """
                INSERT INTO consumers (name, address, contact, connection_date) 
                VALUES (%s, %s, %s, %s)
            """
            values = (
                self.var_name.get(),
                self.var_address.get(),
                self.var_contact.get(),
                self.var_connection_date.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            
            # Generate new random ID for next entry
            x = random.randint(1000, 9999)
            self.var_consumer_id.set(str(x))
            
            messagebox.showinfo("Success", "Consumer added successfully", parent=self.root)
            self.fetch_data()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", 
                               f"Error adding data:\nCode: {err.errno}\nMessage: {err.msg}", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

    def update_data(self):
        """Update existing consumer data"""
        if not self.var_consumer_id.get():
            messagebox.showerror("Error", "Please select a consumer to update", parent=self.root)
            return
            
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            my_cursor = conn.cursor()
            
            query = """
                UPDATE consumers 
                SET name=%s, address=%s, contact=%s, connection_date=%s 
                WHERE consumer_id=%s
            """
            values = (
                self.var_name.get(),
                self.var_address.get(),
                self.var_contact.get(),
                self.var_connection_date.get(),
                self.var_consumer_id.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            
            messagebox.showinfo("Success", "Consumer updated successfully", parent=self.root)
            self.fetch_data()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", 
                               f"Error updating data:\nCode: {err.errno}\nMessage: {err.msg}", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

    def delete_data(self):
        """Delete selected consumer"""
        if not self.var_consumer_id.get():
            messagebox.showerror("Error", "Please select a consumer to delete", parent=self.root)
            return
            
        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this consumer?", parent=self.root):
            return
            
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            my_cursor = conn.cursor()
            
            query = "DELETE FROM consumers WHERE consumer_id=%s"
            values = (self.var_consumer_id.get(),)
            
            my_cursor.execute(query, values)
            conn.commit()
            
            messagebox.showinfo("Success", "Consumer deleted successfully", parent=self.root)
            self.reset_data()
            self.fetch_data()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", 
                               f"Error deleting data:\nCode: {err.errno}\nMessage: {err.msg}", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

    def reset_data(self):
        """Reset form fields"""
        x = random.randint(1000, 9999)
        self.var_consumer_id.set(str(x))
        self.var_name.set("")
        self.var_address.set("")
        self.var_contact.set("")
        self.var_connection_date.set(datetime.now().strftime("%Y-%m-%d"))

    def search_data(self):
        """Search consumers based on criteria"""
        if not self.txt_search.get():
            messagebox.showwarning("Warning", "Please enter search criteria", parent=self.root)
            return
            
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            my_cursor = conn.cursor()
            
            search_text = "%" + self.txt_search.get() + "%"
            
            if self.search_var.get() == "Name":
                query = "SELECT * FROM consumers WHERE name LIKE %s"
            elif self.search_var.get() == "Contact":
                query = "SELECT * FROM consumers WHERE contact LIKE %s"
            else:
                query = "SELECT * FROM consumers WHERE consumer_id LIKE %s"
            
            my_cursor.execute(query, (search_text,))
            rows = my_cursor.fetchall()
            
            self.consumer_table.delete(*self.consumer_table.get_children())
            for row in rows:
                row = list(row)
                if len(row) > 4:  # Ensure we have the connection_date column
                    row[4] = self.safe_date_conversion(row[4])
                self.consumer_table.insert("", END, values=row)
                
            if not rows:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)
                
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", 
                               f"Error searching data:\nCode: {err.errno}\nMessage: {err.msg}", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()