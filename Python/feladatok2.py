#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legkisebb értéket ezek közül!

def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))

    tomb.sort()
    print(tomb[0])

#feladat1()

# Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legnagyobb értéket ezek közül!

def feladat2():
    tomb =[]
    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))

    print(max(tomb))

#feladat2()

def feladat1_2():
    tomb =[]
    
    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))

    print(f"A legkisebb elem: {min(tomb)} ")
    print(f"A legnagyobb elem: {max(tomb)} ")

    print("A legkisebb elem: "+str(min(tomb)))
    print("A legnagyobb elem: "+str(max(tomb)))

#feladat1_2()


#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
#érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

def feladat3():
    pontszam = -1

    while pontszam < 0 or pontszam > 100:
        pontszam =int(input("Add meg a dolgozat pontszámát:"))    
    if pontszam<50:
        print("Elégtelen")
    elif pontszam<60:
        print("Elégséges")
    elif pontszam<70:
        print("Közepes")
    elif pontszam<85:
        print("Jó")
    else:
        print("Jeles")

#feladat3()

# Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
#hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

def feladat4():
    oszthato = False

    szam = int(input("Kérek egy számot: "))

    if szam % 3 == 0 or szam % 5 ==0:
        osztahto=True

    if oszthato ==True:
        print("Igen.")
    else:
        print("Nem.")

#feladat4()

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
#hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

def feladat5():
    a=int(input("Kérem a értékét: "))
    b=int(input("Kérem b értékét: "))
    c=int(input("Kérem c értékét: "))
    
    van=False
    if (a+b)==c:
        van=True

    if (a+c)==b:
        van=True

    if (c+b)==a:
        van=True
    
    if van:
        print("Van ilyen szám!")
    else:
        print("Nincs ilyen szám!")

#feladat5()

#Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
#képernyőre, hogy mind a három páros szám-e (igen/nem)!

def feladat6():
    a=int(input("Kérem a értékét: "))
    b=int(input("Kérem b értékét: "))
    c=int(input("Kérem c értékét: "))

    van=False
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        van=True

    if van:
        print("Az összes páros!")
    else:
        print("Van köztük páratlan!")

#feladat6()

def feladat6_1():
    szamok=[]
    j=1
    db=0
    
    for i in range(3):
        szamok.append(int(input(f"Kérem a(z) {j} számot: ")))
        j=j+1

    for i in szamok:
        if i%2 == 0:
            db=db+1
        else:
            break

    if db == 3:
        print("Az összes páros!")
    else:
        print("Van köztük páratlan!")
        
#feladat6_1()


#Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
#kiírja őket a képernyőre!

def feladat7():
    tomb=[]

    for i in range(2):
        tomb.append(input("Kérem a szót: "))

    tomb.sort()

    for i in range(2):
        print(tomb[i])

#feladat7()