class ConditionViolatedError(BaseException):
    pass


class PreConditionViolatedError(ConditionViolatedError):
    def __init__(self, key, value, predicate):
        super().__init__(
            f"Input parameter '{value}' of type {type(value)} (value for parameter {key}) "
            f"failed to pass precondition {predicate.__name__}"
        )


class PostConditionViolatedError(ConditionViolatedError):
    def __init__(self, result, predicate):
        super().__init__(
            f"Return value '{result}' of type {type(result)} failed to pass postcondition {predicate.__name__}"
        )
