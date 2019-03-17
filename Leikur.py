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
            {"spurning": "Hvað er 5 + 5?",
            "svar": [ "0" , "5" , "10" , "15"],
            "rétt": "3"} ,
            {"spurning": "Hvernig er banani á litinn?",
            "svar":["gulur" , "rauður" , "grænn" , "blár"],
            "rétt": "1"} ,
            {"spurning": "Klukkan hvað er nón?",
            "svar": [ "12:00" , "15:00" , "18:00" , "21:00"],
            "rétt": "2"} ,
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
