from pathfinder.character.character import Character
from pathfinder.character.abilities import AbilityScore
from pathfinder.character.gender import Gender
from pathfinder.golarion.deities import PathfinderCoreDeities

c = Character(name='Jos', player='Peter', deity=PathfinderCoreDeities.DESNA, homeland=PathfinderHomelands.X,
              gender=Gender.MALE, age=62, height=6.2, weight=100, hair='None', eyes='Red')
c.base_strength = AbilityScore(8)
c.base_dexterity = AbilityScore(16)
c.base_constitution = AbilityScore(12)
c.base_intelligence = AbilityScore(16)
c.base_wisdom = AbilityScore(12)
c.base_charisma = AbilityScore(10)

c.verify_point_buy_cost(20)

c.race = Tiefling()

c.add_level(Knifemaster(1, skills=[Skill.ACROBATICS, Skill.KNOWLEDGE_LOCAL]), feat=WeaponFinesse())
c.add_level(Knifemaster(2, talent=ExtinguisingStrike(), hp_roll=5, skills=[Skill.ACROBATICS, Skill.KNOWLEDGE_LOCAL]))

c.equip(Leather())
c.equip(Dagger())


c.print_char_sheet()
