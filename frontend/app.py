import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# Backend API Endpoint
API_URL = "http://127.0.0.1:5000/analyze_resume"

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    
    try:
        with open(file_path, "rb") as file:
            response = requests.post(API_URL, files={"file": file})
        
        if response.status_code == 200:
            result = response.json()
            display_results(result)
        else:
            messagebox.showerror("Error", "Failed to analyze resume")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_results(result):
    score_label.config(text=f"Resume Score: {result.get('score', 'N/A')}%", fg="white")
    score_label.pack()
    suggestions_text.config(state=tk.NORMAL)
    suggestions_text.delete(1.0, tk.END)
    suggestions_text.insert(tk.END, "\n".join(result.get("suggestions", [])))
    suggestions_text.config(state=tk.DISABLED)

# Create UI Window
root = tk.Tk()
root.title("AI Resume Analyzer")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2C2F33")  # Dark mode background

# Upload Button
upload_btn = tk.Button(root, text="Upload Resume (PDF)", command=upload_file, padx=10, pady=5, bg="#7289DA", fg="white")
upload_btn.pack(pady=20)

# Score Label (Initially Hidden)
score_label = tk.Label(root, text="", font=("Arial", 12), bg="#2C2F33", fg="white")

# Suggestions Box
suggestions_text = tk.Text(root, height=10, width=50, state=tk.DISABLED, bg="#23272A", fg="white")
suggestions_text.pack(pady=10)

# Run UI
root.mainloop()