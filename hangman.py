import time
import random
kennarar = ['SIGURÐUR ÖRN','RÖGNVALDUR MÖLLER','INGÓLFUR HJÖRLEIFSSON','GUNNAR SCHRAM','VILMUNDUR TORFI','SIGURÐUR FREYR']
fraegir = ['PYTHAGORAS','ARCHIMEDES','FROBENIUS','EULER','FIBONACCI','ALBERT EINSTEIN']
hugtok = ['JACOBI FYLKI','MILLIGILDISSETNINGIN','TAYLOR MARGLIÐA','HESSE FYLKI','LEIFASETNINGIN','CAUCHY SETNINGIN']

#Hreinsum skjáinn (30 auðar línur)
def clear():
        for i in range(30):
                print ('\n')

#Þetta fall prentar út mynd af hengimanni á skipanalínu. Index er fjöldi skrefa eftir
#og ætti að vera >=0
def hengimadurprent(index):
        if index==0:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('        / \  | ')
                print('             | ')
                print('     ________|_')
                return
        if index==1:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('        /    | ')
                print('             | ')
                print('     ________|_')
                return
        if index==2:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==3:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|   | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==4:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('         |   | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==5:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==6:
                print('         _____ ')
                print('         |   | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==7:
                print('         _____ ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==8:
                print('               ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==9:
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('     ________|_')
                return

#Borð 3 hefst hér, spilari getur valið um 3 möguleika. Byrja, upplýsingar eða hætta.
def startgluggi():
        clear()
        print('######################################')
        print('#         Velkominn í borð 3         #')
        print('#      Hengimaður að hætti Lexa      #')
        print('######################################')
        print('#       1.Byrja                      #')
        print('#       2.Upplýsingar um borð 3      #')
        print('#       3.Hætta                      #')
        choice = input('Veldu möguleika 1,2 eða 3: ')
        return choice

#Spilari fær að velja mismunandi orðaflokka
def startgluggi2():
        clear()
        print('######################################')
        print('#   Nú hefur þú kost á að velja 3    #')
        print('#   mismunandi orðaflokka sem eru    #')
        print('#   í miklu uppáhaldi hjá Lexa.      #')
        print('######################################')
        print('        1.Kennarar í HÍ    #')
        print('        2.Frægir stærðfræðingar   #')
        print('        3.Stærðfræðihugtök #')
        choice = input('Veldu möguleika 1,2 eða 3: ')
        return choice

#Fall sem inniheldur upplýsingar um borð 3.  Til að fara úr því þarf að ýta á einhvern takka
def upplysingar():
        clear()
        print('#######################################################################')
        print('#     Það sem fáir vita um Lexa er að uppáhalds leikur Lexa er        #')
        print('#     hinn klassíski hengimaður. Markmið leiksins er að spilari       #')
        print('#     reynir að komast að því hvaða orð tölvan hefur valið með því    #')
        print('#     að giska á einn staf í einu. Ef spilari giskar á vitlausan staf #')
        print('#     þá missir hann eina tilraun. Leikmaður hefur í heildina 9 til-  #')
        print('#     raunir og ef hann klúðrar þeim öllum þá er maðurinn hengdur.    #')
        print('#     Leikurinn er sérsniðinn að Lexa svo það eru einungis orð sem    #')
        print('#     Lexi elskar. Njótið.                                            #')
        print('#######################################################################')
        print('Ýttu á einhvern staf á lyklaborðinu til að fara til baka')
        input('')
        return

#gameInterface er aðal user interface-ið í leiknum. Guess,miss_attempts á ekki að vera >9, misses er öll röngu giskin
#prentar út interface og skilar # ef spilari vill endurræsa, ! ef spilari vill svarið.
def gameInterface(guess,miss_attempts,misses,hintleft):
        clear()
        left = 9-miss_attempts
        hengimadurprent(left)
        print('###########################################')
        print('Orð: ',end='')
        for i in guess:
                print(i,' ',end='')
        print()
        print('# Röng gisk: ',end='')
        for i in misses:
                print(i,' ',end='')
        print()
        if left != 0:
            print('# Þú átt ',left,' tilraun(ir) eftir')
            print('# Þú átt ',hintleft,' vísbendingu/ar eftir')
            print('# Skrifaðu ? til að fá vísbendingu, # til að byrja upp á nýtt og ! til að sjá svarið!')
            _in = input('# Giskaðu á staf: ')
            if len(_in)>1:
                return '<'
            else:
                if _in == '?' or _in == '#' or _in == '!':
                    return _in
                elif _in.isalpha():
                    return _in.upper()
                else:
                    return '<'
        else:
            print('# Þú tapaðir, skrifaðu inn einhvern staf til að reyna aftur!')
            _in = input('')
            return '#'

#Game is the process of gaming. Skilar false ef leikur endar. hintMax á ekki að vera stærri en 3.
def game(word,hintMax):
        length = len(word)
        miss = 0
        hintTimes = 0
        misses = []
        guess = ['_' for i in range(length)]
        for i in range(length):
            if(word[i]== " "):
                guess[i] = " "
        while True:
            operation = gameInterface(guess,miss,misses,hintMax-hintTimes)
            if operation == '#':
                print('Endurræsa...')
                time.sleep(3)
                return True
            elif operation == '?':
                if hintTimes<hintMax:
                    operation = hint(word,guess)
                    for i in range(length):
                        if word[i]==operation:
                            guess[i] = operation
                    hintTimes = hintTimes+1
                else:
                    print('#Vísbendingarnar eru búnar!')
                    print('# Augnablik!')
                    time.sleep(2)
                    continue
            elif operation == '<':
                print('# Þú mátt bara giska á einn staf í einu!')
                print('# Augnablik!')
                time.sleep(2)
                continue
            elif operation == '!':
                clear()
                hengimadurprent(9-miss)
                print('###########################################')
                print('# Svarið er: ',word)
                print('# Augnablik!')
                time.sleep(3)
                return False
            else:
                flag=0
                for i in range(length):
                    if word[i]==operation:
                        guess[i] = operation
                        flag = 1
                if flag==0:
                    miss = miss+1
                    if not operation in misses:
                        misses.append(operation)

            if not '_' in guess:
                clear()
                hengimadurprent(9-miss)
                print('###########################################')
                print('# ',end='')
                for i in guess:
                    print(i,' ',end='')
                print()
                print('# Vel gert!')
                time.sleep(3)
                return False

#Þetta fall skilar réttum staf. Word er strengur og guess er listi.
def hint(word,guess):
    length = len(word)
    for i in range(length):
        if guess[i]=='_':
            hintletter = word[i]
            return hintletter

#Þetta fall velur random orð úr orðaflokki sem spilari velur. Sel er orðaflokkarnir (1,2,3).
#Fallið skilar orð sem er strengur.
def getWord(sel):
    global kennarar,fraegir,hugtok
    if sel == 1:
        length = len(kennarar)
        index = random.randrange(0,length)
        return kennarar[index]
    elif sel == 2:
        length = len(fraegir)
        index = random.randrange(0,length)
        return fraegir[index]
    elif sel == 3:
        length = len(hugtok)
        index = random.randrange(0,length)
        return hugtok[index]

#Hér næst kemur main fallið fyrir borð 3
clear()
while True:
    gameProcess = True
    sel = startgluggi()
    if sel=='1':
        while True:
            sel2 = startgluggi2()
            if not sel2.isdigit():
                continue
            elif len(sel2)>1:
                continue
            elif int(sel2)>3 or int(sel2)<0:
                continue
            else:
                word = getWord(int(sel2))
                while gameProcess:
                    gameProcess = game(word,4-int(sel2))
                break
    elif sel=='2':
        upplysingar()
        continue
    elif sel=='3':
        break
    else:
        continue
