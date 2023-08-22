import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices()
    password = ''.join(random.choices(characters, k=length))

    # Display the password on the GUI
    password_label.config(text=f"Generated Password: {password}")
    generated_password.set(password)  # Store the generated password in a tkinter variable

def accept_password():
    user_name = name_entry.get()
    accepted_password = generated_password.get()

    # You can add further logic here to do something with the accepted password and user name
    password_label.config(text=f"Accepted Password for {user_name}: {accepted_password}")

def reset_password():
    password_label.config(text="")
    generated_password.set("")
    length_entry.delete(0,tk.END)# Clear the stored generated password

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"))
title_label.pack()
# Create GUI elements
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

length_label = tk.Label(root, text="Enter the desired password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Store the generated password in a tkinter variable
generated_password = tk.StringVar()

password_label = tk.Label(root, text="")
password_label.pack()

accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.pack()

reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.pack()

# Start the main event loop
root.mainloop()
