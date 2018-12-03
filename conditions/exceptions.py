class ConditionViolatedError(BaseException):
    pass


class PreConditionViolatedError(ConditionViolatedError):
    pass


class PostConditionViolatedError(ConditionViolatedError):
    pass


class IncorrectConditionFormatError(BaseException):
    pass
