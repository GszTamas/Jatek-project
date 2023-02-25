import json
import random
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


def harc(csatamod, name, hp, skill):
    while True:
        EllensegAttackSTR = duplakockadobas() + skill  # 1.lépés
        JatekosAttackSTR = duplakockadobas() + Jatekos.Skill  # 2.lépés
        if Jatekos.combatblessed:
            JatekosAttackSTR = JatekosAttackSTR + 1
        if csatamod > 0:
            JatekosAttackSTR = JatekosAttackSTR - csatamod

        if EllensegAttackSTR < JatekosAttackSTR:
            hp = hp - 2
            print("Megsebezted az ellenfelet!")
            if Jatekos.HP < 1:
                print("nem nyertel")
                return False
            elif hp < 1:
                print("nyertel")
                return True
            print("Akarsz Szerencsét próbálni?")
            if not igenvagynem():
                print("Nem probáltál szerencsét!")
            else:
                if szerencseproba():
                    print("Súlyos sebzést ejtettél!")
                    hp = hp - 2
                else:
                    print("A seb puszta karcolás!")
                    hp = hp + 1
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.jatekosSebzes(2)
            print("Az ellenfél megsebzett téged!")
            if Jatekos.HP < 1:
                print("nem nyertel")
                return False
            elif hp < 1:
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
        print(f"{name} Életereje: {hp}")
        print(f"Játékos Életereje: {Jatekos.HP} \n")


Nyert = False
probaltemar = False
fellvettekopenyt = False
csatamod = 0
input("új játék inditásához gépeljen be bármit: ")

Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)  # HP Luck Skill Gold

with open("Kaland.json", "r", encoding="utf-8") as jsn:
    advDict = json.load(jsn)

if advDict['kaland'][Jatekos.lokacio]['akcio'] == "tortenetkezdes":
    Jatekos.tortenetkezdes()

while not Nyert:
    LepettEMar = False
    Jatekos.lokaciostr()
    print(advDict['kaland'][Jatekos.lokacio]['szoveg'] + "\n")
    StartInp = input("Folytatáshoz nyomjon entert vagy írjon be egy commandot [statok, kilepes]: ")
    if StartInp == "statok":
        print(Jatekos)
    elif StartInp == "kilepes":
        exit()

    # stat váltosztatások
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

    # tárgy felvételek
    if "pluszlebeges" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Lebegés Köpenye")

    if "+penz" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszcrystal(advDict['kaland'][Jatekos.lokacio]['mennyiseg'])

    if "+kristaly" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszcrystal(advDict['kaland'][Jatekos.lokacio]['targy'])
    # harc
    if "csatamod" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        csatamod = advDict['kaland'][Jatekos.lokacio]['ertek']

    if "harc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 1:
            harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg'])
            csatamod = 0
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 2:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg'])
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 3:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg']):
                    harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel3']['nev'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['HP'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['ugyesseg'])

    # győzelem vagy gameover detektálás
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif advDict['kaland'][Jatekos.lokacio]['akcio'] == "gameoever":
        Nyert = False
        Jatekos.gameover()
        break

    # lépések
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
