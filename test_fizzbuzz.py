from main import fizzbuzz
import pytest


def test_smoke_test():
    assert fizzbuzz(1)=="1"

def test_return_fizz_multiple_of_3():
    assert fizzbuzz(3)=="Fizz"

def test_return_buzzz_multiple_of_5():
    assert fizzbuzz(5)=="Buzz"


    