from random import * 
import os
import string




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





def mäng():
    tähed = [x for x in string.ascii_lowercase]
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
    print("Õige vastus on: ", *sõna)


        

while True:
    mäng()
    edasi = input("Kas tahate edasi mängida? (j/e): ")
    if edasi == "j":
        continue
    elif edasi == "e":
        break
