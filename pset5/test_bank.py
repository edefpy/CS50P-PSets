import pytest
from bank import value


def test_hello():
    assert value("hello there, friend.") == 0
    assert value("hello, world.") == 0


def test_h():
    assert value("how is it going?") == 20
    assert value("hey there, friend.") == 20


def test_others():
    assert value("are you feeling good today?") == 100
    assert value("what's happening?") == 100


def test_case_and_whitespace():
    assert value("     HELLO THERE, FRIEND.     ") == 0
    assert value("     HOW IS IT GOING?     ") == 20
    assert value("     WHAT'S HAPPENING?     ") == 100
