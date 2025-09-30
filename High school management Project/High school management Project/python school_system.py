# School Management System (GUI-Based using tkinter)
# Module: Student Management
# Data Storage: JSON file (students.json)
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
def add_student():
    student = {
        "student_id": entry_id.get(),
        "name": entry_name.get(),
        "grade": entry_grade.get(),
        "dob": entry_dob.get(),
        "gender": entry_gender.get(),
        "phone": entry_phone.get(),
        "address": entry_address.get(),
        "email": entry_email.get(),
        "guardian_name": entry_guardian_name.get(),
        "guardian_phone": entry_guardian_phone.get(),
        "registered_at": entry_registered_at.get()
    }

    if not all(student.values()):
        messagebox.showerror("Error", "All fields are Requiry.")
        return

    students = load_data("students.json")
    if any(s["student_id"] == student["student_id"] for s in students):
        messagebox.showerror("Error", "Student ID already exists.")
        return

    students.append(student)
    save_data("students.json", students)
    messagebox.showinfo("Success", "Student added successfully.")
    clear_form()

def clear_form():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_guardian_name.delete(0, tk.END)
    entry_guardian_phone.delete(0, tk.END)
    entry_registered_at.delete(0, tk.END)

def view_students():
    students = load_data("students.json")
    display_text = "\n".join([
        f"ID: {s['student_id']}, Name: {s['name']}, Grade: {s['grade']}, Registered: {s['registered_at']}"
        for s in students
    ])
    if not display_text:
        display_text = "No student records found."
    messagebox.showinfo("Student List", display_text)

def exit_student():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Student Management")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 420
window_height = 920
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="Student Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Student Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Student", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Student ID", **label_style).pack(anchor="w", pady=(0,2))
entry_id = tk.Entry(form_frame, **entry_style)
entry_id.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Name", **label_style).pack(anchor="w", pady=(0,2))
entry_name = tk.Entry(form_frame, **entry_style)
entry_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Grade", **label_style).pack(anchor="w", pady=(0,2))
entry_grade = tk.Entry(form_frame, **entry_style)
entry_grade.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Date of Birth (YYYY-MM-DD)", **label_style).pack(anchor="w", pady=(0,2))
entry_dob = tk.Entry(form_frame, **entry_style)
entry_dob.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Gender", **label_style).pack(anchor="w", pady=(0,2))
entry_gender = tk.Entry(form_frame, **entry_style)
entry_gender.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Phone", **label_style).pack(anchor="w", pady=(0,2))
entry_phone = tk.Entry(form_frame, **entry_style)
entry_phone.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Address", **label_style).pack(anchor="w", pady=(0,2))
entry_address = tk.Entry(form_frame, **entry_style)
entry_address.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Email", **label_style).pack(anchor="w", pady=(0,2))
entry_email = tk.Entry(form_frame, **entry_style)
entry_email.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Guardian Name", **label_style).pack(anchor="w", pady=(0,2))
entry_guardian_name = tk.Entry(form_frame, **entry_style)
entry_guardian_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Guardian Phone", **label_style).pack(anchor="w", pady=(0,2))
entry_guardian_phone = tk.Entry(form_frame, **entry_style)
entry_guardian_phone.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Registered At (YYYY-MM-DD)", **label_style).pack(anchor="w", pady=(0,2))
entry_registered_at = tk.Entry(form_frame, **entry_style)
entry_registered_at.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Student", command=add_student, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Students", command=view_students, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_student, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


