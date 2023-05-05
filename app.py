# import the necessary modules from tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

# set the background color for the GUI
bg_color = "#326273"

# create a new Tkinter window object
root = Tk()

# set the size, position, icon and title of the window
root.geometry("700x400+300+200")
root.title("Interstella Registry Form")
root.iconbitmap("stellar-coin.ico")
root.resizable(False, False)

# Connect to database
conn = sqlite3.connect("register.sqlite")

# create a cursor object
cur = conn.cursor()

# Define the table name
table_name = 'users'

# Execute the SELECT statement
cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")

# Fetch the result
result = cur.fetchone()

# Check if the result is not None
if result is None:
    cur.execute('''
                CREATE TABLE "users" (
                        "id"	INTEGER NOT NULL UNIQUE,
                        "name"	TEXT NOT NULL,
                        "contact"	TEXT NOT NULL,
                        "age"	TEXT NOT NULL,
                        "gender"	TEXT NOT NULL,
                        "address"	TEXT NOT NULL,
                        PRIMARY KEY("id" AUTOINCREMENT)
                );
                ''')

# set the background color of the window
root.configure(bg=bg_color)

# define a function to clear all the input fields
def cmd_clear():
    nameValue.set("")
    contactValue.set('')
    ageValue.set("")
    addressEntry.delete(1.0, END)
    
# Define a fuction to Submit the form
def cmd_submit():
    name = nameEntry.get()
    contact = contactEntry.get()
    age = ageEntry.get()
    gender = gender_combo.get()
    address = addressEntry.get(1.0, END)
    
    for detail in (name, contact, age, gender, address):
        if len(detail) == 0:
            return messagebox.showerror("Error Message", "Please Fill the Form Compeletely")

    # Insert the user data into the "user" table
    cur.execute("INSERT INTO users (name, contact, age, gender, address) VALUES (?, ?, ?, ?, ?)", (name, contact, age, gender, address))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    # Show a message box
    messagebox.showinfo("Success", "User data has been stored!")
    
    cmd_clear()

# create a label for the heading
Label(text="Interstella", font="arial 18", bg=bg_color, fg="#fff").place(x=330, y=11)
Label(root, text="Please fill the form Below", font="arial 11", bg=bg_color,fg="#fff").place(x=30, y=40)

# create labels for each input field
Label(root, text="Name", font="23", bg=bg_color, fg="#fff").place(x=50, y=100)
Label(root, text="Contact No", font="23", bg=bg_color, fg="#fff").place(x=50, y=150)
Label(root, text="Age", bg=bg_color, font="23", fg="#fff").place(x=50, y=200)
Label(root, text="Gender", bg=bg_color, font="23", fg="#fff").place(x=370, y=200)
Label(root, text="Address", bg=bg_color, fg="#fff", font="23").place(x=50, y=250)

# create input fields for each input field
nameValue  = StringVar()
contactValue = StringVar()
ageValue = StringVar()

# create an Entry widget for the name input field
nameEntry = Entry(root, textvariable=nameValue, width=45, bd=2, font=20 )
nameEntry.place(x=200, y=100)

# create an Entry widget for the contact input field
contactEntry = Entry(root, textvariable=contactValue, width=45, bd=2, font=20 )
contactEntry.place(x=200, y=150)

# create an Entry widget for the age input field
ageEntry = Entry(root, textvariable=ageValue, width=15, bd=2, font=20 )
ageEntry.place(x=200, y=200)

# create a Combobox widget for the gender input field
gender_combo = Combobox(root, values=["Male", "Female", "Prefer not to say"], font="arial 14",  state="r", width=14)
gender_combo.place(x=435, y= 200)
gender_combo.set("Male")

# create a Text widget for the address input field
addressEntry = Text(root, width=50, height=4, bd=4)
addressEntry.place(x=200, y=250)

# create buttons to submit the form, clear the fields, and exit the program
btn_submit = Button(root, text="Submit", bg=bg_color,fg="white",width=15, height=2, command=cmd_submit)
btn_clear = Button(root, text="Clear", bg=bg_color,fg="white",width=15, height=2, command=cmd_clear)
btn_exit = Button(root, text="Exit", bg=bg_color,fg="white",width=15, height=2, command= lambda: root.destroy())

# position the buttons on the form
btn_submit.place(x=200, y=345)
btn_clear.place(x=340, y=345)
btn_exit.place(x=480, y=345)


# Run app
root.mainloop()
