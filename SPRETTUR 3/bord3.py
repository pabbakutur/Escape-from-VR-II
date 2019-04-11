import sys
import time
import random
from bord import Bord
class Bord3(Bord):
    def __init__(self):
        self.kennarar = ['SIGURÐUR ÖRN','RÖGNVALDUR MÖLLER','INGÓLFUR HJÖRLEIFSSON','GUNNAR SCHRAM','VILMUNDUR TORFI','SIGURÐUR FREYR']
        self.fraegir = ['PYTHAGORAS','ARCHIMEDES','FROBENIUS','EULER','FIBONACCI','ALBERT EINSTEIN']
        self.hugtok = ['JACOBI FYLKI','MILLIGILDISSETNINGIN','KLEMMUREGLAN','HESSE FYLKI','LEIFASETNINGIN','CAUCHY SETNINGIN']
        self.aHengimadur =[
            '         _____ \n         |   | \n         O   | \n        /|\\  | \n        / \\  | \n             | \n     ________|_', #0
            '         _____ \n         |   | \n         O   | \n        /|\\  | \n        /    | \n             | \n     ________|_',  #1
            '         _____ \n         |   | \n         O   | \n        /|\\  | \n             | \n             | \n     ________|_',  #2
            '         _____ \n         |   | \n         O   | \n        /|   | \n             | \n             | \n     ________|_',   #3
            '         _____ \n         |   | \n         O   | \n         |   | \n             | \n             | \n     ________|_',   #4
            '         _____ \n         |   | \n         O   | \n             | \n             | \n             | \n     ________|_',   #5
            '         _____ \n         |   | \n             | \n             | \n             | \n             | \n     ________|_',   #6
            '         _____ \n             | \n             | \n             | \n             | \n             | \n     ________|_',   #7
            '               \n             | \n             | \n             | \n             | \n             | \n     ________|_',   #8
            '               \n               \n               \n               \n               \n               \n     ________|_'  ] #9
        # Þarf að initialize-a base klasann                
        super(Bord3,self).__init__()

        #Borð 3 hefst hér, spilari getur valið um 3 möguleika. Byrja, upplýsingar eða hætta.
    def startgluggi(self):
        self.clearScreen()
        self.setHeader(
            'Velkominn í borð 3\n'+
            'Hengimaður að hætti Lexa')
        self.setDirection('\n')
        self.setOptions(
            '1.Byrja\n'+
            '2.Upplýsingar um borð 3\n'+
            '3.Hætta')
        self.setStats('\n')
        self.printGameScreen()
        return self.GetKeypressS('123','Veldu möguleika')
        #return self.GetKeypressS('123')
        
        #Spilari fær að velja mismunandi orðaflokka
    def startgluggi2(self):
        self.clearScreen()
        self.setHeader(
            'Nú hefur þú kost á að velja 3\n'+
            'mismunandi orðaflokka sem eru\n'+
            'í miklu uppáhaldi hjá Lexa.')
        
        self.setOptions(
            '1.Kennarar í HÍ\n'+
            '2.Frægir stærðfræðingar\n'+
            '3.Stærðfræðihugtök')
        self.printGameScreen()
        ret = self.GetKeypressS('123','Veldu möguleika')
        if ret == '1':
            self.setHeader('Reyndu að finna nafn á kennara í HÍ')
        elif ret == '2':
            self.setHeader('Reyndu að finna nafn á frægum stærðfræðingi')
        else:
            self.setHeader('Reyndu að giska á frægt stærðfræðihugtak')
        return ret
        #return self.GetKeypressS('123')

        #Fall sem inniheldur upplýsingar um borð 3.  Til að fara úr því þarf að ýta á einhvern takka
    def upplysingar(self):
        self.clearScreen()
        self.setDirection(
            'Það sem fáir vita um Lexa er að uppáhalds leikur Lexa er\n'+
            'hinn klassíski hengimaður. Markmið leiksins er að spilari\n'+
            'reynir að komast að því hvaða orð tölvan hefur valið með því\n'+
            'að giska á einn staf í einu. Ef spilari giskar á vitlausan staf\n'+
            'þá missir hann eina tilraun. Leikmaður hefur í heildina 9 til-\n'+
            'raunir og ef hann klúðrar þeim öllum þá er maðurinn hengdur.\n'+
            'Leikurinn er sérsniðinn að Lexa svo það eru einungis orð sem\n'+
            'Lexi elskar. Njótið.\n')
        self.printGameScreen()
        return self.GetKeypressS('','Ýttu á einhvern staf á lyklaborðinu til að fara til baka')

        #gameInterface er aðal user interface-ið í leiknum. Guess,miss_attempts á ekki að vera >9, misses er öll röngu giskin
        #prentar út interface og skilar # ef spilari vill endurræsa, ! ef spilari vill svarið.
    def gameInterface(self,guess,miss_attempts,misses,hintleft):
        self.clearScreen()
        left = 9-miss_attempts
        self.setDirection(self.aHengimadur[left])
        self.setOptions(
            'Orð: ' + ' '.join(guess) +'\n'+
            'Röng gisk: ' + ' '.join(misses))
