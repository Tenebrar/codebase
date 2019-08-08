from pathfinder.character.abilities import AbilityScore
from pathfinder.character.alignment import Alignment
from pathfinder.character.gender import Gender
from pathfinder.character.size import Size


class Character:
    def __int__(self) -> None:
        self.name: str = ''
        self.alignment: Alignment = Alignment.TRUE_NEUTRAL
        self.player: str = ''
        self.character_class_and_level: str = ''
        self.deity: str = ''
        self.homeland: str = ''
        self.race: str = ''
        self.size: Size = Size.MEDIUM
        self.gender: Gender = Gender.MALE
        self.age: int = 0
        self.height: str = ''
        self.weight: str = ''
        self.hair: str = ''
        self.eyes: str = ''

        self.strength: AbilityScore = AbilityScore(10)
        self.dexterity: AbilityScore = AbilityScore(10)
        self.constitution: AbilityScore = AbilityScore(10)
        self.intelligence: AbilityScore = AbilityScore(10)
        self.wisdom: AbilityScore = AbilityScore(10)
        self.charisma: AbilityScore = AbilityScore(10)

        self.hp: int = 0