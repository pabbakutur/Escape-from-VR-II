import sys
from time import sleep
import time
import random

class Bord1():
    def __init__(self):
        self.score= 0
        self.total= 0
        self.spurningar = [
    {"spurning": "4x^3cos(x^4) dx = ?",
    "svar": [ "1/4cos(x^4)" , "cos(x^4) + C" , "sin(x^4) + C" , "16x^4sin(x^4) + C"],
    "rétt": "3"} ,
    {"spurning": "d/dx(1/2Sin(x^2) = ?)",
    "svar":["cos(x)" , "cos(x^2)" , "xcos(x^2)" , "xcos(x)"],
    "rétt": "1"} ,
    {"spurning": "d/dx tan(x) = ?",
     "svar": [ "sec(x)" , "2sec(x^2)" , "1/2sec(x)" , "sec^2(x)"],
     "rétt": "4"},]

    def velja(self):
        x=input("Veldu svar: ")
        return x

    def byrja(self):
        print('') ; sleep(0.1)
        print('') ; sleep(0.1)
        print('') ; sleep(0.1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(0.1)
        print('$$   HEIMAVINNAN   $$') ; sleep(0.1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(0.1)
        print('') ; sleep(0.1)
        print('') ; sleep(0.1)
        print('') ; sleep(0.1)
        string = "Lexi situr á lesstofunni að leggja lokahönd á heimavinnuna sína.\nHann hefur aldrei verið sterkur að heilda eða diffra, þú þarft að hjálpa honum.\nÞú færð 3 tilraunir til að svara 2 spurningum réttum."
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.010)
        print('') ; sleep(0.1)
        print('') ; sleep(0.1)
        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                break

    def spila(self, spurningar):
        print("\n")
        random.shuffle(spurningar)
        while True:
            for spurning in spurningar:
                print("Veldu 1, 2, 3 eða 4")
                print(spurning["spurning"])
                for i, val in enumerate(spurning["svar"]):
                    print(str(i + 1) + ". " + val)
                answer= self.velja()
                if answer == spurning["rétt"]:
                    self.score = self.score + 1
                    self.total = self.total + 1
                    print("\nÞað er rétt.\n")
                elif answer == "Break":
                    sys.exit()
                elif answer == "1":
                    print("\nÞað er rangt. \n")
                    self.total +=1
                elif answer == "2":
                    print("\nÞað er rangt. \n")
                    self.total +=1
                elif answer == "3":
                    print("\nÞað er rangt. \n")
                    self.total +=1
                elif answer == "4":
                    print("\nÞað er rangt. \n")
                    self.total +=1
                else:
                    print("Þetta er ekki valmöguleiki, reyndu aftur")
                print("Stigastaða: ", self.score, "af", self.total, "\n")
                if self.score - self.total == -2:
                    print("Þú tapaðir og þarft að byrja aftur.")
                    self.score=0
                    self.total=0
                    return -1
                elif self.score == 2:
                    print("Þú vannst")
                    return 1
                    #láta fara á næsta borð
                else:
                    pass
                ###########

        print("Þú varst með", self.score, "rétt af", self.total ,"\n")
    

    def main(self):
        B1=Bord1()
        B1.byrja()

    def keyra(self):
        self.byrja()
        return self.spila(self.spurningar)

#if __name__ == '__main__':
#    main()
