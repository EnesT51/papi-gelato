vraag = ''
smaak = ''

prijsbolletjes = 1.10
prijsbakje = 0.75
prijshorrentjes = 1.25

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
                toppingstotaal +=caramelB
        else:
            sorry()
            repeat = True
            
def bon():
    global totaalbollen,toppings
    totaalbollen += vraag
    totaal1 = totaalbollen * prijsbolletjes
    totaal2 = aantalbak * prijsbakje
    totaal3 = aantalhoorn * prijshorrentjes
    totaal = (totaalbollen * prijsbolletjes + aantalbak * prijsbakje + aantalhoorn * prijshorrentjes + toppings1 * toppingstotaal)

    print("------------[Papi Gelato]-------------")
    print("Bollentjes",totaalbollen , "x" , prijsbolletjes, "=" , "€", format(totaal1,".2f"))
    if aantalhoorn >0:
        print("Hoornje",aantalhoorn , "x" , "€" , totaal3)
    else:
        None
    if aantalbak >0:
        print("Bakje",aantalbak , "x" , "€" , totaal2)
    else:
        None
    if toppings1 >0:
        print("Topping", toppings1, "x" , "€" , toppingstotaal)
    else:
        None
    print("------------------------------------------------")
    print("Totaal" , "€" , format(totaal ,".2f"),"betalen")
    
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
        global vraag,smaak,aantalbak,aantalhoorn,caramelH,caramel_bakje
        vraag2 = input('Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje? '.format(vraag)).lower()
        if vraag2 =='a' or vraag2 =='A':
            return "hoorntje"

        elif vraag2 =="b" or vraag2 == "B":
            return "bakje"
           
        else:
            sorry()
            hoorntje_bakje()
            return

def bolletjes_stap1():
    global vraag, aantalbak
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
while actief == True:
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

bedankt()
bon()


