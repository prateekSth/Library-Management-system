import Listsplit
import dt
def returnBook():
    name = input("Enter the name of borrower: ")
    text = "Borrow:" +name+ ".txt"
    try:
        with open(text,"r") as l:
            lines=l.readlines()
            lines=[text.strip("$") for text in lines]
    
        with open(text,"r") as l:
            value = l.read()
            print(value)
    except:
        print("The borrower name is not available, Please input another name.")
        returnBook()

    ret = "Return: "+name+".txt"
    with open(ret,"w")as l:
        l.write("                Library Management System \n")
        l.write("                    Returned By: "+ name+"\n")
        l.write("       Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        l.write("S.N.\t\t\t\tBookName\t\t\t\tCost\n")


    totalamt = 0.0
    for i in range(3):
        if Listsplit.bookName[i] in value:
            with open(ret,"a") as l:
                l.write(str(i+1)+"\t"+Listsplit.bookName[i]+"\t$"+Listsplit.cost[i]+"\n")
                Listsplit.quantity[i]=int(Listsplit.quantity[i])+1
            totalamt += float(Listsplit.cost[i])
            
    print("\t\t\t\t\t Total Amount"+"$"+str(totalamt))
    print("Did the book return date expired? ")
    opn = input("Press Y for Yes and N for No: ")
    if(opn.upper()=="Y"):
        print("By how many days was the book returned was late? ")
        day = int(input())
        fineamt = 2*day
        with open(ret,"a")as l:
            l.write("\t\t\t Fine amount: $"+ str(fineamt)+"\n")
        totalamt = totalamt + fineamt
    print("Total amount: "+ "$"+str(totalamt))
    with open(ret,"a")as l:
        l.write("\t\t\t\t\tTotal amount: $"+ str(totalamt))
    print("The book is returned")
    print ("   ----------   ")
    print("")
    print("")
    with open("Stock.txt","w") as l:
            for i in range(3):
                l.write(Listsplit.bookName[i]+","+Listsplit.authorName[i]+","+str(Listsplit.quantity[i])+","+"$"+Listsplit.cost[i]+"\n")
