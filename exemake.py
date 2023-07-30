import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess

def browse_file():
    filename = filedialog.askopenfilename(filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    file_path.set(filename)

def create_executable():
    py_file = file_path.get()
    command = f'pyinstaller --onefile "{py_file}"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, err = process.communicate()

    # Create the result window
    result_window = tk.Toplevel(root)
    result_window.geometry("300x120")

    if process.returncode != 0:  # If the command failed
        result_window.configure(background='red')
        result_label = tk.Label(result_window, text="Error!", bg="red", fg="white", font=("Arial", 14))
        result_message = tk.Label(result_window, text=f"Error code: {process.returncode}(Likely a bad path)", bg="red", fg="white", wraplength=250, font=("Arial", 12))
    else:
        result_window.configure(background='green')
        result_label = tk.Label(result_window, text="Operation completed successfully!", bg="green", fg="white", font=("Arial", 14))
        result_message = tk.Label(result_window, text="", bg="green", fg="white")

    result_label.pack(pady=5)
    result_message.pack(pady=5)

    close_button = tk.Button(result_window, text="Close", command=root.destroy, font=("Arial", 12))
    close_button.pack(pady=5)

root = tk.Tk()
root.title("Python Executable Master")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_path = tk.StringVar()

file_entry = ttk.Entry(mainframe, width=50, textvariable=file_path)
file_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

browse_button = ttk.Button(mainframe, text="Browse", command=browse_file)
browse_button.grid(column=3, row=1, sticky=tk.W)

create_button = ttk.Button(mainframe, text="Create Executable", command=create_executable)
create_button.grid(column=2, row=2, sticky=tk.W)

close_button = ttk.Button(mainframe, text="Close", command=root.destroy)
close_button.grid(column=3, row=2, sticky=tk.E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

file_entry.focus()

root.mainloop()
