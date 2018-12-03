from hacker.hackvm.integers import verify_integer


class OperandStack(object):
    stack = []

    def push(self, v):
        verify_integer(v)
        self.stack.append(v)

    def pop(self):
        if len(self.stack) == 0:
            raise RuntimeError('Stack underflow')
        return self.stack.pop()

    def do_pick(self):
        where = self._pop_index()
        self.push(self.stack[-1 - where])

    def do_roll(self):
        where = self._pop_index()
        v = self.stack[-1 - where]
        del self.stack[-1 - where]
        self.push(v)

    def _pop_index(self):
        where = self.pop()
        if where < 0 or where >= len(self.stack):
            raise RuntimeError('out of stack bounds @' + str(where))
        return where

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)


# TODO replace with tests
s = OperandStack()
print(s)
s.push(4)
s.push(5)
s.push(6)
print(s)
print(s.pop())
print(s)
s.pop()
