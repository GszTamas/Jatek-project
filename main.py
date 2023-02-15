import json
import random

from classes.Jatekos import Jatekos


def kockadobas():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if duplakockadobas() <= Jatekos.Luck:
        Jatekos.minuszluck()
        return True
    else:
        Jatekos.minuszluck()
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
        print(f"{name} Életereje: {hp}")
        print(f"Játékos Életereje: {Jatekos.HP}")


# HP Luck Skill Gold
Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)