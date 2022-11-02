from random import * 
import os



"""
todo list:
mäng() commentis olevad asjad
teha funktsioon, mis loeb failist kasutaja andmed (võidud, mängude arv, punktid), samuti teha funktsioon, mis iga mängu
    lõpus salvestab uuenenud andmed faili.

teha mingi lihtne achievementi fail, mis pmst checkib eelmist faili (nt kui kogu võitude arv > 10 siis on achievement)
    ning kuidagi võimalus väljaprintida olemasolevad achievementid





kui on valmis cmdl töötav worlde siis see viia üle pygame GUI



"""

while True:
    try:
        tähtede_arv = int(input("Mitme tähega tahad mängida (4,5,6): "))
        if tähtede_arv == 4 or tähtede_arv == 5 or tähtede_arv == 6:
            break
        else:
            print("Palun sisestage arv 4st-6ni. (x, et väljuda).")

        

    except:
        print()


fail = "sonad" + str(tähtede_arv) + ".txt"
sõnad = open(fail, "r", encoding="utf-8").read().splitlines()


sõna = [*choice(sõnad)]
arvamine = [[],[],[],[],[]]
pakkumised = [[],[],[],[],[]]


for i in range(5):
    for j in range(tähtede_arv):
        arvamine[i].append("X")
        pakkumised[i].append("x")


def mäng():
    for x in range(5):
        pakkumine = input("Tee pakkumine: ")

        """
        Siia vahele while loop, mis vaatab, kas pakutud sõna vastab parameetritele, on pakutavate sõnada failis jne...
        samuti teha ka see, mis näitab, mis tähed on kasutatud ja mida veel ei ole
        samuti tuua sõna genereemine funktsiooni sisse
        
        """
        pak = [*pakkumine] #Teeb sõne järjendiks ("auto" -> ["a", "u", "t", "o"])
        pakkumised[x] = pak
        index = 0  


        if pakkumine in sõnad: #vaatab kas antud pakkumine on sõna, mida võib pakkuda
            for i in range(len(pak)):       
                if pak[i] == sõna[i]:     
                    arvamine[x][i] = pak[i]
                    if sõna.count(pak[i]) > 1: #Vaatab kas antud tähte on rohkem, kui üks
                        index = i
                        for j in range(i+1,len(sõna)):
                            if sõna[j] == pak[i]:
                                if pak[i] == sõna[i]:
                                    if arvamine[x][i] == "X":
                                        pak[i] = arvamine[x][i]


                                else:
                                    if arvamine[x][i] == "X":
                                        arvamine[x][i] = pak[i].upper()


                elif pak[i] in sõna:
                    for j in range(len(sõna)):
                        if sõna[j] == pak[i]:
                            if arvamine[x][i] == "X":
                                arvamine[x][i] = pak[i].upper()


        else:
            print("pole")


        if arvamine[x] == sõna:
            print("Olete võitnud")
            return True


        os.system("cls")
        for i in range(len(pakkumised)):
            print("".join(pakkumised[i]) + "        " + "".join(arvamine[i]))


    print("Kaotasite")
    print(sõna)


        

while True:
    mäng()
    edasi = input("Kas tahate edasi mängida? (j/e): ")
    if edasi == "j":
        continue
    elif edasi == "e":
        break
