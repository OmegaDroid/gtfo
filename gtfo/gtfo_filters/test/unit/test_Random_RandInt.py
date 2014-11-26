from unittest import TestCase
from unittest.mock import patch, Mock
from gtfo.gtfo_filters.random import rand_int


def _randint(a, b):
    return {"a": a, "b": b}


@patch("gtfo.gtfo_filters.random.random.randint", Mock(side_effect=_randint))
class Random_RandomInt(TestCase):
    def test_NoArgumentsGiven_ResultIsRandomBetweenZeroAndOne(self):
        res = rand_int()

        self.assertEqual({"a": 0, "b": 1}, res)

    def test_SinglePositiveArgumentsGiven_ResultIsRandomBetweenZeroAndValue(self):
        res = rand_int(2)

        self.assertEqual({"a": 0, "b": 2}, res)

    def test_SingleNegativeArgumentsGiven_ResultIsRandomBetweenZeroAndValue(self):
        res = rand_int(-2)

        self.assertEqual({"a": -2, "b": 0}, res)

    def test_TwoPositiveArgumentsGivenInOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(2, 3)

        self.assertEqual({"a": 2, "b": 3}, res)

    def test_TwoPositiveArgumentsGivenInReverseOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(3, 2)

        self.assertEqual({"a": 2, "b": 3}, res)

    def test_TwoNegativeArgumentsGivenInOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(-3, -2)

        self.assertEqual({"a": -3, "b": -2}, res)

    def test_TwoNegativeArgumentsGivenInReverseOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(-2, -3)

        self.assertEqual({"a": -3, "b": -2}, res)

    def test_OnePositiveOneNegativeArgumentGivenInOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(-3, 2)

        self.assertEqual({"a": -3, "b": 2}, res)

    def test_OnePositiveOneNegativeArgumentGivenInReverseOrder_ResultIsRandomBetweenUpperAndLower(self):
        res = rand_int(2, -3)

        self.assertEqual({"a": -3, "b": 2}, res)
