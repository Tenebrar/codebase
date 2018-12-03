from logging import getLogger
from typing import List

logger = getLogger(__name__)

UNTYPED = 'untyped'
INHERENT = 'inherent'
DODGE = 'dodge'


def get_total_bonus(character, to: str, bonus_types: List[str]=None) -> int:
    from charsheet.models import Bonus  # Avoid cyclical import

    bonuses = Bonus.objects.filter(character=character, to=to)
    if bonus_types:
        bonuses = bonuses.filter(bonus_type__in=bonus_types)
    bonuses = bonuses.all()

    bonus_to_bonus = 0
    for bonus in bonuses:
        if bonus.bonus_type is not UNTYPED:
            bonus_to_bonus += get_total_bonus(character, to=f'{bonus.bonus_type} bonus')

    # TODO take types into account (highest per type, unless of stacking types)
    # TODO take bonus to bonuses into account (e.g. enhancement to armor)
    return sum(get_value(character, bonus.value) for bonus in bonuses) + bonus_to_bonus


def get_value(character, value: str) -> int:
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return getattr(character, value)()
    except Exception:
        logger.warning(f'Could not parse value {value}')
        return 0