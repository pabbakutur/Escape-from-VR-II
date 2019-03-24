from Bord1 import Bord1
from bord2 import Bord2
from bord3 import Bord3
from bord4 import Bord4
import sys
from time import sleep

def kynning():
    for i in range(30):
        print('')
    sleep(1)
    print('                 -------------------------') ; sleep(1)
    print('                 --- Escape from VR-II ---') ; sleep(1)
    print('                 -------------------------') ; sleep(1)
    print('') ; sleep(1)
    print('---------------------------------------------------------') ; sleep(0.5)
    print('-- Velkomin/nn í Escape from VR-II                     --') ; sleep(0.5)
    print('--                                                     --') ; sleep(0.5)
    print('-- Alexander Róbert Magnússon er staddur í lesstofunni --') ; sleep(0.5)
    print('-- í VR-II og ætlar að koma sér heim. Áður en hann     --') ; sleep(0.5)
    print('-- getur það þarf hann að leysa nokkur verkefni sem    --') ; sleep(0.5)
    print('-- þú þarft að hjálpa honum við.                       --') ; sleep(0.5)
    print('---------------------------------------------------------') ; sleep(0.5)
    print('') ; sleep(0.5)
    print('') ; sleep(0.5)

    while 1:
        a = input('Ýttu á ENTER til að halda áfram')
        if(len(a)<1):
           break

b1 = Bord1()
b2 = Bord2()
b3 = Bord3()
b4 = Bord4()

kynning()
i = 1
while True:
    if i==1:
        ret = b1.keyra()
    elif i==2:
        ret = b2.keyra()
    elif i==3:
        ret = b3.keyra()
    elif i==4:
        ret = b4.keyra()

    if ret == -1:
        if i > 1:
            i = i - 1
        else:
            print('Þú tapar. Loser!')
            sys.exit()
    elif ret == 0:
        print('Leik hætt. Takk fyrir að reyna')
        sys.exit()
    else:
        if i < 4:
            i = i + 1
        else:
            print('Til hamingju. Þú hefur klárað leikinn!')
            sys.exit()



# b1 = Bord1()
# ret = b1.keyra()
# if ret == 1:
#     b2 = Bord2()
#     ret = b2.keyra()
# if ret == 1:
#     b3 = Bord3()
#     ret = b3.keyra()
# if ret == 1:
#     b4 = Bord4()
#     b4.keyra()
