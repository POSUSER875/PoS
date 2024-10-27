import os
import datetime
import time
a = 1
print("-------------------------bootloader 1.0------------------------")
print("1.Boot OS ")
print ("2.Shutdown")
boot = input("enter a number:")
if boot == "2":
    os.system("shutdown -s")
if boot == "1":
        print ("starting up...")
        time.sleep(2)
        print ("...............welcome....................")
        a = 2
        comm = 0
while a == 2 and comm != ("help")and("shutdown")and("posver"):
    comm = input ("command enter>>")
    while comm == "help":
        print("help, calc, shutdown, posver, time")
        comm = 0
    while comm == "shutdown":
        print ("shutting down pc")
        os.system("shutdown -s")
        comm = 0
    while comm == "posver":
        print ("POS 2.0")
        print ("Kernel 1.1 rc-2")
        comm = 0
    while comm == "time":
        now = datetime.datetime.now()
        print (str(now))
        comm = 0
    if comm == "calc":
            a = int (input("Первое число:"))
            b = int (input("Второе число:"))
            operator = input ("+-/*")
            if operator == "+":
                summa = a + b
                print (summa)
                a = 2
            if operator == "-":
                summa = a - b
                print (summa)
                a = 2
            if operator == "*":
                 summa = a * b
                 print (summa)
                 a = 2
            if operator == "/":
                 summa = a / b
                 print (summa)
                 a = 2
            
                
                
