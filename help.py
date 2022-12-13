#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
#pontosan a megadott szám legyen! 

def teszt3():

    szam=int(input("Írd be a számot: "))

    for i in range(int(szam/2)):
        print("01")
    if szam % 2 == 1:
        print("0")

#teszt3()


#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
#a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
#téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!

def teszt5():
    N_Param=int(input("Kérem N értékét: "))
    M_Param=int(input("Kérem N értékét: "))

    def progi(N,M):
        for i in range(N):
            for j in range(M):
                print(",",end="")
            print()

    progi(N_Param,M_Param)

teszt5()

#ha simán bekérem a paramétereket:
def teszt5_5():
    N = int(input("Kérem N értékét: "))
    M = int(input("Kérem M értékét: "))

    for i in range(N):
        for j in range(M):
            print("*",end="")
        print()
#teszt5_5()


#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!"""

def feladat8():
    oszthato = False
    szamok=[]

    szam=0
    while szam>0:
        szam = int(input("Kérek egy számot: "))
        if szam % 3 == 0:
            oszthato = True

        if oszthato == True :
            szamok.append(szam)
        else:
            szam=szam-1
        print(szamok)
    
#feladat8()


#Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak! (beletartoznak a határolók)

def feladat9(n):
    szam1=int(input("Kérem az első számot: "))
    szam2=int(input("Kérem a második számot: "))

    if szam1>szam2:
        szamKisebb=szam2
        szamNagyobb=szam1
        kulonbseg=szamNagyobb-szamKisebb
        #print(kulonbseg)
        e = 1
        while e <= (kulonbseg-1):
            szamKisebb = szamKisebb + 1
            e = e + 1
        print(szamKisebb)


#feladat9()