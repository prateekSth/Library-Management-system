# import dt and listsplit file
import dt
import Listsplit

# creating borrowbook method to borrow book
def borrowBook():
    complete = False 
    while(True):
        firstName=input("Enter the first name of the borrower: ")
        if firstName.isalpha(): # isaplha method checks wheather the name is alphabhet or not.
            break
        print("Please input alphabet from A-Z")
    while(True):
        lastName = input("Enter the last name of the borrower: ")
        if lastName.isalpha():  # isaplha method checks wheather the name is alphabhet or not.
            break
        print("please input any alphabet from A-Z")
            
    text = "Borrow:" +firstName+" "+lastName+ ".txt" # creating text file to store borrow detail
    with open(text,"w") as l: # open text file to write
        l.write("               Islington Library Management System  \n")
        l.write("                 Borrowed By: "+ firstName+" "+lastName+"\n")
        l.write("       Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        l.write("S.N. \t\t Bookname \t\t Authorname \n" )
    print("     ---------------------   ")

    
    while complete == False:
        print("Please select a book given below: ")
        for i in range(len(Listsplit.bookName )):
            print("Enter", i, "to borrow book", Listsplit.bookName[i])
    
        try:   
            bo = int(input("Enter the book number: "))
            if(bo<0):
                print("Please enter the positive value.")
                print("")
                print("")
            else:
                try:
                    if(int(Listsplit.quantity[bo])>0):
                        print("The book is borrowed.")
                        print("     ---------------------   ")
                        with open(text,"a") as l:
                            l.write("1. \t\t "+ Listsplit.bookName[bo]+"\t\t  "+Listsplit.authorName[bo]+"\n")

                        Listsplit.quantity[bo]=int(Listsplit.quantity[bo])-1
                        with open("Stock.txt","w") as l:
                            for i in range(3):
                                l.write(Listsplit.bookName[i]+","+Listsplit.authorName[i]+","+str(Listsplit.quantity[i])+","+"$"+Listsplit.cost[i]+"\n")


                        # Code to borrow multiple books
                        loop=True
                        count=1
                        # loop for borrowing multiple book
                        while loop == True:
                            opt = str(input("Do you want to borrow more books?. Press y for yes and n for no.Instruction:You cannot borrow same book.  "))
                            if(opt.upper()=="Y"): # upper method return uppercase string from given string
                                count=count+1
                                print("     ---------------------   ")
                                print("Please select an option given below:") 
                                # for loop
                                for i in range(len(Listsplit.bookName)):
                                    print("Enter", i, "to borrow book", Listsplit.bookName[i])    
                                val = int(input("Enter the book number:")) # user input for book number
                                if (bo==val):
                                    print("Same book cannot be borrowed twice.")
                                elif(int(Listsplit.quantity[val])>0):
                                    print("The book is available  and borrowed.") # book is borrowed
                                    with open(text,"a") as l:
                                        l.write(str(count) +". \t\t"+ Listsplit.bookName[val]+"\t\t  "+Listsplit.authorName[val]+"\n") # storing borrowed book detail. 
                                        
                                    Listsplit.quantity[val]=int(Listsplit.quantity[val])-1 # decreasing quantity of book after borrowed
                                    with open("Stock.txt","w") as l:
                                        for i in range(3):
                                            l.write(Listsplit.bookName[i]+","+Listsplit.authorName[i]+","+str(Listsplit.quantity[i])+","+"$"+Listsplit.cost[i]+"\n")
                                            complete=False
                                else:
                                    loop=False
                                    break
                            elif (opt.upper()=="N"): # upper method return uppercase string from given string
                                print ("Thank you for borrowing books from us. Have a good day. ")
                                print("")
                                loop=False
                                complete=True
                            else:
                                print("Sorry! Invaid option.Please choose the given option only.")
                                print("")
                                print("")
                            
                    else:
                        print("The book is not available now. Thanks for visiting us.") # print if book is not available 
                        borrowBook()
                        complete=False
                except IndexError: # index error exception handling
                    print("")
                    print("Please choose given number only.")         
        except ValueError: # value error exception handling
            print("")
            print("Please choose the suggested number.")
            
