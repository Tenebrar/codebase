from enum import Enum, unique
from typing import Tuple, Iterable


@unique
class Direction(Enum):
    # Directions are defined with X-axis pointing to the right, and Y-axis pointing down
    UP = (-1, 0)
    RIGHT_UP = (-1, 1)
    RIGHT = (0, 1)
    RIGHT_DOWN = (1, 1)
    DOWN = (1, 0)
    LEFT_DOWN = (1, -1)
    LEFT = (0, -1)
    LEFT_UP = (-1, -1)

    KNIGHT_UP_UP_RIGHT = (-2, 1)
    KNIGHT_RIGHT_RIGHT_UP = (-1, 2)
    KNIGHT_RIGHT_RIGHT_DOWN = (1, 2)
    KNIGHT_DOWN_DOWN_RIGHT = (2, 1)
    KNIGHT_DOWN_DOWN_LEFT = (2, -1)
    KNIGHT_LEFT_LEFT_DOWN = (1, -2)
    KNIGHT_LEFT_LEFT_UP = (-1, -2)
    KNIGHT_UP_UP_LEFT = (-2, -1)


ORTHOGONAL = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
EIGHT_DIRECTIONAL = [Direction.UP, Direction.RIGHT_UP, Direction.RIGHT, Direction.RIGHT_DOWN,
                     Direction.DOWN, Direction.LEFT_DOWN, Direction.LEFT, Direction.LEFT_UP]
ORTHOGONAL_WITHOUT_INVERSE = [Direction.UP, Direction.RIGHT]
EIGHT_DIRECTIONAL_WITHOUT_INVERSE = [Direction.UP, Direction.RIGHT_UP, Direction.RIGHT, Direction.RIGHT_DOWN]


def steps(start_coordinate: Tuple[int, int], direction: Direction, amount_of_steps: int) -> Iterable[Tuple[int, int]]:
    for i in range(1, amount_of_steps + 1):
        yield start_coordinate[0] + i * direction.value[0], start_coordinate[1] + i * direction.value[1]
