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
        if Jatekos.combatblessed:
            JatekosAttackSTR = JatekosAttackSTR+1

        if EllensegAttackSTR < JatekosAttackSTR:
            Ellenfel.ellenfelsebzes(2)
            print("Megsebezted az ellenfelet!")
            if Jatekos.HP < 1:
                print("nem nyertel")
                return False
            elif Ellenfel.HP < 1:
                print("nyertel")
                return True
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést ejtettél!")
                    Ellenfel.ellenfelsebzes(2)
                else:
                    print("A seb puszta karcolás!")
                    Ellenfel.ellenfelheal(1)
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.jatekosSebzes(2)
            print("Az ellenfél megsebzett téged!")
            if Jatekos.HP < 1:
                print("nem nyertel")
                return False
            elif Ellenfel.HP < 1:
                print("nyertel")
                return True
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if not szerencseproba():
                    print("Súlyos sebzést Kaptál!")
                    Jatekos.jatekosSebzes(2)
                else:
                    print("A seb puszta karcolás!")
                    Jatekos.jatekosHeal(1)
        else:
            print("Kivédtétek egymás ütését!")
        print(f"{Ellenfel.name} Életereje: {Ellenfel.HP}")
        print(f"Játékos Életereje: {Jatekos.HP} \n")


Nyert = False
probaltemar = False
fellvettekopenyt = False
input("új játék inditásához gépeljen be bármit: ")

Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)  # HP Luck Skill Gold

with open("Kaland.json", "r", encoding="utf-8") as jsn:
    advDict = json.load(jsn)

if advDict['kaland'][Jatekos.lokacio]['akcio'] == "tortenetkezdes":
    Jatekos.tortenetkezdes()

while not Nyert:
    LepettEMar = False
    Jatekos.lokaciostr()
    print(advDict['kaland'][Jatekos.lokacio]['szoveg']+"\n")
    StartInp = input("Folytatáshoz nyomjon entert vagy írjon be egy commandot [statok, kilepes]: ")
    if StartInp == "statok":
        print(Jatekos)
    elif StartInp == "kilepes":
        exit()

#stat váltosztatások
    if "eleterovesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "hplossrng" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(kockadobas())
    if "szerencsevesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "Eleteronyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosHeal(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "szerencsenyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "luckblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosBlessing()
    if "combatblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosCombatBlessing()

#tárgy felvételek
    if "pluszlebeges" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Lebegés Köpenye")

#harc
    if "harc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Ellenfel = Ellenfel(advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                            advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                            advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg'])
        harc()

#győzelem vagy gameover detektálás
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif advDict['kaland'][Jatekos.lokacio]['akcio'] == "gameoever":
        Nyert = False
        Jatekos.gameover()
        break

#lépések
    if "szerencseproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if szerencseproba():
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['HaVan'])
            LepettEMar = True
    if not probaltemar:
        if "gyuruproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a gyűrűt?")
            if igenvagynem():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretne'])
                LepettEMar = True
                probaltemar = True
    if not fellvettekopenyt:
        if "kopeny" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a köpenyt?")
            if igenvagynem():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretnekopenyt'])
                LepettEMar = True
                fellvettekopenyt = True
    if "targy" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if (advDict['kaland'][Jatekos.lokacio]['TargyInfo']['szukseges']) in Jatekos.Items:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['TargyInfo']['HaVan'])
            LepettEMar = True
    if not LepettEMar:
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

#
