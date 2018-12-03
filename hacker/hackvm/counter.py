class IterationCounter(object):
    """
    Class to keep track of an iteration count
    """
    def __init__(self, max_iterations):
        """
        Creates an IterationCounter with a given amount of maximum iterations
        :param max_iterations:
        """
        self._MAX_ITERATIONS = max_iterations
        self._iteration_counter = 0

    def increment(self):
        """
        Increments the iteration count, raises an Exception when the iteration count is greater than the maximum
        """
        self._iteration_counter += 1
        if self._iteration_counter > self._MAX_ITERATIONS:
            raise RuntimeError('Too many iterations')
