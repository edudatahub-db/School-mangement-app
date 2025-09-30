# School Management System (GUI-Based using tkinter)
# Module: Enrollment Management
# Data Storage: JSON file (enrollments.json)
# Libraries: tkinter, json, os, datetime

import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

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
def add_enrollment():
    student_id = entry_student_id.get()
    grade = entry_grade.get()
    academic_year = "2024-2025"
    status = entry_status.get()
    enroll_date = datetime.now().strftime("%Y-%m-%d")

    # Validate student_id and grade against students.json
    students = load_data("students.json")
    student_ids = [s["student_id"] for s in students]
    grades = [s["grade"] for s in students]

    if not all([student_id, grade, status]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if student_id not in student_ids:
        messagebox.showerror("Error", "Student ID does not exist.")
        return

    if grade not in grades:
        messagebox.showerror("Error", "Grade does not exist.")
        return

    enrollment = {
        "student_id": student_id,
        "grade": grade,
        "enroll_date": enroll_date,
        "academic_year": academic_year,
        "status": status
    }

    enrollments = load_data("enrollments.json")
    enrollments.append(enrollment)
    save_data("enrollments.json", enrollments)
    messagebox.showinfo("Success", "Enrollment added successfully.")
    clear_form()

def clear_form():
    entry_student_id.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_status.delete(0, tk.END)

def view_enrollments():
    enrollments = load_data("enrollments.json")
    display_text = "\n".join([
        f"Student ID: {e['student_id']}, Grade: {e['grade']}, Year: {e['academic_year']}, Status: {e['status']}, Enrolled: {e['enroll_date']}"
        for e in enrollments
    ])
    if not display_text:
        display_text = "No enrollment records found."
    messagebox.showinfo("Enrollment List", display_text)

def exit_enrollment():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Enrollment Management")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 420
window_height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="Enrollment Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Enrollment Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Enrollment", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Student ID", **label_style).pack(anchor="w", pady=(0,2))
entry_student_id = tk.Entry(form_frame, **entry_style)
entry_student_id.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Grade", **label_style).pack(anchor="w", pady=(0,2))
entry_grade = tk.Entry(form_frame, **entry_style)
entry_grade.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Status (active, transferred, graduated)", **label_style).pack(anchor="w", pady=(0,2))
entry_status = tk.Entry(form_frame, **entry_style)
entry_status.pack(fill=tk.X, pady=(0,6))

# Show info (not editable)
tk.Label(form_frame, text=f"Academic Year: 2024-2025", fg="blue", bg="#f0f4f7", font=("Arial", 9, "italic")).pack(anchor="w", pady=(8,0))
tk.Label(form_frame, text=f"Enrollment Date: {datetime.now().strftime('%Y-%m-%d')}", fg="blue", bg="#f0f4f7", font=("Arial", 9, "italic")).pack(anchor="w", pady=(0,8))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Enrollment", command=add_enrollment, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Enrollments", command=view_enrollments, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_enrollment, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()



