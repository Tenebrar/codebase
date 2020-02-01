from django.db.models import Model


class Character(Model):
    def __init__(self):
        super().__init__()

        self.name = 'Jos'
        self.alignment_readable = 'CG'
        self.player = 'Peter'
        self.class_and_level = 'Commoner 9'
        self.deity = 'Atheist'
        self.homeland = 'Everywhere'
        self.race = 'Rude question'
        self.size_readable = 'big'
        self.gender_readable = 'X'
        self.age = 999
        self.height_readable = 'tall'
        self.weight_readable = 'big'
        self.hair = 'None'
        self.eyes = 'blue'

        self.strength = 18
        self.strength_modifier = 4
        self.dexterity = 16
        self.dexterity_modifier = 3
        self.constitution = 14
        self.constitution_modifier = 2
        self.intelligence = 12
        self.intelligence_modifier = 1
        self.wisdom = 10
        self.wisdom_modifier = 0
        self.charisma = 8
        self.charisma_modifier = -1

        self.attack1 = Attack()

        self.base_speed_feet = 30
        self.base_speed_squares = 6
        self.base_speed_with_armor_feet = 30
        self.base_speed_with_armor_squares = 6

        self.skills = [Skill(self)]
        self.items = [Item()]

        self.feats = ['Dodge', 'Mobility', 'Spring attack']



class Attack:
    def __init__(self):
        self.name = 'Blade'
        self.attack_bonus = 1
        self.critical = '12-20/*9'
        self.damage_type = 'B'
        self.damage = '5d20+123'


class Skill:
    def __init__(self, character):
        self.name = 'Acrobatics'
        self.class_skill = True
        self.attribute_name = 'Dex'
        self.attribute_modifier = character.dexterity_modifier
        self.ranks = 3
        self.modifiers = 5

        self.total = self.attribute_modifier + self.ranks + self.modifiers


class Item:
    def __init__(self):
        self.name = '10ft. pole'
        self.weight = '1lbs.'
