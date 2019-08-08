from typing import NewType

AbilityScore = NewType('AbilityScore', int)
AbilityModifier = NewType('AbilityModifier', int)


def get_modifier(ability_score: AbilityScore) -> AbilityModifier:
    """
    :param ability_score: An ability score
    :return: The modifier for that score
    """
    if ability_score < 0:
        raise ValueError(f'Ability score must be positive: {ability_score}')

    return AbilityModifier((ability_score - 10) // 2)
