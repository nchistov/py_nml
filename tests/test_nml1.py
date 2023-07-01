import sys

sys.path.insert(0, '../src/')

from py_nml import parse
from py_nml.parse import Keyword  # For testing


def test_only_keyword():
    text = 'module'

    expected = [Keyword(name='module', arguments=[])]
    actual = parse(text)

    assert actual == expected


def test_one_argument():
    text = 'module test_module'

    expected = [Keyword(name='module', arguments=['test_module'])]
    actual = parse(text)

    assert actual == expected


def test_many_arguments():
    text = 'module test_module 1 2 3'

    expected = [Keyword(name='module', arguments=['test_module', '1', '2', '3'])]
    actual = parse(text)

    assert actual == expected


def test_many_lines():
    text = 'module test_module\nversion 0.1.0'

    expected = [Keyword(name='module', arguments=['test_module']),
                Keyword(name='version', arguments=['0.1.0'])]
    actual = parse(text)

    assert actual == expected
