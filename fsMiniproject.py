import tkinter as tk #window based application
import shelve #persistant data #shel-ve
top = tk.Tk() 
top.title("TELECOM PREPAID BILLING SYSTEM")
top.geometry("500x300")
top.configure(bg = "white")
global name,phNumber,location,planName,noOfDays,planCost,nameEntry,phNumberEntry,locationEntry

def register():
    registerWindow = tk.Toplevel()
    registerWindow.title("TELECOM PREPAID BILLING SYSTEM-REGISTRATION")
    registerWindow.geometry("550x650")
    registerWindow.configure(bg = "white")
    nameLabel = tk.Label(registerWindow,text = "Name:",bg = "white").grid(row = 0,column = 0)
    phNumberLabel = tk.Label(registerWindow,text = "Phone Number:",bg = "white").grid(row = 1,column = 0)
    locationLabel = tk.Label(registerWindow,text = "Location:",bg = "white").grid(row = 2,column = 0)
    planLabel = tk.Label(registerWindow,text = "Choose a plan to submit directly:",bg = "white").grid(row = 3,column = 0)
    nameEntry = tk.Entry(registerWindow,width = 40)
    nameEntry.grid(row = 0,column = 1)
    phNumberEntry = tk.Entry(registerWindow,width = 40)
    phNumberEntry.grid(row = 1,column = 1)
    locationEntry = tk.Entry(registerWindow,width = 40)
    locationEntry.grid(row = 2,column = 1)
    plan1Button = tk.Button(registerWindow ,text="Plan 1:Basic Plan-\nDescription: Unlimited Talktime,100 SMS per Day\n1GB per Day\nNumber of Days: 15 Days\nCost:Rs.199\n*Click to choose and submit*",bg = "#00CC44",fg = "white",padx = 20,pady=20,command = lambda: pack(registerWindow,nameEntry,phNumberEntry,locationEntry,1)).grid(row=4,column=1)
    plan2Button = tk.Button(registerWindow ,text="Plan 2:Standard Plan-\nDescription: Unlimited Talktime,100SMS per Day\n1.5GB per Day\nNumber of Days: 80 Days\nCost:Rs.449\n*Click to choose and submit*",bg = "#009933",fg = "white",padx = 20,pady=20,command = lambda: pack(registerWindow,nameEntry,phNumberEntry,locationEntry,2)).grid(row=6,column=1)
    plan3Button = tk.Button(registerWindow ,text="Plan 3:Half Yearly Plan-\nDescription: Unlimited Talktime,100SMS per Day\n2 GB per Day\nNumber of Days: 180 Days\nCost:Rs.999\n*Click to choose and submit*",bg = "#006622",fg = "white",padx = 20,pady=20,command = lambda: pack(registerWindow,nameEntry,phNumberEntry,locationEntry,3)).grid(row=8,column=1)
    plan4Button = tk.Button(registerWindow ,text="Plan 4:Yearly Plan-\nDescription: Unlimited Talktime,100SMS per Day\n3GB per Day\nNumber of Days: 360 Days\nCost:2499\n*Click to choose and submit*",bg = "#005511",fg = "white",padx = 20,pady=20,command = lambda: pack(registerWindow,nameEntry,phNumberEntry,locationEntry,4)).grid(row=10,column=1)
    
    registerWindow.mainloop()
def viewAll(adminWindow):
    dict = shelve.open("Customer_keys")
    viewAllWindow = tk.Toplevel()
    viewAllWindow.configure(bg = "green")
    headerLabel = tk.Label(viewAllWindow,text = "Name:",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 0)
    headerLabel = tk.Label(viewAllWindow,text = "Phone No.",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 1)
    headerLabel = tk.Label(viewAllWindow,text = "Location",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 2)
    headerLabel = tk.Label(viewAllWindow,text = "Plan Name.",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 3)
    headerLabel = tk.Label(viewAllWindow,text = "No. Of Days.",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 4)
    headerLabel = tk.Label(viewAllWindow,text = "Cost",bg = "green",fg = "white",padx = 5,pady = 5).grid(row = 0,column = 5)
    if len(dict) != 0:
        i = 3
        for key in dict.keys():
            record = dict[key]
            for j in range(6):
                recordsLabel = tk.Label(viewAllWindow,text = record[j],bg = "green",fg = "white",padx = 5,pady = 5).grid(row = i,column = j)
            i+=1
    else:
        recordsLabel = tk.Label(viewAllWindow,text = "No Records Exists",bg = "white",font = 50,padx = 5,pady = 5).grid(row = 3,column = 0)
    dict.close()
    viewAllWindow.mainloop()
