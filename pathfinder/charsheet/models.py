from logging import getLogger

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db.models import (BooleanField, CASCADE, CharField, Count, ForeignKey, ManyToManyField, Model,
                              PositiveIntegerField, SET_NULL)

from backend.ability_scores import get_modifier, get_carrying_capacity
from charsheet.bonuses import get_total_bonus
from charsheet.constants import AlignmentGoodAxis, AlignmentLawAxis, Gender, Size
from util.enums import enum_to_choices

logger = getLogger(__name__)


class Skill(Model):
    name = CharField(max_length=32, unique=True)
    key_ability = CharField(max_length=16)
    trained_only = BooleanField(default=False)

    def armor_check_penalty(self):
        return self.key_ability == 'strength' or self.key_ability == 'dexterity'

    def __str__(self) -> str:
        return f'{self.name}'


class CharacterClass(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)
    # In base classes these tend to be alignment restrictions, but prestige classes are also possible
    requirements = CharField(max_length=256, null=True, blank=True)  # May change field type
    is_prestige_class = BooleanField(default=False)  # Needed because saves start out slightly different
    hit_die = PositiveIntegerField()
    class_skills = ManyToManyField(Skill)
    starting_wealth = CharField(max_length=32, null=True, blank=True)
    skill_ranks = PositiveIntegerField()
    base_attack_progression = CharField(max_length=32)  # TODO limit option to half, 3/4 and full
    good_fortitude_progression = BooleanField()
    good_reflex_progression = BooleanField()
    good_will_progression = BooleanField()
    # TODO add abilities and spells
    # TODO add proficiencies

    class Meta:
        verbose_name_plural = 'CharacterClasses'

    def __str__(self) -> str:
        return f'{self.name}'


class Race(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)
    # ability scores
    # type(s)
    size = CharField(max_length=16, default=Size.MEDIUM.name, choices=enum_to_choices(Size))
    base_speed = PositiveIntegerField(help_text='expressed in feet')
    # languages
    # language options

    fly_speed = PositiveIntegerField(default=0, help_text='expressed in feet')
    # TODO make enum for these options
    fly_maneuverability = CharField(max_length=32, default='')  # Needs only be set if fly speed is
    swim_speed = PositiveIntegerField(default=0, help_text='expressed in feet')
    climb_speed = PositiveIntegerField(default=0, help_text='expressed in feet')
    burrow_speed = PositiveIntegerField(default=0, help_text='expressed in feet')

    # racial traits

    def __str__(self) -> str:
        return f'{self.name}'


