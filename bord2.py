import sys
from bord3 import Bord3
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class Bord2:
    def __init__(self):
        self.total=0

    def intro(self):
        print("\n")
        print("Myndagáta! \n")
        print("Skoðaðu myndina og svaraðu\n")
        print("Hversu mörg andlit af Lexa eru á myndinni? \n")
        print("")
        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                break
            else:
                continue

    def mynd(self):

        ImageAddress = 'lexi2.png'  #myndin þarf að vera i sama folder
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(3) # pause
        plt.close()

    def spurning(self):
        while True:
            self.mynd()
            print("Veldu svar. (1, 2, 3 eða 4)")
            print("1. 6 andlit\n")
            print("2. 5 andlit\n")
            print("3. 4 andlit\n")
            print("4. 7 andlit\n")
            svar = input("Þitt svar: ")
        
            if svar == "1":
                print("Það er rétt")
                return 1
            elif svar == "2":
                print("það er rangt")
                self.total+=1
                ##aftur á upphafsskjá eða önnur tilraun
            elif svar == "3":
                print("það er rangt")
                self.total+=1
            elif svar == "4":
                print("það er rangt")
                self.total+=1
            else:
                print("það er ekki valmöguleiki")
                continue
            if self.total == 2:
                print("Þú tapaðir og ferð aftur um eitt borð.")
                return -1
            else:
                print("Reyndu aftur")
                continue

    def keyra(self):
        self.intro()
        return self.spurning()
        
