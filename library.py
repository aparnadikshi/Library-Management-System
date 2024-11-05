from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class libraryManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1480x700+0+0")

        #====================variable=====================================
        self.member_val=StringVar()
        self.prn_val=StringVar()
        self.id_val=StringVar()
        self.name=StringVar()
        self.adress=StringVar()
        self.mobile=StringVar()
        self.bookid=StringVar()
        self.bookname=StringVar()
        self.author=StringVar()
        self.dateborrowed=StringVar()
        self.submissiondate=StringVar()
        self.price=StringVar()

        lbtitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="peach puff",fg="maroon",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=4,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="peach puff") 
        frame.place(x=0,y=130,width=1270,height=300)

        #======================dataframeleft=======================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="peach puff",fg="maroon",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5,width=710,height=250)

        lbMember=Label(DataFrameLeft,bg="peach puff",text="Member Type",font=("bebas neu",12),padx=2,pady=6)
        lbMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_val,
                               state="readonly",font=("bebas neu",12),width=27)
        comMember["value"]=["Admin Staff","Student","Lecturer",]
        comMember.grid(row=0,column=1)

        lbPRN=Label(DataFrameLeft,bg="peach puff",text="PRN Number",font=("bebas neu",12),padx=2,pady=6)
        lbPRN.grid(row=1,column=0,sticky=W)
        txtPRN=Entry(DataFrameLeft,textvariable=self.prn_val,font=("bebas neu",12),width=29)
        txtPRN.grid(row=1,column=1)
        

        lbTitle=Label(DataFrameLeft,bg="peach puff",text="ID No.",font=("bebas neu",12),padx=2,pady=6)
        lbTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_val,font=("bebas neu",12),width=29)
        txtTitle.grid(row=2,column=1)

        lbFirstName=Label(DataFrameLeft,bg="peach puff",text="Name",font=("bebas neu",12),padx=2,pady=6)
        lbFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.name,font=("bebas neu",12),width=29)
        txtFirstName.grid(row=3,column=1)

        # lbLastName=Label(DataFrameLeft,bg="peach puff",text="Enter Last Name.",font=("bebas neu",12),padx=2,pady=6)
        # lbLastName.grid(row=4,column=0,sticky=W)
        # txtLastName=Entry(DataFrameLeft,font=("bebas neu",12),width=29)
        # txtLastName.grid(row=4,column=1)

        lbAdress=Label(DataFrameLeft,bg="peach puff",text=" Adress with pin",font=("bebas neu",12),padx=2,pady=6)
        lbAdress.grid(row=4,column=0,sticky=W)
        txtAdress=Entry(DataFrameLeft,textvariable=self.adress,font=("bebas neu",12),width=29)
        txtAdress.grid(row=4,column=1)

        lbMobile=Label(DataFrameLeft,bg="peach puff",text=" Mobile Number",font=("bebas neu",12),padx=2,pady=6)
        lbMobile.grid(row=5,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile,font=("bebas neu",12),width=29)
        txtMobile.grid(row=5,column=1)

        lbBookid=Label(DataFrameLeft,bg="peach puff",text="Book ID",font=("bebas neu",12),padx=2,pady=6)
        lbBookid.grid(row=0,column=2,sticky=W)
        txtbookid=Entry(DataFrameLeft,textvariable=self.bookid,font=("bebas neu",12),width=17)
        txtbookid.grid(row=0,column=3)

        lbBookName=Label(DataFrameLeft,bg="peach puff",text="Book Name",font=("bebas neu",12),padx=2,pady=6)
        lbBookName.grid(row=1,column=2,sticky=W)
        txtbookname=Entry(DataFrameLeft,textvariable=self.bookname,font=("bebas neu",12),width=17)
        txtbookname.grid(row=1,column=3)

        lbAuthor=Label(DataFrameLeft,bg="peach puff",text="Author",font=("bebas neu",12),padx=2,pady=6)
        lbAuthor.grid(row=2,column=2,sticky=W)
        txtauthor=Entry(DataFrameLeft,textvariable=self.author,font=("bebas neu",12),width=17)
        txtauthor.grid(row=2,column=3)

        lbdateborrow=Label(DataFrameLeft,bg="peach puff",text="Borrowed date",font=("bebas neu",12),padx=2,pady=6)
        lbdateborrow.grid(row=3,column=2,sticky=W)
        txtdateborrow=Entry(DataFrameLeft,textvariable=self.dateborrowed,font=("bebas neu",12),width=17)
        txtdateborrow.grid(row=3,column=3)

        lbsubmit=Label(DataFrameLeft,bg="peach puff",text="Submission date",font=("bebas neu",12),padx=2,pady=6)
        lbsubmit.grid(row=4,column=2,sticky=W)
        txtsubmit=Entry(DataFrameLeft,textvariable=self.submissiondate,font=("bebas neu",12),width=17)
        txtsubmit.grid(row=4,column=3)

        lbprice=Label(DataFrameLeft,bg="peach puff",text="Price",font=("bebas neu",12),padx=2,pady=6)
        lbprice.grid(row=5,column=2,sticky=W)
        txtprice=Entry(DataFrameLeft,textvariable=self.price,font=("bebas neu",12),width=17)
        txtprice.grid(row=5,column=3)

        #=================================data frame right======================================

        DataFrameRight=LabelFrame(frame,text="Book details",bg="peach puff",fg="maroon",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameRight.place(x=720,y=5,width=480,height=250)

        self.txtbox=Text(DataFrameRight,font=("bebas neu",12),width=26,height=10,padx=3,pady=6)
        self.txtbox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        listbook=["Impro:Improvisation and the Theatre","Ignore Everybody",
                  "Born Standing Up","Just Kids","Bird by Bird by Anne Lamott","The Practicing Mind by Thomas M. Sterner",
                 "Daily Rituals: How Artists Work by Mason Currey","Guns, Germs, and Steel: The Fates of Human Societies by Jared Diamond",
                 "Pride and Prejudice","1984","Little Women","Maths NCERT","Science NCERT","Eglish","C/C++coding","Basics of python"]
        
        def selectbook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Impro:Improvisation and the Theatre"):
                self.bookid.set("BKID5656")
                self.bookname.set("Impro: Improvisation and the Theatre")
                self.author.set("Keith Johnstone")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.submissiondate.set(d3)
                self.price.set("Rs 780")

            elif (x=="Ignore Everybody"):
                self.bookid.set("BKID5657")
                self.bookname.set("Ignore Everybody by Hugh MacLeod")
                self.author.set("Hugh MacLeod")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.submissiondate.set(d3)
                self.price.set("Rs 580")

            elif (x=="Born Standing Up"):
                self.bookid.set("BKID5658")
                self.bookname.set("Born Standing Up")
                self.author.set("Steve Martin")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.submissiondate.set(d3)
                self.price.set("Rs 580")
            
            elif (x=="Just Kids"):
                self.bookid.set("BKID5658")
                self.bookname.set("Just Kids")
                self.author.set("Patti Smith")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.submissiondate.set(d3)
                self.price.set("Rs 680")

            elif (x=="Bird by Bird"):
                self.bookid.set("BKID5651")
                self.bookname.set("Bird by Bird")
                self.author.set("by Anne Lamott")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=20)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.submissiondate.set(d3)
                self.price.set("Rs 280")

            
            

            


        listBox=Listbox(DataFrameRight,font=("bebas neu",12),width=20,height=10)
        listBox.bind("<<ListboxSelect>>",selectbook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)
        
        for i in listbook:
            listBox.insert(END,i)

        self.txtbox=Text(DataFrameRight,font=("bebas neu",12),width=23,height=10,padx=3,pady=6)
        self.txtbox.grid(row=0,column=2)

        #========================================================BUTTON FRAME==========================

        framebtn=Frame(self.root,bd=12,relief=FLAT,padx=20,bg="peach puff") 
        framebtn.place(x=0,y=430,width=1270,height=70)

        btndata=Button(framebtn,command=self.data,text="Add Data",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btndata.grid(row=0,column=0)

        btnshow=Button(framebtn,command=self.Show_Data,text="Show Data",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btnshow.grid(row=0,column=1)

        btnupdate=Button(framebtn,command=self.update,text="Update",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btnupdate.grid(row=0,column=2)

        btndelete=Button(framebtn,command=self.delete,text="Delete",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btndelete.grid(row=0,column=3)

        btnreset=Button(framebtn,command=self.reset,text="Reset",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btnreset.grid(row=0,column=4)

        btnexit=Button(framebtn,command=self.iexit,text="Exit",font=("bebas neu",12),width=21,bg="maroon",fg="white")
        btnexit.grid(row=0,column=5)

        #========================================================INFORMATION FRAME==========================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="peach puff") 
        FrameDetails.place(x=0,y=485,width=1270,height=195)

        tableframe =Frame(FrameDetails,bd=6,relief=RIDGE,bg="peach puff") 
        tableframe.place(x=0,y=2,width=1210,height=135)

        xscroll=Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=Scrollbar(tableframe,orient=VERTICAL)

        self.library_table=ttk.Treeview(tableframe,column=("membertype","prnno","title","name",
                                                           "adress","mobile","bookid","bookname","author",
                                                           "borroweddate","submissiondate","price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)


        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("name",text="Name")
        self.library_table.heading("adress",text="Adress")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("bookname",text="Book Name")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("borroweddate",text="Borrowed Date")
        self.library_table.heading("submissiondate",text="Submission Date")
        self.library_table.heading("price",text="Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("name",width=100)
        self.library_table.column("adress",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("bookname",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("submissiondate",width=100)
        self.library_table.column("price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    #================================add data=========================================
    
    def data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dikshi@987",database="demo1")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
    self.member_val.get(),
    self.prn_val.get(),
    self.id_val.get(),
    self.name.get(),
    self.adress.get(),
    self.mobile.get(),
    self.bookid.get(),
    self.bookname.get(),
    self.author.get(),
    self.dateborrowed.get(),
    self.submissiondate.get(),
    self.price.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

     #------UPDATE FUNCTION----------------------------------------------------------------
    def update(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Dikshi@987",database="demo1")
            my_cursor=conn.cursor()
            my_cursor.execute("Update library set Member=%s,ID=%s,Name=%s,Address=%s,mobile=%s,BookID=%s,BookName=%s,author=%s,BorrowedDate=%s,SubmissionDate=%s,price=%s where PRN_No=%s",(
                    self.member_val.get(),
                    self.id_val.get(),
                    self.name.get(),
                    self.adress.get(),
                    self.mobile.get(),
                    self.bookid.get(),
                    self.bookname.get(),
                    self.author.get(),
                    self.dateborrowed.get(),
                    self.submissiondate.get(),
                    self.price.get(),
                    self.prn_val.get(),
                    ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
    
            messagebox.showinfo("Success","Member has been updated successfully.")
    
    #=================================fetch data=================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dikshi@987",database="demo1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from demo1.library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #====================get_cursor================================

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_val.set(row[0])
        self.prn_val.set(row[1])
        self.id_val.set(row[2])
        self.name.set(row[3])
        self.adress.set(row[4])
        self.mobile.set(row[5])
        self.bookid.set(row[6])
        self.bookname.set(row[7])
        self.author.set(row[8])
        self.dateborrowed.set(row[9])
        self.submissiondate.set(row[10])
        self.price.set(row[11])

    #==============================showdata====================================
    
    def Show_Data(self):
        self.txtbox.insert(END,"Member Type\t\t" + self.member_val.get() + "\n")
        self.txtbox.insert(END,"PRN No.\t\t" + self.prn_val.get() + "\n")
        self.txtbox.insert(END,"Title\t\t" + self.id_val.get() + "\n")
        self.txtbox.insert(END,"Name\t\t" + self.name.get() + "\n")
        self.txtbox.insert(END,"Address\t\t" + self.adress.get() + "\n")
        self.txtbox.insert(END,"Mobile Number\t\t" + self.mobile.get() + "\n")
        self.txtbox.insert(END,"book ID\t\t" + self.bookid.get() + "\n")
        self.txtbox.insert(END,"Book Name\t\t" + self.bookname.get() + "\n")
        self.txtbox.insert(END,"Author Name\t\t" + self.author.get() + "\n")
        self.txtbox.insert(END,"Borrowed Date\t\t" + self.dateborrowed.get() + "\n")
        self.txtbox.insert(END,"Submission Date\t\t" + self.submissiondate.get() + "\n")
        self.txtbox.insert(END,"Price\t\t" + self.price.get() + "\n")

    #--------------------------RESET FUNCTION----------------------------------------------
    def reset(self):
        self.member_val.set(""),
        self.prn_val.set(""),
        self.id_val.set(""),
        self.name.set(""),
        self.adress.set(""),
        self.mobile.set(""),
        self.bookid.set(""),
        self.bookname.set(""),
        self.author.set(""),
        self.dateborrowed.set(""),
        self.submissiondate.set(""),
        self.price.set(""),
        self.txtbox.delete("1.0",END)

     #-----------------------EXIT FUNCTION--------------------------------------------------------
    def iexit(self):
            iexit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
            if iexit>0:
                    self.root.destroy()
                    return
            
    #------------------------DELETE FUNCTION-------------------------------------------------------
    def delete(self):
            if self.prn_val.get()=="" or self.id_val.get()=="":
                messagebox.showerror("Error","First select the Member")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Dikshi@987",database="demo1")
                my_cursor=conn.cursor()
                query="delete from library where PRN_No=%s"
                value=(self.prn_val.get(),)
                my_cursor.execute(query,value)
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                messagebox.showinfo("Success","Member has been deleted")
    
        

if __name__=="__main__":
    root=Tk()
    obj=libraryManagement(root)
    root.mainloop()