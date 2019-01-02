class IterationCounter(object):
    """
    Class to keep track of an iteration count
    """
    def __init__(self, max_iterations: int) -> None:
        """
        Creates an IterationCounter with a given amount of maximum iterations
        :param max_iterations: The maximum amount of iterations allowed
        :raises ValueError: If the value is negative
        """
        if max_iterations < 0:
            raise ValueError(f'Maximum iteration value must be positive, not {max_iterations}')
        self._MAX_ITERATIONS = max_iterations

        self._iteration_counter = 0

    def increment(self) -> None:
        """
        Increments the iteration count, raises an Exception when the iteration count is greater than the maximum
        :raises RuntimeError: If the iteration maximum is exceeded
        """
        self._iteration_counter += 1
        if self._iteration_counter > self._MAX_ITERATIONS:
            raise RuntimeError(f'Maximum of {self._MAX_ITERATIONS} iterations exceeded.')
