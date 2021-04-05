import unittest
from fizzbuzz import fizzbuzz

def test_num():
    # Test for a return of number ranges
    assert fizzbuzz(1) == 1

def test_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "Fizzbuzz"
