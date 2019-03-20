def main():
    spurningar = [
        {"spurning": "d/dx 1/2sin(x^2) = ?",
         "svar": [ "1" , "2" , "xcos(x)" , "4"],
         "rétt": "3"} ,
        {"spurning": "d/dx cos(x^3) = ?)",
        "svar":["-3x^2sin(x^3)" , "-3sin(x^3)" , "-cos(x^3)" , "-xcos(x^3)"],
        "rétt": "1"} ,
        {"spurning": "x^2sin(x^3) dx = ?",
         "svar": [ "-x^2cos(x^3) + C" , "-xcos(x^3) + C" , "1/3cos(x^3) + C" , "-1/3cos(x^3) + C"],
         "rétt": "4"} ,
         ]
    print("\n")
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
    print("\n")
    score = 0
    total = 0
    random.shuffle(spurningar)
    for spurning in spurningar:
        print("Veldu 1, 2, 3 eða 4")
        print(spurning["spurning"])
        for i, val in enumerate(spurning["svar"]):
            print(str(i + 1) + ". " + val)
        answer = input("Veldu svar: ")
        while int(answer)-1 not in range(len(spurning["svar"])):
            print("\nÞetta er ekki svarmöguleiki, reyndu aftur. \n")
            answer = input("\nVeldu svar: ")
        if answer == spurning["rétt"]:
            score += 1
            total += 1
            print("\nÞað er rétt.\n")
        else:
            print("\nÞað er rangt. \n")
            total +=1
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
