from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Admin:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Panel")
        self.root.geometry("1200x600+30+20")

        title=Label(self.root,text="Admin Control Panel",font=("Supra Mezzo Mediu",40,"bold"),bg="#00B1AB",fg="white")
        title.pack(side=TOP,fill=X)

        self.id_var=StringVar()
        self.name_var=StringVar()
        self.price_var=StringVar()
        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()
    
        manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=70,width=500,height=300)

        detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        detail_frame.place(x=530,y=70,width=650,height=520)

        m_title=Label(manage_frame,text="Manage Items",font=("Supra Mezzo Mediu",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        food_id_label=Label(manage_frame,text="Food ID",bg="#E9ECED",font=("Supra Mezzo Mediu",15,"bold"))
        food_id_label.grid(row=1,column=0,padx=20,sticky="w")

        txt_id=Entry(manage_frame,textvariable=self.id_var,font=("Supra Mezzo Mediu",15))
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        food_name_label=Label(manage_frame,text="Food NAME",bg="#E9ECED",font=("Supra Mezzo Mediu",15,"bold"))
        food_name_label.grid(row=2,column=0,padx=20,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("Supra Mezzo Mediu",15))
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        food_price_label=Label(manage_frame,text="Food PRICE",bg="#E9ECED",font=("Supra Mezzo Mediu",15,"bold"))
        food_price_label.grid(row=3,column=0,padx=20,sticky="w")

        txt_price=Entry(manage_frame,textvariable=self.price_var,font=("Supra Mezzo Mediu",15))
        txt_price.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        change_charge_btn=Button(manage_frame,text="Change Charges",command=self.change_charge_fn,width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        change_charge_btn.grid(row=4,column=0,pady=10,padx=38)

        go_back_to_main_page_btn=Button(manage_frame,text="Main Page",command=self.go_back_to_main_page_btn_fn,width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        go_back_to_main_page_btn.grid(row=4,column=1,pady=10,padx=30)

        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=20,y=400,width=500,height=150)

        add_btn=Button(btn_frame,text="ADD",command=self.add_foods,width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        add_btn.grid(row=0,column=0,padx=35,pady=15)

        update_btn=Button(btn_frame,command=self.update_foods,text="UPDATE",width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        update_btn.grid(row=0,column=1,padx=50,pady=15)

        delete_btn=Button(btn_frame,command=self.delete_foods,text="DELETE",width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        delete_btn.grid(row=1,column=0,padx=35,pady=15)

        clear_btn=Button(btn_frame,text="CLEAR",command=self.clear_field,width=20,height=2,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        clear_btn.grid(row=1,column=1,padx=50,pady=15)

        search_lbl=Label(detail_frame,text="Search By",bg="#E9ECED",font=("Supra Mezzo Mediu",12,"bold"))
        search_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by_var,width=12,font=("Supra Mezzo Mediu",12),state='readonly')
        combo_search['values']=("f_ID" ,"f_NAME" ,"f_PRICE")
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_search=Entry(detail_frame,textvariable=self.search_txt_var,font=("Supra Mezzo Mediu",10),border=2)
        txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="w")

        search_btn=Button(detail_frame,command=self.fetch_search_data,text="SEARCH",width=10,height=1,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        search_btn.grid(row=0,column=3,padx=10,pady=10)

        showall_btn=Button(detail_frame,command=self.fetch_data,text="SHOW ALL",width=10,height=1,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        showall_btn.grid(row=0,column=4,padx=10,pady=10)

        table_frame=Frame(detail_frame,bd=4,relief=RIDGE)
        table_frame.place(x=10,y=70,width=620,height=430)

        scrollx=Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        self.food_table=ttk.Treeview(table_frame,columns=("Food_Id","Food_Name","Food_Price"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.food_table.xview)
        scrolly.config(command=self.food_table.yview)
        self.food_table.heading("Food_Id",text="FOOD ID")
        self.food_table.heading("Food_Name",text="FOOD NAME")
        self.food_table.heading("Food_Price",text="FOOD PRICE")
        self.food_table['show']='headings'
        self.food_table.pack(fill=BOTH,expand=1)
        self.food_table.bind("<ButtonRelease-1>",self.select_cursor)
        self.fetch_data()

    def add_foods(self):
        if self.id_var.get()=="" or self.name_var.get()=="" or self.price_var.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:   
            try:     
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("insert into food_table values(%s,%s,%s)",(self.id_var.get(),self.name_var.get(),self.price_var.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_field()
                messagebox.showinfo("Success","Entery Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 

    def fetch_data(self):  
            try: 
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("select * from food_table")
                rows=cur.fetchall()
                if rows!=None:
                    self.food_table.delete(*self.food_table.get_children())
                    for row in rows:
                        self.food_table.insert('',END,values=row)

                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)    

    def clear_field(self):
        if self.id_var.get()=="" or self.name_var.get()=="" or self.price_var.get()=="":
            messagebox.showerror("Error","Fields Are Already Clear",parent=self.root)
        else:   
            self.id_var.set("")
            self.name_var.set("")
            self.price_var.set("")    

    def select_cursor(self,event):
        se_row=self.food_table.focus()
        content=self.food_table.item(se_row)
        row=content['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.price_var.set(row[2]) 

    def update_foods(self):  
        if self.id_var.get()=="" or self.name_var.get()=="" or self.price_var.get()=="":
            messagebox.showerror("Error","All fields are required For Update",parent=self.root)
        else:   
            try:     
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("update food_table set f_NAME=%s,f_PRICE=%s where f_ID=%s",(self.name_var.get(),self.price_var.get(),self.id_var.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_field()
                messagebox.showinfo("Success","Entery Updated Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 

    def delete_foods(self):
        if self.id_var.get()=="" or self.name_var.get()=="" or self.price_var.get()=="":
            messagebox.showerror("Error","Please Select An Entry To Delete",parent=self.root)
        else:   
            try:     
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("delete from food_table where f_ID=%s",(self.id_var.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_field()
                messagebox.showinfo("Success","Entery Is Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def fetch_search_data(self):  
        if self.search_txt_var.get()=="":
            messagebox.showerror("Error","Search Area Is Empty",parent=self.root)
        else:    
            try: 
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("select * from food_table where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
                rows=cur.fetchall()
                if rows!=None:
                    self.food_table.delete(*self.food_table.get_children())
                    for row in rows:
                        self.food_table.insert('',END,values=row)

                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)  

    def change_charge_fn(self):
        self.root.destroy()
        import charge_update_panel     

    def go_back_to_main_page_btn_fn(self):
        self.root.destroy()
        import start_panel

        




root=Tk()
ob=Admin(root)
root.mainloop()