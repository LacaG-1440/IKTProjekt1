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

feladat2()