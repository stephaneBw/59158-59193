import tkinter as tk
from tkinter import filedialog
import subprocess

path = 'C:/Users/ostep/PycharmProjects/59158-59193/main.py'


def run_scraper():
    subprocess.run(["python", path])


def browse_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Script File",
                                           filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    if file_path:
        script_path_entry.delete(0, tk.END)
        script_path_entry.insert(0, file_path)


# Create the main application window
root = tk.Tk()
root.title("GUI Interface for Scraper Script")


# Script Path Label and Entry
tk.Label(root, text="Enter Script Path: ").pack()
script_path_entry = tk.Entry(root, width=50)
script_path_entry.pack()

# Browse Button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Run Script Button
run_button = tk.Button(root, text="Run Scraper Script", command=run_scraper)
run_button.pack()


root.mainloop()
