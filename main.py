import json
import random

from classes.Ellenfel import Ellenfel
from classes.Jatekos import Jatekos


def kockadobas():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if duplakockadobas() <= Jatekos.Luck:
        Jatekos.minuszluck(1)
        return True
    else:
        Jatekos.minuszluck(1)
        return False


def igenvagynem():
    while True:
        inp = input("igen vagy nem")
        if inp == "igen":
            return True
        elif inp == "nem":
            return False


def harc(name, hp, ugyesseg):
    while hp > 0 or Jatekos.HP > 0:
        EllensegAttackSTR = duplakockadobas() + ugyesseg  # 1.lépés
        JatekosAttackSTR = duplakockadobas() + Jatekos.Skill  # 2.lépés

        if EllensegAttackSTR < JatekosAttackSTR:
            hp - 2
            print("Megsebezted az ellenfelet!")
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést ejtettél!")
                    hp - 2
                else:
                    print("A seb puszta karcolás!")
                    hp + 1
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.HP = Jatekos.HP - 2
            print("Az ellenfél megsebzett téged!")
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést Kaptál!")
                    Jatekos.HP = Jatekos.HP - 2
                else:
                    print("A seb puszta karcolás!")
                    Jatekos.HP = Jatekos.HP + 1
        else:
            print("Kivédtétek egymás ütését!")
        print(f"{name} Életereje: {hp}")
        print(f"Játékos Életereje: {Jatekos.HP}")


def igenvagynem():
    print("igen vagy nem?")
    while True:
        inp = input()
        if inp == "igen":
            return True
        elif inp == "nem":
            return False
        else:
            print("Hibás bemenet")


def harc():
    while True:
        EllensegAttackSTR = duplakockadobas() + Ellenfel.ugyesseg  # 1.lépés
        JatekosAttackSTR = duplakockadobas() + Jatekos.Skill  # 2.lépés

        if EllensegAttackSTR < JatekosAttackSTR:
            Ellenfel.hpmod(-2)
            print("Megsebezted az ellenfelet!")
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést ejtettél!")
                    Ellenfel.hpmod(-2)
                else:
                    print("A seb puszta karcolás!")
                    Ellenfel.hpmod(+1)
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.jatekosSebzes(2)
            print("Az ellenfél megsebzett téged!")
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést Kaptál!")
                    Jatekos.jatekosSebzes(2)
                else:
                    print("A seb puszta karcolás!")
                    Jatekos.jatekosHeal(1)
        else:
            print("Kivédtétek egymás ütését!")
        print(f"{Ellenfel.name} Életereje: {Ellenfel.HP}")
        print(f"Játékos Életereje: {Jatekos.HP}")
        if Jatekos.HP < 1:
            print("nem nyertel")
            return False
        elif Ellenfel.HP < 1:
            print("nyertel")
            return True


Nyert = False

input("új játék inditásához gépeljen be bármit: ")

Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)  # HP Luck Skill Gold

with open("Kaland.json", "r", encoding="utf-8") as jsn:
    advDict = json.load(jsn)

if advDict['kaland'][Jatekos.lokacio]['akcio'] == "tortenetkezdes":
    Jatekos.tortenetkezdes()

while not Nyert:
    print(advDict['kaland'][Jatekos.lokacio]['szoveg'])
    StartInp = input("Folytatáshoz nyomjon entert vagy írjon be egy commandot [statok, kilepes]: ")
    if StartInp == "statok":
        print(Jatekos)
    elif StartInp == "kilepes":
        exit()

    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "eleterovesztes":
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "szerencsevesztes":
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])

    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "harc":
        Ellenfel = Ellenfel(advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                            advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                            advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg'])
        harc()

    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif advDict['kaland'][Jatekos.lokacio]['akcio'] == "gameoever":
        Nyert = False
        Jatekos.gameover()
        break
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "pluszlebeges":
        Jatekos.pluszitem("Lebegés Köpenye")
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "hplossrng":
        Jatekos.jatekosSebzes(kockadobas())

    if len(advDict['kaland'][Jatekos.lokacio]['ugras']) == 1:
        Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][0])
    elif len(advDict['kaland'][Jatekos.lokacio]['ugras']) > 1:
        print("Merre szeretne haladni?")
        while True:
            inp = input()
            if inp in advDict['kaland'][Jatekos.lokacio]['ugras']:
                Jatekos.lokaciovaltoztatas(inp)
                break

if not Nyert:
    print("Vesztettél!")
elif Nyert:
    print("Gratulálunk nyertél!")

# aranykulcs, gyuruproba [49], szerencsevesztes, 71
