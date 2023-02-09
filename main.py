import json
import random

from classes.Jatekos import Jatekos


def kockadobas():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if duplakockadobas() <= Jatekos.Luck:
        Jatekos.Luck = Jatekos.Luck - 1
        return True
    else:
        Jatekos.Luck = Jatekos.Luck - 1
        return False


# HP Luck Skill Gold
Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)
