import tkinter as tk
from tkinter import messagebox

# Function to calculate and display results
def calculate_design():
    try:
        # Getting input values from the user
        fy = float(entry_fy.get())  # Yield strength of steel in MPa
        Mu = float(entry_Mu.get())  # Factored Moment in kNm
        gamma_m = float(entry_gamma_m.get())  # Partial safety factor for material
        width = float(entry_width.get())  # Width of beam section in mm
        depth = float(entry_depth.get())  # Depth of beam section in mm

        # Conversion factors
        kN_to_N = 1000
        mm_to_m = 1/1000
        m_to_mm = 1000

        # Step 1: Calculate the factored bending moment (in Nmm)
        factored_Moment_Nmm = Mu * kN_to_N * m_to_mm

        # Step 2: Section Modulus (Z) Calculation
        Z_required = factored_Moment_Nmm / (fy / gamma_m)  # in mm^3

        # Step 3: Check if guessed section is sufficient
        Z_provided = (width * (depth ** 2)) / 6  # For a rectangular section, approximate Z

        # Result
        result = f"Required Section Modulus (Z): {Z_required:.2f} mm^3\n"
        result += f"Provided Section Modulus (Z): {Z_provided:.2f} mm^3\n"
        if Z_provided >= Z_required:
            result += "The section is adequate for the design."
        else:
            result += "The section is not adequate. Please choose a larger section."

        # Displaying the result in a messagebox
        messagebox.showinfo("Design Results", result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the GUI window
window = tk.Tk()
window.title("Steel Beam Design")

# Labels and Entry fields for inputs
tk.Label(window, text="Yield Strength (fy) in MPa:").grid(row=0, column=0, padx=10, pady=5)
entry_fy = tk.Entry(window)
entry_fy.grid(row=0, column=1)

tk.Label(window, text="Factored Moment (Mu) in kNm:").grid(row=1, column=0, padx=10, pady=5)
entry_Mu = tk.Entry(window)
entry_Mu.grid(row=1, column=1)

tk.Label(window, text="Partial Safety Factor (gamma_m):").grid(row=2, column=0, padx=10, pady=5)
entry_gamma_m = tk.Entry(window)
entry_gamma_m.grid(row=2, column=1)

tk.Label(window, text="Width of Section (in mm):").grid(row=3, column=0, padx=10, pady=5)
entry_width = tk.Entry(window)
entry_width.grid(row=3, column=1)

tk.Label(window, text="Depth of Section (in mm):").grid(row=4, column=0, padx=10, pady=5)
entry_depth = tk.Entry(window)
entry_depth.grid(row=4, column=1)

# Button to trigger the calculation
btn_calculate = tk.Button(window, text="Calculate", command=calculate_design)
btn_calculate.grid(row=5, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()