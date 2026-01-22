from main import fizzbuzz
import pytest


def test_smoke_test():
    assert fizzbuzz(1)=="1"

def test_return_fizz_multiple_of_3():
    assert fizzbuzz(3)=="Fizz"

def test_return_buzz_multiple_of_5():
    assert fizzbuzz(5)=="Buzz"

def test_return_fizzbuzz_multiple_of_3_and_5():
    assert fizzbuzz(15)=="FizzBuzz"

def test_for_non_integers():
    with pytest.raises(TypeError):
        fizzbuzz("15")
    with pytest.raises(TypeError):
        fizzbuzz(3.0)
    with pytest.raises(TypeError):
        fizzbuzz(None)
    