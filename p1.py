# ===============================
# MODULES
# ===============================
import tkinter as tk
from tkinter import messagebox
import datetime
import random


# ===============================
# CLASS
# ===============================
class IDCardGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("ID Card Management System")
        self.root.geometry("400x400")

        # DATABASE (Using Roll Numbers)
        self.students_db = {
            "2025214043": {"name": "Prathibha", "email": "prathibha@gmail.com"},
            "2025214044": {"name": "Rahul", "email": "rahul@gmail.com"},
            "2025214045": {"name": "Sneha", "email": "sneha@gmail.com"}
        }

        self.lost_cards = {}

        # UI ELEMENTS
        self.label = tk.Label(root, text="Enter Roll Number (QR):", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.collect_btn = tk.Button(root, text="Collect ID", command=self.collect_id)
        self.collect_btn.pack(pady=5)

        self.view_btn = tk.Button(root, text="View Lost Cards", command=self.view_lost_cards)
        self.view_btn.pack(pady=5)

        self.return_btn = tk.Button(root, text="Return ID Card", command=self.return_card)
        self.return_btn.pack(pady=5)


    # ===============================
    # FUNCTION 1: Generate Token
    # ===============================
    def generate_token(self):
        return random.randint(1000, 9999)


    # ===============================
    # FUNCTION 2: Collect ID
    # ===============================
    def collect_id(self):
        roll_no = self.entry.get().strip()

        if roll_no in self.students_db:
            time_now = datetime.datetime.now()
            token = self.generate_token()

            self.lost_cards[roll_no] = {
                "time": time_now,
                "token": token
            }

            name = self.students_db[roll_no]["name"]

            messagebox.showinfo("Success", f"ID collected for {name}\nToken: {token}")

        else:
            messagebox.showerror("Error", "Invalid Roll Number!")


    # ===============================
    # FUNCTION 3: View Lost Cards
    # ===============================
    def view_lost_cards(self):
        if not self.lost_cards:
            messagebox.showinfo("Info", "No lost cards found.")
        else:
            info = ""
            for roll, details in self.lost_cards.items():
                name = self.students_db[roll]["name"]
                info += f"{roll} | {name} | Token: {details['token']}\n"

            messagebox.showinfo("Lost Cards", info)


    # ===============================
    # FUNCTION 4: Return ID
    # ===============================
    def return_card(self):
        roll_no = self.entry.get().strip()

        if roll_no in self.lost_cards:
            token_window = tk.Toplevel(self.root)
            token_window.title("Enter Token")

            tk.Label(token_window, text="Enter Token:").pack(pady=5)
            token_entry = tk.Entry(token_window)
            token_entry.pack(pady=5)

            def verify():
                try:
                    token = int(token_entry.get())
                    if token == self.lost_cards[roll_no]["token"]:
                        name = self.students_db[roll_no]["name"]
                        del self.lost_cards[roll_no]
                        messagebox.showinfo("Success", f"Returned to {name}")
                        token_window.destroy()
                    else:
                        messagebox.showerror("Error", "Wrong token!")
                except:
                    messagebox.showerror("Error", "Enter valid number!")

            tk.Button(token_window, text="Submit", command=verify).pack(pady=5)

        else:
            messagebox.showerror("Error", "No record found!")


# ===============================
# MAIN
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = IDCardGUI(root)
    root.mainloop()