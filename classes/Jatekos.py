class Jatekos:
    def __init__(self, HP, Luck, Skill, Gold, Items = [], Crystals = [], Potions = [], Food = []):
        self.HP = HP
        self.Luck = Luck
        self.Skill = Skill
        self.Gold = Gold
        self.Items = Items
        self.Crystals = Crystals
        self.Potions = Potions
        self.Food = Food

    def tortenetkezdes(self):
        self.Items.append("Kard")
        self.Items.append("Bőrvért")