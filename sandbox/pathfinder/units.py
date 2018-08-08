from typing import NewType

# Units of distance (are sometimes used as speed, if so the speed is that distance per round unless otherwise specified)
DistanceFeet = NewType('DistanceFeet', float)
DistanceMile = NewType('DistanceMile', float)
DistanceInch = NewType('DistanceInch', float)
DistanceMeter = NewType('DistanceMeter', float)

# Units of weight
WeightLbs = NewType('WeightLbs', float)
WeightKg = NewType('WeightKg', float)


def feet_to_meters(feet: DistanceFeet) -> DistanceMeter:
    """
    :param feet: A distance in feet
    :return: That distance in meters
    """
    return DistanceMeter(feet * 0.3048)


def feet_and_inches_to_meters(feet: DistanceFeet, inches: DistanceInch) -> DistanceMeter:
    """
    For example, a character that is 5'9" is 1.7526m tall

    :param feet: A distance in feet
    :param inches: An additional distance in inches
    :return: That total distance in meters
    """
    return DistanceMeter(feet * 0.3048 + inches * 0.0254)


def mile_to_meters(mile: DistanceMile) -> DistanceMeter:
    """
    :param mile: A distance in miles
    :return: That distance in meters
    """
    return DistanceMeter(mile * 1609.34)


def pounds_to_kilograms(pounds: WeightLbs) -> WeightKg:
    """
    :param pounds: A weight in pounds (lbs.)
    :return: That weight in kilograms
    """
    return WeightKg(pounds * 0.453592)
