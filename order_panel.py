from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
root=Tk()
root.geometry("1000x600+150+20")
root.resizable(False, False)

#FOR ADDING INTO CART
def Add(ame, price):
    conn= pymysql.connect(host="localhost", user="root", password="", database="online organic health food store")
    c=conn.cursor()
    c.execute("INSERT INTO Order_table(O_Name, O_Price) VALUES(%s,%s)",(ame, price))
    conn.commit()
    conn.close()
    messagebox.showinfo("showinfo", "Order added") 

#FOR DATA RECIVAL SQL COMMAND
conn= pymysql.connect(host="localhost", user="root", password="", database="online organic health food store")
c=conn.cursor()
c.execute("SELECT * FROM Food_table")
x=c.fetchall()
c.close()
conn.close()


#MAIN FRAME
main_frame=Frame(root, height=600, width=1000, bg="#fae0df")
main_frame.place(x=0, y=0)

#ROW1

#MID FRAME
mid_frame1=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame1.place(x=60, y=70)
#SUB FRAME
sub_frame1=Frame(mid_frame1, height=200, width=150, bg="white", relief=RAISED)
sub_frame1.place(x=5, y=5)
#PRODUCT IMAGE
img1=ImageTk.PhotoImage(file="images/pasta.jpg")
first_Lab1=Label(sub_frame1, image=img1, bd=1)
first_Lab1.place(x=0, y=0)
#DETAIL FRAME
sec_frame1=Frame(sub_frame1, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame1.place(x=0, y=92)
detail_label1=Label(sec_frame1, text=x[0][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label1.place(x=20, y=10);
detail_label1=Label(sec_frame1, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label1.place(x=30, y=40);
price_label1=Label(sec_frame1, text=x[0][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label1.place(x=90, y=40)
cart_button1= Button(sec_frame1, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2", command=lambda:Add(x[0][1],x[0][2]))
cart_button1.place(x=55, y=72)

#MID FRAME
mid_frame2=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame2.place(x=300, y=70)
#SUB FRAME
sub_frame2=Frame(mid_frame2, height=200, width=150, bg="white", relief=RAISED)
sub_frame2.place(x=5, y=5)
#PRODUCT IMAGE
img2=ImageTk.PhotoImage(file="images/biryani.jpg")
first_Lab2=Label(sub_frame2, image=img2, bd=1)
first_Lab2.place(x=0, y=0)
#DETAIL FRAME
sec_frame2=Frame(sub_frame2, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame2.place(x=0, y=92)
detail_label2=Label(sec_frame2, text=x[1][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label2.place(x=20, y=10)
detail_label2=Label(sec_frame2, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label2.place(x=30, y=40);
price_label2=Label(sec_frame2, text=x[1][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label2.place(x=90, y=40)
cart_button2= Button(sec_frame2, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2",command=lambda:Add(x[1][1],x[1][2]))
cart_button2.place(x=55, y=72)

#MID FRAME
mid_frame3=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame3.place(x=540, y=70)
#SUB FRAME
sub_frame3=Frame(mid_frame3, height=200, width=150, bg="white", relief=RAISED)
sub_frame3.place(x=5, y=5)
#PRODUCT IMAGE
img3=ImageTk.PhotoImage(file="images/french.jpg")
first_Lab3=Label(sub_frame3, image=img3, bd=1)
first_Lab3.place(x=0, y=0)
#DETAIL FRAME
sec_frame3=Frame(sub_frame3, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame3.place(x=0, y=92)
detail_label3=Label(sec_frame3, text=x[2][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label3.place(x=20, y=10);
detail_label3=Label(sec_frame3, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label3.place(x=30, y=40);
price_label3=Label(sec_frame3, text=x[2][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label3.place(x=90, y=40)
cart_button3= Button(sec_frame3, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2", command=lambda:Add(x[2][1],x[2][2]))
cart_button3.place(x=55, y=72)

#MID FRAME
mid_frame4=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame4.place(x=780, y=70)
#SUB FRAME
sub_frame4=Frame(mid_frame4, height=200, width=150, bg="white", relief=RAISED)
sub_frame4.place(x=5, y=5)
#PRODUCT IMAGE
img4=ImageTk.PhotoImage(file="images/friedRice.jpg")
first_Lab4=Label(sub_frame4, image=img4, bd=1)
first_Lab4.place(x=0, y=0)
#DETAIL FRAME
sec_frame4=Frame(sub_frame4, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame4.place(x=0, y=92)
detail_label4=Label(sec_frame4, text=x[3][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label4.place(x=20, y=10);
detail_label4=Label(sec_frame4, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label4.place(x=30, y=40);
price_label4=Label(sec_frame4, text=x[3][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label4.place(x=90, y=40)
cart_button4= Button(sec_frame4, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2", command=lambda:Add(x[3][1],x[3][2]))
cart_button4.place(x=55, y=72)


#ROW 2

#MID FRAME
mid_frame5=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame5.place(x=60, y=300)
#SUB FRAME
sub_frame5=Frame(mid_frame5, height=200, width=150, bg="white", relief=RAISED)
sub_frame5.place(x=5, y=5)
#PRODUCT IMAGE
img5=ImageTk.PhotoImage(file="images/pizza.jpg")
first_Lab5=Label(sub_frame5, image=img5, bd=1)
first_Lab5.place(x=0, y=0)
#DETAIL FRAME
sec_frame5=Frame(sub_frame5, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame5.place(x=0, y=92)
detail_label5=Label(sec_frame5, text=x[4][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label5.place(x=20, y=10);
detail_label5=Label(sec_frame5, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label5.place(x=30, y=40);
price_label5=Label(sec_frame5, text=x[4][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label5.place(x=90, y=40)
cart_button5= Button(sec_frame5, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2", command=lambda:Add(x[4][1],x[4][2]))
cart_button5.place(x=55, y=72)

#MID FRAME
mid_frame6=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame6.place(x=300, y=300)
#SUB FRAME
sub_frame6=Frame(mid_frame6, height=200, width=150, bg="white", relief=RAISED)
sub_frame6.place(x=5, y=5)
#PRODUCT IMAGE
img6=ImageTk.PhotoImage(file="images/pie.jpg")
first_Lab6=Label(sub_frame6, image=img6, bd=1)
first_Lab6.place(x=0, y=0)
#DETAIL FRAME
sec_frame6=Frame(sub_frame6, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame6.place(x=0, y=92)
detail_label6=Label(sec_frame6, text=x[5][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label6.place(x=20, y=10)
detail_label6=Label(sec_frame6, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label6.place(x=30, y=40);
price_label6=Label(sec_frame6, text=x[5][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label6.place(x=90, y=40)
cart_button6= Button(sec_frame6, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2",command=lambda:Add(x[5][1],x[5][2]))
cart_button6.place(x=55, y=72)

#MID FRAME
mid_frame7=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame7.place(x=540, y=300)
#SUB FRAME
sub_frame7=Frame(mid_frame7, height=200, width=150, bg="white", relief=RAISED)
sub_frame7.place(x=5, y=5)
#PRODUCT IMAGE
img7=ImageTk.PhotoImage(file="images/tacko.jpg")
first_Lab7=Label(sub_frame7, image=img7, bd=1)
first_Lab7.place(x=0, y=0)
#DETAIL FRAME
sec_frame7=Frame(sub_frame7, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame7.place(x=0, y=92)
detail_label7=Label(sec_frame7, text=x[6][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label7.place(x=20, y=10);
detail_label7=Label(sec_frame7, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label7.place(x=30, y=40);
price_label7=Label(sec_frame7, text=x[6][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label7.place(x=90, y=40)
cart_button7= Button(sec_frame7, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2",command=lambda:Add(x[6][1],x[6][2]))
cart_button7.place(x=55, y=72)

#MID FRAME
mid_frame8=Frame(main_frame, height=210, width=160, bg="grey", relief=RAISED)
mid_frame8.place(x=780, y=300)
#SUB FRAME
sub_frame8=Frame(mid_frame8, height=200, width=150, bg="white", relief=RAISED)
sub_frame8.place(x=5, y=5)
#PRODUCT IMAGE
img8=ImageTk.PhotoImage(file="images/salsa.jpg")
first_Lab8=Label(sub_frame8, image=img8, bd=1)
first_Lab8.place(x=0, y=0)
#DETAIL FRAME
sec_frame8=Frame(sub_frame8, height=110, width=150, bg="#9ad3bc", relief=RAISED)
sec_frame8.place(x=0, y=92)
detail_label8=Label(sec_frame8, text=x[7][1], bg="#9ad3bc", fg="#6a097d", font=("helvetica", 12, "bold"))
detail_label8.place(x=20, y=10);
detail_label8=Label(sec_frame8, text="Price ", bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
detail_label8.place(x=30, y=40);
price_label8=Label(sec_frame8, text=x[7][2] , bg="#9ad3bc", fg="#a05344", font=("helvetica", 15, "bold"))
price_label8.place(x=90, y=40)
cart_button8= Button(sec_frame8, text="Add", font=("helvetica", 12, "bold"),bg="#edc988", cursor="hand2",command=lambda:Add(x[7][1],x[7][2]))
cart_button8.place(x=55, y=72)

def cart_fun():
    root.destroy()
    import shopping_cart

#CART BUTTON
main_button=Button(main_frame, text="CART",command=cart_fun,font=("helvetica", 20, "bold"), fg="red", bg="#7e7474")
main_button.place(x=450, y=540)


root.mainloop()
