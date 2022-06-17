from tkinter import *
from PIL import ImageTk
root=Tk()
root.geometry("1000x600+150+10")
root.title("Developers")
root.resizable(False,False)

#BACKGROUND IMAGE
background_img=ImageTk.PhotoImage(file="images/back.jpg")
background_label=Label(root, image=background_img).place(x=0, y=0)

#HEADING
head_label=Label(root, font=("helvetica" ,30 ,"bold"),text="DEVELOPERS", fg="#ffa62b")
head_label.place(x=400, y=20)

#FIRST FRAME
first_frame=Frame(root, bd=2, bg="white", height=150, width=700)
first_frame.place(x=100, y=90);
#IMAGE OF 1ST FRAME
first_image=ImageTk.PhotoImage(file="images/1st.jpg")
first_label=Label(first_frame, image=first_image).place(x=0, y=0)
#DETAIL FRAME
detail_frame1=Frame(first_frame, height=125, width=480, bg="#f4f4f2")
detail_frame1.place(x=210, y=10)
Name_label1=Label(detail_frame1,text="Name- \n\n Roll- \n\n Section- \n\n Contibution-", font=("helvetica",10,"bold")).place(x=10, y=10)
Value_label=Label(detail_frame1,text="Priyanshu Suman \n\n 08 \n\n K19FR \n\n FrontEnd, BackEnd, File", font=("helvetica",10, "italic")).place(x=115, y=10)


#SECOND FRAME
second_frame=Frame(root, bd=2, bg="white", height=150, width=700)
second_frame.place(x=200, y=250);
#IMAGE OF 2ND FRAME
second_image=ImageTk.PhotoImage(file="images/2nd.jpg")
second_label=Label(second_frame, image=second_image).place(x=500, y=0)
#DETAIL FRAME
detail_frame2=Frame(second_frame, height=125, width=480, bg="#f4f4f2")
detail_frame2.place(x=10, y=10)
Name_label2=Label(detail_frame2,text="Name- \n\n Roll- \n\n Section- \n\n Contibution-", font=("helvetica",10,"bold")).place(x=10, y=10)
Value_label=Label(detail_frame2,text="Ayush Raj \n\n 09 \n\n K19FR \n\n FrontEnd, BackEnd, File", font=("helvetica",10, "italic")).place(x=115, y=10)

#THIRD FRAME
third_frame=Frame(root, bd=2, bg="white", height=150, width=700)
third_frame.place(x=100, y=410)
#IMAGE OF 3RD FRAME
third_image=ImageTk.PhotoImage(file="images/3rd.jpg")
third_label=Label(third_frame, image=third_image).place(x=0, y=0)
#DETAIL FRAME
detail_frame3=Frame(third_frame, height=125, width=480, bg="#f4f4f2")
detail_frame3.place(x=210, y=10)
Name_label=Label(detail_frame3,text="Name- \n\n Roll- \n\n Section- \n\n Contibution-", font=("helvetica",10,"bold")).place(x=10, y=10)
Value_label=Label(detail_frame3,text="Sajjad Hussain \n\n 07 \n\n K19FR \n\n FrontEnd, BackEnd, File", font=("helvetica",10, "italic")).place(x=115, y=10)

root.mainloop()