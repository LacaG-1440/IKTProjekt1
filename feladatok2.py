#Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
#felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
#a megadott szám értéke!

def feladat0():
    szam=-1
    while szam < 0 or szam >20:
        szam = int(input("Adj meg egy 20-nál nem nagyobb pozitív számot: "))
            
        print((szam-1)*(" "),"START")

#feladat0()

#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
#összege! 

def teszt1():

    szam = int(input("Adj meg egy pozitív számot: "))
    osszeg=0

    while (szam >= 0):
        
        osszeg=osszeg+szam
        szam=szam-1 

    print(osszeg)

#teszt1()


#Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
#képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!

def teszt2():

    szoveg = input("Írd be a szöveget: ")

    i = 0
    while i < len(szoveg):
        karakter = szoveg[i]
        print(karakter)
        i += 1

#teszt2()


#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
#pontosan a megadott szám legyen! 

def teszt3():

    szam=int(input("Írd be a számot: "))

    for i in range(int(szam/2)):
        print("0")
        print("1")
    if szam % 2 == 1:
        print("0")

#teszt3()

#Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
#számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
#értékek között helyezkednek el!

def teszt4():
    szamKisebb=int(input("Írd be a kisebb számot: "))
    szamNagyobb=int(input("Írd be a nagyobb számot: "))

    kulonbseg=szamNagyobb-szamKisebb

    e = 1
    while e <= (kulonbseg-1):
        szamKisebb = szamKisebb + 1
        e = e + 1
        print(szamKisebb)

#teszt4()


#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
#a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
#téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!


def teszt5():

    N_Param=int(input("Kérem N értékét: "))
    M_Param=int(input("Kérem N értékét: "))

    def progi(N,M):
        for i in range(N):
            for j in range(M):
                print("*",end="")
            print()

    progi(N_Param,M_Param)

teszt5()