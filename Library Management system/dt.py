# defining get method for date
def getDate():
    import datetime
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date()) 
# defining get method for time
def getTime():
    import datetime
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
