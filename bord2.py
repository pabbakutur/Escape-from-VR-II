import sys
from bord3 import Bord3
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class Bord2:
    def __init__(self):
        self.total=0
    def main(self):
        print("\n")
        print("Myndagáta! \n")
        print("Skoðaðu myndina og svaraðu\n")
        print("Hversu mörg andlit af Lexa eru á myndinni? \n")
        print("")
        while 1:
                a = input('Ýttu á ENTER til að halda áfram')
                if(len(a)<1):
                    self.mynd()
                else:
                    break

    def mynd(self):

        ImageAddress = 'lexi2.png'  #myndin þarf að vera i sama folder
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(2) # pause
        plt.close()
        self.spurning()

    def spurning(self):
        print("Veldu svar. (1, 2, 3 eða 4)")
        print("1. 6 andlit\n")
        print("2. 5 andlit\n")
        print("3. 4 andlit\n")
        print("4. 7 andlit\n")
        svar = input("Þitt svar: ")
        if svar == "1":
            print("Það er rétt")
            sys.exit()
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
            self.spurning()
        if self.total == 2:
            print("Þú tapaðir og ferð aftur um eitt borð.")
            sys.exit()
        else:
            print("Reyndu aftur")
            self.mynd()
b2=Bord2()
b2.main()
