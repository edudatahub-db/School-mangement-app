import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import sys

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def report_student_count_by_grade():
    students = load_data("students.json")
    grade_counts = {}
    for s in students:
        grade = s.get("grade", "Unknown")
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    report = "\n".join([f"Grade {g}: {c} students" for g, c in grade_counts.items()])
    if not report:
        report = "No student records found."
    messagebox.showinfo("Student Count by Grade", report)

def report_average_score_per_subject():
    scores = load_data("scores.json")
    subject_totals = {}
    subject_counts = {}
    for s in scores:
        subject = s.get("subject", "Unknown")
        score = float(s.get("score", 0))
        subject_totals[subject] = subject_totals.get(subject, 0) + score
        subject_counts[subject] = subject_counts.get(subject, 0) + 1
    report = "\n".join([
        f"{subj}: {subject_totals[subj]/subject_counts[subj]:.2f}"
        for subj in subject_totals
    ])
    if not report:
        report = "No score records found."
    messagebox.showinfo("Average Score per Subject", report)

def report_teacher_assignment():
    grades = load_data("grades.json")
    teacher_assignments = {}
    for g in grades:
        teacher = g.get("class_teacher", "Unknown")
        grade_name = g.get("name", "Unknown")
        teacher_assignments.setdefault(teacher, []).append(grade_name)
    report = "\n".join([
        f"Teacher {t}: Grades {', '.join(grades)}"
        for t, grades in teacher_assignments.items()
    ])
    if not report:
        report = "No teacher assignments found."
    messagebox.showinfo("Teacher Assignment Summary", report)

def report_enrollment_status():
    enrollments = load_data("enrollments.json")
    status_counts = {}
    for e in enrollments:
        status = e.get("status", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
    report = "\n".join([f"{status}: {count}" for status, count in status_counts.items()])
    if not report:
        report = "No enrollment records found."
    messagebox.showinfo("Enrollment Status Summary", report)

def report_capacity_vs_actual():
    grades = load_data("grades.json")
    students = load_data("students.json")
    grade_student_counts = {}
    for s in students:
        grade = s.get("grade", "Unknown")
        grade_student_counts[grade] = grade_student_counts.get(grade, 0) + 1
    report_lines = []
    for g in grades:
        name = g.get("name", "Unknown")
        capacity = g.get("capacity", 0)
        actual = grade_student_counts.get(name, 0)
        report_lines.append(f"Grade {name}: {actual}/{capacity} students")
    report = "\n".join(report_lines)
    if not report:
        report = "No grade or student records found."
    messagebox.showinfo("Capacity vs. Actual Students", report)

# --- New Reports Below ---

def report_students_by_grade():
    students = load_data("students.json")
    grades = {}
    for s in students:
        grade = s.get("grade", "Unknown")
        grades.setdefault(grade, []).append(s.get("name", "Unknown"))
    report = ""
    for grade, names in grades.items():
        report += f"Grade {grade}:\n"
        for name in names:
            report += f"  - {name}\n"
    if not report:
        report = "No student records found."
    messagebox.showinfo("Students by Grade", report)

def report_student_report_card():
    students = load_data("students.json")
    scores = load_data("scores.json")
    if not students:
        messagebox.showinfo("Student Report Card", "No student records found.")
        return
    # For demo, show the first student
    student = students[0]
    student_scores = [s for s in scores if s.get("student_id") == student.get("student_id")]
    report = f"Report Card for {student.get('name')} (ID: {student.get('student_id')})\n"
    if student_scores:
        for s in student_scores:
            report += f"{s.get('subject')}: {s.get('score')}\n"
    else:
        report += "No scores found. (Dummy: Math: 80, English: 75)\n"
    messagebox.showinfo("Student Report Card", report)

def report_totals():
    students = load_data("students.json")
    teachers = load_data("teachers.json")
    subjects = load_data("subjects.json")
    report = (
        f"Total Students: {len(students)}\n"
        f"Total Teachers: {len(teachers)}\n"
        f"Total Subjects: {len(subjects)}"
    )
    messagebox.showinfo("Totals", report)

# --- Module Launchers ---

def open_student_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "python school_system.py")])

