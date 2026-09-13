from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb  #pip install stegano


root = Tk()
root.title("SRM - Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")


def Showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title = 'Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG file","*.jpg"),("All file","*.txt")))
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

    
    
def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)


    
def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

    
def Save():
    secret.save("hidden.png")

    


#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

# Logo
logo_img = Image.open("logo.png")

# Resize logo
logo_img = logo_img.resize((80, 80), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(logo_img)
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)


Label(root,text = "CYBER SCIENCE", bg = "#2d4155", fg = "white",font="arial 25 bold").place(x=100,y=20)

#first Frame
f = Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl = Label(f,bg="black")
lbl.place(x=40,y=10)

# Second Frame
frame2 = Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350, y=80)

# Text Area
text1 = Text(frame2,font=("Roboto", 20),bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0, y=0, width=315, height=274)

# Scrollbar
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=315, y=0, width=20, height=274)

# Connect scrollbar and text area
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third Frame
frame3 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)


Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=Showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=Save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)



#fourth Frame
frame4 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)


Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)












root.mainloop()
