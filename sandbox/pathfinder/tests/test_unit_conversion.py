from pytest import mark, param
from typing import NoReturn

from sandbox.pathfinder.types import DistanceFeet, DistanceMeter, DistanceInch, DistanceMile, WeightLbs, WeightKg
from sandbox.pathfinder.unit_conversion import (feet_to_meters, feet_and_inches_to_meters, mile_to_meters,
                                                pounds_to_kilograms)


@mark.parametrize('feet, meters', (
    param(0.0, 0.0, id='zero'),
    param(5.0, 1.524),
))
def test_feet_to_meters(feet: DistanceFeet, meters: DistanceMeter) -> None:
    assert feet_to_meters(feet) == meters


@mark.parametrize('feet, inches, meters', (
    param(0.0, 0.0, 0.0, id='zero'),
    param(5.0, 0.0, 1.524, id='feet only'),
    param(0.0, 8.0, 0.2032, id='inches only'),
    param(5.0, 8.0, 1.7272, id='feet and inches'),
))
def test_feet_and_inches_to_meters(feet: DistanceFeet, inches: DistanceInch, meters: DistanceMeter) -> None:
    assert feet_and_inches_to_meters(feet, inches) == meters


@mark.parametrize('miles, meters', (
    param(0.0, 0.0, id='zero'),
    param(2.0, 3218.688),
))
def test_mile_to_meters(miles: DistanceMile, meters: DistanceMeter) -> None:
    assert mile_to_meters(miles) == meters


@mark.parametrize('pounds, kilograms', (
    param(0.0, 0.0, id='zero'),
    param(2.0, 0.90718474),
))
def test_pounds_to_kilogram(pounds: WeightLbs, kilograms: WeightKg) -> None:
    assert pounds_to_kilograms(pounds) == kilograms
