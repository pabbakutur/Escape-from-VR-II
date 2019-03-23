class Bord4:
    def __init__(self):
        print('''****************************************
        *          Velkominn í borð 4!          *
        * Nú er Lexi að safna heimaverkefnisínu!*
        *    til að geta farið heim að læra.    *
        *         Hjálpaðu honum að             *
        *       leita í tölvustofunin           *
        ****************************************
        ''')
        self.hlutir=2
        self.heilsa = 3
        self.nesti = 0
        self.fullheilsa = 3

        ## Game functions

    def checkstats(self):
        print('''

    ********''')
        print("Hlutir:", self.hlutir)
        print("heilsa:", self.heilsa,"/",self.fullheilsa)
        print("Heimaverkefni:", self.nesti)

    def prompt(self):
        x = input("Veldu möguleika: ")
        return x

        ## Gangur
    def gangur(self):
        print("****************************************")
        print('''

        Lexi er á ganginum og er að reyna komast heim.
        Hvert á hann að fara?
            ''')
        print('''Valkostir:
        1. Fara á lesstofuna
        2. Byrja upp á nýtt
        9. Staða
        ''')

        command = self.prompt()
        if command == "1":
            self.lesstofa()
        elif command == "2":
            print("********")
            print ("Þú hefur byrjað uppá nýtt. (",self.fullheilsa,"/",self.fullheilsa,")")
            #global heilsa
            self.heilsa = self.fullheilsa
            self.gangur()
        elif command == "9":
            self.checkstats()
            self.gangur()
        else:
            self.gangur()
        return False

    ## lesstofa ////
    def lesstofa(self):
        print("****************************************")
        print ('''

     Þú ert kominn á lesstofa. Það er nokkrir ennþá að læra.
        ''')

        print('''Valkostir:
    1. Fara fram á gang
    2. Fara niður í stiglastofuna
    3. Fara í hópavinnustofuna
    9. Staða
    ''')
        command = self.prompt()
        if command == "1":
            self.gangur()
        elif command == "2":
            self.stiglaas()
        elif command == "3":
            self.hopav()
        elif command == "9":
            self.checkstats()
            self.lesstofa()
        else:
            self.lesstofa()

    ## stigllastofuna ////
    def stiglaas(self):
        print('''****************************************

    Hann Lexi labbaði inní stiglastofuna.
        ''')

        ## Þetta gerist þegar maður fer í fyrsta skipti inní stigllastofuna
        #global heilsa
        if self.heilsa > 0:
            print('''********
    Stærðfræði stiglar ráðast á Lexa með Sundurleitnisetningu II
    og hann meiðist og missir 1 líf.
    (-1 heilsa)''')### missir líf
            self.heilsa = self.heilsa - 1
            #heilsan fer niður

        ##Þetta gerist ef þú kemur í annaðskiptið
        if self.heilsa > 0:

            print('''Valkostir:
    Ertu viss um þú viljir fara aftur inní stiglastofuna
    1. Fara fram á gang
    2. Fara inn í stiglastofuna
    3. Fara inná skrifstofu prófessoranna
    9. Stats
        ''') ##It gives you your options
            command = self.prompt()
            if command == ("1"):
              self.gangur()
            elif command == ("2"):
              self.stiglaas()
            elif command == "3":
                self.skrifstofu()
            elif command == "9":
              self.checkstats()
              self.stiglaas()
            else:
              self.stiglaas()

    ## Coast
    def hopav(self):
        print ('''****************************************

    Lexi er kominn inn í hópavinnustofuna til vina sinna
        ''')
        print ('''Valkostir:
    1. Fara fram á gang
    2. Tala við strákana
    3. Athuga hvort Lexi komist út
    9. Stats''')
        command = self.prompt()
        if command == "1":
            self.gangur()
        elif command == "2":
            self.strakar()
        elif command =="3":
            self.boatconvo()
        elif command =="9":
            self.checkstats()
            self.hopav()
        else:
            self.hopav()

    ##City
    def heim(self):
            print('''****************************************
        Þú komst heim.
             ''')

    ## prófissorskrifstofuna//////////
    def skrifstofu(self):
        print('''****************

    Helstu prófessorar HÍ hópast að Lexa
    ''')

        print('''1. Hlaupa fram á gang
    2. Reyna leysa heildið sem þeir leggja fyrir þig
    3. Reyna vera vinur Rögga Möllers og Ragnars S''')
        command = self.prompt()
        if command == "1":
            self.gangur()
        elif command == "2":
            print('''
    *********''')
            print("Því miður var heildið alltof flókið og Lexi nær ekki að leysa það ")
            print("Sigurður Freyr tekur upp bók Ragnars og grýtir henni í andlit Lexa sem deyr samstundis")
            print('''

    Þú tapaðir!!!!!''')
        elif command == "3":
            print('''
    *********''')
            print("Röggi Möller tekur upp bók Ragnars og les fyrir Lexa")
            print("Lexi dáleiðist samstundis og kemst aldrei heim")
            print('''Þú tapaðir!!!!!''')



    ##Training//////////////
    def strakar(self):
        print('''********

    Áttu heimaverkefni til að deila til að geta fengið önnur verkefni frá þeim?

    1. Já
    2. Nei''')
        #global nesti
        command = self.prompt()
        if command == "1" and self.nesti <2:
            self.nesti = self.nesti + 1
            print('''********
    Þú átt fleiri heimaverkefni."
    (+1 heimaverkefni)
    ''')
            self.hopav()
        elif command == "1" and self.nesti >1:
            print('''********
    Þú átt nóg af heimaverkefnum."
            ''')
            self.hopav()
        elif command == "2":
            print(''' ********
    Strákar: Gangi þér vel þú færð ekki að herma eftir okkur."
    ''')
            self.hopav()
        else:
            self.hopav()


    def boatconvo(self):
        print('''********
    Deildarstjóri: Jæja Lexi, ertu búinn með nóg af heimaverkefnum?"

    1. Já Lexi er búinn með nóg af heimaverkefnum
    2. Nei
    ''')
        command = self.prompt()
        if command == "1" and self.nesti > 1:
            print('''****************************************
            Lexi getur farið heim.''')
            self.heim()
        if command == "1" and self.nesti < 2:
            print('''********
            Lexi hefur ekki klárað nægilega mikið af heimaverkefnum
    ''')
            self.gangur()
        elif command =="2":
            self.gangur()


    #    bord3()
