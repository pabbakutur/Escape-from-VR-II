def main():
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
    command=velja()
    print("")
    if command == "1":
        spila(spurningar)
    elif command == "2":
        exit
    else:
        print("þetta er ekki valmöguleiki, veldu 1 eða 2 !")
        veljaAftur()

def veljaAftur():
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
         {"spurning": "Svar 2?",
         "svar": [ "1" , "2" , "3" , "4"],
         "rétt": "2"} ,
         ]
    command = velja()
    if command == "1":
        spila(spurningar)
    elif command == "2":
        exit
    else:
        print("þetta er ekki valmöguleiki, veldu 1 eða 2!")
        veljaAftur()

def velja():
    x = input("Veldu svar: ")
    return x

import random
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
        answer=velja()

        if answer == spurning["rétt"]:
            score += 1
            total += 1
            print("\nÞað er rétt.\n")
        elif answer == "1" :
            print("\nÞað er rangt. \n")
            total +=1
        elif answer == "2":
            print("\nÞað er rangt. \n")
            total +=1
        elif answer =="3":
            print("\nÞað er rangt. \n")
            total +=1
        elif answer == "4":
            print("\nÞað er rangt. \n")
            total +=1
        else:
            print("þetta er ekki svarmöguleiki, reyndu aftur")
        print("Stigastaða: ", score, "af", total, "\n")
        if score - total == -2:
            print("Þú tapaðir")
            break
        elif score == 2:
            print("Þú vannst")
            break
    print("Þú varst með", score, "rétt af", total ,"\n")
    exit

main()
