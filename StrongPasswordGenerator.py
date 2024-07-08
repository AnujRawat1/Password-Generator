from tkinter import *
from random import randint

root = Tk()
root.title('String Password Generator')
#root.iconbitmap()
root.geometry("500x350")

# To Generate a Strong Password
def new_rand():
    # Clear Our Entry Box 
    pw_entry.delete(0, END)
    
    # Clear the copy label
    copy_label.config(text="")
    
    # Get Password Length and convert to integer
    pw_length = int(my_entry.get())
    
    # Create Variable to hold Password
    my_password = ''
    
    # Loop Through Password Length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
        
    # Output Password to the Screen 
    pw_entry.insert(0, my_password)

# To Copy to Clipboard
def clipper():
    # Clear the Clipboard
    root.clipboard_clear()

    # Copy to Clipboard
    root.clipboard_append(pw_entry.get())
    
    # Update the Label to show the password is copied
    copy_label.config(text="Password copied to clipboard!", fg="green")

# Label Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# Create Entry Box to Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica", 20))
my_entry.pack(padx=20, pady=20)

# Create Entry Box for our returned Password
pw_entry = Entry(root, text='', font=("Helvetica", 20), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create Frame For Buttons 
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text='Generate Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

# Label to show copy to clipboard status
copy_label = Label(root, text="", font=("Helvetica", 12))
copy_label.pack(pady=10)

root.mainloop()
