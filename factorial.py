import tkinter as tk
from tkinter import messagebox, filedialog
import math
from datetime import datetime

# Configuration
MAX_HISTORY_ENTRIES = 50  # Limit the number of stored entries

# List to store calculation history
calculation_history = []

def calculate_factorial():
    user_input = entry.get().strip()

    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a number.")
        return

    try:
        number = int(user_input)

        if number < 0:
            messagebox.showerror("Input Error", "Factorial is not defined for negative numbers. Please enter a positive integer.")
            return

        result = math.factorial(number)
        result_str = str(result)

        # Limit output length to avoid breaking the UI with extremely large numbers
        display_result = result_str
        if len(result_str) > 100:
            display_result = result_str[:100] + "… (number is very large)"

        result_label.config(text=f"Factorial of {number} is:\n{display_result}")

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add to history with timestamp
        history_entry = f"{timestamp} | {number}! = {display_result}"
        calculation_history.append(history_entry)

        # Enforce max entries limit (keep only the most recent ones)
        if len(calculation_history) > MAX_HISTORY_ENTRIES:
            calculation_history.pop(0)  # Remove the oldest entry

        update_history_display()

    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid positive integer.")

def update_history_display():
    # Clear current history text
    history_text.delete("1.0", tk.END)
    
    # Insert all history entries (most recent first)
    for i, entry in enumerate(reversed(calculation_history), 1):
        history_text.insert(tk.END, f"{i}. {entry}\n")

def clear_history():
    calculation_history.clear()
    update_history_display()
    messagebox.showinfo("History Cleared", "Calculation history has been cleared.")

def export_history():
    if not calculation_history:
        messagebox.showinfo("Export Status", "No history to export.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="history.txt",
        title="Save History File"
    )

    if not file_path:
        return  # User cancelled the dialog

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for i, entry in enumerate(reversed(calculation_history), 1):
                f.write(f"{i}. {entry}\n")
        messagebox.showinfo("Export Success", f"History successfully saved to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to save history file:\n{str(e)}")

# Initialize main window
root = tk.Tk()
root.title("Factorial Calculator")

# Enable fullscreen mode on startup
root.attributes("-fullscreen", True)

# Set black background for the window
root.configure(bg="#000000")

# Define clean, minimalist fonts
font_main = ("Helvetica", 16)
font_title = ("Helvetica", 24, "bold")
font_input = ("Helvetica", 18)
font_history = ("Consolas", 12)  # Monospace font for history clarity

# Title label
title_label = tk.Label(
    root,
    text="Factorial Calculator",
    font=font_title,
    bg="#000000",
    fg="#FFFFFF"
)
title_label.pack(pady=(30, 15))

# Instruction label
instruction_label = tk.Label(
    root,
    text="Enter a positive integer:",
    font=font_main,
    bg="#000000",
    fg="#CCCCCC"
)
instruction_label.pack(pady=(0, 10))

# Input field with white text and dark background
entry = tk.Entry(
    root,
    font=font_input,
    width=20,
    justify="center",
    bd=2,
    relief="solid",
    bg="#111111",
    fg="#FFFFFF",
    insertbackground="#FFFFFF"  # Cursor color
)
entry.pack(pady=10)

# Calculate button with subtle hover effect styling
calculate_btn = tk.Button(
    root,
    text="Calculate",
    font=("Helvetica", 16, "bold"),
    bg="#333333",
    fg="#FFFFFF",
    activebackground="#555555",
    activeforeground="#FFFFFF",
    cursor="hand2",
    padx=30,
    pady=12,
    command=calculate_factorial
)
calculate_btn.pack(pady=15)

# Result label with word wrapping and centered text
result_label = tk.Label(
    root,
    text="",
    font=font_main,
    bg="#000000",
    fg="#FFFFFF",
    wraplength=800,
    justify="center"
)
result_label.pack(pady=10)

# History section
history_frame = tk.Frame(root, bg="#000000")
history_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

history_title = tk.Label(
    history_frame,
    text="Calculation History",
    font=("Helvetica", 18, "bold"),
    bg="#000000",
    fg="#AAAAAA"
)
history_title.pack(anchor="w", pady=(0, 5))

history_text = tk.Text(
    history_frame,
    font=font_history,
    bg="#111111",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=1,
    highlightbackground="#333333",
    height=8,
    wrap=tk.WORD
)
history_text.pack(fill=tk.BOTH, expand=True)

# Controls for history
history_controls = tk.Frame(history_frame, bg="#000000")
history_controls.pack(fill=tk.X, pady=(10, 0))

clear_history_btn = tk.Button(
    history_controls,
    text="Clear History",
    font=("Helvetica", 12, "bold"),
    bg="#550000",
    fg="#FFFFFF",
    activebackground="#880000",
    activeforeground="#FFFFFF",
    cursor="hand2",
    command=clear_history
)
clear_history_btn.pack(side=tk.LEFT, padx=(0, 10))

export_history_btn = tk.Button(
    history_controls,
    text="Export to File",
    font=("Helvetica", 12, "bold"),
    bg="#2b5e2b",
    fg="#FFFFFF",
    activebackground="#4b8e4b",
    activeforeground="#FFFFFF",
    cursor="hand2",
    command=export_history
)
export_history_btn.pack(side=tk.RIGHT)

# Allow exiting fullscreen mode with Escape key
root.bind("<Escape>", lambda e: root.destroy())

# Start the GUI event loop
root.mainloop()