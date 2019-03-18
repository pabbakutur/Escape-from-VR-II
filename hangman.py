import time
import random
easy = ['PHONE BILL']
#,'HAPPY','APPLE','EARTH','GONGYIWEI'
normal = ['PYTHON','PIONEER','SINGAPORE','FATHER','MOTHER','GONGYIWEI']

#Hreinsum skjáinn (30 auðar línur)
def clear():
        for i in range(30):
                print ('\n')

#Þetta fall prentar út mynd af hengimanni á skipanalínu. Index er fjöldi skrefa eftir
#og ætti að vera >=0
def hangmanInterface(index):
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
def startInterface():
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
def startInterface2():
        clear()
        print('######################################')
        print('#   Nú hefur þú kost á að velja 3    #')
        print('#   mismunandi orðaflokka sem eru    #')
        print('#   í miklu uppáhaldi hjá Lexa.      #')
        print('######################################')
        print('        1.Kennarar í HÍ    #')
        print('        2.Frægir stærðfræðingar   #')
        print('        3.Stærðfræðisetningar  #')
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

#################################################
#gameInterface  : gameInterface is the main user interface in gaming.
#pre-condition  : user's guess,miss_attempts should not greater than 9,misses is the history of mistake
#post-condition : print out the interface and return # if restart, return ! if call for
#                 help,return character else
#################################################
def gameInterface(guess,miss_attempts,misses,hintleft):
        clear()
        left = 9-miss_attempts
        hangmanInterface(left)
        print('###########################################')
        print('Word: ',end='')
        for i in guess:
                print(i,' ',end='')
        print()
        print('# Misses: ',end='')
        for i in misses:
                print(i,' ',end='')
        print()
        if left != 0:
            print('# You have ',left,' attempt(s) left')
            print('# You have ',hintleft,' hint(s) left')
            print('# input ? to get hint, # to restart and ! to see answer')
            _in = input('# Guess: ')
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
            print('# key in any input to Try Again!')
            _in = input('')
            return '#'

#################################################
#game           : game is the process of gaming. return false if game ends
#pre-condition  : the answer 'word' should be a string. hintMax should not be greater than 3
#post-condition : return false if game ends
#################################################
def game(word,hintMax):
        length = len(word)
        miss = 0
        hintTimes = 0
        misses = []
        guess = ""
        for i in range(length):
            if(word[i]== " "):
                guess = guess + " "
            else:
                guess = guess + "_"
        #guess = ['_' for i in range(length)]
        while True:
            operation = gameInterface(guess,miss,misses,hintMax-hintTimes)
            if operation == '#':
                print('Restarting...')
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
                    print('# Can not get hint any more!Try your best!')
                    print('# Wait for 2 seconds')
                    time.sleep(2)
                    continue
            elif operation == '<':
                print('# Please input correctly!')
                print('# Wait for 2 seconds')
                time.sleep(2)
                continue
            elif operation == '!':
                clear()
                hangmanInterface(9-miss)
                print('###########################################')
                print('# The answer is',word)
                print('# wait fewer seconds to back to main menu')
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
                hangmanInterface(9-miss)
                print('###########################################')
                print('# ',end='')
                for i in guess:
                    print(i,' ',end='')
                print()
                print('# Great!')
                time.sleep(3)
                return False


#################################################
#hint           : this function will return a correct character
#pre-condition  : word should be a string and guess should be a list
#post-condition : return back a correct character
#################################################
def hint(word,guess):
    length = len(word)
    for i in range(length):
        if guess[i]=='_':
            hintletter = word[i]
            return hintletter

#################################################
#getWord        : getWord function will get a get a word randomly
#                 Admin model can see the whole library and add words
#pre-condition  : sel is the degree of difficulty and should be less than 3
#                 if sel is greater then 3, that means Admin model!
#post-condition : return a word whose type is string.
#                 Or Admin model to access library!
#################################################
#Þetta fall velur random orð úr orðaflokki sem spilari velur.
def getWord(sel):
    global easy,normal
    if sel==3:
        sel = 2
    if sel == 1:
        length = len(easy)
        index = random.randrange(0,length)
        return easy[index]
    elif sel == 2:
        length = len(normal)
        index = random.randrange(0,length)
        return normal[index]
    else:
        while True:
            clear()
            print('####################################')
            print('# Edit Library, input "exit()" to go back to main menu:')
            print('# 1.Show Library')
            print('# 2.Add word; Program will automatically select degree of difficulty')
            print('# 3.RESET to default.')
            print('####################################')
            selection = input('Selection: ')
            if selection == 'exit()':
                return 'DONE'
            elif selection == '1':
                print('_________________Library Files___________________')
                print('easy:')
                for i in easy:
                    print('    ',i)
                print()
                print('normal and expert:')
                for i in normal:
                    print('    ',i)
                print()
                print('_________________Library Files___________________')
                print('# key in any input to return')
                temp = input()
            elif selection == '2':
                while True:
                    print('_________________Addition___________________')
                    print('Use end() to end')
                    add = input()
                    if add != 'end()':
                        if add.isalpha():
                            degree = check(add)
                            if degree == 1:
                                if not add.upper() in easy:
                                    easy.append(add.upper())
                                    print('# Add successfully!')
                                else:
                                    print('# REPEAT! Words has ready added!')

                            else:
                                if not add.upper() in normal:
                                    normal.append(add.upper())
                                    print('# Add successfully!')
                                else:
                                    print('# REPEAT! Words has ready added!')
                        else:
                            print('# Please input correctly!')
                            continue
                    else:
                        print('_________________Addition___________________')
                        print('Addition Done')
                        time.sleep(2)
                        break
            elif selection == '3':
                    while True:
                        print('# Please be sure all data will be set to default!')
                        print('# key in "confirm()" to continue and key in anything else to cancel')
                        temp = input()
                        if temp=='confirm()':
                                easy = ['PHONE','HAPPY','APPLE','EARTH','GONGYIWEI']
                                normal = ['PYTHON','PIONEER','SINGAPORE','FATHER','MOTHER','GONGYIWEI']
                                print('# Successfully! wait 2 seconds.')
                                time.sleep(2)
                                break
                        else:
                                print('# Canceled! wait 2 seconds.')
                                time.sleep(2)
                                break
            else:
                continue

#################################################
#check          : Check the whether is easy or normal
#pre-condition  : addition should be a string only contenting alpha
#post-condition : return 1 if it is easy return 2 if it is normal
#################################################
def check(addition):
    sign = 0
    result = ['CHECK']
    for i in addition:
        if not i in result:
            result.append(i)
    sign = len(result)
    if sign>6:
        return 2
    else:
        return 1

#Hér næst kemur main fallið fyrir borð 3
clear()
while True:
    gameProcess = True
    sel = startInterface()
    if sel=='1':
        while True:
            sel2 = startInterface2()
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
    elif sel=='admin':
        getWord(4)
    elif sel=='whosyourdaddy':
                    word = 'HANGMAN'
                    temp = game(word,1000)
    else:
        continue
