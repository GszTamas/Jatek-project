class Jatekos:
    def __init__(self, HP, Luck, Skill, Gold, Items=None, Crystals=None, Potions=None, Food=None, lokacio = "0"):
        if Food is None:
            Food = []
        if Potions is None:
            Potions = []
        if Crystals is None:
            Crystals = []
        if Items is None:
            Items = []
        self.HP = HP
        self.Luck = Luck
        self.Skill = Skill
        self.Gold = Gold
        self.Items = Items
        self.Crystals = Crystals
        self.Potions = Potions
        self.Food = Food
        self.lokacio = lokacio

    def tortenetkezdes(self):
        self.Items.append("Kard")
        self.Items.append("Bőrvért")

    def minuszluck(self):
        self.Luck = self.Luck - 1

    def jatekosSebzes(self, szam):
        self.HP = self.HP - szam

    def jatekosHeal(self, szam):
        self.HP = self.HP + szam

    def lokaciovaltoztatas(self, szoba):
        self.lokacio = szoba

    def __repr__(self):
        print(f'Életerőd: {self.HP}\nSzerencséd: {self.Luck}\nÜgyeséged: {self.Skill}\nHelyzeted: {int(self.lokacio)}\nPénzed: {self.Gold}\nTárgyaid: {self.Items}\nKristályaid: {self.Crystals}\nItalaid: {self.Potions}\nÉteleid: {self.Food}')
