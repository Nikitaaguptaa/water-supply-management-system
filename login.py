import tkinter as tk
from tkinter import messagebox
import hashlib
import mysql.connector  # यहाँ जोड़ें
from home import WaterSupplyManagementSystem
from user_dashboard import UserDashboard

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Supply System Login")
        
        # GUI Components
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)
        
        tk.Label(self.root, text="Password:").pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)
        
        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=20)
        
    def authenticate(self):
        username = self.entry_username.get()
        password = hashlib.sha256(self.entry_password.get().encode()).hexdigest()
        
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="water_supply_system"
            )
            cursor = conn.cursor()
            cursor.execute("""
                SELECT consumer_id, is_admin 
                FROM consumers 
                WHERE username=%s AND password_hash=%s
            """, (username, password))
            user = cursor.fetchone()
            
            if user:
                self.root.destroy()
                if user[1]:  # Admin check
                    admin_root = tk.Tk()
                    WaterSupplyManagementSystem(admin_root)
                    admin_root.mainloop()
                else:
                    user_root = tk.Tk()
                    UserDashboard(user_root, user[0])
                    user_root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid credentials")
                
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    login_app = LoginWindow()
    login_app.root.mainloop()