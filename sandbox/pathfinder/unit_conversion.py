from sandbox.pathfinder.types import DistanceFeet, DistanceInch, DistanceMeter, DistanceMile, WeightKg, WeightLbs


def feet_to_meters(feet: DistanceFeet) -> DistanceMeter:
    """
    :param feet: a distance in feet
    :return: That distance in meters
    """
    return DistanceMeter(feet * 0.3048)


def feet_and_inches_to_meters(feet: DistanceFeet, inches: DistanceInch) -> DistanceMeter:
    """
    For example, a character that is 5'9" is 1.7526m tall

    :param feet: a distance in feet
    :param inches: An additional distance in inches
    :return: That total distance in meters
    """
    return DistanceMeter(feet_to_meters(feet) + inches * 0.0254)


def mile_to_meters(mile: DistanceMile) -> DistanceMeter:
    """
    :param mile: a distance in miles
    :return: That distance in meters
    """
    return DistanceMeter(mile * 1609.344)


def pounds_to_kilograms(pounds: WeightLbs) -> WeightKg:
    """
    :param pounds: a weight in pounds (lbs.)
    :return: That weight in kilograms
    """
    return WeightKg(pounds * 0.45359237)
