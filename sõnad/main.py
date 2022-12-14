from random import * 
import os
import string

print()
print()
print("Et mängida, tuleb sisestada kindlas pikkuses sõnu.")
print("Peale igat arvamist tekivad kaks veergu, vasakus on")
print("sinu arvamine ning paremas on lahendus. Lahenduses X")
print("tähendab, et antud samal positsioonil olevad tähed")
print("ei kattu ning lõpplahenduses sellist tähte ei ole.")
print("Kui lahendusse tekib suur täht nt. A, siis see tähendab,")
print("et antud täht eksisteerib kuskil lahendis. Ning kui")
print("lahendisse ilmub väike täht nt. a, siis see tähendab, et")
print("täht on õiges asendis.")
print()
print()

a = "a"
"""
todo list:
mäng() commentis olevad asjad
teha funktsioon, mis loeb failist kasutaja andmed (võidud, mängude arv, punktid), samuti teha funktsioon, mis iga mängu
    lõpus salvestab uuenenud andmed faili.

teha mingi lihtne achievementi fail, mis pmst checkib eelmist faili (nt kui kogu võitude arv > 10 siis on achievement)
    ning kuidagi võimalus väljaprintida olemasolevad achievementid

tuleks läbitöödelda kõik sõna failid, teha igast kaks 
    ühes kõik võimalikud pakkumised(pmst praegune fail, aga neis mõned vigased), 
    teises kõik võimalikud sõnad, mida mäng kasutab tundmatuna



kui on valmis cmdl töötav worlde siis see viia üle pygame GUI



"""




võit = 0
kaotus = 0
def mäng():
    tähed = [x for x in string.ascii_lowercase]
    tähed.append("õ")
    tähed.append("ä")
    tähed.append("ö")
    tähed.append("ü")
    while True:
        try:
            tähtede_arv = int(input("Mitme tähega tahad mängida (4,5,6): "))
            if tähtede_arv == 4 or tähtede_arv == 5 or tähtede_arv == 6:
                break
            else:
                print("Palun sisestage arv 4st-6ni. (x, et väljuda).")

            

        except:
            return True

    fail = "sonad" + str(tähtede_arv) + ".txt"
    sõnad = open(fail, "r", encoding="utf-8").read().splitlines()
    sõnad.append("ssssss")
    sõnad.append("sssxxx")
    

    sõna = [*choice(sõnad)]
    
    arvamine = [[],[],[],[],[],[]]
    pakkumised = [[],[],[],[],[],[]]

    for i in range(6):
        for j in range(tähtede_arv):
            arvamine[i].append("X")
            pakkumised[i].append("X")

    for x in range(6):
        
        sona_sageuds = dict()
        for i in sõna:
            if i in sona_sageuds:
                sona_sageuds[i] += 1
            else:
                sona_sageuds[i] = 1

        while True:
            pakkumine = input("Tee pakkumine: ")
            if pakkumine in sõnad and len(pakkumine) == tähtede_arv:
                break
            elif pakkumine in sõnad and len(pakkumine) != tähtede_arv:
                print("Sisestasite vales pikkuses sõna.")
            else:
                print("Antud sõna ei eksisteeri.")

        """
        samuti teha ka see, mis näitab, mis tähed on kasutatud ja mida veel ei ole
        samuti tuua sõna genereemine funktsiooni sisse
        
        """
        pak = [*pakkumine.lower()] #Teeb sõne järjendiks ("auto" -> ["a", "u", "t", "o"])
        pak_sagedus = dict()
        for i in pak:
            if i in pak_sagedus:
                pak_sagedus[i] += 1
            else:
                pak_sagedus[i] = 1
        pakkumised[x] = pak

   

        if pakkumine in sõnad: 
            for i in range(len(pak)):       
                if pak[i] == sõna[i]:        
                    arvamine[x][i] = pak[i]
                    sona_sageuds[pak[i]] -= 1
            
            for i in range(len(pak)):
                if pak[i] in sõna and pak[i] != sõna[i] :
                    if sona_sageuds[pak[i]] == 0:
                        arvamine[x][i] = "X"
                    else:
                        arvamine[x][i] = pak[i].upper()


        if arvamine[x] == sõna:
            global võit
            võit += 1
            print("Olete võitnud")
            return True


        os.system("cls")
        for i in range(len(pakkumised)):
            if x == i:
                print("".join(pakkumised[i]) + " <----------> " + "".join(arvamine[i]))
            else:
                print("".join(pakkumised[i]) + "              " + "".join(arvamine[i]))
        for i in pak:
            try:
                tähed.remove(i)
            except:
                continue
        print("\nTähed kasutamata:")
        print(*tähed)
        print()

    print("Kaotasite")
    a = ""
    global kaotus
    kaotus += 1
    for i in sõna:
        a += i
    print("Õige vastus on: ", a)


        
k = 1
while True:
    mäng()
    edasi = input("Kas tahate edasi mängida? (j/e): ")
    if edasi == "j":
        k += 1
        continue
    elif edasi == "e":
        break

mitu_mängu = k
if mitu_mängu == 1:
    print("Mängitud on 1 mäng.")
else:
    print("Mängitud on", mitu_mängu, "mängu.") 
print("Võitsite", võit, "mängu, kaotasite", kaotus, "mängu.")


