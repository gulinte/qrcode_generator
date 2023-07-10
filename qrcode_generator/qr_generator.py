from tkinter import *
import qrcode

root=Tk()
root.title("QR Code Generator")
root.geometry("1000x500")
root.config(bg="#A8A4CE")
root.resizable(False,False)

#image
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")
    
    global Image
    Image=PhotoImage(file="Qrcode/"+ str(name)+".png")
    Image_view.config(image=Image)


Image_view=Label(root,bg="#A8A4CE")
Image_view.pack(padx=50,pady=10,side=RIGHT)

heading=Label(root,text="QR Code Generator", font="arial 36 bold", bg="#A8A4CE", fg="#495C83")
heading.place(x=250,y=30)

Label(root,text="Title", fg="#495C83", bg="#A8A4CE", font=30).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

Label(root,text="Link", fg="#495C83", bg="#A8A4CE", font=30).place(x=50,y=230)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=260)

Button(root,text="Generate",width=20,height=2,bg="#7A86B6",fg="white", font="arial 10 bold", command=generate).place(x=50,y=310)


root.mainloop()
