from unittest import TestCase
from unittest.mock import patch, Mock
from gtfo.gtfo_filters.random import rand_int, rand_float


@patch("gtfo.gtfo_filters.random.random.random")
class Random_RandomInt(TestCase):
    def test_NoArgumentsAreGiven_ResultIsBetweenZeroAndOne(self, rand):
        rand.return_value = 0

        self.assertEqual(0, rand_float())

        rand.return_value = 1

        self.assertEqual(1, rand_float())

    def test_SinglePositiveValueGiven_ResultIsBetweenZeroAndTheValue(self, rand):
        rand.return_value = 0

        self.assertEqual(0, rand_float(2))

        rand.return_value = 1

        self.assertEqual(2, rand_float(2))


    def test_SingleNegativeValueGiven_ResultIsBetweenZeroAndTheValue(self, rand):
        rand.return_value = 0

        self.assertEqual(-2, rand_float(-2))

        rand.return_value = 1

        self.assertEqual(0, rand_float(-2))

    def test_TwoPositiveArgumentsInOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(2, rand_float(2, 3))

        rand.return_value = 1

        self.assertEqual(3, rand_float(2, 3))

    def test_TwoPositiveArgumentsInReverseOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(2, rand_float(3, 2))

        rand.return_value = 1

        self.assertEqual(3, rand_float(3, 2))

    def test_TwoNegativeArgumentsInOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(-2, rand_float(-2, -1))

        rand.return_value = 1

        self.assertEqual(-1, rand_float(-2, -1))

    def test_TwoNegativeArgumentsInReverseOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(-2, rand_float(-1, -2))

        rand.return_value = 1

        self.assertEqual(-1, rand_float(-1, -2))

    def test_OneNegativeOnePositiveArgumentInOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(-1, rand_float(-1, 2))

        rand.return_value = 1

        self.assertEqual(2, rand_float(-1, 2))

    def test_OneNegativeOnePositiveArgumentInReverseOrder_ResultIsBetweenLowerAndUpper(self, rand):
        rand.return_value = 0

        self.assertEqual(-1, rand_float(2, -1))

        rand.return_value = 1

        self.assertEqual(2, rand_float(2, -1))