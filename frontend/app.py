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
    score_label.pack(pady=10)
    suggestions_text.config(state=tk.NORMAL)
    suggestions_text.delete(1.0, tk.END)
    suggestions_text.insert(tk.END, "\n".join(result.get("suggestions", [])))
    suggestions_text.config(state=tk.DISABLED)

# Create UI Window
root = tk.Tk()
root.title("AI Resume Analyzer")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#2C2F33")  # Dark mode background

# Frame for better alignment
frame = tk.Frame(root, bg="#2C2F33")
frame.pack(expand=True)

# Upload Button
upload_btn = tk.Button(frame, text="Upload Resume (PDF)", command=upload_file, padx=15, pady=7, 
                       bg="#7289DA", fg="white", font=("Arial", 12, "bold"), 
                       activebackground="#5B6EAE", relief="flat")
upload_btn.pack(pady=20)

# Score Label (Initially Hidden)
score_label = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="#2C2F33", fg="white")

# Suggestions Box
suggestions_text = tk.Text(frame, height=8, width=55, state=tk.DISABLED, bg="#23272A", fg="white", font=("Arial", 10))
suggestions_text.pack(pady=10)

# Run UI
root.mainloop()