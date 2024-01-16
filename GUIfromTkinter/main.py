import tkinter as tk
FONT = ("Arial", 10, "bold")


def button_clicked():
    result.config(text=round((int(display.get()) * 1.6093), 2))


# WINDOW
window = tk.Tk()
window.title("Mile to kilometer converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=30)

# EQUAL
equal = tk.Label(text="is equal to", font=FONT)
equal.grid(column=0, row=1)

# RESULT
result = tk.Label(text="0", font=FONT)
result.grid(column=1, row=1)

# MILES
miles = tk.Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

# KM
km = tk.Label(text="Km", font=FONT)
km.grid(column=2, row=1)

# BUTTON
button = tk.Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)

# ENTRY
display = tk.Entry(width=10,)
display.grid(column=1, row=0)

window.mainloop()
