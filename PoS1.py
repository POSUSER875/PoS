import os
a = 1
comm = 0
while a == 1 and comm != ("help")and("shutdown")and("posver"):
    comm = input ("command enter>>")
    while comm == "help":
        print("help, shutdown, posver")
        comm = 0
    while comm == "shutdown":
        print ("shutting down pc")
        os.system("shutdown -s")
        comm = 0
    while comm == "posver":
        print ("POS 1.0")
        comm = 0
        
            
        
