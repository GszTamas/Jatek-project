class Ellenfel:

    def __init__(self, name, HP, ugyesseg):
        self.name = name
        self.HP = HP
        self.ugyesseg = ugyesseg

    def hpmod(self, szam):
        if szam > 0:
            self.HP = self.HP + szam
        else:
            self.HP = self.HP - szam