def open_teacher_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "Teacher.py")])

def open_grade_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "Grade.py")])

def open_subject_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "Subject.py")])

def open_score_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "score.py")])

def open_enrollment_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "enrollment.py")])

def open_user_module():
    subprocess.Popen([sys.executable, os.path.join(os.getcwd(), "user.py")])

def logout():
    root.destroy()

root = tk.Tk()
root.title("School Management System - Dashboard")
root.configure(bg="#f0f4f7")

# --- Set window size and center it ---
window_width = 900
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# --- Header ---
header = tk.Label(root, text="School Management System", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white", pady=15)
header.pack(fill=tk.X)

# --- Main Content Frame (for horizontal layout) ---
main_content = tk.Frame(root, bg="#f0f4f7")
main_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# --- Reports Frame (Centered & Modern) ---
reports_frame = tk.Frame(main_content, bg="#f0f4f7")
reports_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=0)

report_header = tk.Label(
    reports_frame,
    text="Reports",
    font=("Arial", 16, "bold"),
    bg="#2980b9",
    fg="white",
    pady=10
)
report_header.pack(fill=tk.X, pady=(0, 10))

report_btn_style = {
    "font": ("Arial", 12),
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "bd": 0,
    "relief": tk.FLAT,
    "width": 32,
    "anchor": "center",
    "padx": 10,
    "pady": 7
}

btns = [
    ("Student Count by Grade", report_student_count_by_grade),
    ("Average Score per Subject", report_average_score_per_subject),
    ("Teacher Assignment", report_teacher_assignment),
    ("Enrollment Status", report_enrollment_status),
    ("Capacity vs Actual", report_capacity_vs_actual),
    ("Students by Grade", report_students_by_grade),
    ("Student Report Card (Demo)", report_student_report_card),
    ("Total Students, Teachers, Subjects", report_totals)
]

for text, cmd in btns:
    tk.Button(reports_frame, text=text, command=cmd, **report_btn_style).pack(pady=4)

# --- Modules Frame (Centered & Modern) ---
modules_frame = tk.Frame(main_content, bg="#f0f4f7")
modules_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=0)

module_header = tk.Label(
    modules_frame,
    text="Open Modules",
    font=("Arial", 16, "bold"),
    bg="#27ae60",
    fg="white",
    pady=10
)
module_header.pack(fill=tk.X, pady=(0, 10))

module_btn_style = {
    "font": ("Arial", 12),
    "bg": "#0f2a1b",
    "fg": "white",
    "activebackground": "#800FD7",
    "activeforeground": "white",
    "bd": 0,
    "relief": tk.FLAT,
    "width": 32,
    "anchor": "center",
    "padx": 10,
    "pady": 7
}

module_btns = [
    ("Student Management", open_student_module),
    ("Teacher Management", open_teacher_module),
    ("Grade Management", open_grade_module),
    ("Subject Management", open_subject_module),
    ("Score Management", open_score_module),
    ("Enrollment Management", open_enrollment_module),
    ("User Management", open_user_module)
]

for text, cmd in module_btns:
    tk.Button(modules_frame, text=text, command=cmd, **module_btn_style).pack(pady=4)

# --- Exit/Logout Button ---
tk.Button(root, text="Exit / Logout", command=logout, font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white", bd=0, relief=tk.FLAT, padx=20, pady=10).pack(side=tk.BOTTOM, pady=20)

# --- Footer ---
footer = tk.Label(root, text="Developed By Tech Tonic", font=("Arial", 10), bg="#f0f4f7", fg="grey")
footer.pack(side=tk.BOTTOM, pady=0)

root.mainloop()



