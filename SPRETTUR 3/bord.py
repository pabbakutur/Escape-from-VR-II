import sys
import time
import msvcrt

class Bord():
    # class variables
    screenLength = 80
    iIndent = 5
    sIndent = ' '*iIndent
    lf = '#'+sIndent+'{:'+str(screenLength-2-iIndent)+'}#'  #align left
    cf = '#{:^'+str(screenLength-2)+'}#'  #align center
    rf = '#{:>'+str(screenLength-2-iIndent)+'}'+sIndent+'#'  #align right

    def formatString(self, inString, inFormat='l'):
        if inFormat == 'l':
            lcr = self.lf
        elif inFormat =='c':
            lcr = self.cf
        else:
            lcr = self.rf
        sNewString = ''
        for x in inString.splitlines(False):
            sNewString = sNewString + lcr.format(x) + '\n'
        return sNewString

    def __init__(self):
        self.sHeader = self.formatString('Header for the table...',self.lf)
        self.sDirections = self.formatString('Directions on what to do or what is happening',self.lf)
        self.sOptions = self.formatString('What options do you have',self.lf)
        self.sStats = self.formatString('Stats for this table, hints used, lives lost',self.lf)


    def setHeader(self, pIntro, left_center_right='l'):
        # Use this time of format the header
        self.sHeader = self.formatString(pIntro, left_center_right)

    def setDirection(self, pDir, left_center_right='l'):
        # Format to fixed number of lines
        self.sDirections = self.formatString(pDir, left_center_right)

    def setOptions(self, pOpt, left_center_right='l'):
        self.sOptions = self.formatString(pOpt, left_center_right)

    def setStats(self, pStats, left_center_right='l'):
        self.sStats = self.formatString(pStats, left_center_right)

    def clearScreen(self):
        #Hreinsum skjáinn (30 auðar línur)
        for i in range(30):
           print ('\n')   

    def printGameScreen(self):
        #print formatted games-screen
        print('#' * self.screenLength)
        print(self.sHeader,end='')
        print('#' * self.screenLength)
        print(self.sDirections,end='')
        print('#' * self.screenLength)
        print(self.sOptions,end='')
        print('#' * self.screenLength)
        print(self.sStats,end='')
        print('#' * self.screenLength)

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
    #b.clearScreen()
    print(b.GetKeypressS('123'))
    b.setHeader("First line\nSecond line",'c')
    b.printGameScreen()
    b.setHeader("First line\nSecond line",'r')
    b.printGameScreen()
    b.setHeader("First line\nSecond line",'l')
    b.printGameScreen()


    print(b.GetKeypressS('123'))
    print(b.GetKeypressS('123','Veldu eitthvað af valmöguleikum'))
    print(b.GetKeypressS('','Giskaðu á einhvern staf'))
    print(b.GetKeypressS('','Press any key'))


