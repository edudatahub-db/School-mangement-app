# School Management System (GUI-Based using tkinter)
# Module: User Management
# Data Storage: JSON file (users.json)
# Libraries: tkinter, json, os

import tkinter as tk
from tkinter import messagebox
import json
import os

# ========== Data Utilities ==========
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ========== GUI Functions ==========
def add_user():
    user = {
        "username": entry_username.get(),
        "password": entry_password.get(),
        "role": entry_role.get(),
        "full_name": entry_full_name.get(),
        "created_at": entry_created_at.get()
    }

    if not all(user.values()):
        messagebox.showerror("Error", "All fields are required.")
        return

    users = load_data("users.json")
    if any(u["username"] == user["username"] for u in users):
        messagebox.showerror("Error", "Username already exists.")
        return

    users.append(user)
    save_data("users.json", users)
    messagebox.showinfo("Success", "User added successfully.")
    clear_form()

def clear_form():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_full_name.delete(0, tk.END)
    entry_created_at.delete(0, tk.END)

def view_users():
    users = load_data("users.json")
    display_text = "\n".join([
        f"Username: {u['username']}, Role: {u['role']}, Name: {u['full_name']}, Created: {u['created_at']}"
        for u in users
    ])
    if not display_text:
        display_text = "No user records found."
    messagebox.showinfo("User List", display_text)

def exit_user():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - User Management")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 420
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="User Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- User Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add User", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Username", **label_style).pack(anchor="w", pady=(0,2))
entry_username = tk.Entry(form_frame, **entry_style)
entry_username.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Password", **label_style).pack(anchor="w", pady=(0,2))
entry_password = tk.Entry(form_frame, show="*", **entry_style)
entry_password.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Role (admin, staff, etc.)", **label_style).pack(anchor="w", pady=(0,2))
entry_role = tk.Entry(form_frame, **entry_style)
entry_role.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Full Name", **label_style).pack(anchor="w", pady=(0,2))
entry_full_name = tk.Entry(form_frame, **entry_style)
entry_full_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Created At (YYYY-MM-DD)", **label_style).pack(anchor="w", pady=(0,2))
entry_created_at = tk.Entry(form_frame, **entry_style)
entry_created_at.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add User", command=add_user, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Users", command=view_users, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_user, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


