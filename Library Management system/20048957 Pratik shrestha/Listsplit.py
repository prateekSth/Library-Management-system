# defining method
def listsplit():
    # defining global variable
    global bookName
    global authorName
    global quantity
    global cost

    # creating list of variables
    bookName=[]
    authorName=[]
    quantity=[]
    cost=[]
    with open("Stock.txt","r") as l: # open stock.txt file
        line1=l.readlines()
        line1=[line.strip('\n') for line in line1] # strip \n from list 
        for i in range(len(line1)): 
            index=0
            for c in line1[i].split(','):
                if(index==0): # condition 1
                    bookName.append(c)
                elif(index==1): # condition 2
                    authorName.append(c)
                elif(index==2): # condition 3
                    quantity.append(c)
                elif(index==3): # conditon 4
                    cost.append(c.strip("$")) # strip $ from cost
                index+=1
