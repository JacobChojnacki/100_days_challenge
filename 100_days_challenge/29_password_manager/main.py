import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_username_input.get()
    passwordInput = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": passwordInput
        }}
    if len(website) > 0 and len(email) > 0 and len(passwordInput) > 0:
        is_ok = messagebox.askokcancel(title=website_input.get(),
                                       message=f"There are the details entered: "
                                               f"\nEmail: {email}"
                                               f"\nPassword: {passwordInput}"
                                               f"\nIs it ok to save?")
        if is_ok:
            try:
                with open('passwords.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('passwords.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
    else:
        messagebox.showinfo(message="Please don't leave any fields empty")


# ----------------------- FIND PASSWORD --------------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no file with such a data.")
    else:
        if website in data:
            email_user = data[website]["email"]
            password_user = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email_user}\nPassword: {password_user}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no details for {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Label
website_label = tkinter.Label(text="Website:")
email_username_label = tkinter.Label(text="Email/Username:")
password = tkinter.Label(text="Password:")

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password.grid(column=0, row=3)

# inputs
website_input = tkinter.Entry(width=35)
website_input.focus()
email_username_input = tkinter.Entry(width=35)
email_username_input.insert(0, "jacobchojnacki@protonmail.com")
password_input = tkinter.Entry(width=35)

website_input.grid(row=1, column=1)
email_username_input.grid(row=2, column=1)
password_input.grid(row=3, column=1)

# buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
add_password = tkinter.Button(text="Add", width=35, command=save_password)
search_button = tkinter.Button(text="Search", width=14, command=find_password)

search_button.grid(column=2, row=1)
generate_password_button.grid(column=2, row=3)
add_password.grid(column=1, row=4)

window.mainloop()
