#Upphafsmynd
from time import sleep
import sys
import random
from bord1 import Bord1

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

        bord1=Bord1()
        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                break
            bord1.byrja()


#################################################
def main():
    leikur = upphafsmynd()
    leikur.kynning()


if __name__ == '__main__':
    main()
