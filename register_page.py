from tkinter import *
from typing import Pattern
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("720x630+250+10")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(Image.open("images/reg.png"))
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        lbl_registration=Label(self.root,text="USER REGISTRATION",font=("Supra Mezzo Medium",25,"bold"),fg="#00B1AB",bg="#E9ECED").place(x=100,y=20,width=500,height=100)
        
        self.txt_email=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_email.place(x=287,y=125,width=250,height=29)

        self.txt_pass1=Entry(self.root,font=("Supra Mezzo Medium",12,),bg="white")
        self.txt_pass1.place(x=287,y=160,width=250,height=29)

        self.txt_pass2=Entry(self.root,font=("Supra Mezzo Medium",12,),bg="white")
        self.txt_pass2.place(x=287,y=195,width=250,height=29)

        self.txt_fname=Entry(self.root,font=("Supra Mezzo Medium",12,),bg="white")
        self.txt_fname.place(x=287,y=230,width=250,height=29)

        self.txt_lname=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_lname.place(x=287,y=265,width=250,height=29)

        self.txt_num=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_num.place(x=287,y=300,width=250,height=29)

        self.txt_address1=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_address1.place(x=287,y=335,width=250,height=29)
        
        self.txt_address2=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_address2.place(x=287,y=370,width=250,height=29)
        
        self.txt_town=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_town.place(x=287,y=405,width=250,height=29)

        self.txt_region=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_region.place(x=287,y=440,width=250,height=29)

        self.txt_zip=Entry(self.root,font=("Supra Mezzo Medium",12),bg="white")
        self.txt_zip.place(x=287,y=475,width=250,height=29)

        register_btn=Button(self.root,command=self.Register_function,text="REGISTER",fg="#E9ECED",bd=2,bg="#00B1AB",font=("Supra Mezzo Medium",20,"bold")).place(x=209,y=510,width=400,height=50)
        back_btn=Button(self.root,text="Back To Login",command=self.Login_page,bg="#E9ECED",bd=0,fg="#01827A",font=("Supra Mezzo Medium",12,"bold")).place(x=200,y=560,width=400,height=80)

    def Clear_fields(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_address1.delete(0,END)
        self.txt_address2.delete(0,END)
        self.txt_pass1.delete(0,END)
        self.txt_pass2.delete(0,END)
        self.txt_num.delete(0,END)
        self.txt_region.delete(0,END)
        self.txt_zip.delete(0,END)
        self.txt_town.delete(0,END)


    def Login_page(self):
        self.root.destroy()
        import User_Login_page


    def Register_function(self):  
        if self.txt_email.get()=="" or self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_pass1.get()=="" or self.txt_pass2.get()=="" or self.txt_address1.get()=="" or self.txt_address2.get()=="" or self.txt_num.get()=="" or self.txt_region.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass1.get()!=self.txt_pass2.get():
            messagebox.showerror("Error","Password do not match!",parent=self.root)
        else: 
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("select * from register_table where Email_id=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists,Please try with different Email")
                else:    
                    cur.execute("insert into register_table (F_name,L_name,Email_id,Password,Number,Address1,Address2,Town,Region,Zipcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_email.get(),
                                    self.txt_pass1.get(),
                                    self.txt_num.get(),
                                    self.txt_address1.get(),
                                    self.txt_address2.get(),
                                    self.txt_town.get(),
                                    self.txt_region.get(),
                                    self.txt_zip.get()
                                ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","REGISTRATION  SUCCESSFULL",parent=self.root) 
                    self.Clear_fields()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)






root=Tk()
obj=register(root)
root.mainloop()



