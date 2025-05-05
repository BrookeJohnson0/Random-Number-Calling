import tkinter as tk
import random

# generation code
def get_random_numbers():
    numbers = []
    for count in range(5):
        numbers.append(random.randint(1, 100))
    return numbers

# GUI coding
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("400x300")
root.configure(bg="#ffe6f0")

# Title
title = tk.Label(root, text="5 Random Numbers (1–100)",
                 font=("Arial", 16, "bold"),
                 bg="#ffe6f0", fg="#8e44ad")
title.pack(pady=10)

# Output Box
output_box = tk.Text(root, height=8, width=35,
                     font=("Arial", 12),
                     bg="#f3e5f5", fg="#6a1b9a",
                     borderwidth=2, relief="ridge")
output_box.pack(pady=10)

# Display Numbers
def show_numbers():
    output_box.delete("1.0", tk.END)
    numbers = get_random_numbers()
    for num in numbers:
        output_box.insert(tk.END, f"{num}\n")

# Button
generate_btn = tk.Button(root, text="Generate Numbers",
                         command=show_numbers,
                         bg="#e1bee7", fg="#4a148c",
                         font=("Arial", 12, "bold"))
generate_btn.pack(pady=10)

# code finished, execute
root.mainloop()
