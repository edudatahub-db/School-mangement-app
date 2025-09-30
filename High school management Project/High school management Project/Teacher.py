# School Management System (GUI-Based using tkinter)
# Modules: Teacher Management (GUI Only Version for Now)
# Data Storage: JSON file (teachers.json)
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
def add_teacher():
    teacher = {
        "Teacher_id": entry_id.get(),
        "name": entry_name.get(),
        "age": entry_age.get(),
        "dob": entry_dob.get(),
        "gender": entry_gender.get(),
        "phone": entry_phone.get(),
        "salary": entry_salary.get(),
        "employment_date": entry_employment_date.get(),
        "courses": entry_courses.get()
    }

    if not all(teacher.values()):
        messagebox.showerror("Error", "All fields are required.")
        return

    teachers = load_data("teachers.json")
    if any(t["Teacher_id"] == teacher["Teacher_id"] for t in teachers):
        messagebox.showerror("Error", "Teacher ID already exists.")
        return

    teachers.append(teacher)
    save_data("teachers.json", teachers)
    messagebox.showinfo("Success", "Teacher added successfully.")
    clear_form()

def clear_form():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_employment_date.delete(0, tk.END)
    entry_courses.delete(0, tk.END)

def view_teachers():
    teachers = load_data("teachers.json")
    display_text = "\n".join([
        f"ID: {t['Teacher_id']}, Name: {t['name']}, Age: {t['age']}, Salary: {t['salary']}, Courses: {t['courses']}"
        for t in teachers
    ])
    if not display_text:
        display_text = "No teacher records found."
    messagebox.showinfo("Teacher List", display_text)

def exit_teacher():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Teacher Management")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 420
window_height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="Teacher Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Teacher Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Teacher", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Teacher ID", **label_style).pack(anchor="w", pady=(0,2))
entry_id = tk.Entry(form_frame, **entry_style)
entry_id.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Name", **label_style).pack(anchor="w", pady=(0,2))
entry_name = tk.Entry(form_frame, **entry_style)
entry_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Age", **label_style).pack(anchor="w", pady=(0,2))
entry_age = tk.Entry(form_frame, **entry_style)
entry_age.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Date of Birth (YYYY-MM-DD)", **label_style).pack(anchor="w", pady=(0,2))
entry_dob = tk.Entry(form_frame, **entry_style)
entry_dob.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Gender", **label_style).pack(anchor="w", pady=(0,2))
entry_gender = tk.Entry(form_frame, **entry_style)
entry_gender.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Phone", **label_style).pack(anchor="w", pady=(0,2))
entry_phone = tk.Entry(form_frame, **entry_style)
entry_phone.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Salary", **label_style).pack(anchor="w", pady=(0,2))
entry_salary = tk.Entry(form_frame, **entry_style)
entry_salary.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Employment Date (YYYY-MM-DD)", **label_style).pack(anchor="w", pady=(0,2))
entry_employment_date = tk.Entry(form_frame, **entry_style)
entry_employment_date.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Courses (comma separated)", **label_style).pack(anchor="w", pady=(0,2))
entry_courses = tk.Entry(form_frame, **entry_style)
entry_courses.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Teacher", command=add_teacher, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Teachers", command=view_teachers, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_teacher, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


