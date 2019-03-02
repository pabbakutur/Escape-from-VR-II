def main():
    print("\n")
    print("Myndagáta! \n")
    print("Skoðaðu myndina og svaraðu\n")
    print("Insert_spurning \n")
    print("")
    while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                mynd()
            else:
                break

def mynd():
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image

    ImageAddress = 'blom.jpg'
    ImageItself = Image.open(ImageAddress)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.draw()
    plt.pause(2) # pause how many seconds
    plt.close()
    spurning()

def spurning():
    print("Veldu svar. (1, 2, 3 eða 4)")
    print("1. Möguleiki 1\n")
    print("2. Möguleiki 2\n")
    print("3. Möguleiki 3\n")
    print("4. Möguleiki 4\n")
    svar = input("Þitt svar: ")
    if svar == "1":
        print("Það er rétt")
        ##fara á næsta borð
    elif svar == "2":
        print("það er rangt")
        ##aftur á upphafsskjá eða önnur tilraun?

main()
