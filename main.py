import json
import random

from classes.Jatekos import Jatekos


def kockadobas():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if duplakockadobas():
        print("a")

# HP Luck Skill Gold
Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)
