from tkinter import *
from PIL import Image, ImageTk
from custumer import Cust_Win
from bill import Bill_Win
from Complaint import ComplaintManagementPage

class WaterSupplyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Supply Management System")
        self.root.geometry("1550x800+0+0")

        # Title Bar
        lbl_title = Label(
            self.root,
            text="Water Supply Management System",
            font=("Times New Roman", 45, "bold"),
            bg="black", fg="gold", bd=4, relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1550, height=75)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=80, width=1550, height=750)

        # Menu Label
        lbl_menu = Label(
            main_frame,
            text="MENU",
            font=("Times New Roman", 20, "bold"),
            bg="black", fg="gold", bd=4, relief=RIDGE
        )
        lbl_menu.place(x=0, y=0, width=230)

        # Buttons Frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=710)

        # Button List (Text, Command)
        buttons = [
            ("Consumer", self.open_consumer_page),
            ("Bill", self.open_bill_page),
            ("Complaint", self.open_complaint_page),
            ("LOGOUT", self.logout)
        ]

        for i, (text, cmd) in enumerate(buttons):
            btn = Button(
                btn_frame,
                text=text,
                command=cmd,
                width=20,
                font=("Times New Roman", 16, "bold"),
                bg="black", fg="white", bd=0, cursor="hand1"
            )
            btn.grid(row=i, column=0, pady=1)

        # Right Image
        img3 = Image.open(r"C:\\Users\\Nikita\\OneDrive\\Desktop\\water\\image wa.jpg")
        img3 = img3.resize((1500, 900), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=230, y=0, width=1310, height=900)

    def open_consumer_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def open_bill_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Bill_Win(self.new_window)

    def open_complaint_page(self):
        self.new_window = Toplevel(self.root)
        self.app = ComplaintManagementPage(self.new_window)

    def logout(self):
        self.root.destroy()
        LoginWindow()
        

if __name__ == "__main__":
    root = Tk()
    obj = WaterSupplyManagementSystem(root)
    root.mainloop()
    
