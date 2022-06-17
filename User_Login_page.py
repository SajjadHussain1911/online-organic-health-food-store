from tkinter import *
from typing import Pattern
from PIL import ImageTk
from tkinter import messagebox
import pymysql


class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("720x630+250+10")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="images/pg_2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.user_id=StringVar()
        self.user_pass=StringVar()
        self.txt_user=Entry(self.root,textvariable=self.user_id,font=("Supra Mezzo Medium",15,"bold"),bg="white")
        self.txt_user.place(x=210,y=162,width=400,height=66)

        self.txt_pass=Entry(self.root,textvariable=self.user_pass,font=("Supra Mezzo Medium",15,"bold"),bg="white")
        self.txt_pass.place(x=210,y=271,width=400,height=66)

        Login_btn=Button(self.root,command=self.login_function,text="LOGIN",fg="#00B1AB",bd=0,bg="white",font=("Supra Mezzo Medium",20,"bold")).place(x=209,y=393.25,width=400,height=66)
        register_btn=Button(self.root,text="REGISTER  HERE",command=self.register_page,bg="#00B1AB",bd=1,fg="white",font=("Supra Mezzo Medium",15,"bold")).place(x=275,y=510)

    def register_page(self):
        self.root.destroy()
        import register_page

    def login_function(self):
        if self.user_pass.get()=="" or self.user_id.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("select * from register_table where Email_id=%s and Password=%s",(self.user_id.get(),self.user_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                else:
                    self.root.destroy()
                    import order_panel
                    messagebox.showinfo("success","Login Success",parent=self.root)
    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)





root=Tk()
obj=login(root)
root.mainloop()



