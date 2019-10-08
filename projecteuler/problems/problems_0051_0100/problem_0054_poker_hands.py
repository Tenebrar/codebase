from __future__ import annotations

from collections import Counter
from enum import Enum, IntEnum, auto, unique
from typing import List, Sized, Tuple

from projecteuler.settings import inputfile
from util.conditions.decorators import precondition
from util.enums.ordered import OrderedEnum


def has_length(expected_length: int):
    def _has_length(s: Sized) -> bool:
        return len(s) == expected_length
    _has_length.__name__ = f'_has_length_{expected_length}'
    return _has_length


@unique
class Value(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


VALUES = {
    '2': Value.TWO,
    '3': Value.THREE,
    '4': Value.FOUR,
    '5': Value.FIVE,
    '6': Value.SIX,
    '7': Value.SEVEN,
    '8': Value.EIGHT,
    '9': Value.NINE,
    'T': Value.TEN,
    'J': Value.JACK,
    'Q': Value.QUEEN,
    'K': Value.KING,
    'A': Value.ACE,
}


@unique
class Suit(Enum):
    CLUBS = 'C'
    DIAMONDS = 'D'
    HEARTS = 'H'
    SPADES = 'S'


class Card:
    def __init__(self, value: Value, suit: Suit):
        self.suit = suit
        self.value = value

    @staticmethod
    @precondition(0, has_length(2))
    def parse(string: str) -> Card:
        return Card(VALUES[string[0]], Suit(string[1]))

    def __str__(self):
        return f'{self.value.name.capitalize()} of {self.suit.name.lower()}'

    def __repr__(self):
        return f'{self.value.name.capitalize()} of {self.suit.name.lower()}'

    def __eq__(self, other: Card):
        return self.suit == other.suit and self.value == other.value


class Hand:
    def __init__(self, cards: Tuple[Card, ...]):
        self.cards = cards

    @staticmethod
    def parse(string: str) -> Hand:
        return Hand(tuple(Card.parse(s) for s in string.split()))

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return repr(self.cards)


@unique
class Rank(OrderedEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_FLUSH = auto()


class PokerHand:
    @precondition(1, has_length(5))
    def __init__(self, hand: Hand):
        self.hand = hand

    def _is_straight(self):
        # The problem does not indicate anything about A2345 straights, so we don't count them (for now)
        sorted_hand = sorted(card.value for card in self.hand.cards)
        for i in range(len(sorted_hand) - 1):
            if sorted_hand[i].value + 1 != sorted_hand[i + 1].value:
                return False
        return True

    def _is_flush(self):
        return len(set(card.suit for card in self.hand.cards)) == 1

    def get_rank(self) -> Tuple[Rank, List[Value]]:
        # Sort by number of occurrences first, and value second (from high to low each time)
        high_to_low = sorted((c.value for c in self.hand.cards), reverse=True)
        occurence = sorted(high_to_low, key=Counter(high_to_low).get, reverse=True)

        if self._is_straight() and self._is_flush() and occurence[0] == Value.ACE:
            return Rank.STRAIGHT_FLUSH, occurence

        if self._is_straight() and self._is_flush():
            return Rank.STRAIGHT_FLUSH, occurence

        if occurence[0] == occurence[3]:
            return Rank.FOUR_OF_A_KIND, occurence

        if occurence[0] == occurence[2] and occurence[3] == occurence[4]:
            return Rank.FULL_HOUSE, occurence

        if self._is_flush():
            return Rank.FLUSH, occurence

        if self._is_straight():
            return Rank.STRAIGHT, occurence

        if occurence[0] == occurence[2]:
            return Rank.THREE_OF_A_KIND, occurence

        if occurence[0] == occurence[1] and occurence[2] == occurence[3]:
            return Rank.TWO_PAIRS, occurence

        if occurence[0] == occurence[1]:
            return Rank.ONE_PAIR, occurence

        return Rank.HIGH_CARD, occurence

    def __len__(self):
        return len(self.hand)

    def __gt__(self, other):
        return self.get_rank() > other.get_rank()

    def __lt__(self, other):
        return not self.__gt__(other)


def problem_0054(filename: str) -> int:
    with open(inputfile(filename), 'r') as file:
        hand_pairs = []
        for line in file.readlines():
            hand_pairs.append((Hand.parse(line[:14]), Hand.parse(line[15:])))

    player1_wins = 0
    for pair in hand_pairs:
        if PokerHand(pair[0]) > PokerHand(pair[1]):
            player1_wins += 1

    return player1_wins


if __name__ == '__main__':
    FILENAME = 'p054_poker.txt'

    print(problem_0054(FILENAME))
    # Expected: 376
