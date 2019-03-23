import sys
from time import sleep
import time
import random

class Bord1():
    spurningar = [
    {"spurning": "4x^3cos(x^4) dx = ?",
    "svar": [ "1/4cos(x^4)" , "cos(x^4) + C" , "sin(x^4) + C" , "16x^4sin(x^4) + C"],
    "rétt": "3"} ,
    {"spurning": "d/dx(1/2Sin(x^2) = ?)",
    "svar":["cos(x)" , "cos(x^2)" , "xcos(x^2)" , "xcos(x)"],
    "rétt": "1"} ,
    {"spurning": "d/dx tan(x) = ?",
     "svar": [ "sec(x)" , "2sec(x^2)" , "1/2sec(x)" , "sec^2(x)"],
     "rétt": "4"},]

    def __init__(self):
        pass

    def byrja(self):
        print('') ; sleep(1)
        print('') ; sleep(1)
        print('') ; sleep(1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(1)
        print('$$   HEIMAVINNAN   $$') ; sleep(1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(1)
        print('') ; sleep(1)
        print('') ; sleep(1)
        print('') ; sleep(1)
        string = "Lexi situr á lesstofunni að leggja lokahönd á heimavinnuna sína.\nHann hefur aldrei verið sterkur að heilda eða diffra, þú þarft að hjálpa honum.\nÞú færð 3 tilraunir til að svara 2 spurningum réttum."
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.10)
        print('') ; sleep(0.5)
        print('') ; sleep(0.5)

        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                spila(Bord1.spurningar)

def velja():
    x=input("Veldu svar: ")
    return x

def spila(spurningar):
    print("\n")
    random.shuffle(spurningar)
    for spurning in spurningar:
        print("Veldu 1, 2, 3 eða 4")
        print(spurning["spurning"])
        for i, val in enumerate(spurning["svar"]):
            print(str(i + 1) + ". " + val)
        answer = velja()

        if answer == spurning["rétt"]:
            score += 1
            total += 1
            print("\nÞað er rétt.\n")
        elif answer == "1":
            print("\nÞað er rangt. \n")
            total +=1
        elif answer == "2":
            print("\nÞað er rangt. \n")
            total +=1
        elif answer == "3":
            print("\nÞað er rangt. \n")
            total +=1
        elif answer == "4":
            print("\nÞað er rangt. \n")
            total +=1
        else:
            print("Þetta er ekki valmöguleiki, reyndu aftur")
        print("Stigastaða: ", score, "af", total, "\n")
        if score - total == -2:
            print("Þú tapaðir")
            break
        elif score == 2:
            print("Þú vannst")
            break
        else:
            spila(spurningar)
    def stigastafla():
        self.score= 0
        self.total= 0
        ###########

    print("Þú varst með", score, "rétt af", total ,"\n")
    exit


    main()
