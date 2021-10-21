import tkinter as tk
from tkinter import IntVar
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as sql
from datetime import date

mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
cursor=mycon.cursor(buffered=True)

if mycon.is_connected()==True:
    print("Connection to Database successful.")
else:
    print("Error connecting to Database.")
                                                                                     
def Login():

    def Mainscreen():
    
        global MainWin,EntryUser,TkBackImage,TkAccImage,TkDepImage,TkWithImage,TkTrnsImage,TkHistoryImage,TkSetImage,BalTxt,TkBigAccImage,TkBigDepImage,TkBigWithImage,TkBigTrnsImage,TkBigHistoryImage,TkBigSetImage,TkBigAccImage,TkSendImage

        master.withdraw()
        MainWin.deiconify()
        MainWin.state("zoomed")

        print("Opened new window")

        MainWin.grid_columnconfigure((0,1),weight=1)

        AccIDQ = "select AccNo from Accdetails where name = '{0}'".format(EntryUser)
        cursor.execute(AccIDQ)
        IDRes = cursor.fetchone()
        AccID = sum(IDRes)

        AccInfoCon = tk.Frame(MainWin,highlightbackground='black',highlightthickness=1)
        AccInfoCon.grid(row=1,column=0)

        MainInfo = tk.Frame(MainWin)
        MainInfo.grid(row=1,column=1)

        MainInfoSec = tk.Frame(MainWin)
        MainInfoSec.grid(row=2,column=1)

        ButtonInfo = tk.Frame(MainWin,background='white',highlightbackground='black',highlightthickness=2)
        ButtonInfo.grid(row=2,column=0,sticky='w')
        
        tk.Label(MainWin, text="Login successful - iBanking             ",font=BFont,anchor='w',bg= 'pale green', fg = 'forest green').grid(row=0,column=1,sticky='we')
        tk.Label(MainWin, text="Message Contacts here",font=BFont,anchor='w',bg= 'pale green', fg = 'forest green').grid(row=0,column=2,sticky='we')
        tk.Label(AccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(AccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(AccInfoCon,text=EntryUser+" ",font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(AccInfoCon,text="   Account ID           :  ",font=BFont,anchor='w').grid(row=2,pady=5,sticky='n')
        tk.Label(AccInfoCon,text=AccID,font=BFont,anchor='w').grid(row=2,column=1,pady=5,sticky='n')
        tk.Label(AccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=3,pady=5,sticky='n')

        CurrQ="select balance from Accdetails where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(CurrQ)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(AccInfoCon,textvariable=BalTxt,font=TFont,anchor='w')
        BalLab.grid(row=3,column=1,sticky='w')

        BigHistoryImage = Image.open("historyy.png")
        BigHistoryImage = BigHistoryImage.resize((200,100),Image.ANTIALIAS)
        TkBigHistoryImage = ImageTk.PhotoImage(BigHistoryImage)

        BigDepImage = Image.open("deposit.png")
        BigDepImage = BigDepImage.resize((200,100),Image.ANTIALIAS)
        TkBigDepImage = ImageTk.PhotoImage(BigDepImage)

        BigWithImage = Image.open("withdraw.png")
        BigWithImage = BigWithImage.resize((200,100),Image.ANTIALIAS)
        TkBigWithImage = ImageTk.PhotoImage(BigWithImage)

        BigTrnsImage = Image.open("transfer.png")
        BigTrnsImage = BigTrnsImage.resize((200,100),Image.ANTIALIAS)
        TkBigTrnsImage = ImageTk.PhotoImage(BigTrnsImage)

        BigSetImage = Image.open("settings.png")
        BigSetImage = BigSetImage.resize((200,100),Image.ANTIALIAS)
        TkBigSetImage = ImageTk.PhotoImage(BigSetImage)

        BigAccImage = Image.open("accdetails.png")
        BigAccImage = BigAccImage.resize((200,100),Image.ANTIALIAS)
        TkBigAccImage = ImageTk.PhotoImage(BigAccImage)

        SendImage = Image.open("send.png")
        SendImage = SendImage.resize((25,25),Image.ANTIALIAS)
        TkSendImage = ImageTk.PhotoImage(SendImage)

        tk.Button(MainInfo,text='Account Details',command=AccountDetails,font=BigFont,borderwidth=0,image=TkBigAccImage,compound='top').grid(row=1,column=1,pady=30,sticky='w')
        tk.Button(MainInfo,text='Deposit',command=Depositscreen,font=BigFont,borderwidth=0,image=TkBigDepImage,compound='top').grid(row=1,column=2,pady=30,sticky='w')
        tk.Button(MainInfo,text='Withdraw',command=Withdrawalscreen,font=BigFont,borderwidth=0,image=TkBigWithImage,compound='top').grid(row=1,column=3,pady=30,sticky='w')
        tk.Button(MainInfoSec,text='Transfer',command=Transferscreen,font=BigFont,borderwidth=0,image=TkBigTrnsImage,compound='top').grid(row=0,column=0,pady=30,sticky='w')
        tk.Button(MainInfoSec,text='Transaction History',command=History,font=BigFont,borderwidth=0,image=TkBigHistoryImage,compound='top').grid(row=0,column=1,pady=30,sticky='w')
        tk.Button(MainInfoSec,text='Settings',command=DevelopmentOptions,font=BigFont,borderwidth=0,image=TkBigSetImage,compound='top').grid(row=0,column=2,pady=30,sticky='w')
                 
        tk.Button(MainWin, text="    Logout",command=BackButtonLogin,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')
        tk.Button(ButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(ButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(ButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(ButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(ButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(ButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(ButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(ButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(ButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(ButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(ButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')

        from tkinter import scrolledtext

        ViewMsg = scrolledtext.ScrolledText(MainWin, wrap=tk.WORD,width=22, height=19,font=TxtFont,state="disabled")
        ViewMsg.grid(row=1,column=2,rowspan=2,pady=10)
        
        FFont = ("TKDefaultFont",12)
        AddFriendBox = tk.Entry(MainWin,font=FFont,width=17)
        AddFriendBox.grid(row=7,column=2,sticky='ne')
        
        MsgBox = tk.Entry(MainWin,font=TxtFont,width=21)
        MsgBox.grid(row=2,column=2,sticky='sw')
        MsgBox.insert(tk.END,"Type your message...")

        Q1 = "select AccNo from Accdetails where name = '{0}'".format(EntryUser)
        cursor.execute(Q1)
        result = cursor.fetchone()
        SenderID = sum(result)

        FriendsQ = "select name from friends where SenderID = {0}".format(SenderID)
        cursor.execute(FriendsQ)
        ResultF = cursor.fetchall()

        Friends = []

        for i in ResultF:
            Friends.append(i[0])

        tk.Label(MainWin,text = "Select friend.",font = TxtFont).grid(row=1,column=2,sticky='nw')

        FriendBox = ttk.Combobox(MainWin,values = Friends,state="readonly")
        FriendBox.grid(row=1,column=2,sticky='ne')

        def ClearMsgBox(*args):
            MsgBox.delete(0,tk.END)

        def Send(*args):
            ReceiverName = FriendBox.get()

            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor = mycon.cursor(buffered=True)
            
            NewMsgQ = "select AccNo from Accdetails where name = '{0}'".format(ReceiverName)
            cursor.execute(NewMsgQ)
            fetch = cursor.fetchone()
            RecID = fetch[0]

            Msg = MsgBox.get()

            AddMsgQ = "insert into messages(SenderID,RecieverID,NameofSender,Message) values({0},{1},'{2}','{3}')".format(SenderID,RecID,EntryUser,Msg)
            cursor.execute(AddMsgQ)
            mycon.commit()

            GetMsgQ = "select message,SenderID,nameofSender from messages where (SenderID = {0} and RecieverID = {1}) or (SenderID = {1} and RecieverID = {0})".format(SenderID,RecID)
            cursor.execute(GetMsgQ)
            AllMsgs = cursor.fetchall()
            
            ViewMsg['state'] = "normal"
            ViewMsg.delete("1.0",tk.END)
            for z in AllMsgs:
                ViewMsg.insert(tk.END,EntryUser + " : " + z[0] + "\n")
            MsgBox.delete(0,tk.END)
            ViewMsg['state'] = "disabled"

        BindMsgBox = MsgBox.bind("<Button-1>",ClearMsgBox)
        
        tk.Button(MainWin,text="  ",image=TkSendImage,command=Send,borderwidth=0,compound='left').grid(row=2,column=2,sticky='se')
        BindSend = MainWin.bind("<Return>",Send)
        
        def AddFriend():
            global FriendID
            FriendID = AddFriendBox.get()

            IDQ = "select AccNo from Accdetails"
            cursor.execute(IDQ)
            IDS = cursor.fetchall()

            CheckQ = "select * from friends"
            cursor.execute(CheckQ)
            ans = cursor.fetchall()

            for i in IDS:                           #check all IDS
                if int(i[0])==int(FriendID):        #If FriendID exists
                    print("First condition reached.")
                    for j in ans:                   #Open Friend List
                        print("Checking Friend List.")
                        print(j[0],j[1])
                        if j[0]==int(FriendID) and j[1]==int(SenderID): #Check whether user is already added in Friend list
                            print("User already added as a friend.")
                            tk.Label(MainWin,text = "Already in Friend List").grid(row=6,column=2)
                            break
                    else:                                               #If none of the users existing are friends with user, add them
                        print("User is not added as Friend. Adding user now")

                        QFriendID = int(FriendID)
                        NameQ = "select Name from Accdetails where AccNo = {0}".format(QFriendID)
                        cursor.execute(NameQ)
                        rowcount = cursor.rowcount
                        if rowcount == 0:
                            break
                        fetched = cursor.fetchone()
                        FriendName = fetched[0]
                        
                        Q2 = "insert into Friends(SenderID,ReceiverID,Name) values({0},{1},'{2}')".format(SenderID,FriendID,FriendName)
                        newcursor.execute(Q2)

                        Q3 = "insert into Friends(SenderID,ReceiverID,Name) values({0},{1},'{2}')".format(FriendID,SenderID,EntryUser)
                        newcursor.execute(Q3)
                        mycon.commit()
                        tk.Label(MainWin,text="Added Friend").grid(row=6,column=2)
                        break
                    break
            else:   #If FriendID does not exist
                print("User does not exist")
                tk.Label(MainWin,text = "User does not exist.").grid(row=6,column=2)

        Friendbutton = tk.Button(MainWin,text="Add Friend",command=AddFriend,borderwidth=0,font=TxtFont)
        Friendbutton.grid(row=7,column=2,sticky='nw')

    def BackButtonLogin():
        
        master.deiconify()
        MainWin.withdraw()
        master.state("zoomed")

    def BackButtonDep():

        MainWin.deiconify()
        CloseWin()
        MainWin.state("zoomed")

    def BackButtonHis():
        
        MainWin.deiconify()
        CloseWin()
        MainWin.state("zoomed")

    def BackButtonTransfer():

        MainWin.deiconify()
        CloseWin()
        MainWin.state("zoomed")

    def BackButtonWith():

        MainWin.deiconify()
        CloseWin()
        MainWin.state("zoomed")

    def Deposit():

        import tkinter as tk
        import mysql.connector as sql
        import datetime
        
        global DepInput
        
        DepInput = int(DepEntry.get())

        q="select balance from Accdetails where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)
        data = cursor.fetchone()
        conv = sum(data)
        Balance = conv+DepInput

        DOT = datetime.date.today()
        AccNoQ = "select AccNo from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(AccNoQ)
        data = cursor.fetchone()
        AccNo = sum(data)
        
        try:
            q1="update Accdetails set balance={0} where name='{1}' and password='{2}'".format(Balance,EntryUser,EntryPass)
            cursor.execute(q1)                                                            

            q2="insert into history(AccNo,Name,DateofTransaction,Credit,Debit,TotalBalance) values({0},'{1}','{2}',{3},{4},{5})".format(AccNo,EntryUser,DOT,DepInput,0,Balance)
            cursor.execute(q2)
            mycon.commit()

            BalTxt.set(Balance)

            tk.Label(DepMainInfo, text="Deposited amount is :",font=BFont).grid(row=5,sticky='e')
            tk.Label(DepMainInfo, text=DepInput,font=BFont).grid(row=5,column=1,sticky='w')
            tk.Label(DepMainInfo, text="Total amount is :",font=BFont).grid(row=6,sticky='e')
            tk.Label(DepMainInfo, text=Balance,font=BFont).grid(row=6,column=1,sticky='w')

        except Exception as e:
            print(str(e))
            tk.Label(DepMainInfo, text="Some Error has occurred.").grid(row=3)

    def Depositscreen():
        
        global DepWin,DepEntry,DepMainInfo
        
        DepWin.deiconify()
        MainWin.withdraw()
        DepWin.state("zoomed")

        DepWin.grid_columnconfigure((0,1),weight=1)

        tk.Label(DepWin, text="Deposit Screen                                 ",bg='pale green',fg='forest green', font=TFont,anchor='w').grid(row=0,column=1,sticky='ew')
        tk.Label(DepWin, text="Deposit your cash here",bg = 'pale green',fg = 'forest green',font=TFont).grid(row=0,column=2,sticky='we')

        DepMainInfo = tk.Frame(DepWin)
        DepMainInfo.grid(row=2,column=1,sticky='n')
        
        tk.Label(DepWin, text="Logged in",bg = 'pale green',fg = 'forest green',font=BFont,anchor='nw').grid(row=1,column=1,sticky='n')
        tk.Label(DepMainInfo, text="Enter deposit amount :  ", font=BFont,anchor='nw').grid(row=1,sticky='nw',pady=10)
        DepEntry = tk.Entry(DepMainInfo, font=BFont)
        DepEntry.grid(row=1,column=1,pady=10)

        DepAccInfoCon = tk.Frame(DepWin,highlightbackground='black',highlightthickness=1)
        DepAccInfoCon.grid(row=1,column=0,padx=20)

        tk.Label(DepAccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(DepAccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(DepAccInfoCon,text=EntryUser,font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(DepAccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=2,pady=5,sticky='n')

        mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
        cursor=mycon.cursor()

        CurrBal = "select balance from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(CurrBal)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(DepAccInfoCon,textvariable=BalTxt,font=BFont,anchor='w')
        BalLab.grid(row=2,column=1,sticky='w',pady=5)

        DepButtonInfo = tk.Frame(DepWin,background='white',highlightbackground='black',highlightthickness=2)
        DepButtonInfo.grid(row=2,pady=30)

        tk.Button(DepWin, text="    Back ",command=BackButtonDep,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')    
        tk.Button(DepButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(DepButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(DepButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(DepButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(DepButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(DepButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(DepButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(DepButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(DepButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(DepButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(DepButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')

        tk.Button(DepMainInfo, text="Deposit amount", command=Deposit, font=BFont).grid(row=3,columnspan=2)
    
                                                                                                  
    def search():                                                           
        
        global EntryUser,EntryPass
        EntryUser = e1.get()
        EntryPass = e2.get()

        import tkinter as tk

        if len(EntryUser)==0 or len(EntryPass)==0:
            tk.Label(master, text="Ensure that both fields are filled",font=TFont).grid(row=8,column=1)
            return None

        import mysql.connector as sql

        q="select * from Accdetails where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)                                                               
                                                                                                                                                
        data = cursor.fetchall()
        
        if data:
            
            Mainscreen()

        else:
            tk.Label(master, text="Incorrect username or password",font=TFont).grid(row=8,column=1)

    def History():

        global HisWin

        import mysql.connector as sql
        import tkinter as tk
        
        HisWin.deiconify()
        MainWin.withdraw()
        HisWin.state("zoomed")
        HisWin.grid_columnconfigure((0,1),weight=1)

        tk.Label(HisWin,text="Transaction history for Account",font=TFontbold,justify='center').grid(row=0,column=1,sticky='sw')
        
        q = "Select * from history where name='%s' limit 0,10"%(EntryUser)
        cursor.execute(q)

        HistoryMain = tk.Frame(HisWin)
        HistoryMain.grid(column=1,rowspan=3,sticky='w')

        HisFont = ('TkDefaultFont',16)
        
        tk.Label(HistoryMain,text="Acc ID",font=BFont).grid(row=0,column=0)
        tk.Label(HistoryMain,text="Name",font=BFont).grid(row=0,column=1)
        tk.Label(HistoryMain,text="Date",font=BFont).grid(row=0,column=2)
        tk.Label(HistoryMain,text="Credit",font=BFont).grid(row=0,column=3)
        tk.Label(HistoryMain,text="Debit",font=BFont).grid(row=0,column=4)
        tk.Label(HistoryMain,text="Balance",font=BFont).grid(row=0,column=5)
        i=1
        for record in cursor: 
            for j in range(len(record)):
                e = tk.Entry(HistoryMain, width=11,font=HisFont,borderwidth=0,justify='center')
                e.grid(row=i, column=j)
                if i%2==0:
                    e['bg']='#F0F0F0'
                e.insert(tk.END, record[j])
            i=i+1
            
        HisAccInfoCon = tk.Frame(HisWin,highlightbackground='black',highlightthickness=1)
        HisAccInfoCon.grid(row=1,column=0,padx=20)

        tk.Label(HisAccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(HisAccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(HisAccInfoCon,text=EntryUser,font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(HisAccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=2,pady=5,sticky='n')

        CurrBal = "select balance from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(CurrBal)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(HisAccInfoCon,textvariable=BalTxt,font=BFont,anchor='w')
        BalLab.grid(row=2,column=1,sticky='w',pady=5)
        
        HisButtonInfo = tk.Frame(HisWin,background='white',highlightbackground='black',highlightthickness=2)
        HisButtonInfo.grid(row=2,pady=30)

        tk.Button(HisWin, text="    Back ",command=BackButtonHis,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')          
        tk.Button(HisButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(HisButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(HisButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(HisButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(HisButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(HisButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(HisButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(HisButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(HisButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(HisButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(HisButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')

        tk.Button(HistoryMain,text="Show Graph",command=Graphscreen,font=HisFont).grid(row=12,columnspan=2,column=2,sticky='w',pady=10)

    def Graphscreen():

        import mysql.connector as sql
        
        q1 = "select TotalBalance from history where name='%s' limit 0,10"%(EntryUser)
        cursor.execute(q1)
        data = cursor.fetchall()
        
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

        Win7 = tk.Toplevel()

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
        
        global GetName,GetAmt

        EntryUser = e1.get()
        
        GetName = TransferName.get()
        GetAmt = int(TransferAmt.get())

        q="select balance from Accdetails where name='%s'"%(EntryUser)
        cursor.execute(q)
        data = cursor.fetchone()	
        FirstBal = sum(data)
        FirstUpBal = FirstBal-GetAmt

        DOT = datetime.date.today()
        AccNoQ = "select AccNo from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(AccNoQ)
        data = cursor.fetchone()
        AccNo = sum(data)
        
        try:
            q1="update Accdetails set balance={0} where name='{1}'".format(FirstUpBal,EntryUser)
            cursor.execute(q1)

            q2="select balance from Accdetails where name='%s'"%(GetName)
            cursor.execute(q2)
            data = cursor.fetchone()
            SecondBal = sum(data)
            SecondUpBal = SecondBal+GetAmt
        
            q3="update Accdetails set balance={0} where name='{1}'".format(SecondUpBal,GetName)
            cursor.execute(q3)	

            q4="insert into history(AccNo,Name,DateofTransaction,Credit,Debit,TotalBalance) values({0},'{1}','{2}',{3},{4},{5})".format(AccNo,EntryUser,DOT,0,GetAmt,FirstUpBal)
            cursor.execute(q4)

            q5="insert into history(AccNo,Name,DateofTransaction,Credit,Debit,TotalBalance) values({0},'{1}','{2}',{3},{4},{5})".format(AccNo,GetName,DOT,GetAmt,0,SecondUpBal)
            cursor.execute(q5)
            mycon.commit()

            tk.Label(TrnsMainInfo,text="Name of sender : ", font = BFont).grid(row=4)
            tk.Label(TrnsMainInfo,text=EntryUser, font = BFont,anchor='w').grid(row=4,column=1,sticky='w')
            tk.Label(TrnsMainInfo,text="Name of reciever : ", font = BFont).grid(row=5)
            tk.Label(TrnsMainInfo,text=GetName , font = BFont,anchor='w').grid(row=5,column=1,sticky='w')
            tk.Label(TrnsMainInfo,text="Amount sent : ", font = BFont).grid(row=6)
            tk.Label(TrnsMainInfo,text=GetAmt, font = BFont,anchor='w').grid(row=6,column=1,sticky='w')
            tk.Label(TrnsMainInfo,text="Balance left : ", font = BFont).grid(row=7)
            tk.Label(TrnsMainInfo,text=FirstUpBal, font = BFont,anchor='w').grid(row=7,column=1,sticky='w')
            
        except Exception as e:
            print(str(e))
            tk.Label(TrnsMainInfo,text="Some Error has occured.",font=BFont).grid(row=4)
        
    def Transferscreen():

        global TrnsWin,TransferName,TransferAmt,TrnsMainInfo
        
        MainWin.withdraw()
        TrnsWin.deiconify()
        TrnsWin.state("zoomed")
        
        TrnsWin.grid_columnconfigure((0,1),weight=1)

        tk.Label(TrnsWin, text="Transfer Screen                                 ",bg='pale green',fg='forest green', font=TFont,anchor='w').grid(row=0,column=1,sticky='ew')
        tk.Label(TrnsWin, text="Transfer your cash here",bg = 'pale green',fg = 'forest green',font=TFont).grid(row=0,column=2,sticky='we')

        TrnsMainInfo = tk.Frame(TrnsWin)
        TrnsMainInfo.grid(row=2,column=1,sticky='n')
        
        tk.Label(TrnsWin, text="Logged in",bg = 'pale green',fg = 'forest green',font=BFont,anchor='nw').grid(row=1,column=1,sticky='n')
        tk.Label(TrnsMainInfo, text="Enter receiver name :   ", font=BFont,anchor='nw').grid(row=0,sticky='nw',pady=10)
        TransferName = tk.Entry(TrnsMainInfo, font = BFont)
        TransferName.grid(row=0,column=1,pady=10)
        tk.Label(TrnsMainInfo, text="Enter transfer amount :  ", font=BFont,anchor='nw').grid(row=1,sticky='nw',pady=10)
        TransferAmt = tk.Entry(TrnsMainInfo, font=BFont)
        TransferAmt.grid(row=1,column=1,pady=10)

        TrnsAccInfoCon = tk.Frame(TrnsWin,highlightbackground='black',highlightthickness=1)
        TrnsAccInfoCon.grid(row=1,column=0,padx=20)

        tk.Label(TrnsAccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(TrnsAccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(TrnsAccInfoCon,text=EntryUser,font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(TrnsAccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=2,pady=5,sticky='n')

        CurrBal = "select balance from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(CurrBal)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(TrnsAccInfoCon,textvariable=BalTxt,font=BFont,anchor='w')
        BalLab.grid(row=2,column=1,sticky='w',pady=5)

        TrnsButtonInfo = tk.Frame(TrnsWin,background='white',highlightbackground='black',highlightthickness=2)
        TrnsButtonInfo.grid(row=2,pady=30)

        tk.Button(TrnsWin, text="    Back ",command=BackButtonTransfer,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')    
        tk.Button(TrnsButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(TrnsButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(TrnsButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(TrnsButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(TrnsButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(TrnsButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(TrnsButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(TrnsButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(TrnsButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(TrnsButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(TrnsButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')

        tk.Button(TrnsMainInfo, text="Transfer amount", command=Transfer, font=BFont).grid(row=3,columnspan=2)        
        

    def Withdrawal():

        import tkinter as tk
        import mysql.connector as sql
        import datetime
        
        global WithInput
        
        WithInput = int(WithEntry.get())

        q="select balance from Accdetails where name='%s' and password='%s'"%(EntryUser,EntryPass)
        cursor.execute(q)
        data = cursor.fetchone()
        conv = sum(data)
        Balance = conv-WithInput

        DOT = datetime.date.today()
        AccNoQ = "select AccNo from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(AccNoQ)
        data = cursor.fetchone()
        AccNo = sum(data)
        
        try:
            q1="update Accdetails set balance={0} where name='{1}' and password='{2}'".format(Balance,EntryUser,EntryPass) 
            cursor.execute(q1)

            q2="insert into history(AccNo,Name,DateofTransaction,Credit,Debit,TotalBalance) values({0},'{1}','{2}',{3},{4},{5})".format(AccNo,EntryUser,DOT,0,WithInput,Balance)
            cursor.execute(q2)
            mycon.commit()
        
            BalTxt.set(Balance)
        
            tk.Label(WithMainInfo, text="Withdrawan amount is : ",font=BFont).grid(row=4)
            tk.Label(WithMainInfo, text=WithInput,font=BFont).grid(row=4,column=1)
            tk.Label(WithMainInfo, text="Total balance is : ",font=BFont).grid(row=5)
            tk.Label(WithMainInfo, text=Balance,font=BFont).grid(row=5,column=1)
            
        except Exception as e:
            print(str(e))
            tk.Label(WithMainInfo,text="Some Error has occured.",font=BFont).grid(row=4)


    def Withdrawalscreen():
        
        global WithWin,WithEntry,WithMainInfo
        
        WithWin.deiconify()
        MainWin.withdraw()
        WithWin.state("zoomed")

        WithWin.grid_columnconfigure((0,1),weight=1)

        tk.Label(WithWin, text="Withdraw Screen                                 ",bg='pale green',fg='forest green', font=TFont,anchor='w').grid(row=0,column=1,sticky='ew')
        tk.Label(WithWin, text="Withdraw your cash here",bg = 'pale green',fg = 'forest green',font=TFont).grid(row=0,column=2,sticky='we')

        WithMainInfo = tk.Frame(WithWin)
        WithMainInfo.grid(row=2,column=1,sticky='n')
        
        tk.Label(WithWin, text="Logged in",bg = 'pale green',fg = 'forest green',font=BFont,anchor='nw').grid(row=1,column=1,sticky='n')
        tk.Label(WithMainInfo, text="Enter withdrawal amount :  ", font=BFont,anchor='nw').grid(row=1,sticky='nw',pady=10)
        WithEntry = tk.Entry(WithMainInfo, font=BFont)
        WithEntry.grid(row=1,column=1,pady=10)

        WithAccInfoCon = tk.Frame(WithWin,highlightbackground='black',highlightthickness=1)
        WithAccInfoCon.grid(row=1,column=0,padx=20)

        tk.Label(WithAccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(WithAccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(WithAccInfoCon,text=EntryUser,font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(WithAccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=2,pady=5,sticky='n')

        CurrBal = "select balance from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(CurrBal)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(WithAccInfoCon,textvariable=BalTxt,font=BFont,anchor='w')
        BalLab.grid(row=2,column=1,sticky='w',pady=5)

        WithButtonInfo = tk.Frame(WithWin,background='white',highlightbackground='black',highlightthickness=2)
        WithButtonInfo.grid(row=2,pady=30)

        tk.Button(WithWin, text="    Back ",command=BackButtonWith,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')    
        tk.Button(WithButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(WithButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(WithButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(WithButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(WithButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(WithButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(WithButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(WithButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(WithButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(WithButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(WithButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')

        tk.Button(WithMainInfo, text="Withdraw amount", command=Withdrawal, font=BFont).grid(row=3,columnspan=2)
        

        
    def AccountDetails():

        MainWin.withdraw()
        AccWin.deiconify()
        AccWin.state("zoomed")

        global EntryUser,EntryPass    
        EntryUser = e1.get()
        EntryPass = e2.get()

        def BackButtonAcc():

            AccWin.withdraw()
            MainWin.deiconify()
            MainWin.state("zoomed")

        def ChangeInfo():

            import tkinter as tk
            import mysql.connector as sql

            UserAccGet = UserAccName.get()
            PassAccGet = PassAccName.get()

            ChangeInfoQ = "update Accdetails set name='{0}',password='{1}' where name='{2}' and password='{3}'".format(UserAccGet,PassAccGet,EntryUser,EntryPass)
            cursor.execute(ChangeInfoQ)
            mycon.commit()

            tk.Label(AccWin,text = "Account has been updated.").grid(row=4)

        AccInfoCon = tk.Frame(AccWin,highlightbackground='black',highlightthickness=1)
        AccInfoCon.grid(row=1,column=0,padx=20)

        tk.Label(AccInfoCon,text=" Account Summary",font=BFont,anchor='n').grid(row=0,pady=5,sticky='n')
        tk.Label(AccInfoCon, text="  Account Name     : ",font=BFont,anchor='n').grid(row=1,pady=5,sticky='n')
        tk.Label(AccInfoCon,text=EntryUser,font=BFont,anchor='w').grid(row=1,column=1,pady=5,sticky='n')
        tk.Label(AccInfoCon, text=" Account balance  :",font=BFont,anchor='n').grid(row=2,pady=5,sticky='n')

        CurrBal = "select balance from Accdetails where name='{0}'".format(EntryUser)
        cursor.execute(CurrBal)
        Currdata = cursor.fetchone()

        BalTxt.set(Currdata)
        BalLab = tk.Label(AccInfoCon,textvariable=BalTxt,font=BFont,anchor='w')
        BalLab.grid(row=2,column=1,sticky='w',pady=5)

        AccWinInfo = tk.Frame(AccWin)
        AccWinInfo.grid(row=2,column=1,sticky='n')
            
        tk.Label(AccWin,text = "Account settings",font=TFont).grid(row=0,column=1)
        tk.Label(AccWinInfo,text = "Change current password.",font=TFont).grid(row=1,columnspan=2,sticky='we',pady=15)

        AccButtonInfo = tk.Frame(AccWin,background='white',highlightbackground='black',highlightthickness=2)
        AccButtonInfo.grid(row=2,column=0,pady=30)

        tk.Button(AccWin, text="    Back ",command=BackButtonAcc,image=TkBackImage,compound = 'left',font=TFont,anchor='w',bg='black',fg='white').grid(row=0,column=0,ipadx=30,pady=10,sticky='w')    
        tk.Button(AccButtonInfo, text="   Account Details  ",command=AccountDetails,font=BigFont,bg='white',borderwidth=0,image=TkAccImage,compound='left').grid(row=2,column=0,padx=0,sticky='w')
        ttk.Separator(AccButtonInfo,orient='horizontal').grid(row=3,sticky='ew')
        tk.Button(AccButtonInfo, text="   Deposit Money   ",command=Depositscreen,font=BigFont,bg='white',borderwidth=0,image=TkDepImage,compound='left').grid(row=4,column=0,sticky='w')
        ttk.Separator(AccButtonInfo,orient='horizontal').grid(row=5,sticky='ew')
        tk.Button(AccButtonInfo, text="   Withdraw Money",command=Withdrawalscreen,font=BigFont,bg='white',borderwidth=0,image=TkWithImage,compound='left').grid(row=6,column=0,sticky='w')
        ttk.Separator(AccButtonInfo,orient='horizontal').grid(row=7,sticky='ew')
        tk.Button(AccButtonInfo, text="   Transfer Money  ",command=Transferscreen,font=BigFont,bg='white',borderwidth=0,image=TkTrnsImage,compound='left').grid(row=8,column=0,sticky='w')
        ttk.Separator(AccButtonInfo,orient='horizontal').grid(row=9,sticky='ew')
        tk.Button(AccButtonInfo, text="   Transaction History  ",command=History,font=BigFont,bg='white',borderwidth=0,image=TkHistoryImage,compound='left').grid(row=10,column=0,sticky='w')
        ttk.Separator(AccButtonInfo,orient='horizontal').grid(row=11,sticky='ew')
        tk.Button(AccButtonInfo, text="   Developers Options  ",command=DevelopmentOptions,font=BigFont,bg='white',borderwidth=0, image=TkSetImage,compound='left').grid(row=12,column=0,sticky='w')
        
        tk.Label(AccWinInfo,text = "    Your username is :  ",font=TFont).grid(row=2,sticky='e',pady=5)
        UserAccName = tk.Entry(AccWinInfo,font=TFont)
        UserAccName.grid(row=2,column=1,pady=5)
        UserAccName.insert(tk.END,EntryUser)
        
        tk.Label(AccWinInfo,text = "    Your password is :  ",font=TFont).grid(row=3,sticky='e',pady=5)
        PassAccName = tk.Entry(AccWinInfo,font=TFont)
        PassAccName.grid(row=3,column=1,pady=5)
        PassAccName.insert(tk.END,EntryPass)
        
        tk.Button(AccWinInfo,text = "Change Info",command = ChangeInfo,font=TFont).grid(row=4,columnspan=2,pady=5)
        
                  
    search()
            
def DevelopmentOptions():

    def BackButtonDev():

        DevWin.withdraw()
        MainWin.deiconify()
        MainWin.state("zoomed")

    def CreateTable():
        
        import mysql.connector as sql

        AccCheck = "show tables like 'Accdetails'"
        cursor.execute(AccCheck)
        Accresult = cursor.fetchone()
        if Accresult:
            
            tk.Label(DevWin,text="Account details table already exists",font=BFont).grid(row=4,column=1)
      
        else:

            CreateAcc = "create table Accdetails(AccNo int NOT NULL AUTO_INCREMENT PRIMARY KEY,name char(30),password char(30),balance int unsigned check (balance > -1))"
            cursor.execute(CreateAcc)
            mycon.commit()

            DummyAcc = "insert into Accdetails values(10001,'Dummy','pass',0)"
            cursor.execute(DummyAcc)
            mycon.commit()

        HisCheck = "show tables like 'History'"
        cursor.execute(HisCheck)
        Hisresult = cursor.fetchone()

        if Hisresult:

            tk.Label(DevWin,text="History table already exists",font=BFont).grid(row=5,column=1)

        else:

            CreateHis = "create table history(AccNo int NOT NULL,name char(30),DateofTransaction date,Credit int unsigned check (Credit > -1),Debit int unsigned check (Debit > -1),TotalBalance int unsigned check (TotalBalance > -1))"
            cursor.execute(CreateHis)
            mycon.commit()

    def DeleteTableScreen():

        global DelWin,TableNames,Values

        DevWin.withdraw()
        DelWin=tk.Toplevel()
        DelWin.state("zoomed")

        import mysql.connector as sql

        Values = []

        def BackButtonDel():

            DelWin.withdraw()
            DevWin.deiconify()

        def DeleteTable():

            import mysql.connector as sql

            global DelWin,TableNames,Values

            GetName = TableNames.get()
            Delquery = "delete from Accdetails where name = '{0}'".format(GetName)
            cursor.execute(Delquery)
            mycon.commit()
        
            TableNames.set('')
            tk.Label(DelWin,text = "The account deleted is : ").grid(row=3)
            tk.Label(DelWin,text = GetName).grid(row=3,column=1)
        
        def UpdateValue():

            global Values

            import mysql.connector as sql
            
            SelectAcc = "select name from Accdetails"
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
        ModWin = tk.Toplevel()
        ModWin.state("zoomed")

        import mysql.connector as sql

        ModValues = []

        def BackButtonMod():

            ModWin.withdraw()
            DevWin.deiconify()

        def GetValue():

            global ModValues

            import mysql.connector as sql
            mycon = sql.connect(host="localhost",user="User",passwd="Rootpassword123",database="test")
            cursor=mycon.cursor()
            
            SelectQ = "select name from Accdetails"
            cursor.execute(SelectQ)
            AccList = cursor.fetchall()
            ModValues = []
            for i in AccList:
                ModValues.append(i)

            TableList['values'] = ModValues

        def Modify():

            import mysql.connector as sql

            TableUser = TableList.get()
            ModAmt = ModVal.get()
            
            AmountQ = "update Accdetails set balance={0} where name='{1}'".format(ModAmt,TableUser)
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
    DevWin.deiconify()
    DevWin.state("zoomed")
    DevWin.grid_columnconfigure((0,1),weight=1)

    tk.Label(DevWin, text="Development options are provided here.                     ",font=TFont).grid(row=0,column=1,sticky='w')

    tk.Button(DevWin, text="     Back ",command=BackButtonDev,image=TkBackImage,compound='left',font=TFont,bg='black',fg='white',anchor='w').grid(row=0,column=0,ipadx=25,pady=10,sticky='w')
    tk.Button(DevWin, text="Create necessary tables",command=CreateTable,font=TFont).grid(row=1,column=1,sticky='w')
    tk.Button(DevWin, text="Delete Tables",command=DeleteTableScreen,font=TFont).grid(row=2,column=0,sticky='e')
    tk.Button(DevWin, text="Modify Value",command=ModifyAmount,font=TFont).grid(row=2,column=1,sticky='w')

def signup():
    
    def register():
        
       global a,b
       
       a = UserName.get()
       b = PassWord.get()
       
       Endresult = tk.Label(SignWin, text="",font=TFont)
       Endresult.grid(row=7,column=1)

       if len(a)==0 or len(b)==0:
           Endresult['text'] = 'Ensure fields are filled'
           return None
       
       c="insert into Accdetails(name,password,balance) values('{0}','{1}',{2})".format(a,b,0)
       
       consearch = "select name,password from Accdetails where name = '{0}'".format(a)
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
        SignWin.withdraw()

    def ClearUserName(*args):

        UserName.delete(0,tk.END)
        UserName.unbind("<Button-1>")

    def ClearPassWord(*args):

        PassWord.delete(0,tk.END)
        PassWord.unbind("<Button-1>")
    
    global a,b,TkUserImage,TkPassImage	
    import tkinter as tk
    import mysql.connector as sql
    from PIL import Image,ImageTk
    
    master.withdraw()
    SignWin.deiconify()
    SignWin.state("zoomed")
    print("New window opened")

    SignWin.grid_columnconfigure((0,1,2), weight=1)

    UserImage = Image.open("signup.png")
    UserImage = UserImage.resize((50,30),Image.ANTIALIAS)
    TkUserImage = ImageTk.PhotoImage(UserImage)

    PassImage = Image.open("password.png")
    PassImage = PassImage.resize((50,30),Image.ANTIALIAS)
    TkPassImage = ImageTk.PhotoImage(PassImage)
    
    tk.Label(SignWin, text="Create account",font=TFont).grid(row=1, column=1,pady=20)
    
    UserName = tk.Entry(SignWin,font=TFont,width=20)
    PassWord = tk.Entry(SignWin,font=TFont,width=20, show='*')

    tk.Label(SignWin,text = "Username",image=TkUserImage,compound=tk.LEFT,font=TFont).grid(row=2,column=1,padx=20)
    tk.Label(SignWin,text = "Password",font=TFont,image=TkPassImage,compound=tk.LEFT).grid(row=4,column=1)

    UserName.insert(tk.END,"Username here")
    PassWord.insert(tk.END,"Password here")
    
    UserName.grid(row=3, column=1,pady=20)
    PassWord.grid(row=5, column=1,pady=20)

    UserName.bind("<Button-1>",ClearUserName)
    PassWord.bind("<Button-1>",ClearPassWord)

    SignButtonCon = tk.Frame(SignWin)
    SignButtonCon.grid(row=6,column=1,pady=20)
    
    tk.Button(SignButtonCon,text="Register",command=register,font=TFont).grid(row=0,column=1)
    tk.Button(SignButtonCon,text="Back",command=Back,font=TFont).grid(row=0,column=0)

def Showpassword():

    if BoxState.get()==0:
        e2['show']="*"
    else:
        e2['show']=""

def ClearE1(*args):

    e1.delete(0,tk.END)
    e1.unbind("<Button-1>")

def ClearE2(*args):

    e2.delete(0,tk.END)
    e2.unbind("<Button-1>")
    
master=tk.Tk()
MainWin = tk.Toplevel()
SignWin = tk.Toplevel()
DepWin = tk.Toplevel()
WithWin = tk.Toplevel()
TrnsWin = tk.Toplevel()
HisWin = tk.Toplevel()
AccWin = tk.Toplevel()
DevWin = tk.Toplevel()

MainWin.withdraw()
SignWin.withdraw()
DepWin.withdraw()
WithWin.withdraw()
TrnsWin.withdraw()
HisWin.withdraw()
AccWin.withdraw()
DevWin.withdraw()

Child = master.winfo_children()
Windows = []
for i in Child:
    if "!toplevel" in str(Child):
        Windows.append(i)

print(Windows)

def ChkWinState():
    for i in Windows:
        if i.state()=='withdrawn':
            print("Window is withdrawn")
        else:
            print("Window is visible")

def CloseWin():
    for i in Windows:
        if i.state()!='withdrawn':
            i.withdraw()

def Quit():
    mycon.close()
    master.destroy()

w, h = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (w, h))

master.grid_columnconfigure((0,1,2), weight=1)

BalTxt = tk.StringVar() #Account balance, used in multiple functions

TFont = ('TkDefaultFont',20) # Changes font
TFontbold = ('TkDefaultFont bold',20)
BFont = ('TkDefaultFont',18)
TxtFont = ('TkDefaultFont',16)
BigFont = ('TkDefaultFont',22)

BackImage = Image.open("back.jpg")
BackImage = BackImage.resize((60,40),Image.ANTIALIAS)
TkBackImage = ImageTk.PhotoImage(BackImage)

AccImage = Image.open("accdetails.png")
AccImage = AccImage.resize((60,40),Image.ANTIALIAS)
TkAccImage = ImageTk.PhotoImage(AccImage)

DepImage = Image.open("deposit.png")
DepImage = DepImage.resize((60,40),Image.ANTIALIAS)
TkDepImage = ImageTk.PhotoImage(DepImage)

WithImage = Image.open("withdraw.png")
WithImage = WithImage.resize((60,40),Image.ANTIALIAS)
TkWithImage = ImageTk.PhotoImage(WithImage)

TrnsImage = Image.open("transfer.png")
TrnsImage = TrnsImage.resize((60,40),Image.ANTIALIAS)
TkTrnsImage = ImageTk.PhotoImage(TrnsImage)

HistoryImage = Image.open("historyy.png")
HistoryImage = HistoryImage.resize((60,40),Image.ANTIALIAS)
TkHistoryImage = ImageTk.PhotoImage(HistoryImage)

SetImage = Image.open("settings.png")
SetImage = SetImage.resize((60,40),Image.ANTIALIAS)
TkSetImage = ImageTk.PhotoImage(SetImage)

LoginImage = Image.open("bank.png")
LoginImage = LoginImage.resize((100,50),Image.ANTIALIAS)
tkLogImage = ImageTk.PhotoImage(LoginImage)

tk.Label(master,pady=1,image=tkLogImage).grid(row=0,column=1)

L1 = tk.Label(master, text="iBanking",font=TFontbold,pady=20).grid(row=1,column=1)
    
e1 = tk.Entry(master,font=TFont)
e2 = tk.Entry(master,show='*',font=TFont)

e1.insert(tk.END,'Username')
e2.insert(tk.END,'Password')
    
e1.grid(row=2,column=1,pady=10)
e2.grid(row=4,column=1,pady=10)

BindUser = e1.bind("<Button-1>",ClearE1)
BindPass = e2.bind("<Button-1>",ClearE2)

BoxState = IntVar()
Showpass = tk.Checkbutton(master,text="Show password",variable=BoxState,command=Showpassword,font=TFont)
Showpass.grid(row=5,column=1,pady=20)

buttonContainer = tk.Frame(master)
buttonContainer.grid(row = 7,column = 1)

tk.Button(buttonContainer,text="Quit",command=Quit,font=TFont,anchor='w',padx=20).grid(row=0,column=0,pady=20)
tk.Button(buttonContainer,text="Login",command=Login,font=TFont,anchor='e',padx=20).grid(row=0,column=1,pady=20)
tk.Button(master,text="Create account",command=signup,font=TFont,borderwidth=0).grid(row=6,column=1,pady=1)
tk.Button(master,text="Dev Options",command=DevelopmentOptions,font=TFont,height=1,anchor='e')

master.mainloop()
