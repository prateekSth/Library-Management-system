# import file 
import Return
import Listsplit
import Borrow


# creating start method
class start():
    while(True):
        print("      Welcome to the Islington library management system     ")
        print("-------------------------------------------------------------------------")
        print("Press 1. To Display books: ")
        print("Press 2. To Borrow book: ")
        print("Press 3. To return book: ")
        print("Press 4. To exit: ")
        # exception handling 
        try:
            c = int(input("Select a number from 1-4: "))
            if(c==1):
                with open("stock.txt","r") as l: # open stock text file and read
                    lines=l.read()
                    print(lines)
                    print ()
           #condition check
            elif(c==2):
                Listsplit.listsplit()
                Borrow.borrowBook()
            elif(c==3):
                Listsplit.listsplit()
                Return.returnBook()
            elif(c==4):
                print("Thank you for visiting Islington library. Have a good day.")
                break
            else:
                print("Please enter a valid number from 1-4")
                print("")
                print("")
        except ValueError: # value error handling
            print("Please input suggested number only.")
            print("-------------------------------------------------------------------------")

