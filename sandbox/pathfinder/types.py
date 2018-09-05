from typing import NewType

# Define 2 types to be sure no confusion occurs for functions that accept numbers
AbilityScore = NewType('AbilityScore', int)
AbilityModifier = NewType('AbilityModifier', int)

# Units of distance (are sometimes used as speed, if so the speed is that distance per round unless otherwise specified)
DistanceFeet = NewType('DistanceFeet', float)
DistanceMile = NewType('DistanceMile', float)
DistanceInch = NewType('DistanceInch', float)
DistanceMeter = NewType('DistanceMeter', float)

# Units of weight
WeightLbs = NewType('WeightLbs', float)
WeightKg = NewType('WeightKg', float)
