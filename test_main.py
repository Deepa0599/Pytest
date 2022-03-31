import main
import pytest


@pytest.fixture
def input():
    a = 315
    return a
def test_divby5_1(input):
    # a = 10
    out1 = main.divby5(input)
    assert out1 == True

def test_divby5_2(input):
    #a = 11
    out1 = main.divby5(input)
    assert out1 == False

def test_divby7_1(input):
    #a = 14
    out1 = main.divby7(input)
    assert out1 == True

def test_divby7_2(input):
   # a = 15
    out1 = main.divby7(input)
    assert out1 == False

def test_divby9_1(input):
   # a = 18
    out1 = main.divby9(input)
    assert out1 == True

def test_divby9_2():
  #  a = 19
    out1 = main.divby9(input)
    assert out1 == False

def test_divby11_1(input):
   # a = 22
    out1 = main.divby11(input)
    assert out1 == True

def test_divby11_2(input):
    #a = 23
    out1 = main.divby11(input)
    assert out1 == False

