from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class ShoppingCart:
    def __init__(self,root):
        self.root=root
        self.root.title("Shopping Cart")
        self.root.geometry("1175x400+40+130")

        self.O_Id=StringVar()
        self.O_Name=StringVar()
        self.O_Price=StringVar()

        self.d=IntVar()
        self.p=IntVar()
        self.g=IntVar()
        self.str=StringVar()
        self.Total=IntVar()
        self.Gstcal=IntVar()
        self.tcal=IntVar()
        self.showGst=IntVar()

        title=Label(self.root,text="YOUR SHOPPING CART",font=("Supra Mezzo Mediu",20,"bold"),bg="#00B1AB",fg="white")
        title.pack(side=TOP,fill=X)

        order_list_farme=Frame(self.root,bd=4,relief=RIDGE)
        order_list_farme.place(x=20,y=50,width=610,height=250)

        charge_farme=Frame(self.root,bd=4,relief=RIDGE)
        charge_farme.place(x=20,y=310,width=770,height=80)

        order_btn_farme=Frame(self.root,bd=4,relief=RIDGE)
        order_btn_farme.place(x=636,y=50,width=157,height=250)

        total_amt_frame=Frame(self.root,bd=4,relief=RIDGE)
        total_amt_frame.place(x=800,y=50,width=350,height=339)



        scrollx=Scrollbar(order_list_farme,orient=HORIZONTAL)
        scrolly=Scrollbar(order_list_farme,orient=VERTICAL)
        self.Order_table=ttk.Treeview(order_list_farme,columns=("Order_Id","Order_Name","Order_Price"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Order_table.xview)
        scrolly.config(command=self.Order_table.yview)
        self.Order_table.heading("Order_Id",text="ORDER ID")
        self.Order_table.heading("Order_Name",text="ORDER NAME")
        self.Order_table.heading("Order_Price",text="ORDER PRICE")
        self.Order_table['show']='headings'
        self.Order_table.pack(fill=BOTH,expand=1)
        self.fetch_cart_data()


        continue_shopping_btn=Button(order_btn_farme,text="Continue Shopping",command=self.continue_shopping_fn,height=2,width=15,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        continue_shopping_btn.grid(row=0,column=0,padx=10,pady=15)

        remove_item_btn=Button(order_btn_farme,command=self.remove_item,text="Remove Item",height=2,width=15,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        remove_item_btn.grid(row=1,column=0,padx=10,pady=15)

        place_order_btn=Button(order_btn_farme,command=self.place_order,text="Place Order",height=2,width=15,font=("Supra Mezzo Mediu",10,"bold"),bg="#00B1AB",fg="white")
        place_order_btn.grid(row=2,column=0,padx=10,pady=15)

        self.fetch_charges()

        delivary_label=Label(charge_farme,text="Delivary Charges(₹) :",font=("Supra Mezzo Mediu",10,"bold"))
        delivary_label.grid(row=0,column=0,padx=20,pady=25)
        delivary_field_label=Label(charge_farme,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        delivary_field_label.grid(row=0,column=1)

        gst_label=Label(charge_farme,text="GST(%) :",font=("Supra Mezzo Mediu",10,"bold"))
        gst_label.grid(row=0,column=2,padx=20,pady=10)
        gst_field_label=Label(charge_farme,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        gst_field_label.grid(row=0,column=3)

        packing_label=Label(charge_farme,text="Packing Charges(₹) :",font=("Supra Mezzo Mediu",10,"bold"))
        packing_label.grid(row=0,column=4,padx=20,pady=10)
        packing_field_label=Label(charge_farme,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        packing_field_label.grid(row=0,column=5) 

        delivary_field_label['text']=self.d
        gst_field_label['text']=self.g
        packing_field_label['text']=self.p
        self.total_mrp()
        self.Extra_Charge_cal()
        self.Show_GST_value()

        total_mrp_label=Label(total_amt_frame,text="Total MRP(₹) ",font=("Supra Mezzo Mediu",13,"bold"))
        total_mrp_label.grid(row=0,column=0,padx=20,pady=15)
        total_mrp_field_label=Label(total_amt_frame,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        total_mrp_field_label.grid(row=0,column=1,padx=15)

        delivary_amt_label=Label(total_amt_frame,text="Delivary Charge(₹) ",font=("Supra Mezzo Mediu",13,"bold"))
        delivary_amt_label.grid(row=1,column=0,padx=20,pady=20)
        delivary_amt_field_label=Label(total_amt_frame,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        delivary_amt_field_label.grid(row=1,column=1,padx=20)

        packing_amt_label=Label(total_amt_frame,text="Packing Charge(₹) ",font=("Supra Mezzo Mediu",13,"bold"))
        packing_amt_label.grid(row=2,column=0,padx=20,pady=20)
        packing_amt_field_label=Label(total_amt_frame,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        packing_amt_field_label.grid(row=2,column=1,padx=20)

        gst_label=Label(total_amt_frame,text="GST(₹) ",font=("Supra Mezzo Mediu",13,"bold"))
        gst_label.grid(row=3,column=0,padx=20,pady=20)
        gst_amt_field_label=Label(total_amt_frame,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        gst_amt_field_label.grid(row=3,column=1,padx=20)

        dash_line_label=Label(total_amt_frame,text="---------------------------------------------------------",font=("Supra Mezzo Mediu",12))
        dash_line_label.place(x=25,y=240)

        total_amount_label=Label(total_amt_frame,text="Total Amount(₹) ",font=("Supra Mezzo Mediu",13,"bold"))
        total_amount_label.grid(row=5,column=0,padx=20,pady=30)
        total_amount_field_label=Label(total_amt_frame,text="",font=("Supra Mezzo Mediu",10,"bold"),width=10,bg="white")
        total_amount_field_label.grid(row=5,column=1,padx=20)

        
        total_mrp_field_label['text']=self.Total
        delivary_amt_field_label['text']=self.d
        packing_amt_field_label['text']=self.p
        gst_amt_field_label['text']=self.showGst
        total_amount_field_label['text']=self.tcal
    
        self.Order_table.bind("<ButtonRelease-1>",self.select_cursor)


    def fetch_cart_data(self):  
            try: 
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("select * from Order_table")
                rows=cur.fetchall()
                if rows!=None:
                    self.Order_table.delete(*self.Order_table.get_children())
                    for row in rows:
                        self.Order_table.insert('',END,values=row)

                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"{str(es)}",parent=self.root)    

    def continue_shopping(self):
        self.root.destroy()

    def select_cursor(self,event):
        se_row=self.Order_table.focus()
        content=self.Order_table.item(se_row)
        row=content['values']
        self.O_Id.set(row[0])
        self.O_Name.set(row[1])
        self.O_Price.set(row[2])     

    def remove_item(self):
        if self.O_Id.get()=="":
            messagebox.showerror("Error","No Item Is Selected",parent=self.root)
        else:    
            try:     
                conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
                cur=conn.cursor()
                cur.execute("delete from Order_table where O_Id=%s",(self.O_Id.get()))
                conn.commit()
                self.fetch_cart_data()
                conn.close()
                messagebox.showinfo("Success","Entery Is Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"{str(es)}",parent=self.root)

    def place_order(self):
        try:     
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select * from Order_table")
            rows=cur.fetchone()
            if rows==None:
                messagebox.showwarning("Empty","Your cart is Empty",parent=self.root)
            else:
                cur.execute("delete from Order_table")
                messagebox.showinfo("Success","Order Has Been Placed")

            conn.commit()  
            self.fetch_cart_data()  
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"{str(es)}",parent=self.root)



    def fetch_charges(self):
        li=list()
        try: 
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select * from Charges_table where C_Id=1")
            rows=cur.fetchone() 
            for i in rows:
                li.append(i)   
            self.d=li[1]
            self.p=li[2]
            self.g=li[3]
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"{str(es)}",parent=self.root)   

    def total_mrp(self):
        li=(100)
        try: 
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select sum(O_Price) from Order_table")
            rows=cur.fetchall()
            self.Total=rows[0]
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"{str(es)}",parent=self.root)

    def Extra_Charge_cal(self):
        try: 
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select C_Delivary+C_Packing+(sum(O_Price)+(sum(O_Price)*C_Gst*0.01)) from charges_table,Order_table")
            rows=cur.fetchall()
            self.tcal=rows[0]
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"{str(es)}",parent=self.root)


    def Show_GST_value(self):
        try: 
            conn=pymysql.connect(host="localhost",user="root",password="",database="online organic health food store")
            cur=conn.cursor()
            cur.execute("select (sum(O_Price)*C_Gst*0.01) from charges_table,Order_table")
            rows=cur.fetchall()
            self.showGst=rows[0]
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"{str(es)}",parent=self.root)  


    def continue_shopping_fn(self):
        self.root.destroy()
        import order_panel        





root=Tk()
ob=ShoppingCart(root)
root.mainloop()