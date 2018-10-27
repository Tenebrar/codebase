from enum import Enum
from typing import List, Tuple, Type


def enum_to_choices(enum_class: Type[Enum]) -> List[Tuple[str, str]]:
    """
    Convert an Enum into choices for a CharField where the stored values are the Enum names and the human-readable
    values are are the Enum values
    """
    # TODO there is a class DjangoChoices, check it out
    return [(member.name, member.value) for member in enum_class]
