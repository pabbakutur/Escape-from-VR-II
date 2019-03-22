class Bord4:
    def __init__(self):
        print('''****************************************
        *            Nú er Lexi að              *
        * Nú er Lexi að safna heimaverkefnisínu!*
        *    til að geta farið heim að læra.    *
        *         Hjálpaðu honum að             *
        *       leita í tölvustofunin           *
        ****************************************
        ''')
        self.hlutir=2
        self.heisla = 3
        self.nesti = 0
        self.fullheisla = 3

        ## Game functions

        def checkstats(self):
            print('''

        ********''')
            print("Hlutir:", hlutir)
            print("Heisla:", heisla,"/",fullheisla)
            print("Heimaverkefni:", nesti)

        def prompt(self):
            x = input("Type a command: ")
            return x



        ##*********************************************************


        ## Gangur////

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

            command = prompt()
            if command == "1":
                lesstofa()
            elif command == "2":
                print("********")
                print ("Þú hefur byrjað uppá nýtt. (",fullheisla,"/",fullheisla,")")
                global heisla
                heisla = fullheisla
                gangur()
            elif command == "9":
                checkstats()
                gangur()
            else:
                gangur()


        ## lesstofa ////
        def lesstofa():
            print("****************************************")
            print ('''

         Þú er kominn á lesstofa. Það er nokkri ennþá að læra.
            ''')

            print('''Valkostir:
        1. Fara framm á gang
        2. Fara niður í stigllastofuna
        3. Fara í hópavinnustofuna
        9. Staða
        ''')
            command = prompt()
            if command == "1":
                gangur()
            elif command == "2":
                stiglaas()
            elif command == "3":
                hopav()
            elif command == "9":
                checkstats()
                lesstofa()
            else:
                lesstofa()








        ## stigllastofuna ////
        def stiglaas():
            print('''****************************************

        Hann Lexi labbaði inní stigllastofuna.
            ''')

            ## Þetta gerist þegar maður fer í fyrsta skipti inní stigllastofuna
            global heisla
            if heisla > 0:
                print('''********
        Stæfræði stigllar ráðast á Lexa með Sundurleitnisetningin II
        og hann meiðist
        (-1 heilsa)


        ''')### missir líf
                heisla = heisla - 1
                #heilsan fer niður



            ##Þetta gerist ef þú kemur í annaðskiptið
            if heisla > 0:

                print('''Valkostir:
        Ertu viss um þú viljir fara aftur inní stigllastofuna
        1. Fara fram á gang
        2. Fara inn í stigllastofuna
        3. Fara inná prófissorskrifstofuna
        9. Stats
            ''') ##It gives you your options
                command = prompt()
                if command == ("1"):
                  gangur()
                elif command == ("2"):
                  stiglaas()
                elif command == "3":
                    skrifstofu()
                elif command == "9":
                  checkstats()
                  stiglaas()
                else:
                  stiglaas()






        ## Coast
        def hopav():
            print ('''****************************************

        Þú ert kominn í góðra vinahóp í hópavinnustofuni
            ''')
            print ('''Valkostir:
        1. Fara fram á gang
        2. Tala við strákan
        3. Athuga hvort ég geti komist út
        9. Stats''')
            command = prompt()
            if command == "1":
                gangur()
            elif command == "2":
                strakar()
            elif command =="3":
                boatconvo()
            elif command =="9":
                checkstats()
                hopav()
            else:
                hopav()


        ##City
        def heim():
                print('''****************************************
            Þú komst heim.
                 ''')





        ## prófissorskrifstofuna//////////
        def skrifstofu():
            print('''****************

        Nú hafa helstu prófessorar Stæfræðinnar komið að þér
        ''')

            print('''1. Hlaupa fram á gang
        2. Reyna leysa heildið sem þeir leggja fyrir þig
        3. Reyna vera vinur Rögga Möller og Ragnar S''')
            command = prompt()
            if command == "1":
                gangur()
            elif command == "2":
                print('''
        *********''')
                print("Því miður var heildið alltof flókið og Lexi nær ekki að leysa ")
                print("og festi í skólanum að leysa það")
                print('''

        Þú tapaðir!!!!!''')
            elif command == "3":
                print('''
        *********''')
                print("Þú festi í skólanum við að lesa bókina hans Ragga og chilla með")
                print("Rögga Möller og kemst ekki heim")
                print('''


        Þú tapaðir!!!!!''')



        ##Training//////////////
        def strakar():
            print('''********

        Áttu heimaverkefni til að deila til að geta fengið frá þeim?

        1. Já
        2. nei''')
            global nesti
            command=prompt()
            if command == "1" and nesti <2:
                nesti = nesti + 1
                print('''********
        Þú átt fleir heimaverkefni."
        (+1 heimaverkefni)
        ''')
                hopav()
            elif command == "1" and nesti >1:
                print('''********
        Þú átt nó af heimaverkefni."
                ''')
                hopav()
            elif command == "2":
                print(''' ********
        Strákar: gangi þér vel þú fræð ekki að herma eftir okkur."
        ''')
                hopav()
            else:
                hopav()


        def boatconvo():
            print('''********
        Deildarstjóri: Hefur efni á að fara heima?"

        1. Já Lexi er búinn með nóg af heimaverkefnum
        2. Nei
        ''')
            command = prompt()
            if command == "1" and nesti > 1:
                print('''********
                Lexi getur farið heim.
        ''')
                heim()
            if command == "1" and nesti < 2:
                print('''********
                Lexi hefur ekki klárað nó af heimavinnuna
        ''')
                gangur()
            elif command =="2":
                gangur()


    #    bord3()
