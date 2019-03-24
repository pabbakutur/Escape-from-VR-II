from bord3 import Bord3
class Bord2:
    def __init__(self):
        pass
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
        import numpy as np
        import matplotlib.pyplot as plt
        from PIL import Image

        ImageAddress = 'lexi1.png'  #myndin þarf að vera i sama folder
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(2) # pause
        plt.close()
        self.spurning()

    def spurning(self):
        print("Veldu svar. (1, 2, 3 eða 4)")
        print("1. Möguleiki 1\n")
        print("2. Möguleiki 2\n")
        print("3. Möguleiki 3\n")
        print("4. Möguleiki 4\n")
        svar = input("Þitt svar: ")
        if svar == "1":
            print("Það er rétt")
            ##fara á næsta borð
        elif svar == "2" or "3" or "4":
            print("það er rangt")
            ##aftur á upphafsskjá eða önnur tilraun?
        else:
            print("það er ekki valmöguleiki")
            self.spurning()
b2=Bord2()
b2.main()
