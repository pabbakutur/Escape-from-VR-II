def main():
    print("\n")
    print("Myndagáta! \n")
    print("Skoðaðu myndina og svaraðu\n")
    print("Hversu mörg andlit af Alexander koma fyrir á myndinni? \n")
    print("")
    while 1:
            a = input('Ýttu á ENTER til að sjá myndina')
            if(len(a)<1):
                mynd()
            else:
                main()


def mynd():
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image

    ImageAddress = 'blom.jpg'  #myndin þarf að vera i sama folder
    ImageItself = Image.open(ImageAddress)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.draw()
    plt.pause(2) # pause
    plt.close()
    spurning()

def velja():
    x = input("Veldu svar: ")
    return x

def spurning():
    print("Veldu svar. (1, 2, 3 eða 4)")
    print("1. Möguleiki 1\n")
    print("2. Möguleiki 2\n")
    print("3. Möguleiki 3\n")
    print("4. Möguleiki 4\n")
    svar = velja()
    if svar == "1":
        print("Það er rétt")
        ##fara á næsta borð
    elif svar== "2" or "3" or "4":
        print("Það er rangt")
        ##aftur á upphafsskjá eða önnur tilraun?
    else:
        print("það er ekki valmöguleiki")
        ##aftur á upphafsskjá eða önnur tilraun?

main()
