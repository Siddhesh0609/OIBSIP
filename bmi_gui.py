import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Please enter valid positive values.")
            return

        height_m = height_cm / 100  # cm to meter
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"Your BMI: {bmi}\nCategory: {category}",
            fg="green"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter numeric values only.")


# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x450")
root.configure(bg="#f2f2f2")

# Heading
title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=20)

# Frame
frame = tk.Frame(root, bg="white", padx=40, pady=30)
frame.pack(pady=10)

# Weight
tk.Label(frame, text="Weight (kg):", font=("Arial", 14), bg="white").grid(row=0, column=0, pady=10, sticky="w")
weight_entry = tk.Entry(frame, font=("Arial", 14), width=20)
weight_entry.grid(row=0, column=1)

# Height
tk.Label(frame, text="Height (cm):", font=("Arial", 14), bg="white").grid(row=1, column=0, pady=10, sticky="w")
height_entry = tk.Entry(frame, font=("Arial", 14), width=20)
height_entry.grid(row=1, column=1)

# Button
calc_btn = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 16),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=calculate_bmi
)
calc_btn.pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 18),
    bg="#f2f2f2"
)
result_label.pack()

root.mainloop()
