from __future__ import annotations

from enum import Enum, auto, unique
from typing import List, Tuple

from projecteuler.settings import inputfile
from util.enums.ordered import OrderedEnum


@unique
class Value(OrderedEnum):
    TWO = '2'
    THREE = '3'
    FOUT = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


@unique
class Suit(Enum):
    HEARTS = 'H'
    CLUBS = 'C'
    SPADES = 'S'
    DIAMONDS = 'D'


class Card:
    def __init__(self, value: Value, suit: Suit):
        self.suit = suit
        self.value = value

    @staticmethod
    def parse(string: str) -> Card:
        assert len(string) == 2

        return Card(Value(string[0]), Suit(string[1]))

    def __str__(self):
        return str((self.value, self.suit))


@unique
class Rank(OrderedEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()  # The problem does not indicate anything about A2345 straights
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_FLUSH = auto()


class Hand:
    def __init__(self, cards: Tuple[Card, Card, Card, Card, Card]):
        self.cards = cards

    @staticmethod
    def parse(string: str) -> Hand:
        string.split()
        # TODO

    def __str__(self):
        return str(self.cards)


def _evaluate_hand(hand: Hand) -> Tuple[Rank, List[Value]]:
    return Rank.HIGH_CARD, sorted(hand, reverse=True)


def problem_0054() -> int:
    filename = 'p054_poker.txt'
    with open(inputfile(filename), 'r') as file:
        card_list = [line.split() for line in file.readlines()]  # Lines look like: 8C TS KC 9H 4S 7D 2S 5D 3S AC

    player1_wins = 0
    # for cards in card_list:
    #     hand1 = Hand((Card(cards[0]), Card(cards[1]), Card(cards[2]), Card(cards[3]), Card(cards[4])))
    #     hand2 = Hand((Card(cards[5]), Card(cards[6]), Card(cards[7]), Card(cards[8]), Card(cards[9])))
    #     ev1, ev2 = _evaluate_hand(hand1), _evaluate_hand(hand2)
    #     #print(ev1, ev2)
    #     if ev1 > ev2:
    #         player1_wins += 1

    return player1_wins


if __name__ == '__main__':
    print(problem_0054())
    # Expected:
