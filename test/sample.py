import customtkinter as ctk

# Initialize the app
app = ctk.CTk()
app.title("Calculator")
app.geometry("400x500")

# Set appearance mode (light/dark)
ctk.set_appearance_mode("light")

# Define the input field
input_field = ctk.CTkEntry(app, width=300, height=50, justify='right', font=("Arial", 24))
input_field.grid(row=0, column=0, columnspan=4, pady=20)

# Global variable to store the input
expression = ""

# Function to update the expression in the input field
def update_expression(symbol):
    global expression
    expression += str(symbol)
    input_field.delete(0, ctk.END)
    input_field.insert(ctk.END, expression)

# Function to evaluate the expression
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_field.delete(0, ctk.END)
        input_field.insert(ctk.END, result)
        expression = result  # Update expression with the result
    except:
        input_field.delete(0, ctk.END)
        input_field.insert(ctk.END, "Error")
        expression = ""  # Reset the expression in case of error

# Function to clear the input field
def clear_expression():
    global expression
    expression = ""
    input_field.delete(0, ctk.END)

# Button creation
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

# Add buttons to the grid
for (text, row, column) in buttons:
    if text == "=":
        btn = ctk.CTkButton(app, text=text, width=80, height=60, command=evaluate_expression)
    else:
        btn = ctk.CTkButton(app, text=text, width=80, height=60, command=lambda t=text: update_expression(t))
    btn.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_btn = ctk.CTkButton(app, text="C", width=80, height=60, command=clear_expression)
clear_btn.grid(row=4, column=3, padx=5, pady=5)

# Start the app
app.mainloop()
