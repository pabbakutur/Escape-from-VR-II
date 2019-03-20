#Upphafsmynd
from time import sleep
import sys
import random

class upphafsmynd:
    def __init__(self):
        pass

#################################################
    def kynning(self):
        print('                 -------------------------') ; sleep(1)
        print('                 --- Escape from VR-II ---') ; sleep(1)
        print('                 -------------------------') ; sleep(1)
        print('') ; sleep(1)
        print('---------------------------------------------------------') ; sleep(0.5)
        print('-- Velkomin/nn í Escape from VR-II                     --') ; sleep(0.5)
        print('--                                                     --') ; sleep(0.5)
        print('-- Alexander Róbert Magnússon er nýbúinn að taka gott  --') ; sleep(0.5)
        print('-- session á lesstofunni í VR-II og ætlar að koma sér  --') ; sleep(0.5)
        print('-- heim. Áður en hann getur það þarf hann að leysa     --') ; sleep(0.5)
        print('-- nokkur verkefni.                                    --') ; sleep(0.5)
        print('---------------------------------------------------------') ; sleep(0.5)
        print('') ; sleep(0.5)
        print('') ; sleep(0.5)

        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                break
        self.bord1()

##########################################
    def bord1(self):
        print('') ; sleep(1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(1)
        print('$$   HEIMAVINNAN   $$') ; sleep(1)
        print('$$$$$$$$$$$$$$$$$$$$$') ; sleep(1)
        print('') ; sleep(0.5)
        spurningar = [
            {"spurning": "d/dx 1/2sin(x^2) = ?",
            "svar": [ "2cos(x^2)" , "1/2xcos(x^2)" , "xcos(x^2)" , "x^2cos(x^2)"],
            "rétt": "3"} ,
            {"spurning": "2xsin(x^2) dx = ?",
            "svar":["cos(x^2)" , "-cos(x)" , "1/2cos(x^2)" , "-cos(x^2)"],
            "rétt": "4"} ,
            {"spurning": "d/dx tan(x)?",
            "svar": [ "sec^2(x)" , "1/2sec(x)" , "sec(x^2)" , "sec(x)"],
            "rétt": "1"} ,
         ]
        print("Alexander þarf að svara þremur spurningum réttum")
        print("í þremur tilraunum")


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
            print("Rétt svör: ", score, "af", total, "\n")
            if score - total == -2:
                print("Alexander náði ekki að klára heimavinnuna.")
                break
            elif score == 2:
                print("Jæja þá er Lexi loksins búinn að læra heima")
                break



###############################################
    def bord2(self):
        print('kominn a bord 2')
#################################################
def main():
    leikur = upphafsmynd()
    leikur.kynning()


if __name__ == '__main__':
    main()
