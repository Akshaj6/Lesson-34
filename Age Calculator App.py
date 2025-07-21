import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# --- Core Logic Function ---
def calculate_age():
    """
    Gets user input, validates it, calculates the age,
    and displays a personalized message.
    """
    try:
        # Get values from entry widgets
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        if not name:
            messagebox.showerror("Input Error", "Please enter a name.")
            return

        # Create a date object for the user's birthday
        birth_date = date(year, month, day)
        
        # Get today's date
        today = date.today()
        
        # Check if the birth date is in the future
        if birth_date > today:
            messagebox.showerror("Date Error", "Date of birth cannot be in the future.")
            return

        # Calculate age
        # The logic subtracts one year if the birthday hasn't occurred yet this year
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Create the personalized message
        birth_date_str = birth_date.strftime("%d %B, %Y") # e.g., "15 March, 2000"
        result_message = f"Hello, {name}!\nBorn on {birth_date_str},\nyou are currently {age} years old."

        # Update the result label
        result_label.config(text=result_message, foreground="blue")

    except ValueError:
        # This handles errors if the user enters non-numbers for dates
        # or an invalid date like February 30th
        messagebox.showerror("Input Error", "Please enter a valid day, month, and year.")
    except Exception as e:
        # Catch any other unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f0f0") # Set a light grey background

# Use a style for better-looking widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 12, "bold"))
style.configure("TEntry", font=("Helvetica", 12))

# --- Using .grid() for the input fields ---
# Create a frame to hold the input widgets
input_frame = ttk.Frame(root, padding="30 10 30 10")
input_frame.pack(pady=20) # Use pack for the frame itself

# Name
name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w") # sticky='w' aligns to the west (left)
name_entry = ttk.Entry(input_frame, width=20)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Day
day_label = ttk.Label(input_frame, text="Day (DD):")
day_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
day_entry = ttk.Entry(input_frame, width=20)
day_entry.grid(row=1, column=1, padx=10, pady=10)

# Month
month_label = ttk.Label(input_frame, text="Month (MM):")
month_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
month_entry = ttk.Entry(input_frame, width=20)
month_entry.grid(row=2, column=1, padx=10, pady=10)

# Year
year_label = ttk.Label(input_frame, text="Year (YYYY):")
year_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
year_entry = ttk.Entry(input_frame, width=20)
year_entry.grid(row=3, column=1, padx=10, pady=10)


# --- Using .pack() for the button and result label ---

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=20) # Use pack for this widget

# Result Label
result_label = ttk.Label(root, text="", font=("Helvetica", 14, "bold"), justify="center")
result_label.pack(pady=10) # Use pack for this widget


# --- Start the main event loop ---
root.mainloop()