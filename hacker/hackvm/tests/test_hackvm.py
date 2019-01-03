from os import environ
from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile
import sys


def call_hackvm(program):
    """ Calls the hackvm (its initial implementation needs to be called as a process) """
    my_env = environ.copy()
    my_env['PYTHONPATH'] = './'
    with NamedTemporaryFile(delete=False) as tf:
        tf.write(program.encode('utf-8'))
        tf.close()
        proc = Popen([sys.executable, 'hacker/hackvm/hackvm.py', tf.name], stdout=PIPE, stderr=STDOUT, env=my_env)
        return proc.communicate()[0].decode('utf-8')


def test_case1() -> None:
    """ Example from http://www.hacker.org/hvm/ """
    assert call_hackvm('78*p').strip() == '56'


def test_case2() -> None:
    """ Example from http://www.hacker.org/hvm/ """
    assert call_hackvm('123451^2v5:4?9p2g8pppppp').strip() == '945321'


def test_div() -> None:
    """ Test for integer division even though the example implementation does not do this """
    assert call_hackvm('43/p').strip() == '1'
