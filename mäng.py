from random import *
from string import *
import pygame

#loen kõik võimalikud sõnad listi, ning valin suvalise
fail = "sonad5.txt"
sõnad = open(fail, "r", encoding="utf-8").read().splitlines()
vastus = choice(sõnad).upper()
print(vastus)


pygame.init()
pygame.font.init()


#parameetrid, et joonistada mängu aken, ja ruudud jne
laius = 600
pikkus = 700
vahe = 10
vahe2 = 100
ruudusuurus = (laius-4*vahe-2*vahe2) // 5 
screen = pygame.display.set_mode((laius,pikkus))
font = pygame.font.SysFont("free sans bold", ruudusuurus-1)
font2 = pygame.font.SysFont("free sans bold", 42)


HALL = (70,70,70)
ROHELINE = (6, 214, 160)
KOLLANE = (255,209,102)

pakkumine = ""
vastused = []
tähestik = ascii_lowercase + "öäüõ"
tähti_mitte_pakutud = tähestik
mäng_läbi = False

#pygame parameetrid

pygame.display.set_caption("Wordle")

def kasti_värv(pak, m):
    täht = pak[m]
    if täht == vastus[m]:
        return ROHELINE
    elif täht in vastus:
        mitu_õiget = vastus.count(täht)
        mitu_olemas = 0
        mitu_esineb = 0
        for i in range(5):
            if pak[i] == täht:
                if i <= m:
                    mitu_esineb += 1
                if täht == vastus[i]:
                    mitu_olemas += 1
        if mitu_õiget - mitu_olemas - mitu_esineb >= 0:
            return KOLLANE
    return HALL


#pygame akna visualiseerimine
visualiseerimine = True
while visualiseerimine:

    screen.fill("white")
    """
    #kuvan tähestiku
    tähed = font2.render(tähti_mitte_pakutud.upper(), False, HALL)
    surface = tähed.get_rect(center = (laius//2, vahe2//2))
    screen.blit(tähed, surface)
"""
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
        surface = tähed.get_rect(center = (laius//2,pikkus-vahe2/2))
        screen.blit(tähed, surface)
#ekraani uuendamine
    pygame.display.flip()

    #main mängu loop
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
                    mäng_läbi = True if vastus == pakkumine else False
                    pakkumine = ""


            elif sündmus.key == pygame.K_SPACE:
                mäng_läbi = False
                vastus = choice(sõnad).upper()
                vastused = []
                tähestik = ascii_lowercase + "öäüõ"
                tähti_mitte_pakutud = tähestik
                pakkumine = ""


            #panen vastuse võrduma mängija pakkumisega
            elif len(pakkumine) < 5 and not mäng_läbi:
                pakkumine = pakkumine + sündmus.unicode.upper()
                print(pakkumine)

            

                