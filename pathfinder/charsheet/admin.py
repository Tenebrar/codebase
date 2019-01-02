from django.contrib import admin

from .models import Attack, Bonus, Character, CharacterClass, CharacterClassLevel, ClassSkill, ConditionalModifier, \
    FullAttack, Immunity, Language, Note, Race, Rank, Roll, Skill, SpecificWeapon, Speed, Weapon, WeaponProperty


class RollInline(admin.TabularInline):
    model = Roll
    extra = 0


class BonusInline(admin.TabularInline):
    model = Bonus
    extra = 0


class CharacterClassLevelInline(admin.TabularInline):
    model = CharacterClassLevel
    extra = 0


class NoteInline(admin.TabularInline):
    model = Note
    extra = 0


class ImmunityInline(admin.TabularInline):
    model = Immunity
    extra = 0


class ConditionalModifierInline(admin.TabularInline):
    model = ConditionalModifier
    extra = 0


class SpeedInline(admin.TabularInline):
    model = Speed
    extra = 0


class RankInline(admin.TabularInline):
    model = Rank
    extra = 0


class ClassSkillInline(admin.TabularInline):
    model=ClassSkill
    extra=0


class SpecificWeaponInline(admin.TabularInline):
    model=SpecificWeapon
    extra=0


class AttackInline(admin.TabularInline):
    model=Attack
    extra=0


class FullAttackInline(admin.TabularInline):
    model=FullAttack
    extra=0


class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description', {'fields': ['name', 'alignment_law_axis', 'alignment_good_axis', 'player',
                                    'deity', 'homeland', 'race', 'size', 'gender', 'age', 'height', 'weight', 'hair',
                                    'eyes']}),
        ('Base stats', {'fields': ['base_strength', 'base_dexterity', 'base_constitution',
                                   'base_intelligence', 'base_wisdom', 'base_charisma', ]}),
        ('Money', {'fields': ['copper', 'silver', 'gold', 'platinum', ]}),
        ('Experience', {'fields': ['experience', ]}),
        ('Languages', {'fields': ['languages', ]}),
    ]
    inlines = [RollInline, BonusInline, CharacterClassLevelInline, NoteInline, ImmunityInline,
               ConditionalModifierInline, SpeedInline, RankInline, ClassSkillInline, SpecificWeaponInline,
               AttackInline, FullAttackInline, ]
    list_display = ('name', )
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Character, CharacterAdmin)

admin.site.register(CharacterClass)
admin.site.register(Language)
admin.site.register(Race)
admin.site.register(Skill)
admin.site.register(Weapon)
admin.site.register(WeaponProperty)