class Language(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)
    secret = BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Character(Model):
    # I want every field of this Model to have a default so it can be left empty during construction

    # Description fields
    name = CharField(max_length=128, blank=True, default='')
    alignment_law_axis = CharField(max_length=8, default=AlignmentLawAxis.TRUE.name,
                                   choices=enum_to_choices(AlignmentLawAxis))
    alignment_good_axis = CharField(max_length=8, default=AlignmentGoodAxis.NEUTRAL.name,
                                    choices=enum_to_choices(AlignmentGoodAxis))
    player = CharField(max_length=128, blank=True, default='')
    deity = CharField(max_length=128, blank=True, default='')
    homeland = CharField(max_length=128, blank=True, default='')
    race = ForeignKey(Race, null=True, default=Race.objects.get(name='Human'), on_delete=SET_NULL)
    size = CharField(max_length=16, default=Size.MEDIUM.name,
                     choices=enum_to_choices(Size))
    gender = CharField(max_length=8, default=Gender.MALE.name,
                       choices=enum_to_choices(Gender))
    age = PositiveIntegerField(default=0)
    height = PositiveIntegerField(default=0, help_text='expressed in inches')
    weight = PositiveIntegerField(default=0, help_text='expressed in pounds')
    hair = CharField(max_length=32, blank=True, default='')
    eyes = CharField(max_length=32, blank=True, default='')

    experience = PositiveIntegerField(default=0)  # TODO change so it can be tracked per session
    languages = ManyToManyField(Language, blank=True)

    def alignment_readable(self):
        print(f'{self.alignment_law_axis} {self.alignment_good_axis}')
        return f'{AlignmentLawAxis[self.alignment_law_axis].value} {AlignmentGoodAxis[self.alignment_good_axis].value}'

    def size_readable(self):
        return Size[self.size].value

    def gender_readable(self):
        return Gender[self.gender].value

    def height_readable(self):
        return f'{self.height // 12}\' {self.height % 12}"'

    def weight_readable(self):
        return f'{self.weight} lbs.'

    base_strength = PositiveIntegerField(default=10)
    base_dexterity = PositiveIntegerField(default=10)
    base_constitution = PositiveIntegerField(default=10)
    base_intelligence = PositiveIntegerField(default=10)
    base_wisdom = PositiveIntegerField(default=10)
    base_charisma = PositiveIntegerField(default=10)

    copper = PositiveIntegerField(default=0)
    silver = PositiveIntegerField(default=0)
    gold = PositiveIntegerField(default=0)
    platinum = PositiveIntegerField(default=0)

    def strength(self):
        return self.base_strength + get_total_bonus(self, 'strength')

    def strength_modifier(self):
        return get_modifier(self.strength())

    def dexterity(self):
        return self.base_dexterity + get_total_bonus(self, 'dexterity')

    def dexterity_modifier(self):
        return get_modifier(self.dexterity())

    def constitution(self):
        return self.base_constitution + get_total_bonus(self, 'constitution')

    def constitution_modifier(self):
        return get_modifier(self.constitution())

    def intelligence(self):
        return self.base_intelligence + get_total_bonus(self, 'intelligence')

    def intelligence_modifier(self):
        return get_modifier(self.intelligence())

    def wisdom(self):
        return self.base_wisdom + get_total_bonus(self, 'wisdom')

    def wisdom_modifier(self):
        return get_modifier(self.wisdom())

    def charisma(self):
        return self.base_charisma + get_total_bonus(self, 'charisma')

    def charisma_modifier(self):
        return get_modifier(self.charisma())

