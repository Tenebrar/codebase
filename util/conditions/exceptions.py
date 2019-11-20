from __future__ import annotations


class ConditionViolatedError(BaseException):
    """ Used to indicate some condition was violated for the function """


class PreconditionViolatedError(ConditionViolatedError):
    """ Used to indicate a precondition on the function was violated """


class PostconditionViolatedError(ConditionViolatedError):
    """ Used to indicate a postcondition was violated on the function """


class MalformedDecoratorError(BaseException):
    """
    Used to indicate that the used decorator is not correct. E.g. it specifies parameters that do not occur in the
    decorated function.
    """
