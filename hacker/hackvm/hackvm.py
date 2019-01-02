from functools import partial
from numpy import zeros
import sys

from hacker.hackvm.counter import IterationCounter
from hacker.hackvm.stack import OperandStack

# Adapted from http://www.hacker.org/hvm/hackvm.py, with explanations on http://www.hacker.org/hvm/

MEMORY = zeros(16384, dtype=int)
CALL_STACK = []
OPERAND_STACK = OperandStack()
PROGRAM_COUNTER = 0

OUT = sys.stdout


def do_print_char():
    value = OPERAND_STACK.pop()
    OUT.write(chr(value & 0x7F))


def do_print_int():
    value = OPERAND_STACK.pop()
    OUT.write(str(value))


def do_goto():
    global PROGRAM_COUNTER
    PROGRAM_COUNTER += OPERAND_STACK.pop()


def do_goto_if_zero():
    global PROGRAM_COUNTER
    offset = OPERAND_STACK.pop()
    if OPERAND_STACK.pop() == 0:
        PROGRAM_COUNTER += offset


def do_call():
    global PROGRAM_COUNTER
    CALL_STACK.append(PROGRAM_COUNTER)
    PROGRAM_COUNTER = OPERAND_STACK.pop()


def do_return():
    global PROGRAM_COUNTER
    PROGRAM_COUNTER = CALL_STACK.pop()


def do_peek():
    addr = OPERAND_STACK.pop()
    if addr < 0 or addr >= len(MEMORY):
        raise RuntimeError('memory read access violation @' + str(addr))
    OPERAND_STACK.push(MEMORY[addr])


def do_poke():
    addr = OPERAND_STACK.pop()
    if addr < 0 or addr >= len(MEMORY):
        raise RuntimeError('memory write access violation @' + str(addr))
    MEMORY[addr] = OPERAND_STACK.pop()


def do_end():
    global PROGRAM_COUNTER
    PROGRAM_COUNTER = len(Code)


OPERATIONS = {
    ' ': lambda: None,  # NO_OP
    '\n': lambda: None,  # NO_OP
    'p': do_print_int,
    'P': do_print_char,
    '0': partial(OPERAND_STACK.push, 0),
    '1': partial(OPERAND_STACK.push, 1),
    '2': partial(OPERAND_STACK.push, 2),
    '3': partial(OPERAND_STACK.push, 3),
    '4': partial(OPERAND_STACK.push, 4),
    '5': partial(OPERAND_STACK.push, 5),
    '6': partial(OPERAND_STACK.push, 6),
    '7': partial(OPERAND_STACK.push, 7),
    '8': partial(OPERAND_STACK.push, 8),
    '9': partial(OPERAND_STACK.push, 9),
    '+': OPERAND_STACK.add_two_operands,
    '-': OPERAND_STACK.subtract_two_operands,
    '*': OPERAND_STACK.multiply_two_operands,
    '/': OPERAND_STACK.divide_two_operands,
    ':': OPERAND_STACK.cmp_two_operands,
    'g': do_goto,
    '?': do_goto_if_zero,
    'c': do_call,
    '$': do_return,
    '<': do_peek,
    '>': do_poke,
    '^': OPERAND_STACK.pick,
    'v': OPERAND_STACK.roll,
    'd': OPERAND_STACK.pop,
    '!': do_end
}


def run(verbose=False):
    global PROGRAM_COUNTER

    iteration_counter = IterationCounter(max_iterations=10000)
    op_code = ' '
    try:
        while PROGRAM_COUNTER != len(Code):
            op_code = Code[PROGRAM_COUNTER]
            if verbose:
                sys.stderr.write('@' + str(PROGRAM_COUNTER) + ' ' + op_code + ' ')
            PROGRAM_COUNTER += 1
            iteration_counter.increment()
            OPERATIONS[op_code]()
            if not 0 <= PROGRAM_COUNTER <= len(Code):
                raise RuntimeError('out of code bounds')
            if verbose:
                sys.stderr.write(str(OPERAND_STACK) + '\n')

        OUT.write('\n')
    except BaseException as e:
        OUT.write('\n')
        OUT.write('!ERROR: exception while executing I=' + str(op_code) + ' PC=' + str(PROGRAM_COUNTER - 1) +
                  ' STACK_SIZE=' + str(len(OPERAND_STACK)) + '\n')
        OUT.write(e)


if len(sys.argv) < 2:
    OUT.write('hackvm.py [--init <init-mem-filename>] [--trace] <code-filename>')
    OUT.write('The format for the initial memory file is: cell0,cell1,...')
else:
    verbose = False
    args = sys.argv
    args.reverse()
    args.pop()
    while len(args):
        arg = args.pop()
        if len(args) == 0:  # The last argument is always the code
            Code = open(arg).read()
        elif arg == '--trace':
            verbose = True
        elif arg == '--init':
            initial_memory = open(args.pop()).read().split(',')
            MEMORY[:len(initial_memory)] = [int(val) for val in initial_memory]
        else:
            raise ValueError('invalid argument ' + arg)

    run(verbose)
