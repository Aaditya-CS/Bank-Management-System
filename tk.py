import tkinter as tk
from tkinter import IntVar
from tkinter import ttk
import mysql.connector as sql
from datetime import date

mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
cursor=mycon.cursor()


if mycon.is_connected()==True:
    print("Connection to Database successful.")
else:
    print("Error connecting to Database.")

                                                                                                  
def Login():

    def Mainscreen():
    
        global Win1,EntryUser            
        master.withdraw()
        Win1.deiconify()
        Win1['bg'] = 'blue'
        tk.Label(Win1, text="Main screen", bg = 'blue', fg = 'cyan').grid(row=0,column=0)
        tk.Label(Win1, text="Welcome "+EntryUser, bg = 'blue', fg = 'cyan').grid(row=0,column=1)
        tk.Button(Win1, text="Quit", bg = 'green',command=Win1.destroy).grid(row=1)
        tk.Button(Win1, text="Back to Login", bg = 'green',command=BackButtonLogin).grid(row=1,column=1)
        tk.Button(Win1, text="Deposit",command=Depositscreen, bg = 'cyan').grid(row=2)                                                                    
        tk.Button(Win1, text="Withdrawal",command=Withdrawalscreen, bg = 'cyan').grid(row=2,column=1)
        tk.Button(Win1, text="Transfer",command=Transferscreen, bg = 'yellow').grid(row=3)
        tk.Button(Win1, text="View Account History",command=History, bg = 'yellow').grid(row=3,column=1)
        tk.Button(Win1, text="Settings",command=Settings).grid(row=4)

    def BackButtonLogin():
        
        master.deiconify()
        Win1.withdraw()

    def BackButtonDep():

        Win1.deiconify()
        Win3.withdraw()

    def BackButtonHis():
        
        Win1.deiconify()
        Win6.withdraw()

    def BackButtonTransfer():

        Win1.deiconify()
        Win5.withdraw()

    def BackButtonWith():

        Win1.deiconify()
        Win4.withdraw()

    def Deposit():

        import tkinter as tk
        import mysql.connector as sql
        import datetime
        
                                                                                          
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()
        
        global DepInput
        
        DepInput = int(DepEntry.get())

        q="select balance from amount where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)
        data = cursor.fetchone()
        conv = sum(data)
        Balance = conv+DepInput
        
        q1="update amount set balance={0} where name='{1}' and password='{2}'".format(Balance,EntryUser,EntryPass)
        cursor.execute(q1)                                                            
        mycon.commit()

        DOT = datetime.date.today()

        q2="insert into history(Name,DateofTransaction,Credit,Debit,TotalBalance) values('{0}','{1}',{2},{3},{4})".format(EntryUser,DOT,DepInput,0,Balance)
        cursor.execute(q2)
        mycon.commit()

        tk.Label(Win3, text="Deposited amount is : ", bg = 'cyan').grid(row=3)
        tk.Label(Win3, text=DepInput, bg = 'cyan').grid(row=3,column=1)
        tk.Label(Win3, text="Total amount is : ", bg = 'cyan').grid(row=4)
        tk.Label(Win3, text=Balance, bg = 'cyan').grid(row=4,column=1)                                              

    def Depositscreen():
        
        global Win3,DepEntry
        Win3.deiconify()
        Win1.withdraw()
        Win3['bg'] = 'cyan'
        tk.Label(Win3, text="Deposit Screen", bg = 'cyan').grid(row=0)
        tk.Label(Win3, text="Enter amount to be deposited", bg = 'cyan').grid(row=1)
        DepEntry = tk.Entry(Win3)
        DepEntry.grid(row=1,column=1)
        tk.Button(Win3, text="Back to Mainscreen", command=BackButtonDep, bg = 'red').grid(row=2)
        tk.Button(Win3, text="Display Entered account", command=Deposit, bg = 'green').grid(row=2,column=1)
    
                                                                                                  
    def search():                                                           
        
        global EntryUser,EntryPass
        EntryUser = e1.get()
        EntryPass = e2.get()

        import tkinter as tk

        if len(EntryUser)==0 or len(EntryPass)==0:
            tk.Label(master, text="Ensure that both fields are filled").grid(row=5,column=1)
            return None

        import mysql.connector as sql

        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()

        q="select * from amount where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)                                                               
                                                                                                                                                
        data = cursor.fetchall()
        
        if data:
            
            Mainscreen()

        else:
            tk.Label(master, text="Incorrect username or password").grid(row=5,column=1)

    def History():

        global Win6

        import mysql.connector as sql
        import tkinter  as tk
        import matplotlib.pyplot as pl
        Win6.deiconify()
        Win1.withdraw()
        Win6['bg'] = 'blue'                                                                                                                 
        mycon = sql.connect(host="localhost",user="User", passwd="Rootpassword123",database="test")
        cursor = mycon.cursor()
        q = "Select * from history where name='%s' limit 0,10"%(EntryUser)
        cursor.execute(q)
        tk.Label(Win6,text="Name").grid(row=0,column=0)
        tk.Label(Win6,text="Date").grid(row=0,column=1)
        tk.Label(Win6,text="Credit").grid(row=0,column=2)
        tk.Label(Win6,text="Debit").grid(row=0,column=3)
        tk.Label(Win6,text="Balance").grid(row=0,column=4)
        i=1
        for record in cursor: 
            for j in range(len(record)):
                e = tk.Entry(Win6, width=15, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(tk.END, record[j])
            i=i+1                                                                            
        tk.Button(Win6,text="Back to Login",command=BackButtonHis).grid(row=12,column=0)
        tk.Button(Win6,text="Display Graph",command=Graphscreen).grid(row=12,column=2)

    def Graphscreen():

        import mysql.connector as sql
        mycon = sql.connect(host="localhost",user="User", passwd="Rootpassword123",database="test")
        cursor = mycon.cursor()
        
        q1 = "select TotalBalance from history where name='%s' limit 0,10"%(EntryUser)
        cursor.execute(q1)
        data = cursor.fetchall()
        
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

        Win7.deiconify()

        x = list(data)

        y = [50,100,150,200,250,300,350,400,450,500]

        fig = plt.figure(figsize=(3,3))
        plt.plot(x,y)                                                                   

        plt.xticks(x)

        canvas = FigureCanvasTkAgg(fig, master=Win7)
        canvas.draw()
        canvas.get_tk_widget().grid(row=15, column=0)

        toolbarFrame = tk.Frame(master=Win7)
        toolbarFrame.grid(row=17,column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        

    def Transfer():

        import tkinter as tk
        import mysql.connector as sql
        import datetime                                                                 
        
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()
        
        global GetName,GetAmt

        EntryUser = e1.get()
        
        GetName = TransferName.get()
        GetAmt = int(TransferAmt.get())


        q="select balance from amount where name='%s'"%(EntryUser)
        cursor.execute(q)
        data = cursor.fetchone()	
        FirstBal = sum(data)
        FirstUpBal = FirstBal-GetAmt
        
        q1="update amount set balance={0} where name='{1}'".format(FirstUpBal,EntryUser)
        cursor.execute(q1)
        mycon.commit()

        q2="select balance from amount where name='%s'"%(GetName)
        cursor.execute(q2)
        data = cursor.fetchone()
        SecondBal = sum(data)
        SecondUpBal = SecondBal+GetAmt
        
        q3="update amount set balance={0} where name='{1}'".format(SecondUpBal,GetName)
        cursor.execute(q3)	
        mycon.commit()

        DOT = datetime.date.today()

        q4="insert into history(Name,DateofTransaction,Credit,Debit,TotalBalance) values('{0}','{1}',{2},{3},{4})".format(EntryUser,DOT,0,GetAmt,FirstUpBal)
        cursor.execute(q4)
        mycon.commit()

        q5="insert into history(Name,DateofTransaction,Credit,Debit,TotalBalance) values('{0}','{1}',{2},{3},{4})".format(GetName,DOT,GetAmt,0,SecondUpBal)
        cursor.execute(q5)
        mycon.commit()

        tk.Label(Win5,text="Name of sender : ", bg = 'cyan').grid(row=4)
        tk.Label(Win5,text=EntryUser, bg = 'cyan').grid(row=4,column=1)
        tk.Label(Win5,text="Name of reciever : ", bg = 'cyan').grid(row=5)
        tk.Label(Win5,text=GetName , bg = 'cyan').grid(row=5,column=1)
        tk.Label(Win5,text="Amount sent : ", bg = 'cyan').grid(row=6)
        tk.Label(Win5,text=GetAmt, bg = 'cyan').grid(row=6,column=1)
        tk.Label(Win5,text="Balance left : ", bg = 'cyan').grid(row=7)
        tk.Label(Win5,text=FirstUpBal, bg = 'cyan').grid(row=7,column=1)
        

    def Transferscreen():

        global Win5,TransferName,TransferAmt
        
        Win1.withdraw()
        Win5.deiconify()
        Win5['bg'] = 'cyan'
        
        tk.Label(Win5, text="Transfer screen", bg = 'cyan').grid(row=0)
        tk.Label(Win5, text="Enter name of the recipient.", bg = 'cyan').grid(row=1)
        TransferName = tk.Entry(Win5)
        TransferName.grid(row=1,column=1)
        
        tk.Label(Win5, text="Enter amount to be transfered.", bg = 'cyan').grid(row=2)
        TransferAmt = tk.Entry(Win5)	
        TransferAmt.grid(row=2,column=1)

        tk.Button(Win5, text="Transfer Amount",command=Transfer, bg = 'green').grid(row=3,column=1)
        tk.Button(Win5, text="Back to Mainscreen",command=BackButtonTransfer, bg = 'red').grid(row=3)        
        

    def Withdrawal():

        import tkinter as tk
        import mysql.connector as sql
        import datetime
        
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()
        
        global WithInput
        
        WithInput = int(WithEntry.get())
        tk.Label(Win4, text=WithInput).grid(row=3)

        q="select balance from amount where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)
        data = cursor.fetchone()
        conv = sum(data)
        Balance = conv-WithInput
        
        q1="update amount set balance={0} where name='{1}' and password='{2}'".format(Balance,EntryUser,EntryPass) 
        cursor.execute(q1)
        mycon.commit()

        DOT = datetime.date.today()

        q2="insert into history(Name,DateofTransaction,Credit,Debit,TotalBalance) values('{0}','{1}',{2},{3},{4})".format(EntryUser,DOT,0,WithInput,Balance)
        cursor.execute(q2)
        mycon.commit()
        
        tk.Label(Win4, text="Withdrawan amount is : ", bg = 'cyan').grid(row=3)
        tk.Label(Win4, text=WithInput, bg = 'cyan').grid(row=3,column=1)
        tk.Label(Win4, text="Total balance is : ", bg = 'cyan').grid(row=4)
        tk.Label(Win4, text=Balance, bg = 'cyan').grid(row=4,column=1)


    def Withdrawalscreen():
        
        global Win4,WithEntry
        Win4.deiconify()
        Win1.withdraw()
        Win4['bg'] = 'cyan'
        tk.Label(Win4, text="Withdrawal Screen", bg = 'cyan').grid(row=0)
        tk.Label(Win4, text="Enter amount to be Withdrawn", bg = 'cyan').grid(row=1)
        WithEntry = tk.Entry(Win4)
        WithEntry.grid(row=1,column=1)
        tk.Button(Win4, text="Back to Mainscreen", command=BackButtonWith, bg = 'red').grid(row=2)
        tk.Button(Win4, text="Withdraw amount", command=Withdrawal, bg = 'green').grid(row=2,column=1)

        
    def Settings():

        Win1.withdraw()
        SetWin=tk.Tk()

        global EntryUser,EntryPass    
        EntryUser = e1.get()
        EntryPass = e2.get()

        def BackButtonSet():

            SetWin.withdraw()
            Win1.deiconify()

        def ChangeInfo():

            import tkinter as tk
            import mysql.connector as sql

            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()

            UserAccGet = UserAccName.get()
            PassAccGet = PassAccName.get()

            ChangeInfoQ = "update amount set name='{0}',password='{1}' where name='{2}' and password='{3}'".format(UserAccGet,PassAccGet,EntryUser,EntryPass)
            cursor.execute(ChangeInfoQ)
            mycon.commit()

            tk.Label(SetWin,text = "Account has been updated.").grid(row=4)
            
        tk.Label(SetWin,text = "Account settings").grid(row=0)
        tk.Label(SetWin,text = "Overwrite new pass over old pass.").grid(row=0,column=1)
        
        tk.Label(SetWin,text = "Your username is : ").grid(row=1)
        UserAccName = tk.Entry(SetWin)
        UserAccName.grid(row=1,column=1)
        UserAccName.insert(tk.END,EntryUser)
        
        tk.Label(SetWin,text = "Your password is : ").grid(row=2)
        PassAccName = tk.Entry(SetWin)
        PassAccName.grid(row=2,column=1)
        PassAccName.insert(tk.END,EntryPass)
        
        tk.Button(SetWin,text = "Back to Mainscreen",command = BackButtonSet).grid(row=3)
        tk.Button(SetWin,text = "Change Info",command = ChangeInfo).grid(row=3,column=1)
        
                  
    search()
            
def DevelopmentOptions():

    def BackButtonDev():

        master.deiconify()
        DevWin.withdraw()

    def CreateTable():
        
        import mysql.connector as sql
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()

        q1 = "create table if not exists amount(name char(30),password char(30),balance int)"
        q2 = "create table if not exists history(name char(30),DateofTransaction date,Credit int,Debit int,TotalBalance int)"
        cursor.execute(q1)
        cursor.execute(q2)

    def DeleteTableScreen():

        global DelWin,TableNames,Values

        DevWin.withdraw()
        DelWin=tk.Tk()

        import mysql.connector as sql
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()

        Values = []

        def BackButtonDel():

            DelWin.withdraw()
            DevWin.deiconify()

        def DeleteTable():

            import mysql.connector as sql
            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()

            global DelWin,TableNames,Values

            GetName = TableNames.get()
            Delquery = "delete from amount where name = '{0}'".format(GetName)
            cursor.execute(Delquery)
            mycon.commit()
        
            TableNames.set('')
            tk.Label(DelWin,text = "The account deleted is : ").grid(row=3)
            tk.Label(DelWin,text = GetName).grid(row=3,column=1)
        
        def UpdateValue():

            global Values

            import mysql.connector as sql
            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()
            
            SelectAcc = "select name from amount"
            cursor.execute(SelectAcc)
            AccNames = cursor.fetchall()
            Values = []
            for i in AccNames:
                Values.append(i)

            TableNames['values'] = Values
        
        tk.Label(DelWin,text = "Delete accounts here.").grid(row=0)
        tk.Label(DelWin,text = "Select account to be deleted.").grid(row=1)
        TableNames = ttk.Combobox(DelWin, values = Values, postcommand = UpdateValue)
        TableNames.grid(row=1,column=1)

        tk.Button(DelWin,text = "Back to Dev options",command = BackButtonDel).grid(row=2)
        tk.Button(DelWin,text = "Delete Account",command = DeleteTable).grid(row=2,column=1)

    def ModifyAmount():

        DevWin.withdraw()
        ModWin = tk.Tk()

        import mysql.connector as sql
        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor = mycon.cursor()

        ModValues = []

        def BackButtonMod():

            ModWin.withdraw()
            DevWin.deiconify()

        def GetValue():

            global ModValues

            import mysql.connector as sql
            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()
            
            SelectQ = "select name from amount"
            cursor.execute(SelectQ)
            AccList = cursor.fetchall()
            ModValues = []
            for i in AccList:
                ModValues.append(i)

            TableList['values'] = ModValues

        def Modify():

            import mysql.connector as sql
            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()

            TableUser = TableList.get()
            ModAmt = ModVal.get()
            
            AmountQ = "update amount set balance={0} where name='{1}'".format(ModAmt,TableUser)
            cursor.execute(AmountQ)
            mycon.commit()

            tk.Label(ModWin,text = "The account value has been successfully modified").grid(row=4)
            tk.Label(ModWin,text = "The account's username is : ").grid(row=5)
            tk.Label(ModWin,text = TableUser).grid(row=5,column=1)
            tk.Label(ModWin,text = "The account's modified value is : ").grid(row=6)
            tk.Label(ModWin,text = ModAmt).grid(row=6,column=1)

        tk.Label(ModWin,text = "Modify any particular account's value here.").grid(row=0)
        tk.Label(ModWin,text = "Select which account to change : ").grid(row=1)    
        TableList = ttk.Combobox(ModWin, values = ModValues, postcommand = GetValue)
        TableList.grid(row=1,column=1)

        tk.Label(ModWin,text = "Enter the new value : ").grid(row=2)
        ModVal = tk.Entry(ModWin)
        ModVal.grid(row=2,column = 1)

        tk.Button(ModWin,text = "Back to Dev Options",command = BackButtonMod).grid(row=3)
        tk.Button(ModWin,text = "Modify Value",command = Modify).grid(row=3,column=1)
        
    master.withdraw()
    DevWin = tk.Tk()

    tk.Label(DevWin, text="Development options are provided here.").grid(row=0,column=1)

    tk.Button(DevWin, text="Back to Login",command=BackButtonDev).grid(row=1,column=0)
    tk.Button(DevWin, text="Create necessary tables",command=CreateTable).grid(row=1,column=1)
    tk.Button(DevWin, text="Delete Tables",command=DeleteTableScreen).grid(row=2,column=0)
    tk.Button(DevWin, text="Modify Value",command=ModifyAmount).grid(row=2,column=1)

def signup():
    
    def register():
        
       global a,b
       
       a = UserName.get()
       b = PassWord.get()
       
       Endresult = tk.Label(Win2, text="", bg = 'cyan')
       Endresult.grid(row=4,column=1)

       if len(a)==0 or len(b)==0:
           Endresult['text'] = 'Ensure fields are filled'
           return None
       
       c="insert into amount(name,password,balance) values('{0}','{1}',{2})".format(a,b,0)
       
       consearch = "select name,password from amount where name = '{0}'".format(a)
       cursor.execute(consearch)
       data = cursor.fetchall()
       if data:
           Endresult['text'] = ''
           Endresult['text'] = 'Acc with same username exists'

       else:
           cursor.execute(c)
           mycon.commit()
           Endresult['text'] = ''
           Endresult['text'] = 'Successfully created account!!'   

       UserName.delete(0,tk.END)
       PassWord.delete(0,tk.END)
       
    def Back():
        
        master.deiconify()
        Win2.withdraw()
    
    global a,b	
    import tkinter as tk
    import mysql.connector as sql

    mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
    cursor=mycon.cursor()
    
    master.withdraw()
    Win2=tk.Tk()
    Win2['bg'] = 'blue'
    
    tk.Label(Win2, text="Signup page", bg = 'blue').grid(row=0, column=1)
    tk.Label(Win2, text='Enter username', bg = 'blue').grid(row=1)                                                      
    tk.Label(Win2, text='Enter password', bg = 'blue').grid(row=2)
    
    UserName = tk.Entry(Win2)
    PassWord = tk.Entry(Win2, show='*')
    
    UserName.grid(row=1, column=1)
    PassWord.grid(row=2, column=1)
    
    tk.Button(Win2,text="Register",command=register, bg = 'green').grid(row=3,column=1)
    tk.Button(Win2,text="Back",command=Back, bg = 'red').grid(row=3,column=0)

def Showpassword():

    if BoxState.get()==0:
        e2['show']="*"
    else:
        e2['show']=""
    
master=tk.Tk()
master['bg']='blue'

Win1 = tk.Toplevel()
Win2 = tk.Toplevel()
Win3 = tk.Toplevel()
Win4 = tk.Toplevel()
Win5 = tk.Toplevel()
Win6 = tk.Toplevel()
Win7 = tk.Toplevel()

Win1.withdraw()
Win2.withdraw()
Win3.withdraw()
Win4.withdraw()
Win5.withdraw()
Win6.withdraw()
Win7.withdraw()

tk.Label(master, text="Login screen", fg = 'cyan', bg = 'blue').grid(row=0, column=1)
tk.Label(master, text="User", fg = 'cyan', bg = 'blue').grid(row=1)
tk.Label(master, text="Password", fg = 'cyan', bg = 'blue').grid(row=2)
    
e1 = tk.Entry(master)
e2 = tk.Entry(master,show='*')
    
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

BoxState = IntVar()
Showpass = tk.Checkbutton(master,text="Show password",variable=BoxState,command=Showpassword, bg='blue', fg='cyan')
Showpass.grid(row=3)

tk.Button(master,text="Quit",command=master.destroy, bg = 'red').grid(row=4,column=0)                                                
tk.Button(master,text="Login",command=Login, bg = 'green').grid(row=4,column=1)
tk.Button(master,text="Signup",command=signup, bg = 'yellow').grid(row=4,column=2)
tk.Button(master,text="Dev Options",command=DevelopmentOptions).grid(row=0,column=2)

mycon.close()
master.mainloop()
