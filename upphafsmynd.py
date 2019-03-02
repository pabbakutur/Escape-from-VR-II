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
        print('---------------------------------------------------------') ; sleep(0.5)
        print('-- Velkomin/nn í Escape from VR-II                       --') ; sleep(0.5)
        print('--                                                     --') ; sleep(0.5)
        print('-- Alexander Róbert Magnússon er nýbúinn að taka gott  --') ; sleep(0.5)
        print('-- session á lesstofunni í VR-II og ætlar að koma sér  --') ; sleep(0.5)
        print('-- heim. Áður en hann getur það þarf hann að leysa úr  --') ; sleep(0.5)
        print('-- nokkrum þrautum sem samnemendur hans hafa lagt      --') ; sleep(0.5)
        print('-- í veg fyrir hann.                                   --') ; sleep(0.5)
        print('---------------------------------------------------------') ; sleep(0.5)
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
        print('velkominn á borð 1')

        spurningar = [
            {"spurning": "Svar 3?",
            "svar": [ "1" , "2" , "3" , "4"],
            "rétt": "3"} ,
            {"spurning": "Hvernig er banani á litinn?",
            "svar":["gulur" , "rauður" , "grænn" , "blár"],
            "rétt": "1"} ,
            {"spurning": "Svar 2?",
            "svar": [ "1" , "2" , "3" , "4"],
            "rétt": "2"} ,
         ]
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
            exit
##########################################
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



###############################################
    def bord2(self):
        print('kominn a bord 2')
#################################################
def main():
    leikur = upphafsmynd()
    leikur.kynning()


if __name__ == '__main__':
    main()
