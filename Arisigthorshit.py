def main():
    spurningar = [
        {"spurning": "What's .5 + .5?",
         "svar": [ "1" , "2" , "3" , "4"],
         "rétt": "1"} ,
        {"spurning": "Hvernig er banani á litinn?",
        "svar":["gulur" , "rauður" , "grænn" , "blár"],
        "rétt": "1"} ,
         ]
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

import random

def spila(spurningar):

    nafn = input("Hvað heitiru: ")
    score = 0
    random.shuffle(spurningar)

    for spurning in spurningar:
        print(spurning["spurning"])
        for i, val in enumerate(spurning["svar"]):
            print(str(i + 1) + ". " + val)
        answer = input("Veldu svar: ")
        while int(answer)-1 not in range(len(spurning["svar"])):
            print("\nÞetta er ekki svarmöguleiki, reyndu aftur. \n")
            answer = input("\nVeldu svar: ")
        if answer == spurning["rétt"]:
            score += 1
            print("\nÞað er rétt.\n")
        else:
            print("\nÞað er rangt. \n")
        print("Stigastaða: ", score, "\n")
    print(nafn + ", þú ert með", score, "rétt.\n")
    main()

main()
