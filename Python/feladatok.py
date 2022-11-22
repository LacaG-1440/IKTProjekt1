import random

def feladat1():
    napod=input("jó napod van?")

    if napod=="Igen":
        print("Örülök neki!")
    elif napod=="Nincs":
        print("Nem örülök neki!")
    else:
        print("Sajnos nem értem a válaszodat!")
#feladat1()

def feladat2():

    try:   
        number=int(input("Kérem a számot!"))

        if number%2==0:
            print("A szám páros")
        else:
            print("A szám páratlan")

    except:
            print("Nem jó értéket adtál meg!")

#feladat2()

def feladat3():
    try:
        rnd=random.randrange(1,6)

        number=0

        while number<1 or number>5:

            number=int(input("Kérem a számod"))

        print(rnd)

        if rnd>number:
            print("Nagyobb a generált szám")
        elif rnd<number:
            print("Kisebb a generált szám")
        else:
            print("Eltaláltad")
    except:
        print("Nem jó formátum.")

#feladat3()

def ciklus1():
    for i in range(1,11):
        if(i%2==0):
            print (i)

#ciklus1()

def ciklus2():
    for i in reversed(range(1,11)):
        print (i)
        
#ciklus2()

def ciklus3():
    for i in range(10,0,-1):
        if i%2!=0:
            print (i)
#ciklus3()

def ciklus4():
    number=int(input("Kérem az ismétlések számát"))
    text=input("Kérem az ismétlődő szöveget")

    for i in range(number):
        print(text)
#ciklus4()

def ciklus5():

    number=1

    while number%2!=0:
        number=int(input("Kérek egy számot"))

#ciklus5()

def ciklus6():
    db=0
    for i in range(20):
        rnd=random.randrange(1,13)
        if (rnd%3==0):
            print(rnd)
            db=db+1
    
    print("A 3-mal osztható számok száma: "+str(db))
ciklus6()