# School Management System (GUI-Based using tkinter)
# Module: Score Management
# Data Storage: JSON file (scores.json)
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
def add_score():
    try:
        score_value = float(entry_score.get())
    except ValueError:
        messagebox.showerror("Error", "Score must be a number.")
        return

    score = {
        "student_id": entry_student_id.get(),
        "subject": entry_subject.get(),
        "teacher_id": entry_teacher_id.get(),
        "score": score_value
    }

    if not all([score["student_id"], score["subject"], score["teacher_id"], entry_score.get()]):
        messagebox.showerror("Error", "All fields are required.")
        return

    scores = load_data("scores.json")
    scores.append(score)
    save_data("scores.json", scores)
    messagebox.showinfo("Success", "Score added successfully.")
    clear_form()

def clear_form():
    entry_student_id.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    entry_teacher_id.delete(0, tk.END)
    entry_score.delete(0, tk.END)

def view_scores():
    scores = load_data("scores.json")
    display_text = "\n".join([
        f"Student ID: {s['student_id']}, Subject: {s['subject']}, Teacher ID: {s['teacher_id']}, Score: {s['score']}"
        for s in scores
    ])
    if not display_text:
        display_text = "No score records found."
    messagebox.showinfo("Score List", display_text)

def exit_score():
    root.destroy()

# ========== GUI Setup ==========
root = tk.Tk()
root.title("School Management System - Score Management")
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
header = tk.Label(root, text="Score Management", font=("Arial", 15, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill=tk.X)

# --- Main Content Frame ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Score Form Frame ---
form_frame = tk.LabelFrame(main_content, text="Add Score", font=("Arial", 11, "bold"), bg="#f0f4f7", fg="#2c3e50", padx=10, pady=10, bd=2, relief=tk.GROOVE)
form_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

label_style = {"font": ("Arial", 10), "bg": "#f0f4f7", "anchor": "w"}
entry_style = {"font": ("Arial", 10), "bg": "white"}

tk.Label(form_frame, text="Student ID", **label_style).pack(anchor="w", pady=(0,2))
entry_student_id = tk.Entry(form_frame, **entry_style)
entry_student_id.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Subject", **label_style).pack(anchor="w", pady=(0,2))
entry_subject = tk.Entry(form_frame, **entry_style)
entry_subject.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Teacher ID", **label_style).pack(anchor="w", pady=(0,2))
entry_teacher_id = tk.Entry(form_frame, **entry_style)
entry_teacher_id.pack(fill=tk.X, pady=(0,6))

tk.Label(form_frame, text="Score", **label_style).pack(anchor="w", pady=(0,2))
entry_score = tk.Entry(form_frame, **entry_style)
entry_score.pack(fill=tk.X, pady=(0,6))

btn_style = {"font": ("Arial", 10), "bg": "#3498db", "fg": "white", "activebackground": "#2980b9", "activeforeground": "white", "bd": 0, "relief": tk.FLAT, "padx": 5, "pady": 3, "width": 20, "anchor": "center"}

tk.Button(form_frame, text="Add Score", command=add_score, **btn_style).pack(pady=2)
tk.Button(form_frame, text="View Scores", command=view_scores, **btn_style).pack(pady=2)
tk.Button(form_frame, text="Clear Form", command=clear_form, **btn_style).pack(pady=2)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=exit_score, font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=10, pady=6).pack(side=tk.BOTTOM, pady=10)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 8), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()


