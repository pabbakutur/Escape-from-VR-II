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
        for i in range(30):
            print('')
#        sleep(5)
#        print('                 -------------------------') ; sleep(1)
#        print('                 --- Escape from VR-II ---') ; sleep(1)
#        print('                 -------------------------') ; sleep(1)
#        print('') ; sleep(1)
#        print('---------------------------------------------------------') ; sleep(0.5)
#        print('-- Velkomin/nn í Escape from VR-II                     --') ; sleep(0.5)
#        print('--                                                     --') ; sleep(0.5)
#        print('-- Alexander Róbert Magnússon er staddur í lesstofunni --') ; sleep(0.5)
#        print('-- í VR-II og ætlar að koma sér heim. Áður en hann     --') ; sleep(0.5)
#        print('-- getur það þarf hann að leysa nokkur verkefni sem    --') ; sleep(0.5)
#        print('-- þú þarft að hjálpa honum við.                       --') ; sleep(0.5)
#        print('---------------------------------------------------------') ; sleep(0.5)
#        print('') ; sleep(0.5)
#        print('') ; sleep(0.5)

        bord1=Bord1()
        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                bord1.byrja()


#################################################
def main():
    leikur = upphafsmynd()
    leikur.kynning()


if __name__ == '__main__':
    main()
