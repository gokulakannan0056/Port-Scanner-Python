import tkinter as tk
from datetime import datetime

def key_pressed(event):
    key = event.keysym

    if key == "space":
        key = "[SPACE]"
    elif key == "Return":
        key = "[ENTER]"
    elif key == "BackSpace":
        key = "[BACKSPACE]"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("keystrokes.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {key}\n")

    output.insert(tk.END, f"{key} ")
    output.see(tk.END)

root = tk.Tk()
root.title("Keylogger Security Research Demo")
root.geometry("600x400")

label = tk.Label(
    root,
    text="Security Research Demo\n"
         "Keystrokes are recorded only in this application.",
    font=("Arial", 14)
)
label.pack(pady=20)

output = tk.Text(root, height=10, width=60)
output.pack(pady=10)

root.bind("<KeyPress>", key_pressed)

root.mainloop()