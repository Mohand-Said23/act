import pytest
from calcul import add, multi

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_multi():
    assert multi(2, 2) == 4
    assert multi(0, 2) == 0