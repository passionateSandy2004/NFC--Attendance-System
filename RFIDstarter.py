import tkinter as tk
import subprocess

def start_application():
    # Replace 'your_application.exe' with the path to your application
    subprocess.Popen(['streamlit', 'run', 'E:\IOT projects\main application\main.py'])

# Create the main Tkinter window
root = tk.Tk()
root.title("Launch Application")

root.geometry("400x200")

# Create a button to start the application
start_button = tk.Button(root, text="Start Application", command=start_application)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
