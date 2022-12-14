from random import *
from string import *
import pygame


#funktsioonid, et lugada andmeid ning neid salvestada
def loe_failist():
    f = open("andmed.txt").read().splitlines()
    for i in range(len(f)):
        f[i] = int(f[i])
    return f

andmed = loe_failist()
#andmed = [mängitud, võidud, kaotused]

def kirjuta_faili(list):
    f = open("andmed.txt", "w")
    for i in list:
        f.write("{}".format(i))
        f.write("\n")

    f.close()

#loen kõik võimalikud sõnad listi, ning valin suvalise
fail = "sonad5.txt"
sõnad = open(fail, "r", encoding="utf-8").read().splitlines()
vastus = choice(sõnad).upper()
print(vastus)

#initaliseerin pygame
pygame.init()
pygame.font.init()


#parameetrid, et joonistada mängu aken, ja ruudud jne
laius = 600
pikkus = 700
vahe = 10
vahe2 = 100
ruudusuurus = 72
screen = pygame.display.set_mode((laius,pikkus))
font = pygame.font.SysFont("free sans bold", ruudusuurus-1)
font2 = pygame.font.SysFont("free sans bold", 42)
font3 = pygame.font.SysFont("free sans bold", 15)

#värvi ja muud vajalikud variabelid
HALL = (70,70,70)
ROHELINE = (6, 214, 160)
KOLLANE = (255,209,102)
pakkumine = ""
vastused = []
tähestik = ascii_lowercase + "öäüõ"
tähti_mitte_pakutud = tähestik.upper()
mäng_läbi = False
võit = False


#funktsioon, et arusaada, mis tähed on kasutatud
def eemalda_tähed(pak):
    
    pak
    pak_list = []
    for i in pak:
        if i not in pak_list:
            pak_list.append(i)

    tähti_mitte_pakutud_list = []
    for i in tähti_mitte_pakutud:
        tähti_mitte_pakutud_list.append(i)

    for i in pak_list:
        if i in tähti_mitte_pakutud_list:
            tähti_mitte_pakutud_list.remove(i)

    a = "".join(tähti_mitte_pakutud_list).upper()



    return a


#Mis värvi tuleb kast värvida? loogika põhineb main.py loopil ning 
def kasti_värv(pak, m):
    täht = pak[m]
    if täht == vastus[m]:
        return ROHELINE
    elif täht in vastus:
        mitu_esineb_vastuses = vastus.count(täht)
        mitu_esineb_pakkumises_õigel = 0
        mitu_on_olnud = 0
        for i in range(5):
            if pak[i] == täht:
                if i <= m:
                    mitu_on_olnud += 1
                if täht == vastus[i]:
                    mitu_esineb_pakkumises_õigel += 1
        if mitu_esineb_vastuses - mitu_esineb_pakkumises_õigel - mitu_on_olnud >= 0:
            return KOLLANE
    return HALL


#pygame akna visualiseerimine
visualiseerimine = True
while visualiseerimine:

    screen.fill("white")

    #kuvan tähestiku
    tähed = font2.render(tähti_mitte_pakutud.upper(), False, HALL)
    surface = tähed.get_rect(center = (laius//2, vahe2//2))
    screen.blit(tähed, surface)


    #kuvan mängitud, võidetud mängude arvu
    mängitud_tekst = font3.render("MÄNGE MÄNGITUD:", False, HALL)
    surface = mängitud_tekst.get_rect(center = (50, 120))
    screen.blit(mängitud_tekst, surface)

    mängitud = font2.render(str(andmed[0]), False, HALL)
    surface = mängitud.get_rect(center = (50, 120+30))
    screen.blit(mängitud, surface)


    võidetud_tekst = font3.render("MÄNGE VÕIDETUD:", False, ROHELINE)
    surface = võidetud_tekst.get_rect(center = (50, 120+ruudusuurus+vahe))
    screen.blit(võidetud_tekst, surface)

    võidetud = font2.render(str(andmed[1]), False, ROHELINE)
    surface = võidetud.get_rect(center = (50, 120+ruudusuurus+vahe+30))
    screen.blit(võidetud, surface)


    #joonistan ekraanile ruudud ja pakkumised
    y = vahe2
    for i in range(6):
        x = vahe2
        for j in range(5):
            ruut = pygame.Rect(x, y, ruudusuurus, ruudusuurus)
            pygame.draw.rect(screen, HALL, ruut, width=2)
            




            #tähtede kuvamine
            if i < len(vastused):
                värv = kasti_värv(vastused[i], j)
                pygame.draw.rect(screen, värv, ruut)
                täht = font.render(vastused[i][j], False, (255,255,255))
                surface = täht.get_rect(center = (x+ruudusuurus//2,y+ruudusuurus//2))
                screen.blit(täht, surface)

            #tähtede kuvamine kirjutamise ajal
            if i == len(vastused) and j < len(pakkumine):
                täht = font.render(pakkumine[j], False, HALL)
                surface = täht.get_rect(center = (x+ruudusuurus//2,y+ruudusuurus//2))
                screen.blit(täht, surface)

            x = x + ruudusuurus + vahe
        y = ruudusuurus + vahe + y


    #mäng läbi ja vastuse kuvamine
    if len(vastused) == 6 and vastused[5] != vastus:
        
        mäng_läbi = True
        tähed = font.render(vastus, False, ROHELINE)
        surface = tähed.get_rect(center = (laius//2,(pikkus-vahe2/2)-20))
        screen.blit(tähed, surface)
#ekraani uuendamine
    pygame.display.flip()

    #sündmuste kuulamine
    for sündmus in pygame.event.get():


        #ekraani sulgemine
        if sündmus.type == pygame.QUIT:
            visualiseerimine = False

        #mängija klaviatuuri vajutused
        elif sündmus.type == pygame.KEYDOWN:

            if sündmus.key == pygame.K_BACKSPACE:
                if len(pakkumine) > 0:
                    pakkumine = pakkumine[:len(pakkumine)-1]


            elif sündmus.key == pygame.K_RETURN:
                if len(pakkumine) == 5 and pakkumine.lower() in sõnad:
                    vastused.append(pakkumine)
                    tähti_mitte_pakutud = eemalda_tähed(pakkumine)
                    if vastus == pakkumine:
                        mäng_läbi = True
                        võit = True
                        andmed[0] = andmed[0] + 1
                        andmed[1] = andmed[1] + 1
                        print(andmed)
                        kirjuta_faili(andmed)
                        
                    else:
                        mäng_läbi = False
                    pakkumine = ""


            elif sündmus.key == pygame.K_SPACE:
                if võit == True:
                    mäng_läbi = False
                    vastus = choice(sõnad).upper()
                    print(vastus)
                    vastused = []
                    tähestik = ascii_lowercase + "öäüõ"
                    tähti_mitte_pakutud = tähestik.upper()
                    pakkumine = ""
                    võit = False
                else:
                    andmed[0] += 1
                    andmed[2] += 1
                    kirjuta_faili(andmed)
                    mäng_läbi = False
                    vastus = choice(sõnad).upper()
                    print(vastus)
                    vastused = []
                    tähestik = ascii_lowercase + "öäüõ"
                    tähti_mitte_pakutud = tähestik.upper()
                    pakkumine = ""


            #panen vastuse võrduma mängija pakkumisega
            elif len(pakkumine) < 5 and not mäng_läbi:
                pakkumine = pakkumine + sündmus.unicode.upper()
                print(pakkumine)

            

                