def update():
    rec = ""
    fp = open("Customer_record.txt","w")
    dict = shelve.open("Customer_keys")
    for key in dict.keys():
        record = dict[key]
        rec = "|".join(record)
        fp.write(rec+"\n")
    dict.close()
    fp.close()
def modifyAndDelete(number,window):   
    dict = shelve.open("Customer_keys")
    if number in dict:
        del dict[number]
        update()
        register()
    else:
        errorLabel = tk.Label(window,text = "Number Does Not Exist\nTry Registering First!",font = 50).grid(row = 13,column = 0)
    dict.close()

def generateBill(plan_name,userWindow):
    generateBillWindow = tk.Toplevel()
    generateBillWindow.title("TELECOM PREPAID BILLING SYSTEM-BILL")
    generateBillWindow.geometry("350x150")
    generateBillWindow.configure(bg = "white")
    gstLevied = "18%"
    if plan_name == "Basic Plan":
        costWithoutGST = "Rs.168.64"
        amountPayable = "Rs.199.00"
    elif plan_name == "Standard Plan":
        costWithoutGST = "Rs.380.51"
        amountPayable = "Rs.449.00"
    elif plan_name == "Half Yearly Plan":
        costWithoutGST = "Rs.846.61"
        amountPayable = "Rs.999.00"
    elif plan_name == "Yearly Plan":
        costWithoutGST = "Rs.2117.80"
        amountPayable = "Rs.2499.00"
    costWithoutGSTLabel = tk.Label(generateBillWindow,text ="Cost Without GST="+costWithoutGST,bg = "green",fg = "white",padx = 5,pady=5,width = 30,font = 50).grid(row = 10,column = 0,sticky = "W")
    gstLeviedLabel = tk.Label(generateBillWindow,text ="GST(Updated Value)="+gstLevied,bg = "green",fg = "white",padx = 5,pady=5,width = 30,font = 50).grid(row = 11,column = 0,sticky = "W")
    amountPayableLabel = tk.Label(generateBillWindow,text ="Amount Payable="+amountPayable,bg = "green",fg = "white",padx = 5,pady=5,width = 30,font = 50).grid(row = 12,column = 0,sticky = "W")
