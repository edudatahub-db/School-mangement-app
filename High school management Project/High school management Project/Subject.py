# School Management System (GUI-Based using tkinter)
# Module: Subject Management
# Data Storage: JSON file (subjects.json)
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
def add_subject():
    name = entry_name.get()
    grades = entry_grades.get()
    category = entry_category.get()
    description = entry_description.get()

    if not all([name, grades, category, description]):
        messagebox.showerror("Error", "All fields are required.")
        return

    grades_list = [g.strip() for g in grades.split(",") if g.strip()]

    subject = {
        "name": name,
        "grades": grades_list,
        "category": category,
        "description": description
    }

    subjects = load_data("subjects.json")
    if any(s["name"].lower() == name.lower() for s in subjects):
        messagebox.showerror("Error", "Subject name already exists.")
        return

    subjects.append(subject)
    save_data("subjects.json", subjects)
    messagebox.showinfo("Success", "Subject added successfully.")
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_grades.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def view_subjects():
    subjects = load_data("subjects.json")
    display_text = "\n".join([
        f"Name: {s['name']}, Grades: {', '.join(s['grades'])}, Category: {s['category']}, Desc: {s['description']}"
        for s in subjects
    ])
    if not display_text:
        display_text = "No subject records found."
    messagebox.showinfo("Subject List", display_text)

def exit_subject():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Subject Management")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 420
window_height = 470
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="Subject Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Subject Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Subject", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Subject Name", **label_style).pack(anchor="w", pady=(0,2))
entry_name = tk.Entry(form_frame, **entry_style)
entry_name.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Grades (comma separated, e.g. 9,10,11)", **label_style).pack(anchor="w", pady=(0,2))
entry_grades = tk.Entry(form_frame, **entry_style)
entry_grades.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Category (Science, Arts, Commerce, etc.)", **label_style).pack(anchor="w", pady=(0,2))
entry_category = tk.Entry(form_frame, **entry_style)
entry_category.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Description", **label_style).pack(anchor="w", pady=(0,2))
entry_description = tk.Entry(form_frame, **entry_style)
entry_description.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Subject", command=add_subject, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Subjects", command=view_subjects, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_subject, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


