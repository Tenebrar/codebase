import re
import sys
from functools import partial

from hacker.hackvm.integers import verify_integer
from hacker.hackvm.counter import IterationCounter


Memory = [0] * 16384
CallStack = []
OperandStack = []
ProgramCounter = 0


def push(v):
    verify_integer(v)
    OperandStack.append(v)


def pop():
    if len(OperandStack) == 0:
        raise RuntimeError('Stack underflow')
    return OperandStack.pop()


def do_print_char():
    sys.stdout.write(chr(pop() & 0x7F))


def do_print_int():
    sys.stdout.write(str(pop()))


def do_add():
    push(pop() + pop())


def do_sub():
    a = pop()
    b = pop()
    push(b - a)


def do_mul():
    push(pop() * pop())


def do_div():
    a = pop()
    b = pop()
    push(b / a)


def do_cmp():
    a = pop()
    b = pop()
    push((b > a) - (b < a))  # replacement for cmp suggested at: https://docs.python.org/3.0/whatsnew/3.0.html


def do_goto():
    global ProgramCounter
    ProgramCounter += pop()


def do_goto_if_zero():
    global ProgramCounter
    offset = pop()
    if pop() == 0:
        ProgramCounter += offset


def do_call():
    global ProgramCounter
    CallStack.append(ProgramCounter)
    ProgramCounter = pop()


def do_return():
    global ProgramCounter
    ProgramCounter = CallStack.pop()


def do_peek():
    addr = pop()
    if addr < 0 or addr >= len(Memory):
        raise RuntimeError('memory read access violation @' + str(addr))
    push(Memory[addr])


def do_poke():
    addr = pop()
    if addr < 0 or addr >= len(Memory):
        raise RuntimeError('memory write access violation @' + str(addr))
    Memory[addr] = pop()


def do_pick():
    where = pop()
    if where < 0 or where >= len(OperandStack):
        raise RuntimeError('out of stack bounds @' + str(where))
    push(OperandStack[-1 - where])


def do_roll():
    where = pop()
    if where < 0 or where >= len(OperandStack):
        raise RuntimeError('out of stack @' + str(where))
    v = OperandStack[-1 - where]
    del OperandStack[-1 - where]
    push(v)


def do_drop():
    pop()


def do_end():
    global ProgramCounter
    ProgramCounter = len(Code)


def do_nothing():
    pass


OPS = {
    ' ': do_nothing,
    '\n': do_nothing,
    'p': do_print_int,
    'P': do_print_char,
    '0': partial(push, 0),
    '1': partial(push, 1),
    '2': partial(push, 2),
    '3': partial(push, 3),
    '4': partial(push, 4),
    '5': partial(push, 5),
    '6': partial(push, 6),
    '7': partial(push, 7),
    '8': partial(push, 8),
    '9': partial(push, 9),
    '+': do_add,
    '-': do_sub,
    '*': do_mul,
    '/': do_div,
    ':': do_cmp,
    'g': do_goto,
    '?': do_goto_if_zero,
    'c': do_call,
    '$': do_return,
    '<': do_peek,
    '>': do_poke,
    '^': do_pick,
    'v': do_roll,
    'd': do_drop,
    '!': do_end
}


def run(verbose=False):
    global ProgramCounter

    iteration_counter = IterationCounter(max_iterations=10000)
    op_code = ' '
    try:
        while ProgramCounter != len(Code):
            op_code = Code[ProgramCounter]
            if verbose:
                sys.stderr.write('@' + str(ProgramCounter) + ' ' + op_code + ' ')
            ProgramCounter += 1
            iteration_counter.increment()
            OPS[op_code]()
            if not 0 <= ProgramCounter <= len(Code):
                raise RuntimeError('out of code bounds')
            if verbose:
                sys.stderr.write(str(OperandStack) + '\n')
    except BaseException:
        sys.stderr.write('!ERROR: exception while executing I=' + str(op_code) + ' PC=' + str(ProgramCounter - 1) +
                         ' STACK_SIZE=' + str(len(OperandStack)) + '\n')
        sys.stderr.write(str(sys.exc_info()[1]) + '\n')
        sys.exit(1)

    print()


# Parse the command line
if len(sys.argv) < 2:
    print('hackvm.py [--init <init-mem-filename>] [--trace] <code-filename>')
    print('The format for the initial memory file is: cell0,cell1,...')
    sys.exit(0)

trace = False
args = sys.argv
args.reverse()
args.pop()
while len(args):
    arg = args.pop()
    if len(args) == 0:
        Code = open(arg).read()
    elif arg == '--trace':
        trace = True
    elif arg == '--init':
        initial_memory = re.compile('\s*,\s*').split(open(args.pop()).read())
        for i in range(0, len(initial_memory)):
            Memory[i] = int(initial_memory[i].strip())
    else:
        raise ValueError('invalid argument ' + arg)

run(trace)