#    def class_and_level(self):
#        levels = self.levels.values('character_class__name').annotate(Count("id")).order_by()
#        output = ', '.join(f"{level['character_class__name']} {level['id__count']}" for level in levels)
#        return f'{self.level()}: {output}'

    def class_and_level(self):
        # TODO this works but is hideous compared to the code above (which only shows the classes in a different
        # order than I would like
        levels = self.levels.values('character_class__name').annotate(Count("id")).order_by()
        levels = {level['character_class__name']: level['id__count'] for level in levels}
        o = self.levels.values('character_class__name').order_by('character_level')
        res = []
        for l in o:
            if l['character_class__name'] in levels:
                res.append(f"{l['character_class__name']} {levels[l['character_class__name']]}")
                del levels[l['character_class__name']]
        output = ', '.join(res)
        return f'{self.level()}: {output}'

    def level(self):
        return self.levels.count()
    
    def hit_dice(self):
        return self.level()

    def get_starting_hit_points(self):
        # TODO error handling, but I want to handle the specific error
        return self.levels.filter(character_level=1).get().character_class.hit_die

    def hit_points(self):
        return self.get_starting_hit_points() \
               + sum(roll.result for roll in self.roll_set.all()) \
               + get_modifier(self.constitution()) * self.level() \
               + get_total_bonus(self, 'hit points')

    def damage_resistance(self):
        return 0 + get_total_bonus(self, 'damage resistance')

    def initiative(self):
        return get_modifier(self.dexterity()) + get_total_bonus(self, 'initiative')

    def base_speed(self):
        return self.race.base_speed + get_total_bonus(self, 'base speed')

    def speed_with_armor(self):
        return self.base_speed()  # TODO check gear for armor

    def fly_speed(self):
        speed = self.get_best_speed('fly')
        return max(self.race.fly_speed, speed) + get_total_bonus(self, 'fly speed')

    def fly_maneuverability(self):
        try:
            # TODO will not work with more than 1 fly speed present
            return self.speed_set.filter(type='fly').get().maneuverability
        except:
            return self.race.fly_maneuverability

    def swim_speed(self):
        speed = self.get_best_speed('swim')
        return max(self.race.swim_speed, speed) + get_total_bonus(self, 'swim speed')

    def climb_speed(self):
        speed = self.get_best_speed('climb')
        return max(self.race.climb_speed, speed) + get_total_bonus(self, 'climb speed')

    def burrow_speed(self):
        speed = self.get_best_speed('burrow')
        return max(self.race.burrow_speed, speed) + get_total_bonus(self, 'burrow speed')

    def get_best_speed(self, type):
        # TODO maneuverability
        try:
            return max(s.speed for s in self.speed_set.filter(type=type).all())
        except ValueError:
            return 0


    # TODO refactor the 3 AC calculations into a coherent whole
    def armor_class(self):
        try:
            max_dex = min(item.max_dex for item in self.ac_items() if item.max_dex is not None)
            dexterity_modifier = min(max_dex, self.dexterity_modifier())
        except ValueError:  # If there is no AC item with a max dex
            dexterity_modifier = self.dexterity_modifier()
        return 10 + dexterity_modifier + get_total_bonus(self, 'armor class')

    def armor_class_modifiers(self):
        return ''

    def armor_class_notes(self):
        #TODO make notes and modifier for everything, but make them show only when present
        return ', '.join(note.value for note in self.note_set.filter(to='armor class'))

    def touch_armor_class(self):
        return self.armor_class() - get_total_bonus(self, 'armor class',
                                                    bonus_types=['armor', 'shield', 'natural armor'])

    def flatfooted_armor_class(self):
        return 10 + get_total_bonus(self, 'armor class') - get_total_bonus(self, 'armor class',
                                                                           bonus_types=['dodge'])

    def fortitude_save(self):
        levels = self.levels.values('character_class__id').annotate(Count("id")).order_by()
        base_save = 0
        for level in levels:
            character_class = CharacterClass.objects.filter(id=level['character_class__id']).get()
            base_save += self.get_base_save(character_class.good_fortitude_progression, level['id__count'],
                                            character_class.is_prestige_class)
        return base_save + self.constitution_modifier() + get_total_bonus(self, 'fortitude save')

    def reflex_save(self):
        levels = self.levels.values('character_class__id').annotate(Count("id")).order_by()
        base_save = 0
        for level in levels:
            character_class = CharacterClass.objects.filter(id=level['character_class__id']).get()
            base_save += self.get_base_save(character_class.good_reflex_progression, level['id__count'],
                                            character_class.is_prestige_class)
        return base_save + self.dexterity_modifier() + get_total_bonus(self, 'reflex save')

    def will_save(self):
        levels = self.levels.values('character_class__id').annotate(Count("id")).order_by()
        base_save = 0
        for level in levels:
            character_class = CharacterClass.objects.filter(id=level['character_class__id']).get()
            base_save += self.get_base_save(character_class.good_will_progression, level['id__count'],
                                            character_class.is_prestige_class)
        return base_save + self.wisdom_modifier() + get_total_bonus(self, 'will save')

    def get_base_save(self, good, level, prestige):
        # TODO move to backend
        if prestige:
            if good:
                return level // 2
            return (level + 1) // 3
        if good:
            return 2 + (level // 2)
        return level // 3

    def immunities(self):
        # TODO distint?
        return ', '.join(immunity.to for immunity in self.immunity_set.all())

    def save_modifiers(self):
        return ', \n'.join(modifier.value for modifier in self.conditionalmodifier_set.filter(to='saves').all())

    def base_attack_bonus(self):
        levels = self.levels.values('character_class__id').annotate(Count("id")).order_by()
        base_attack = 0
        for level in levels:
            character_class = CharacterClass.objects.filter(id=level['character_class__id']).get()
            base_attack += self.get_base_attack(character_class.base_attack_progression, level['id__count'])
        return base_attack

    def get_base_attack(self, type, level):
        # TODO move to backend
        if type == 'full':
            return level
        if type == 'half':
            return level // 2
        # '3/4'
        return (level * 3) // 4

    def spell_resistance(self):
        return 0 + get_total_bonus(self, 'spell resistance')

    def combat_maneuver_bonus(self):
        return self.base_attack_bonus() + self.strength_modifier() + self.get_special_size_modifier(self.size)

    def get_special_size_modifier(self, size):
        # TODO move to backend and move mapping out of the function
        mod = {
            Size.FINE: -8,
            Size.DIMINUTIVE: -4,
            Size.TINY: -2,
            Size.SMALL: -1,
            Size.MEDIUM: 0,
            Size.LARGE: 1,
            Size.HUGE: 2,
            Size.GARGANTUAN: 4,
            Size.COLOSSAL: 8,
        }
        return mod[Size[size]]

    def combat_maneuver_defense(self):
        return 10 + self.base_attack_bonus() + self.strength_modifier() + self.dexterity_modifier() + \
               self.get_special_size_modifier(self.size) + get_total_bonus(self, 'armor class', bonus_types=[
                    'circumstance', 'deflection', 'dodge', 'insight', 'luck', 'morale', 'profane', 'sacred', 'penalty'
                ])

    def attacks(self):
        return self.attack_set.all()

    def attacks_notes(self):
        return ', '.join(note.value for note in self.note_set.filter(to='attacks'))

    def skill_bonus(self, skill):
        trained_bonus = 3 if (self.trained(skill) and self.class_skill(skill)) else 0
        return self.rank_set.filter(to=skill).count() + trained_bonus + self.get_ability_modifier(skill.key_ability) + \
            get_total_bonus(self, skill.name.lower())

    def get_ability_modifier(self, name):
        return getattr(self, f'{name}_modifier')()

    def trained(self, skill):
        return self.rank_set.filter(to=skill).exists()

    def class_skill(self, skill):
        return self.classskill_set.filter(skill=skill).exists() or \
               self.levels.filter(character_class__class_skills=skill).exists()

    def languages_readable(self):
        return ', '.join(language.name for language in self.languages.all())

    def ac_items(self):
        return []  # TODO

    def light_load(self):
        return get_carrying_capacity(self.strength())[0]  # TODO size, pedalism

    def medium_load(self):
        return get_carrying_capacity(self.strength())[1]  # TODO size, pedalism

    def heavy_load(self):
        return get_carrying_capacity(self.strength())[2]  # TODO size, pedalism

    #def get_total_bonus(self, ...):
    #    return calculate_bonus(self.bonus_set.filter(...))

    def __str__(self)  -> str:
        return self.name


class CharacterClassLevel(Model):
    character = ForeignKey(Character, on_delete=CASCADE, related_name='levels')
    character_level = PositiveIntegerField()
    character_class = ForeignKey(CharacterClass, null=True, blank=True, on_delete=CASCADE)

    class Meta:
        unique_together = (('character', 'character_level'),)

    def __str__(self)  -> str:
        return f'{self.character_level}: {self.character_class.name}'


class Roll(Model):
    die_size = PositiveIntegerField(choices=((1, 'd1'), (2, 'd2'), (3, 'd3'), (4, 'd4'), (6, 'd6'), (8, 'd8'),
                                             (10, 'd10'), (12, 'd12'), (20, 'd20'), (100, 'd100'), ))
    result = PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    reason = CharField(max_length=200)
    character = ForeignKey(Character, on_delete=CASCADE)

    def clean(self):
        if self.result > self.die_size:
            raise ValidationError(f'Result {self.result} may not be greater than die size {self.die_size}')
        super(Roll, self).clean()

    def __str__(self) -> str:
        return f'{self.character}: {self.reason}'


class Bonus(Model):
    to = CharField(max_length=32)  # E.g. 'strength' (or 'AC', ...)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    value = CharField(max_length=32, default='1')  # E.g. 6 (or 'half_level' referring to callable functions)
    minimum = PositiveIntegerField(default=None, null=True, blank=True)
    bonus_type = CharField(max_length=32)  # E.g. 'enhancement' (or 'dodge', 'luck, 'untyped', ...)

    source = CharField(max_length=32)  # E.g. 'belt of giant strength +6' (or 'weapon focus')
    source_type = CharField(max_length=32)  # E.g. 'item' (or 'feat', ...)

    class Meta:
        verbose_name_plural = 'Bonuses'

    def __str__(self) -> str:
        return f'{self.bonus_type} bonus to {self.to} of {self.value}'


class Note(Model):
    to = CharField(max_length=32)  # E.g. 'strength' (or 'AC', ...)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    value = CharField(max_length=256, default='')

    def __str__(self) -> str:
        return f'Note on {self.to}: {self.value}'


class ConditionalModifier(Model):
    to = CharField(max_length=32)  # E.g. 'saves' (or 'AC', ...)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    value = CharField(max_length=32, default='')  # E.g. +2 vs. enchantment

    source = CharField(max_length=32)  # E.g. 'half-elf'
    source_type = CharField(max_length=32)  # E.g. 'race' (or 'feat', ...)

    def __str__(self) -> str:
        return f'Conditional modifier on {self.to}: {self.value}'


class Immunity(Model):
    to = CharField(max_length=32)  # E.g. 'fire' (or 'fear', ...)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    source = CharField(max_length=32)  # E.g. 'belt of giant strength +6' (or 'weapon focus')
    source_type = CharField(max_length=32)  # E.g. 'item' (or 'feat', ...)

    class Meta:
        verbose_name_plural = 'Immunities'

    def __str__(self) -> str:
        return f'Immunity to {self.to}'


class Speed(Model):
    type = CharField(max_length=32)  # E.g. 'base' (or 'fly', ...)
    speed = PositiveIntegerField()  # E.g. 30
    maneuverability = CharField(max_length=32, default='', help_text='only needed for fly speeds')
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    source = CharField(max_length=32)  # E.g. 'fly'
    source_type = CharField(max_length=32)  # E.g. 'spell'

    def __str__(self) -> str:
        return f'{self.type}'


class Rank(Model):
    to = ForeignKey(Skill, on_delete=CASCADE)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1
    character_level = PositiveIntegerField()

    class Meta:
        unique_together = (('to', 'character_level'),)

    def __str__(self) -> str:
        return f'{self.to} at lvl {self.character_level}'


class ClassSkill(Model):
    skill = ForeignKey(Skill, on_delete=CASCADE)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1

    source = CharField(max_length=32)  # E.g. 'half-elf'
    source_type = CharField(max_length=32)  # E.g. 'race'

    def __str__(self) -> str:
        return f'{self.skill}'


class WeaponProperty(Model):
    name = CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Weapon properties'

    def __str__(self) -> str:
        return f'{self.name}'


class Weapon(Model):
    proficiency_category = CharField(max_length=32)  # e.g. 'simple', 'exotic'
    # e.g. Unarmed, Light, One-handed, Two-handed, Thrown, Projectile, Ammunition
    use_category = CharField(max_length=32)

    name = CharField(max_length=32)
    cost = PositiveIntegerField()
    # Damage for medium creature, double weapons should be handled as 2 separate pieces (for now)
    damage_dice = PositiveIntegerField()  # e.g. 2d6 would have 2 here
    damage_die_type = PositiveIntegerField()  # e.g. 2d6 would have 6 here
    critical_range = PositiveIntegerField(default=20)
    critical_multiplier = PositiveIntegerField(default=2)
    range = PositiveIntegerField(default=0)
    ammunition_type = CharField(max_length=8, default='', null=True, blank=True)  # e.g. 'bolt' or 'arrow'
    weight = PositiveIntegerField()
    damage_type = CharField(max_length=16)
    properties = ManyToManyField(WeaponProperty, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'


class SpecificWeapon(Model):
    weapon = ForeignKey(Weapon, on_delete=CASCADE)
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1
    # TODO add properties (enlarged, frost, masterwork, enhancement,...)

    def __str__(self) -> str:
        return f'{self.weapon}'


class Attack(Model):
    character = ForeignKey(Character, on_delete=CASCADE)  # E.g. Kyras, id 1
    name = CharField(max_length=32, default='')  # Empty defaults to the name of the weapon

    weapon = ForeignKey(SpecificWeapon, on_delete=CASCADE)

    note = CharField(max_length=128)
