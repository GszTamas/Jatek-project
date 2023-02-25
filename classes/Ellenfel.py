class Ellenfel:

    def __init__(self, name, HP, ugyesseg):
        self.name = name
        self.HP = HP
        self.ugyesseg = ugyesseg
    def ellenfelsebzes(self, szam):
        self.HP = self.HP - szam

    def ellenfelheal(self, szam):
        self.HP = self.HP + szam
