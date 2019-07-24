from __future__ import annotations

from collections import OrderedDict
from typing import Any, Callable


class ConditionViolatedError(BaseException):
    pass


class PreconditionViolatedError(ConditionViolatedError):
    @staticmethod
    def _parameter_description(parameter_name: str, value: Any):
        return f"input parameter '{value}' of type {type(value)} (value for parameter {parameter_name})"

    @classmethod
    def single_arg(cls, key: str, value: Any, predicate: Callable[[Any], bool]) -> PreconditionViolatedError:
        description = cls._parameter_description(key, value).capitalize()
        return PreconditionViolatedError(f"{description} failed to pass precondition {predicate.__name__}")

    @classmethod
    def multi_arg(cls, key_value_pairs: OrderedDict,
                  predicate: Callable[..., bool]) -> PreconditionViolatedError:
        parameter_descriptions = map(lambda key_value: cls._parameter_description(*key_value), key_value_pairs.items())
        descriptions = ', '.join(parameter_descriptions).capitalize()
        return PreconditionViolatedError(f"{descriptions} failed to pass precondition {predicate.__name__}")

    @classmethod
    def no_arg(cls, predicate: Callable[[], bool]) -> PreconditionViolatedError:
        return PreconditionViolatedError(f"Failed to pass precondition {predicate.__name__}")


class PostconditionViolatedError(ConditionViolatedError):
    def __init__(self, result, predicate):
        super().__init__(
            f"Return value '{result}' of type {type(result)} failed to pass postcondition {predicate.__name__}"
        )


class MalformedDecoratorError(BaseException):
    """ Used to indicate that the used decorator specifies parameters that do not occur in the decorated function. """
