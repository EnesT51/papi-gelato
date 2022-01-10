vraag = 0
smaak = ''

prijsbolletjes = 1.10
prijsbakje = 0.75
prijshoorntjes = 1.25

aantalbak = 0
aantalhoorn = 0
totaalbollen = 0

slagroom = 0.50
sprinkels = 0.30
caramelH = 0.60
caramelB =0.90

toppings1 = 0
toppingstotaal = 0

def begin():
    print('Welkom bij Papi Gelato.')

def bedankt():
    print("Bedankt en tot ziens!")

def sorry():
    print("sorry dat snap ik niet")
        
def grote():
    print("Sorry, zulke grote bakken hebben we niet")


def nogmaals_bestellen():
    bestellen = input("wilt u nog een bestelling plaatsen? Y/N ")
    if bestellen == "y" or bestellen == "Y":
        return True
    elif bestellen == "n" or bestellen == "N":
        return False
    else:
        sorry()
        nogmaals_bestellen()

def particulier_zakelijk():
    herhaal2 = True
    while herhaal2:
        herhaal2 = False
        part_zakelijk = input("Bent u (A) zakelijk of (B) particuier? kies (A) voor zakelijk (B) voor particulier ")
        if part_zakelijk == "a" or part_zakelijk == "A":
            return part_zakelijk
        elif part_zakelijk == "b" or part_zakelijk == "B":
            return part_zakelijk

        else:
            sorry()
            herhaal2 = True

def zakelijkbon():
    prijsliterijs = 9.80
    totaal = (literijs * prijsliterijs)
    btw = (totaal/109*9)
    print("------------[Papi Gelato------------]")
    print("liter         {:.2f} x {:.2f}   = €{:.2f}".format((literijs), prijsliterijs,totaal))
    print("totaal                      = €{:.2f}".format(totaal))
    print("btw (9%)                    = €{:.2f}".format(btw))


def zakelijksmaken():
    global literijs
    literinhoud = 0
    literijs = int (input("hoeveel liter ijs wilt u hebben? "))
    for x in range (literijs):
        literinhoud +=1
        Zsmaken = input("Welke smaak wilt u voor {} literijs? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ".format(literinhoud))
        if Zsmaken == "a" or Zsmaken == "A":
            Zsmaken = "Aardbei"
        elif Zsmaken == "c" or Zsmaken == "C":
            Zsmaken = "Chocolade"
        elif Zsmaken == "m" or Zsmaken == "M":
            Zsmaken = "mint"
        elif Zsmaken == "v" or Zsmaken == "V":
            Zsmaken = "Vanille"
        else:
            sorry()
            zakelijksmaken()

def topping(bakje_hoorntje):
    repeat = True
    while repeat:
        repeat = False
        global toppings1,toppingstotaal
        toppings = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
        if toppings == "a" or toppings == "A":
            pass
        elif toppings == "b" or toppings == "B":
            toppings1+=1
            toppingstotaal += slagroom
        elif toppings == "c" or toppings == "C":
            toppings1+=1
            toppingstotaal += sprinkels
        elif toppings == "d" or toppings == "D":
            toppings1+=1
            if bakje_hoorntje == "hoorntje":
                
                toppingstotaal += caramelH
            else:
                toppingstotaal += caramelB
        else:
            sorry()
            repeat = True
            
def bon():
    global totaalbollen,toppings
    totaalbollen += vraag
    totaal1 = totaalbollen * prijsbolletjes
    totaal2 = aantalbak * prijsbakje
    totaal3 = aantalhoorn * prijshoorntjes
    totaal =  (totaal1 + totaal2 + totaal3 + toppingstotaal)

    print("------------[Papi Gelato]-------------")
    print("Bollentjes  {} x  = €{:.2f} = €{:.2f}  ".format(totaalbollen,prijsbolletjes,totaal1))
    if aantalhoorn >0:
        print("Hoornje {} x = €{}".format(aantalhoorn,totaal3))
    else:
        None
    if aantalbak >0:
        print("Bakje   {} x = €{}".format(aantalbak,totaal2))
    else:
        None
    if toppings1 >0:
        print("Topping {} x = €{:.2f}".format(toppings1,toppingstotaal))
    else:
        None
    print("------------------------------------------------")
    print("Totaal €{:.2f} betalen".format(totaal))
    
def bestellen():
    vraag3 = input('wilt u nog meer bestellen Y/N:? ')
    if vraag3 == 'y' or vraag3 == 'Y':
        return True
    elif vraag3 == 'n' or vraag3 == 'N':
        
        return False
    else:
        sorry()
        bestellen()

def hoorntje_bakje():
    herhaal = True
    while herhaal:
        herhaal = False
        vraag2 = input('Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje? '.format(vraag))
        if vraag2 =='a' or vraag2 =='A':
            return "hoorntje"

        elif vraag2 =="b" or vraag2 == "B":
            return "bakje"
           
        else:
            sorry()
            hoorntje_bakje()
            return

def bolletjes_stap1():
    vraag = int (input("Hoeveel bolletjes wilt u?: "))
    if vraag >=1 and vraag <=8:
        return vraag
  
    else:
        grote()
        bolletjes_stap1()

def smaken(aantalbolletjes):
    nummer = 0
    for i in range(aantalbolletjes):
        nummer+=1
        smaak = input('Welke smaak wilt u voor bolletje nummer {}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? '.format(nummer))
        if smaak == 'a' or smaak == 'A':
            smaak = 'Aardbei'
        elif smaak == 'c' or smaak == 'C':
            smaak = 'Chocolade'
        elif smaak == 'm' or smaak == 'M':
            smaak = 'Mint'
        elif smaak == 'v' or smaak == 'V':
            smaak = 'Vanille'
        else:
            sorry()
            smaken()

#(----------------------------------funcions above---------------------------------------------------)
begin()
actief = True
while actief:
    part_zakelijk = particulier_zakelijk()
    if part_zakelijk == "a" or part_zakelijk == "A":
        part_zak = zakelijksmaken()
        actief = nogmaals_bestellen()
        zakelijk_bon = zakelijkbon()
    else: 
        part_zakelijk == "b" or part_zakelijk == "B"
        bolletje = bolletjes_stap1()
        totaalbollen += bolletje
        if bolletje >=1 and bolletje <=3:
            keuze_hoorn_bakje = hoorntje_bakje()
        elif bolletje >= 3 and bolletje <=8:
            keuze_hoorn_bakje = "bakje"
        print("Dan krijgt u van mij een {} met {} bolletjes".format(keuze_hoorn_bakje,bolletje))
        if keuze_hoorn_bakje == "hoorntje":
            
            aantalhoorn +=1
        else:
            aantalbak +=1

        smaken(bolletje)
        topping(keuze_hoorn_bakje)
        actief = bestellen()
        bon()
bedankt()



