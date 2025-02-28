import itertools
import string
import tkinter as tk
from tkinter import messagebox

# Hardcoded user credentials
USER_CREDENTIALS = {
    "user1": "abcde",
    "user2": "qwerty",
    "user3": "letmein"
}

def dictionary_attack(username):
    """Attempts to find the password using a dictionary attack."""
    with open("C:/Users/EW2023/Downloads/dictionary.txt", "r") as file:
        password_list = file.readlines()
    
    for password in password_list:
        if password.strip() == USER_CREDENTIALS.get(username, ""):
            return True
    return False

def brute_force_attack(username):
    """Performs a brute force attack to find a 5-letter password."""
    chars = string.ascii_letters  # A-Z, a-z
    for attempt in itertools.product(chars, repeat=5):
        if "".join(attempt) == USER_CREDENTIALS.get(username, ""):
            return "".join(attempt)
    return None

def perform_dictionary_attack():
    username = username_entry.get()
    if dictionary_attack(username):
        messagebox.showinfo("Success", "Dictionary attack successful!")
        open_success_window()
    else:
        messagebox.showerror("Failure", "Dictionary attack failed.")

def perform_brute_force_attack():
    username = username_entry.get()
    brute_force_result = brute_force_attack(username)
    if brute_force_result:
        messagebox.showinfo("Success", f"Brute force attack successful! Password: {brute_force_result}")
        open_success_window()
    else:
        messagebox.showerror("Failure", "Brute force attack failed.")

def open_success_window():
    success_window = tk.Tk()
    success_window.title("Success")
    tk.Label(success_window, text="Assignment Done!", font=("Arial", 14)).pack()
    success_window.mainloop()

# GUI Setup
root = tk.Tk()
root.title("Login and Attack Options")
root.geometry("300x300")

# Login Section
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=lambda: messagebox.showinfo("Info", "Login successful!" if username_entry.get() in USER_CREDENTIALS and USER_CREDENTIALS[username_entry.get()] == password_entry.get() else messagebox.showerror("Error", "Invalid credentials!"))).pack()

# Attack Options
tk.Button(root, text="Dictionary Attack", command=perform_dictionary_attack).pack()
tk.Button(root, text="Brute Force Attack", command=perform_brute_force_attack).pack()

root.mainloop()
