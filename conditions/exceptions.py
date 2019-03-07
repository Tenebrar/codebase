from __future__ import annotations

from typing import Any, Callable, List, Tuple


class ConditionViolatedError(BaseException):
    pass


class PreconditionViolatedError(ConditionViolatedError):
    @classmethod
    def _parameter_description(cls, parameter_name: str, value: Any):
        return f"input parameter '{value}' of type {type(value)} (value for parameter {parameter_name})"

    @classmethod
    def single_arg(cls, key: str, value: Any, predicate: Callable[[Any], bool]) -> PreconditionViolatedError:
        description = cls._parameter_description(key, value).capitalize()
        return PreconditionViolatedError(f"{description} failed to pass precondition {predicate.__name__}")

    @classmethod
    def multi_arg(cls, key_value_pairs: List[Tuple[str, Any]],
                  predicate: Callable[..., bool]) -> PreconditionViolatedError:
        parameter_descriptions = map(lambda key_value: cls._parameter_description(*key_value), key_value_pairs)
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
