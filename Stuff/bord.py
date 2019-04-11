import sys
import time
import msvcrt

class Bord():
    def __init__(self):
        self.sHeader = 'Header for the table...'
        self.sDirections ='Directions on what to do or what is happening'
        self.sOptions = 'What options do you have'
        self.sStats = 'Stats for this table, hints used, lives lost'
        self.screenLength = 60

    def setHeader(self, pIntro):
        # Use this time of format the header
        self.sHeader = pIntro

    def setDirecion(self, pDir):
        # Format to fixed number of lines
        self.sDirections = pDir

    def setOptions(self, pOpt):
        self.sOptions = pOpt

    def setStats(self, pStats):
        self.sStats = pStats

    def printGameScreen(self):
        #print formatted games-screen
        print('#' * self.screenLength)
        print(self.sHeader)
        print('#' * self.screenLength)
        print(self.sDirections)
        print('#' * self.screenLength)
        print(self.sOptions)
        print('#' * self.screenLength)
        print(self.sStats)
        print('#' * self.screenLength)

    def clearScreen(self):
        #Hreinsum skjáinn (30 auðar línur)
        for i in range(30):
           print ('\n')   

    def getEnter(self):  
        while 1:
            a = input('Ýttu á ENTER til að halda áfram')
            if(len(a)<1):
                break 

    def GetKeypressS(self, sOptions='', sPrompt= 'Veldu möguleika'):
        # Input limited by string. Key pressed must be a character in the string
        if sOptions != '':
            val = ' ('
            for x in sOptions:
                if val == ' (':
                    val = val + x
                else:
                    val = val + ', ' + x
            val = val + ')'
        else:
            val = ''
#        val = ','.join(str(x) for x in sOptions)
        print(sPrompt + val)
        while True:
            key = msvcrt.getwch()
            if key == '!':
                # Putting in an exit code for quick exit when debugging. 
                sys.exit(0)
            elif sOptions == '':
                # If sOptions is empty, accept any key
                return key
            elif key in sOptions:
                # only return if key pressed is in the string
                return key
            else:
                # Might print out what options the user has
                print(key + ' er ekki leyfilegur valmöguleiki')
                print(sPrompt + val)
                



if __name__ == '__main__':
    b = Bord()
    b.printGameScreen()
    b.clearScreen()
    b.setHeader("First line\nSecond line")
    b.printGameScreen()
    while True:
        #print(b.GetKeypressS('123'))
        #print(b.GetKeypressS('123','Veldu eitthvað af valmöguleikum'))
        #print(b.GetKeypressS('','Giskaðu á einhvern staf'))
        print(b.GetKeypressS('','Press any key'))
        #b.getEnter()
