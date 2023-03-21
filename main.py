from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)



# password = ""
# for char in password_list:
#   password += char

    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


        # is_ok = messagebox.askokcancel(title=website, message=f"Save current info? \nEmail {email} \nPassword: {password}")
        #
        # if is_ok:
        # with open("data.txt", "a") as data_file:  #creates a new data file to store inputs
        #      data_file.write(f"{website} | {email} | {password}\n")  #writes typed data into the text file
        #      website_entry.delete(0, END) #clears the screen of typed data
        #      password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website", font=("Arial", 15, "italic"))  #used when importing all classes of tkinter
website_label.grid(column=0, row=1)  # uses grid format to place items

email = Label(text="Email/Username", font=("Arial", 15, "italic"))
email.grid(column=0, row=2)

password_label = Label(text="Password", font=("Arial", 15, "italic"))
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # places the cursor inside this entry

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "myemail@mail.com")

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()