#        self.printGameScreen()
        if left != 0:
            self.setStats(
                'Þú átt '+ str(left) + ' tilraun(ir) eftir\n'+
                'Þú átt ' + str(hintleft) +' vísbendingu/ar eftir\n'+
                'Skrifaðu ? til að fá vísbendingu og ! til að hætta'   )
            self.printGameScreen()

            _in = self.GetKeypressS('','Giskaðu á staf: ')
            if len(_in)>1:
                return '<'
            else:
                if _in == '?' or _in == '!':
                    return _in
                elif _in.isalpha():
                    return _in.upper()
                else:
                    return '<'
        else:
            self.setStats('Þú tapaðir. Ekki nógu gott!')
            self.printGameScreen()
            _in = self.GetKeypressS('','Ýttu á einhvern staf til að reyna aftur!')
            return -1

        #Game is the process of gaming. Skilar false ef leikur endar. hintMax á ekki að vera stærri en 3.
    def game(self,word,hintMax):
        length = len(word)
        miss = 0
        hintTimes = 0
        misses = []
        #b4=Bord4()

        guess = ['_' for i in range(length)]
        for i in range(length):
            if(word[i]== " "):
                guess[i] = " "
        keyra=True
        while keyra:
            operation = self.gameInterface(guess,miss,misses,hintMax-hintTimes)
            #if operation == '#':
                #print('Endurræsa...')
                #time.sleep(3)
                #return True
            if operation == '?':
                if hintTimes<hintMax:
                    operation = self.hint(word,guess)
                    for i in range(length):
                        if word[i]==operation:
                            guess[i] = operation
                    hintTimes = hintTimes+1
                else:
                    self.setStats('Vísbendingarnar eru búnar!')
                    self.printGameScreen()
                    continue
            elif operation == '<':
                self.GetKeypressS('','Vinsamlega sláðu inn 1 bókstaf')
                continue
            elif operation == '!':
                #sys.exit()
                #self.clearScreen()
                #self.hengimadurprent(9-miss)
                #print('###########################################')
                #print('# Svarið er: ',word)
                #print('# Augnablik!')
                #time.sleep(3)
                return 0
            elif operation == -1:
                return -1
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
                self.clearScreen()
                self.setDirection(self.aHengimadur[9-miss])
                self.setOptions('Orð: ' + ' '.join(guess)+'\n\n'+'Vel gert!')
                self.printGameScreen()
                time.sleep(2)
                keyra = False
                #b4.gangur()
                return 1
                #return False

        #Þetta fall skilar réttum staf. Word er strengur og guess er listi.
    def hint(self,word,guess):
        length = len(word)
        for i in range(length):
            if guess[i]=='_':
                hintletter = word[i]
                return hintletter

        #Þetta fall velur random orð úr orðaflokki sem spilari velur. Sel er orðaflokkarnir (1,2,3).
        #Fallið skilar orð sem er strengur.
    def getWord(self, sel):
        if sel == 1:
            length = len(self.kennarar)
            index = random.randrange(0,length)
            return self.kennarar[index]
        elif sel == 2:
            length = len(self.fraegir)
            index = random.randrange(0,length)
            return self.fraegir[index]
        elif sel == 3:
            length = len(self.hugtok)
            index = random.randrange(0,length)
            return self.hugtok[index]

    def keyra(self):
        self.clearScreen()
        while True:
            sel = self.startgluggi()
            if sel=='1':
                while True:
                    sel2 = self.startgluggi2()
                    if not sel2.isdigit():
                        continue
                    elif len(sel2)>1:
                        continue
                    elif int(sel2)>3 or int(sel2)<0:
                        continue
                    else:
                        word = self.getWord(int(sel2))
                        return self.game(word,4-int(sel2))
            elif sel=='2':
                self.upplysingar()
                continue
            elif sel=='3':
                sys.exit(0)
            else:
                continue
#Hér næst kemur main fallið fyrir borð 3
#if kalla á borð 4
#bord4=Bord4()
#bord4.gangur()

if __name__ == '__main__':
    b = Bord3()
    b.keyra()
