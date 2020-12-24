
from tkinter import *
from tkinter import ttk
import pymysql
#from PIL import ImageTk,Image
from tkinter import messagebox


class BP:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root['bg']='#191927'
        self.root.title("Bharathi plastics 36ANCPR1165L1ZR")
        #self.root.iconbitmap(r'BP.ico')

        title = Label(self.root, text='Bharathi plastics', font=('Harlow Solid Italic', 30,), fg='#15ae48',bg='#191927')
        title.pack(side=TOP)
        title.place(x=700, y=0)

        #=========all varabale=========
        self.Sno=IntVar()
        self.Type=StringVar()
        self.Invoiceno=IntVar()
        self.Date=StringVar()
        self.Partyname=StringVar()
        self.Gstno=StringVar()
        self.Decription=StringVar()
        self.WT=IntVar()
        self.Qty=IntVar()
        self.Rate=IntVar()
        self.Taxablevalue1=IntVar()
        self.Igst18=IntVar()
        self.Cgst9=IntVar()
        self.Sgst9=IntVar()
        self.TotalGst=IntVar()
        self.GrandTotal=IntVar()

        self.WT=DoubleVar()
        self.Rate=DoubleVar()
        self.Taxablevalue1=DoubleVar()
        self.Igst18=DoubleVar()
        self.Cgst9=DoubleVar()
        self.Sgst9=DoubleVar()
        self.TotalGst=DoubleVar()
        self.GrandTotal=DoubleVar()

        self.Searchby=StringVar()
        self.Searchtxt=StringVar()




        # ================manage_frame=========
        
        manage_Frame = Frame(self.root, bd=4, relief=FLAT, borderwidth=0,bg='#191927')
        manage_Frame.place(x=20, y=0, width=450, height=740,)

        #============box1=====
        sno = Label(manage_Frame, text="Sno:", bg='#191927', fg='white', font=('Bahnschrift', 15,"bold"))
        sno.grid(row=0, column=0,pady=10, padx=8,sticky='w')

        sno = Entry(manage_Frame,textvariable=self.Sno,font=('arial', 15, "bold"), bd=5, width=10,relief=FLAT,highlightthickness=2, highlightbackground= "#003366",borderwidth=0,)
        sno.grid(row=0, column=1, pady=10, sticky='w')
        sno.place(x=50,y=10)

        #============box2=======
        Type = Label(manage_Frame, text="Ty:", bg='#191927', fg='white', font=('Bahnschrift', 15,"bold"))
        Type.grid(row=0, columnspan=2, pady=10,padx=60, sticky='w')
        Type.place(x=173,y=10)

        type = Entry(manage_Frame,textvariable=self.Type,font=('Bahnschrift', 15,), bd=5,width=20,relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        type.grid(row=0,column=1,padx=10,pady=10)
        type.place(x=200,y=10)

        # =================box3=========
        Invoiceno = Label(manage_Frame, text="Invoice no:",bg='#191927', fg='white', font=('Bahnschrift', 15,"bold"))
        Invoiceno.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        Invoiceno = Entry(manage_Frame,textvariable=self.Invoiceno,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        Invoiceno.grid(row=1, column=1, pady=10, padx=20, sticky='w')
        
        #=================box4=========
        date = Label(manage_Frame, text="Date:",bg='#191927', fg='white', font=('Bahnschrift', 15,"bold"))
        date.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        date = Entry(manage_Frame,textvariable=self.Date,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        date.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        
        #=================box5=========
        partyname = Label(manage_Frame, text="Party name:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        partyname.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        partyname = Entry(manage_Frame,textvariable=self.Partyname,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        partyname.grid(row=3, column=1, pady=10, padx=20, sticky='w')
        
        #=================box6===========
        gstno = Label(manage_Frame, text="Gst no:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        gstno.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        gstno = Entry(manage_Frame,textvariable=self.Gstno,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        gstno.grid(row=4, column=1, pady=10, padx=20, sticky='w')
        
        # =================box7==========
        Decription = Label(manage_Frame, text="Decription:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Decription.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        Decription = Entry(manage_Frame,textvariable=self.Decription,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        Decription.grid(row=5, column=1, pady=10, padx=20, sticky='w')
        
        # =================box8==========
        WT = Label(manage_Frame, text="WT:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        WT.grid(row=6, column=0,pady=10, padx=20,sticky='w')
        
        WT = Entry(manage_Frame, textvariable=self.WT,font=('arial', 15, "bold"), bd=5,relief=FLAT,highlightthickness=2, highlightbackground="#003366",width=8,borderwidth=0)
        WT.grid(row=6, column=2, pady=10, sticky='w')
        WT.place(x=65,y=315)
        

        # =================box8==========
        Qty = Label(manage_Frame, text="Qty:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Qty.grid(row=6, column=0,pady=10, padx=20,sticky='w')
        Qty.place(x=160,y=315)

        Qty = Entry(manage_Frame,textvariable=self.Qty,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",width=8,borderwidth=0)
        Qty.grid(row=6, column=1, pady=10, sticky='w')
        Qty.place(x=205,y=315)

        #===============box9=======
        Rate = Label(manage_Frame, text="Rate:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Rate.grid(row=6, column=0,pady=10, padx=20,sticky='w')
        Rate.place(x=300,y=315)
        

        Rate = Entry(manage_Frame, textvariable=self.Rate,font=('arial', 15, "bold"), bd=5,relief=FLAT,highlightthickness=2, highlightbackground="#003366",width=8,borderwidth=0)
        Rate.grid(row=6, column=2, pady=10, sticky='w')
        Rate.place(x=355,y=315)
        
        

        
        #=================box10========
        Taxablevalue1 = Label(manage_Frame, text="Taxable value:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Taxablevalue1 .grid(row=7, column=0, pady=10, padx=20, sticky='w')

        Taxablevalue1  = Entry(manage_Frame,textvariable=self.Taxablevalue1,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",width=12,borderwidth=0)
        Taxablevalue1.grid(row=7, column=1, pady=10, padx=20, sticky='w')
        

        #=================box11========
        
        Igst = Label(manage_Frame, text="Igst@18%:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Igst.grid(row=8, column=0, pady=10, padx=20, sticky='w')
        
        Igst = Entry(manage_Frame,textvariable=self.Igst18,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366", width=12,borderwidth=0)
        Igst.grid(row=8, column=1, pady=10, padx=20, sticky='w')
   
        # =================box12=====
        Cgst = Label(manage_Frame, text="Cgst@9%:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        Cgst.grid(row=9, column=0, pady=10, padx=20, sticky='w')
        
        Cgst = Entry(manage_Frame,textvariable=self.Cgst9,font=('arial', 15, "bold"), bd=5,relief=FLAT,highlightthickness=2, highlightbackground="#003366", width=12,borderwidth=0)
        Cgst.grid(row=9, column=1, pady=10, padx=20, sticky='w')
		
        # =================box13========
        sgst = Label(manage_Frame, text="sgst@9%:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        sgst.grid(row=10, column=0, pady=10, padx=20, sticky='w')
        
        sgst = Entry(manage_Frame,textvariable=self.Sgst9,font=('arial', 15, "bold"), bd=5,relief=FLAT,highlightthickness=2, highlightbackground="#003366", width=12,borderwidth=0)
        sgst.grid(row=10, column=1, pady=10, padx=20, sticky='w')
       
        # =================box14=====
        TotalGst = Label(manage_Frame, text="Total Gst:",bg='#191927', fg='#FFFFFF', font=('Bahnschrift', 15,"bold"))
        TotalGst.grid(row=11, column=0, pady=10, padx=20, sticky='w')
        
        TotalGst = Entry(manage_Frame,textvariable=self.TotalGst,font=('arial', 15, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        TotalGst.grid(row=11, column=1, pady=10, padx=20, sticky='w')

        #=================box15=========
        GrandTotal = Label(manage_Frame, text="Grand Total:",bg='#191927', fg='#14a5FFFFFFae', font=('Bahnschrift', 15,"bold"))
        GrandTotal.grid(row=12, column=0, pady=10, padx=20, sticky='w')
        
        GrandTotal = Entry(manage_Frame,textvariable=self.GrandTotal,font=('arial', 15, "bold"), bd=5,relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        GrandTotal.grid(row=12, column=1, pady=10, padx=20, sticky='w')

    

        #============BUTTONFRAME===========
        #===========button frame1=========
        btn_Frame1=Frame(manage_Frame,bd=4,relief=FLAT,borderwidth=0,bg="#003366")
        btn_Frame1.place(x=30,y=650,width=340)

        
        Total=Button(btn_Frame1,text="Total",font=('Arial',10,"bold"),command=self.total,width=10,borderwidth=0,bg="#15ae48",fg="white",).grid(row=0,column=1,padx=0,pady=0)
        Clear=Button(btn_Frame1,text="Clear",font=('Arial',10,"bold"),width=10,command=self.clear,borderwidth=0,bg="#6513da",fg="white").grid(row=0,column=3,padx=0,pady=0)
        Addbtn=Button(btn_Frame1,text="Add",font=('Arial',10,"bold"),width=10,borderwidth=0,command=self.add_bharathiplastics,bg="#419eca",fg="white").grid(row=0,column=2,padx=0,pady=0)
        deletetn=Button(btn_Frame1,text="Delete",font=('Arial',10,"bold"),width=10,command=self.delete_data,borderwidth=0,bg="#e14753",fg="white").grid(row=0,column=5,padx=0,pady=0)
    
        #===========button frame2=========
        btn_Frame2=Frame(manage_Frame,bd=4,relief=RIDGE,borderwidth=0,bg='#003366')
        btn_Frame2.place(x=350,y=362,width=78,height=25,)

        clickhere=Button(btn_Frame2,text="Click here",bg='#003366',fg='white',command=self.click1,width=9,borderwidth=0,).grid(row=0,column=0,padx=0,pady=0)
        
        #===========button frame3=========
        btn_Frame3=Frame(manage_Frame,bd=4,relief=RIDGE,borderwidth=0,bg='#003366')
        btn_Frame3.place(x=350,y=412,width=78,height=25)

        clickhere1=Button(btn_Frame3,text="Click here",command=self.click2,bg='#003366',fg='white',width=9,borderwidth=0).grid(row=0,column=0,padx=0,pady=0)
        
        #===========button frame4=========
        btn_Frame4=Frame(manage_Frame,bd=4,relief=RIDGE,borderwidth=0,bg='#003366')
        btn_Frame4.place(x=350,y=462,width=78,height=25)

        clickhere=Button(btn_Frame4,text="Click here",command=self.click3,bg='#003366',fg='white',width=9,borderwidth=0).grid(row=0,column=0,padx=0,pady=0)

        #===========button frame5=========
        btn_Frame5=Frame(manage_Frame,bd=4,relief=RIDGE,borderwidth=0,bg='#003366')
        btn_Frame5.place(x=350,y=512,width=78,height=25)

        clickhere=Button(btn_Frame5,text="Click here",command=self.click4 ,bg='#003366',fg='white',width=9,borderwidth=0).grid(row=0,column=0,padx=0,pady=0, )


        #=================details_Frame=========

        details_Frame = Frame(self.root, bd=4, relief=FLAT, borderwidth=0, bg='#191927',)
        details_Frame.place(x=470, y=50, width=810, height=690)

        search = Label(details_Frame, text="Search :", bg='#191927', fg='white', font=('Bahnschrift', 15,"bold"))
        search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_type=ttk.Combobox(details_Frame,textvariable=self.Searchby,width=10,font=('Bahnschrift', 15,"bold"), state='readonly')
        combo_type['values']=("Sno","Invoiceno","Type","Date","Partyname","Gstno",)
        combo_type.grid(row=0,column=1,padx=5,pady=10)

        u5_title = Entry(details_Frame,textvariable=self.Searchtxt,font=('arial', 17, "bold"), bd=5, relief=FLAT,highlightthickness=2, highlightbackground="#003366",borderwidth=0)
        u5_title.grid(row=0, column=2, pady=10, padx=20, sticky='w') 

        searchbtn=Button(details_Frame,text="Search",font=('Arial',10,"bold"),command=self.search_data,width=10,relief=FLAT,bg='#003366',fg='white').grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(details_Frame,text="Show all",font=('Arial',10,"bold"),width=10,command=self.fetch_data,bg='#003366',fg='white',relief=FLAT).grid(row=0,column=4,padx=10,pady=10)
#=================Table frame=========
        
        Table_Frame=Frame(self.root,bd=4,relief=FLAT,borderwidth=0,bg='black')
        Table_Frame.place(x=480,y=120,width=780,height=600)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Accounts_table=ttk.Treeview(Table_Frame,column=("Sno","Type","Inv no","Date","Party name","Gst no","Decription","WT","Qty","Rate","Taxable value","Igst@18%","Cgst@9%","Sgst@9%","Total Gst","Grand Total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Accounts_table.xview)
        scroll_y.config(command=self.Accounts_table.yview)
        self.Accounts_table.heading("Sno", text="Sno"),self.Accounts_table.column("Sno",width=50)
        self.Accounts_table.heading("Type", text="Type"),self.Accounts_table.column("Type",width=150)
        self.Accounts_table.heading("Inv no", text="Inv No"),self.Accounts_table.column("Inv no",width=50)
        self.Accounts_table.heading("Date", text="Date"),self.Accounts_table.column("Date",width=100)
        self.Accounts_table.heading("Party name", text="Party name"),self.Accounts_table.column("Party name",width=200)
        self.Accounts_table.heading("Gst no", text="Gst No"),self.Accounts_table.column("Gst no",width=150)
        self.Accounts_table.heading("Decription", text="Decription"),self.Accounts_table.column("Decription",width=200)
        self.Accounts_table.heading("WT", text="WT"),self.Accounts_table.column("WT",width=80)
        self.Accounts_table.heading("Qty", text="Qty"),self.Accounts_table.column("Qty",width=80)
        self.Accounts_table.heading("Rate", text="Rate"),self.Accounts_table.column("Rate",width=80)
        self.Accounts_table.heading("Taxable value", text="Taxable value"),self.Accounts_table.column("Taxable value",width=100)
        self.Accounts_table.heading("Igst@18%", text="Igst@18%"),self.Accounts_table.column("Igst@18%",width=100)
        self.Accounts_table.heading("Cgst@9%", text="Cgst@9%"),self.Accounts_table.column("Cgst@9%",width=100)
        self.Accounts_table.heading("Sgst@9%", text="Sgst@9%"),self.Accounts_table.column("Sgst@9%",width=100)
        self.Accounts_table.heading("Total Gst", text="Total Gst"),self.Accounts_table.column("Total Gst",width=100)
        self.Accounts_table.heading("Grand Total", text="Grand Total"),self.Accounts_table.column("Grand Total",width=100)
        self.Accounts_table["show"]="headings"


        self.Accounts_table.pack(fill=BOTH,expand=1)
        self.Accounts_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        
    def add_bharathiplastics(self):
        if self.Type.get()=="" or self.Invoiceno.get()=="" or self.Date.get()=="" or self.Gstno.get()=="" or self.Decription.get()=="":
                messagebox.showerror("Error","Please fill the details!")      
        else:        
            con=pymysql.connect(host="localhost",user="root",password="",database="test")
            cur=con.cursor()
            cur.execute("insert into bunty values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Sno.get(),
                                                                                                    self.Type.get(),
                                                                                                    self.Invoiceno.get(),
                                                                                                    self.Date.get(),
                                                                                                    self.Partyname.get(),
                                                                                                    self.Gstno.get(),
                                                                                                    self.Decription.get(),
                                                                                                    self.WT.get(),
                                                                                                    self.Qty.get(),
                                                                                                    self.Rate.get(),
                                                                                                    self.Taxablevalue1.get(),
                                                                                                    self.Igst18.get(),
                                                                                                    self.Cgst9.get(),
                                                                                                    self.Sgst9.get(),
                                                                                                    self.TotalGst.get(),
                                                                                                    self.GrandTotal.get(),
                                                                                                    ))
                                                                                              
            con.commit()
            self.fetch_data()   
            con.close()
            messagebox.showinfo("Success","Details has been insert successful")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="test")
        cur=con.cursor()
        cur.execute("select * from bunty")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Accounts_table.delete(*self.Accounts_table.get_children())
                for row in rows:
                        self.Accounts_table.insert('',END,values=row)
                con.commit()
        con.close()


    def clear(self)          :
        self.Sno.set("0")
        self.Type.set("")
        self.Invoiceno.set("0")
        self.Date.set("")
        self.Partyname.set("")
        self.Gstno.set("")
        self.Decription.set("")
        self.WT.set("0.0")
        self.Qty.set("0")
        self.Rate.set("0")
        self.Taxablevalue1.set("0")
        self.Igst18.set("0")
        self.Cgst9.set("0")
        self.Sgst9.set("0")
        self.TotalGst.set("0")
        self.GrandTotal.set("0")

    def get_cursor(self,ev)        :
        curosor_row=self.Accounts_table.focus()
        contents=self.Accounts_table.item(curosor_row)
        row=contents['values']
        print(row)
        self.Sno.set(row[0])
        self.Type.set(row[1])
        self.Invoiceno.set(row[2])
        self.Date.set(row[3])
        self.Partyname.set(row[4])
        self.Gstno.set(row[5])
        self.Decription.set(row[6])
        self.WT.set(row[7])
        self.Qty.set(row[8])
        self.Rate.set(row[9])
        self.Taxablevalue1.set(row[10])
        self.Igst18.set(row[11])
        self.Cgst9.set(row[12])
        self.Sgst9.set(row[13])
        self.TotalGst.set(row[14])
        self.GrandTotal.set(row[15])

    

    def delete_data(self)        :
        con=pymysql.connect(host="localhost",user="root",password="",database="test")
        cur=con.cursor()
        cur.execute("delete from bunty where Sno=%s",self.Sno.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        


    def click1(self)        :
        self.Taxable_value1=int(
                              (self.WT.get())*
                              (self.Rate.get())
                           )    
        self.Taxablevalue1.set(str(self.Taxable_value1))

        
    def click2(self)        :
        self.igst_tax=float(
                      (self.Taxablevalue1.get()*0.18)
                    )
        self.Igst18.set(float(self.igst_tax))


    def click3(self)        :
        self.cgst_tax=float(
                      (self.Taxablevalue1.get()*0.09)
                      )
        self.Cgst9.set(float(self.cgst_tax))
    
    def click4(self):
        self.sgst_tax=float(       

                      (self.Taxablevalue1.get()*0.09)
                    )
        self.Sgst9.set(float(self.sgst_tax))

    def total(self)        :
        self.total_gst=float(
                         (self.Igst18.get())+
                         (self.Cgst9.get())+
                         (self.Sgst9.get())
                      )
        self.TotalGst.set(float(self.total_gst))

        self.grand_total=float(
                         (self.Taxablevalue1.get())+
                         (self.TotalGst.get())
                      )
        self.GrandTotal.set(float(self.grand_total))

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="test")
        cur=con.cursor()

        cur.execute("select * from bunty where "+str(self.Searchby.get())+" LIKE '%"+str(self.Searchtxt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Accounts_table.delete(*self.Accounts_table.get_children())
                for row in rows:
                        self.Accounts_table.insert('',END,values=row)
                con.commit()
        con.close()


      


                              

                             
   




   
        

    	 		
		 
	    
	    
	    	
		

root = Tk()
ob = BP(root)
root.mainloop()
