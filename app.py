# Import the Tkinter module and the messagebox module
from tkinter import *
from tkinter import messagebox

# Create the main application window
app = Tk()

# Set the window size and title
app.geometry("500x300")
app.title("Registration From")

# Create a label for the header of the form
lblhead = Label(app, text="Interstellar Travel Form", font="arial 15 bold")
lblhead.grid(row=0, column=3)

# Define a function to display a message when the user submits the form
def getval():
    messagebox.showinfo("Status", "Data Stored")

# Create labels for each of the input fields on the form
lbl_name = Label(app, text="Name:")
lbl_age = Label(app, text="Age:")
lbl_occupation = Label(app, text="Occupation:")
lbl_phone_no = Label(app, text="Phone Number:")
lbl_payment_method = Label(app, text="Payment Method:")

# Set the labels on the grid
lbl_name.grid(row=1,column=2)
lbl_age.grid(row=2,column=2)
lbl_occupation.grid(row=3,column=2)
lbl_phone_no.grid(row=4,column=2)
lbl_payment_method.grid(row=5,column=2)

# Define StringVar and IntVar variables to store the user input for each field
namevalue = StringVar
agevalue = StringVar
occupationvalue = StringVar
phonenovalue = StringVar
paymentmethodvalue = StringVar
checkvalue = IntVar

# Create Entry widgets for each field and link them to the corresponding variables
name_entry = Entry(app, textvariable=namevalue)
age_entry = Entry(app, textvariable= agevalue)
occupation_entry = Entry(app, textvariable=occupationvalue)
phone_no_entry = Entry(app, textvariable=phonenovalue)
payment_method_entry = Entry(app, textvariable=paymentmethodvalue)

# Set the Entry widgets on the grid
name_entry.grid(row=1, column=3)
age_entry.grid(row=2,column=3)
occupation_entry.grid(row=3, column=3)
phone_no_entry.grid(row=4, column=3)
payment_method_entry.grid(row=5, column=3)

# Create a checkbox widget and link it to the checkvalue variable
rdb_check = Checkbutton(text="Remind Me", variable=checkvalue)
rdb_check.grid(row=6, column=3)

# Create a Submit button which calls the getval() function when clicked
Button(text="Submit", command=getval).grid(row=7, column=3)

# Start the main event loop to display the window and interact with the user
app.mainloop()
