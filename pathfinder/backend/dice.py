from enum import IntEnum, unique
from random import randint
from typing import Tuple


@unique
class DieType(IntEnum):
    """ A type of die used in the Pathfinder system """

    D1 = 1
    D2 = 2
    D3 = 3
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20
    D100 = 100

    def roll(self) -> int:
        """ Return a random value from the die """
        return randint(1, self.value)

    def __str__(self) -> str:
        return f'd{self.value}' if self.value != 100 else 'd%'

    @classmethod
    def parse(cls, value: str) -> 'DieType':
        """
        :param value: A string representation of a DieType, such as 'd6'
        :return: The corresponding DieType
        :raises ValueError: if the string cannot be parsed as a 'd' followed by a number, or
        if the value is not one of the available dice in the system

        Percentile dice have 3 ways they may be represented, the normal 'd100', or the special 'd00' or 'd%'
        """
        if value[0].lower() != 'd':
            raise ValueError(f"Incorrect die type (does not start with 'd'): '{value}'")

        if value in ['d%', 'd00']:  # Alternative ways to represent a percentile die
            return DieType.D100

        return DieType(int(value[1:]))


class Dice(object):
    """ Object representing multiple dice of the same type, e.g. used to indicate the damage a weapon deals """

    def __init__(self, dice: int, die_type: DieType) -> None:
        """
        :param dice: The amount of dice
        :param die_type: The type of die
        :raises ValueError: if a negative or zero amount of dice is requested,
        if an int is passed instead of a DieType
        """
        if dice <= 0:
            raise ValueError(f'Can only create a positive amount of dice, not {dice}')
        if not isinstance(die_type, DieType):
            raise ValueError(f"Die type must be of type DieType, not '{die_type}'")

        self.dice: int = dice
        self.die_type: DieType = die_type

    def __str__(self) -> str:
        return f'{self.dice}{str(self.die_type)}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'

    def to_tuple(self) -> Tuple[int, int]:
        """ Convert the Dice object to a tuple of (amount of dice, sides to a die) """
        return self.dice, self.die_type.value

    @classmethod
    def from_tuple(cls, t: Tuple[int, int]) -> 'Dice':
        """ Convert a tuple of (amount of dice, sides to a die) to a Dice object"""
        return Dice(t[0], DieType(t[1]))

    @classmethod
    def parse(cls, value: str) -> 'Dice':
        """
        :param value: A string representation of a Dice object, such as '4d6'
        :return: The corresponding Dice object
        :raises ValueError: if something in the parsing goes wrong
        """
        index = value.lower().index('d')
        dice = int(value[:index]) if index != 0 else 1  # Allow parsing 'd6' as '1d6'
        return Dice(dice, DieType.parse(value[index:]))
