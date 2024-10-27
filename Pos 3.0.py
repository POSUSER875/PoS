import os
import datetime
import time
import sys
a = 1
b = 1
m = 1
notepad = "note"
print("-------------------------bootloader 1.0------------------------")
print("1.Boot OS ")
print ("2.Shutdown")
print ("3.Boot from Kernel")
boot = input("enter a number:")
if boot == "2":
    os.system("shutdown -s")
if boot == "3":
    b = 2
    m = 0
    print ("booting from kernel...")
    time.sleep(2)
    print ("loading os")
while b == 2 and m != ("help")and("krnlver")and("Ktest"):
    m = input ("kernelprog:")
    while m == "help":
        print ("help, krnlver, Ktest")
        m = 0
    while m == "krnlver":
         print ("Kernel 1.2 rc-1")
         print ("now you started from kernel")
         m = 0
    while m == "Ktest":
          print ("kernel is testing...")
          time.sleep(3)
          print ("Kernel is stable to use!")
          m = 0
if boot == "1":
       print ("starting up")
       time.sleep(2)
       print ("...............welcome....................")
       a = 2
       comm = 0
while a == 2 and comm != ("help")and("shutdown")and("posver")and("calc")and("time")and("notepad")and("begin"):
    comm = input ("command enter>>")
    while comm == "help":
        print("help, calc, shutdown, posver, time, notepad, begin")
        comm = 0
    while comm == "shutdown":
        print ("shutting down pc")
        os.system("shutdown -s")
        comm = 0
    while comm == "posver":
        print ("POS 3.0")
        print ("Kernel 1.2 rc-1")
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
    while comm == "begin":
        print ("|---------|     |---------|         |------------")
        print ("|_____|      |        |          |")
        print ("|                |        |          -----------|")
        print ("|                |_____|          -----------|")
        print ("добро пожаловать в pos 3.0 это инструкция для начинающих. Напишите help чтобы увидеть все доступные команды. Напишите time чтобы увидеть текущее время. Напишите calc чтобы запустить калькулятор. Напишите posver для просмотра версии pos. Напишите notepad для открытия блокнота. Напишите begin для запуска этой инструкции. Хорошего пользования команда PoS.")
        comm = 0
    while comm == "notepad":
        print (notepad)
        print ("редактировать?")
        nselect = input ("Y/N")
        if nselect == "N" or "n":
            comm = 0
        if nselect == "Y" or "y":
            print ("ВНИМАНИЕ! после перезагрузки данные стираются рекомендуется их.скопировать куда нибудь!")
            notepad = input ("введите заметку:")
            print (notepad)