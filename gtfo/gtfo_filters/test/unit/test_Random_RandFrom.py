from unittest import TestCase
from unittest.mock import patch, Mock

from gtfo.gtfo_filters.templatetags.random import rand_from


class Random_RandFrom(TestCase):
    def test_NoArgumentsGiven_ValueErrorIsRaised(self):
        self.assertRaises(ValueError, rand_from)

    @patch("gtfo.gtfo_filters.templatetags.random.random.choice", Mock(side_effect=lambda args: {"chose_from": args}))
    def test_ArgumentsGiven_ReturnValueIsRandomChosenFromArgs(self):
        self.assertEqual({"chose_from": (1, 2, "foo", "bar")}, rand_from(1, 2, "foo", "bar"))