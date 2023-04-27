# import the necessary modules from tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# set the background color for the GUI
bg_color = "#326273"

# create a new Tkinter window object
root = Tk()

# set the size, position, and title of the window
root.geometry("700x400+300+200")
root.title("Interstella Registry Form")
root.resizable(False, False)

# set the background color of the window
root.configure(bg=bg_color)

# define a function to clear all the input fields
def clear():
    nameValue.set("")
    contactValue.set('')
    ageValue.set("")
    addressEntry.delete(1.0, END)

# create a label for the heading
Label(root, text="Please fill the form Below", font="arial 13", bg=bg_color).place(x=20, y=20)

# create labels for each input field
Label(root, text="Name", font="23", bg=bg_color, fg="#fff").place(x=50, y=100)
Label(root, text="Contact No", font="23", bg=bg_color, fg="#fff").place(x=50, y=150)
Label(root, text="Age", bg=bg_color, font="23", fg="#fff").place(x=50, y=200)
Label(root, text="Gender", bg=bg_color, font="23", fg="#fff").place(x=370, y=200)
Label(root, text="Address", bg=bg_color, fg="#fff", font="23").place(x=50, y=250)

# create input fields for each input field
nameValue  = StringVar()
contactValue = StringVar()
ageValue = IntVar()

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
gender = Combobox(root, values=["Male", "Female", "Prefer not to say"], font="arial 14",  state="r", width=14)
gender.place(x=435, y= 200)
gender.set("Male")

# create a Text widget for the address input field
addressEntry = Text(root, width=50, height=4, bd=4)
addressEntry.place(x=200, y=250)

# create buttons to submit the form, clear the fields, and exit the program
btn_submit = Button(root, text="Submit", bg=bg_color,fg="white",width=15, height=2)
btn_clear = Button(root, text="Clear", bg=bg_color,fg="white",width=15, height=2, command=clear)
btn_exit = Button(root, text="Exit", bg=bg_color,fg="white",width=15, height=2, command= lambda: root.destroy())

# position the buttons on the form
btn_submit.place(x=200, y=345)
btn_clear.place(x=340, y=345)
btn_exit.place(x=480, y=345)


# Run app
root.mainloop()
