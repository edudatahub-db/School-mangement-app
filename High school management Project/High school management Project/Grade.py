# School Management System (GUI-Based using tkinter)
# Module: Grade Management
# Data Storage: JSON file (grades.json)
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
def add_grade():
    try:
        capacity_value = int(entry_capacity.get())
    except ValueError:
        messagebox.showerror("Error", "Capacity must be an integer.")
        return

    grade = {
        "name": entry_name.get(),
        "description": entry_description.get(),
        "level": entry_level.get(),
        "class_teacher": entry_class_teacher.get(),
        "capacity": capacity_value
    }

    if not all([grade["name"], grade["description"], grade["level"], grade["class_teacher"], entry_capacity.get()]):
        messagebox.showerror("Error", "All fields are required.")
        return

    grades = load_data("grades.json")
    if any(g["name"] == grade["name"] for g in grades):
        messagebox.showerror("Error", "Grade name already exists.")
        return

    grades.append(grade)
    save_data("grades.json", grades)
    messagebox.showinfo("Success", "Grade added successfully.")
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_level.delete(0, tk.END)
    entry_class_teacher.delete(0, tk.END)
    entry_capacity.delete(0, tk.END)

def view_grades():
    grades = load_data("grades.json")
    display_text = "\n".join([
        f"Name: {g['name']}, Desc: {g['description']}, Level: {g['level']}, Class Teacher: {g['class_teacher']}, Capacity: {g['capacity']}"
        for g in grades
    ])
    if not display_text:
        display_text = "No grade records found."
    messagebox.showinfo("Grade List", display_text)

def exit_grade():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Grade Management")
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
header = tk.Label(root, text="Grade Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Grade Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Grade", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Grade Name", **label_style).pack(anchor="w", pady=(0,2))
entry_name = tk.Entry(form_frame, **entry_style)
entry_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Description", **label_style).pack(anchor="w", pady=(0,2))
entry_description = tk.Entry(form_frame, **entry_style)
entry_description.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Level (Junior, Senior, etc.)", **label_style).pack(anchor="w", pady=(0,2))
entry_level = tk.Entry(form_frame, **entry_style)
entry_level.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Class Teacher (Teacher ID)", **label_style).pack(anchor="w", pady=(0,2))
entry_class_teacher = tk.Entry(form_frame, **entry_style)
entry_class_teacher.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Capacity", **label_style).pack(anchor="w", pady=(0,2))
entry_capacity = tk.Entry(form_frame, **entry_style)
entry_capacity.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Grade", command=add_grade, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Grades", command=view_grades, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_grade, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


