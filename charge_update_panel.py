from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class update_charge:
    def __init__(self,root):
        self.root=root
        self.root.title("Update Charge")
        self.root.geometry("600x500+350+90")

        self.delivary=IntVar()
        self.packing=IntVar()
        self.gst=IntVar()

        self.show_rates()

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=20,y=10,width=560,height=350)

        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=20,y=370,width=560,height=115)

        delivary_title=Label(main_frame,text="Delivary Charge",font=("Supra Mezzo Mediu",15,"bold"),bg="#E9ECED")
        delivary_title.grid(row=0,column=0,padx=40,pady=40)
        delivary_entry=Entry(main_frame,textvariable=self.delivary,font=("Supra Mezzo Mediu",15))
        delivary_entry.grid(row=0,column=1,pady=10,padx=20)

        packing_title=Label(main_frame,text="Packing Charge",font=("Supra Mezzo Mediu",15,"bold"),bg="#E9ECED")
        packing_title.grid(row=1,column=0,padx=10,pady=40)
        packing_entry=Entry(main_frame,textvariable=self.packing,font=("Supra Mezzo Mediu",15))
        packing_entry.grid(row=1,column=1,pady=10,padx=20)

        gst_title=Label(main_frame,text="GST Rate",font=("Supra Mezzo Mediu",15,"bold"),bg="#E9ECED")
        gst_title.grid(row=2,column=0,padx=10,pady=40)
        gst_entry=Entry(main_frame,textvariable=self.gst,font=("Supra Mezzo Mediu",15))
        gst_entry.grid(row=2,column=1,pady=10,padx=20)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_btn_fn,width=19,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        update_btn.grid(row=0,column=0,padx=10,pady=29)

        clear_btn=Button(btn_frame,text="CLEAR",command=self.clear_field,width=19,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        clear_btn.grid(row=0,column=1,padx=10,pady=29)

        back_btn=Button(btn_frame,text="EXIT",command=self.exit_fun,width=19,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        back_btn.grid(row=0,column=2,padx=10,pady=29)

        


    def update_btn_fn(self):
        if self.delivary.get()=="" or self.packing.get()=="" or self.gst.get()=="":
            messagebox.showerror("Error","All fields are required For Update",parent=self.root)
        else:   
            try:  
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("update Charges_table set C_Delivary=%s,C_Packing=%s,C_Gst=%s where C_Id=1",(self.delivary.get(),self.packing.get(),self.gst.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)    

    def show_rates(self):
        try:     
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select * from Charges_table")
            rows=cur.fetchone()
            self.delivary.set(rows[1])
            self.packing.set(rows[2])
            self.gst.set(rows[3])
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 

    def clear_field(self):   
        self.delivary.set("")
        self.packing.set("")
        self.gst.set("")        

    def exit_fun(self):
        self.root.destroy()
        import admin_panel




root=Tk()
obj=update_charge(root)
root.mainloop()        