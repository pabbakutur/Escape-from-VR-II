import sys

class Bord1():
    spurningar = [
    {"spurning": "Svar 3?","svar": [ "1" , "2" , "3" , "4"],
    "rétt": "3"} ,
    {"spurning": "d/dx(1/2Sin(x^2)=?)",
    "svar":["cos(x)" , "cos(x^2)" , "xcos(x^2)" , "xcos(x)"],
    "rétt": "1"} ,
    {"spurning": "Svar 2?",
     "svar": [ "1" , "2" , "3" , "4"],
     "rétt": "2"},]

    def __init__(self):
        pass

    def byrja(self):
        pass

        print("\n")
        print("Spurningaleikur! \n")
        print("Svaraðu 2 spurningum rétt til að vinna\n")
        print("Þú hefur 3 tilraunir\n")
        print("Menu\n"
        "1. Byrja leik\n"
        "2. Loka leik\n")
        val = int(input("Veldu möguleika: "))
        print("")
        while int(val) not in range(1, 3):
            val = input("Veldu 1 eða 2: ")
        if val == 1:
            spila(spurningar)
        elif val == 2:
            sys.exit()

import random
def spila(spurningar):
    print("\n")
    score = 0
    total = 0
    random.shuffle(spurningar)
    for spurning in spurningar:
        print("Veldu 1, 2, 3 eða 4")
        print(spurning["spurning"])
        for i, val in enumerate(spurning["svar"]):
            print(str(i + 1) + ". " + val)
        answer = input("Veldu svar: ")
        while int(answer)-1 not in range(len(spurning["svar"])):
            print("\nÞetta er ekki svarmöguleiki, reyndu aftur. \n")
            answer = input("\nVeldu svar: ")
        if answer == spurning["rétt"]:
            score += 1
            total += 1
            print("\nÞað er rétt.\n")
        else:
            print("\nÞað er rangt. \n")
            total +=1
        print("Stigastaða: ", score, "af", total, "\n")
        if score - total == -2:
            print("Þú tapaðir")
            break
        elif score == 2:
            print("Þú vannst")
            break
    print("Þú varst með", score, "rétt af", total ,"\n")
    exit


main()