def getData(phNumberEntry,window):
    dict = shelve.open("Customer_keys")
    number = str(int(phNumberEntry.get())%100000)
    if number in dict:
        record = dict[number]
        nameLabel = tk.Label(window,text = "Name:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 3,column = 0,sticky = "W")
        nameOutputLabel = tk.Label(window,text = record[0],bg = "white",font = 50,padx = 5,pady=5).grid(row = 3,column = 1,sticky = "W")
        phNumberLabel = tk.Label(window,text = "Phone Number:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 4,column = 0,sticky = "W")
        phNumberOutputLabel = tk.Label(window,text = record[1],bg = "white",font = 50,padx = 5,pady=5).grid(row = 4,column = 1,sticky = "W")
        locationLabel = tk.Label(window,text = "Location:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 5,column = 0,sticky = "W")
        locationOutputLabel = tk.Label(window,text = record[2],bg = "white",font = 50,padx = 5,pady=5).grid(row = 5,column = 1,sticky = "W")
        planLabel = tk.Label(window,text = "Your plan:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 6,column = 0,sticky = "W")
        planNameLabel = tk.Label(window,text = "Plan Name:"+record[3],bg = "white",font = 50,padx = 5,pady=5).grid(row = 6,column = 1,sticky = "W")
        planNoOfDaysLabel = tk.Label(window,text = "Number of Days:"+record[4],bg = "white",font = 50,padx = 5,pady=5,width = 15).grid(row = 7,column = 1,sticky = "W")
        planCostLabel = tk.Label(window,text = "Cost:Rs."+record[5],bg = "white",font = 50,padx = 5,pady=5).grid(row = 8,column = 1,sticky = "W")
        generateButton = tk.Button(window,text = "Generate the Bill",padx = 5,pady=5,fg = "white",bg = "green",command = lambda: generateBill(record[3],window)).grid(row = 9,column = 0,sticky = "N")
        modifyPlanButton = tk.Button(window,text = "Modify",bg = "green",fg = "white",padx = 5,pady=5,command = lambda: modifyAndDelete(number,window)).grid(row = 9,column = 1)
    else:
        errorLabel = tk.Label(window,text = "Number Does Not Exist\nTry Registering First!",bg = "white",font = 50).grid(row = 13,column = 0)
    dict.close()
def user():
    userWindow = tk.Toplevel()
    userWindow.title("TELECOM PREPAID BILLING SYSTEM-USER")
    userWindow.geometry("650x450")
    userWindow.configure(bg = "white")
    phNumberLabel = tk.Label(userWindow,text = "Enter your Registered Number:",bg = "white").grid(row = 0,column = 0)
    phNumberEntry = tk.Entry(userWindow,width = 20)
    phNumberEntry.grid(row = 0,column = 1)
    loginButton = tk.Button(userWindow,text = "Login",bg = "green",fg = "white",padx = 5,pady=5,command = lambda: getData(phNumberEntry,userWindow)).grid(row = 0,column = 2)
    
    userWindow.mainloop()
def admin():
    adminWindow = tk.Toplevel()
    adminWindow.title("TELECOM PREPAID BILLING SYSTEM-ADMIN MODE")
    adminWindow.geometry("800x600")
    adminWindow.configure(bg = "white")
    viewAllButton = tk.Button(adminWindow,text="View All the Records",padx = 15,pady = 10,width = 20,bg = "green",fg = "white",command = lambda:viewAll(adminWindow)).grid(sticky = "W",row = 0,column = 0)
    keyLabel = tk.Label(adminWindow,text = "Enter the key at which to modify the data:",bg = "white",padx = 5,pady=5).grid(row = 1,column = 0,sticky = "W")
    keyEntry = tk.Entry(adminWindow,width = 20)
    keyEntry.grid(row = 1,column = 1)
    modifyButton = tk.Button(adminWindow,text="Modify a Customer Record",padx = 15,pady = 10,width = 20, bg = "green",fg = "white",command = lambda:modifyAndDelete(str(keyEntry.get()),adminWindow)).grid(sticky = "W",row = 1,column = 2)
    phNumberLabel = tk.Label(adminWindow,text = "Enter the Ph.number of the Customer:",bg = "white",padx = 5,pady=5).grid(row = 2,column = 0,sticky = "W")
    phNumberEntry = tk.Entry(adminWindow,width = 20)
    phNumberEntry.grid(row = 2,column = 1)
    searchButton = tk.Button(adminWindow,text="Search for a Customer Record",padx = 15,pady = 10,width = 20,bg = "green",fg = "white",command = lambda:getData(phNumberEntry,adminWindow)).grid(sticky = "W",row = 2,column = 2)

    adminWindow.mainloop()
def pack(registerWindow,nameEntry,phNumberEntry,locationEntry,number):
    dict = shelve.open("Customer_keys")
    record = []
    if number == 1:
        planName = "Basic Plan"
        noOfDays = "15"
        planCost = "199.0"
    if number == 2:
        planName = "Standard Plan"
        noOfDays = 80
        planCost = 449.0
    if number == 3:
        planName = "Half Yearly Plan"
        noOfDays = 180
        planCost = 999.0
    if number == 4:
        planName = "Yearly Plan"
        noOfDays = 360
        planCost = 2499.0
    
    name = nameEntry.get()
    phNumber = phNumberEntry.get()
    location = locationEntry.get()
    if len(name)!=0 and len(location)!=0:
        if phNumber.isnumeric() and len(phNumber) == 10:
        
            record.append(planName)
            record.append(str(noOfDays))
            record.append(str(planCost))
            record.insert(0,name)
            record.insert(1,phNumber)
            record.insert(2,location)
            key = int(phNumber)%100000
            if str(key) not in dict:
                dict[str(key)] = record
                registerWindow.destroy()
                update()
            else:
                registerWindow.destroy()
                register()
        else:
            registerWindow.destroy()
            register()
    else:
        registerWindow.destroy()
        register()
    dict.close()
welcomeLabel = tk.Label(text = "Welcome to the Telecom Billing Portal",font = 50,bg = "green",fg = "white").pack()
descriptionLabel = tk.Label(text = "\nThe telecom billing portal was created \nto provide a easy and managable system \nTo store the User Details ,Choose a Suitable Plan ,Generate a Bill for the given number.\n\n",bg = "white").pack()
buttonFrame = tk.Frame().pack()
registerButton = tk.Button(buttonFrame,text="New User? Register Here",padx = 30,pady = 10,width = 50,bg = "green",fg = "white",command = register).pack(side = "top")
userButton = tk.Button(buttonFrame,text="Already a User? Click Here",padx = 30,pady = 10,width = 50, bg = "green",fg = "white",command = user).pack(side = "top")
adminButton = tk.Button(buttonFrame,text="Admin Mode",padx = 30,pady = 10,width = 50,bg = "green",fg = "white",command = admin).pack(side = "top")
top.mainloop()
