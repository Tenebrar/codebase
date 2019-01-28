from collections import defaultdict

# This seems to be a brainfuck program
value = '>++++++++[<+++++++++++>-]<+.>+++[<+++++++>-]<+.++++++.---.>+++++++++[<--------->-]<-.>++++++++[<++++++++>-]<+.+++++++++++++.+++++.++++.>+++[<------>-]<.+++++++++++++.>+++++++++[<--------->-]<-.>++++++++[<+++++++++>-]<+.++++++++++.>+++++++[<------------>-]<+.++.>++++++[<+++++++++++>-]<.+.>+++[<++++++>-]<.>+++[<------>-]<-.++++++++++++++.---.+.>++++++[<------------->-]<.'  # noqa


class BrainfuckInterpreter:
    def __init__(self, program):
        self.commands = {
            '>': self.increment_data_pointer,
            '<': self.decrement_data_pointer,
            '+': self.increment_byte_at_data_pointer,
            '-': self.decrement_byte_at_data_pointer,
            '.': self.print_byte_at_data_pointer,
            ',': self.store_input_at_data_pointer,
            '[': self.conditional_jump_forward,
            ']': self.conditional_jump_backward,
        }

        self.instruction = 0
        self.data_pointer = 0
        self.data = defaultdict(lambda: 0)
        self.program = program

    def __call__(self, *args, **kwargs):
        while self.instruction < len(self.program):
            command = self.program[self.instruction]
            self.instruction += 1

            self.commands[command]()

    def increment_data_pointer(self):
        self.data_pointer += 1

    def decrement_data_pointer(self):
        self.data_pointer -= 1

    def increment_byte_at_data_pointer(self):
        self.data[self.data_pointer] += 1

    def decrement_byte_at_data_pointer(self):
        self.data[self.data_pointer] -= 1

    def print_byte_at_data_pointer(self):
        print(chr(self.data[self.data_pointer]), end='')

    def store_input_at_data_pointer(self):
        self.data[self.data_pointer] = self._get_input()

    def conditional_jump_forward(self):
        if self.data[self.data_pointer] == 0:
            unmatched = ['[']
            while unmatched:
                if self.program[self.instruction] == '[':
                    unmatched.append('[')
                elif self.program[self.instruction] == ']':
                    unmatched.pop()
                self.instruction += 1

    def conditional_jump_backward(self):
        if self.data[self.data_pointer] != 0:
            unmatched = [']']
            self.instruction -= 2  # Go back to before the ]
            while unmatched:
                if self.program[self.instruction] == ']':
                    unmatched.append(']')
                elif self.program[self.instruction] == '[':
                    unmatched.pop()
                self.instruction -= 1
            self.instruction += 2  # Go to after the [

    def _get_input(self):
        raise NotImplementedError('Not relevant for this challenge')


BrainfuckInterpreter(value)()
