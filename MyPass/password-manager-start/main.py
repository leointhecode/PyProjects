import tkinter as kin
from tkinter import messagebox
import pandas as pd
from random import choice, randint, shuffle
import pyperclip
import json

# CONSTANTS
COMMON_MAIL = "leonardespicass@gmail.com"
FONT = ("Arial", 10,)

# C:/Users/leona/Documents/
FILE_ADDRESS = "P_DATA.json"

FILE_ADDRESS_CSV = "C:/Users/leona/Documents/P_DATA.csv"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [[choice(letters) for _ in range(randint(8, 10))] +
                     [choice(symbols) for _ in range(randint(2, 4))] +
                     [choice(numbers) for _ in range(randint(2, 4))]]

    shuffle(password_list[0])

    password = "".join(password_list[0])

    password_entry.delete(first=0, last='end')
    password_entry.insert(index=0, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == 'extract::csv':
        get_csv = messagebox.askokcancel(title="Extract Confirmation",
                                         message="The data is about to be extracted.")
        if get_csv:
            password_dataframe = pd.read_csv(FILE_ADDRESS)
            password_dataframe.to_csv(FILE_ADDRESS_CSV)
    else:
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showwarning(title="Oops", message="Hey it seems like you forget some fields.")

        is_ok = messagebox.askokcancel(title="Data Confirmation", message=f"This is the data submitted "                                                                             
                                                                          f"\nWebsite: {website}"
                                                                          f"\nEmail: {email} "
                                                                          f"\nPassword: {password}")
        if is_ok:

            try:
                with open(FILE_ADDRESS, "r") as data_file:
                    # read old data
                    data = json.load(data_file)
                    # update with new data
                    data.update(new_data)
                with open(FILE_ADDRESS, "w") as data_file:
                    # save updated data
                    json.dump(data, data_file, indent=4)

            except FileNotFoundError:
                with open(FILE_ADDRESS, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            except json.JSONDecodeError:
                with open(FILE_ADDRESS, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            finally:
                website_entry.delete(first=0, last='end')
                password_entry.delete(first=0, last='end')


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open(FILE_ADDRESS) as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title="Search Result", message=f"Email: {data[website]['email']} "
                                                           f"\nPassword: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title="Data Not Founded",
                               message="The database is empty, please submit some information before.")
    except KeyError:
        messagebox.showwarning(title="Data Not Founded",
                               message="The submitted data was not founded, please check the inserted data.")
    except json.JSONDecodeError:
        messagebox.showwarning(title="Data Not Founded",
                               message="The database is empty, please submit some information before.")


# ---------------------------- UI SETUP ------------------------------- #
window = kin.Tk()
window.title("Password generator")
window.config(padx=40, pady=40)

# IMAGE
photo_pass = kin.PhotoImage(file="/home/lenny/development/learning/python/MyPass/password-manager-start/logo.png")
canvas = kin.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo_pass)
canvas.grid(column=1, row=0)

# TEXT
website_name = kin.Label(text="Website: ", font=FONT)
website_name.grid(column=0, row=1)

email_name = kin.Label(text="Email/Username: ", font=FONT)
email_name.grid(column=0, row=2)

password_name = kin.Label(text="Password: ", font=FONT)
password_name.grid(column=0, row=3)

# ENTRIES
website_entry = kin.Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = kin.Entry(width=52)
email_entry.insert(index=0, string=COMMON_MAIL)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = kin.Entry(width=33)
password_entry.grid(column=1, row=3, )

# BUTTONS
add_button = kin.Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

password_button = kin.Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row=3)

search_button = kin.Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()
