vraag = ""
def begin():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is. ')

def sorry():
    print("sorry dat snap ik niet")
        
def grote():
    print("Sorry, zulke grote bakken hebben we niet")

def bestellen():
    vraag3 = input('wilt u nog meer bestellen Y/N:? ')
    if vraag3 == 'y' or vraag3 == 'Y'.lower():
        bolletjes_stap1()
    elif vraag3 == 'n' or vraag3 == 'N'.lower():
        bedankt()
        quit
    else:
        sorry()
        bestellen()

def bedankt():
    print("Bedankt en tot ziens!")

def vraagherhalen():
    global vraag
    vraag2 = input('Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje? '.format(vraag)).lower()
    if vraag2 =='a':
        print('Hier is uw hoorntje met {} bolletje(s).'.format(vraag))
        bestellen()
    elif vraag2 =='b':
        print("Hier is uw bakje met {} bolletje(s).".format(vraag))
        bestellen()
    else:
        sorry()
        vraagherhalen()
def bolletjes_stap1():
    global vraag
    vraag = int (input("Hoeveel bolletjes wilt u?: "))
    if vraag >=1 and vraag <=3:
        vraagherhalen()
    elif vraag >=4 and vraag <=8:
        print("Dan krijgt u van mij een bakje met {} bolletjes".format(vraag))

    else:
        grote()
        bolletjes_stap1()
#(----------------------------------funcions above---------------------------------------------------)
begin()
bolletjes_stap1()