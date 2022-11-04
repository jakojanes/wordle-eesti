from random import * 
import os


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
    sõnad.append("iiii")
    

    sõna = [*choice(sõnad)]
    #sõna = [*"petetu"]   #baaba
    arvamine = [[],[],[],[],[],[]]
    pakkumised = [[],[],[],[],[],[]]


    for i in range(6):
        for j in range(tähtede_arv):
            arvamine[i].append("X")
            pakkumised[i].append("X")

    for x in range(6):
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
        pakkumised[x] = pak
        index = 0  


        if pakkumine in sõnad: #vaatab kas antud pakkumine on sõna, mida võib pakkuda
            for i in range(len(pak)):       
                if pak[i] == sõna[i]:        #h == l False
                    arvamine[x][i] = pak[i]
                elif pak[i] in sõna:  #True
                    
                    sõna_count = 0 
                    sõna_olemas = 0 #1
                    
                     #4
                    for k in sõna:  #l u h t
                        if k == pak[i]:  #pak[i] h == h
                            sõna_olemas += 1
                            

                    for k in sõna:
                        if k == sõna[i]:
                            sõna_count += 1

                    # [a s e t u s]   [p e t e tu]
                    
                    print(sõna_count, sõna_olemas)
                    print(arvamine[x].count(pak[i]))
                    print(arvamine[x])
                    
                    if sõna_count > sõna_olemas and (arvamine[x].count(pak[i]) > sõna_olemas or arvamine[x].count(pak[i]) == 0):
                        arvamine[x][i] = pak[i].upper()
                    elif sõna_count == sõna_olemas:
                        a = False
                        for p in range(len(pak)):
                            if pak[p] == sõna[p]:
                                a = True
                        if a == True:
                            
                            arvamine[x][i] = "X"
                        else:
                            arvamine[x][i] = pak[i].upper()
                    else:
                        
                        arvamine[x][i] = "X"


        else:
            print("pole")


        if arvamine[x] == sõna:
            print("Olete võitnud")
            return True


        os.system("cls")
        for i in range(len(pakkumised)):
            if x == i:
                print("".join(pakkumised[i]) + " <----------> " + "".join(arvamine[i]))
            else:
                print("".join(pakkumised[i]) + "              " + "".join(arvamine[i]))

    print("Kaotasite")
    print(sõna)


        

while True:
    mäng()
    edasi = input("Kas tahate edasi mängida? (j/e): ")
    if edasi == "j":
        continue
    elif edasi == "e":
        break
