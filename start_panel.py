from tkinter import *
from PIL import ImageTk
root=Tk()

#MAIN PAGE
root.geometry("600x600+330+30")
root.resizable(False,False)
root.title("Welcome")

def devloper_fun():
    root.destroy()
    import developers_panel

def admin_fun():
    root.destroy()
    import admin_Login_page

def user_fun():
    root.destroy()
    import User_Login_page



#BACKGROUND
my_image1=ImageTk.PhotoImage(file="images/background.jpg")
my_label=Label(image=my_image1)
my_label.place(x=0, y=0)

#MAIN PAGE BUTTON
Login_btn=Button(root,text="LOGIN",command=user_fun,fg="white",bd=0,bg="#f5a25d",font=("Supra Mezzo Medium",25,"bold"),cursor="hand2").place(x=170,y=200,width=240,height=60)
Admin_btn=Button(root, text="ADMIN",command=admin_fun,fg="white",bd=0,bg="#008891",font=("Supra Mezzo Medium",25,"bold"),cursor="hand2").place(x=170,y=290,width=240,height=60)
Developer_btn=Button(root, text="DEVELOPERS",command=devloper_fun,fg="white",bd=0,bg="#625261",font=("Supra Mezzo Medium",25,"bold"),cursor="hand2").place(x=170,y=380,width=240,height=60)

#HEADING
title_label=Label(root, relief="solid", text="WELCOME",font=("Supra Mezzo Medium",35,"bold"),pady=10, padx=10)
title_label.place(x=150, y=50)

root.mainloop()