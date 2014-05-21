from unittest.mock import patch, Mock, MagicMock
from django.test import TestCase
from twisted.names import client
from gtfo.gtfo_site import dns


class Dns_Mapping(TestCase):
    def test_NoPrefixOrSuffixIsSupplied_ValueErrorIsRaised(self):
        self.assertRaises(ValueError, dns.Mapping)

    def test_PrefixIsSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping(prefix="gtfo.")

        self.assertIn("gtfo.foo", map)

    def test_SuffixIsSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping(suffix=".gtfo")

        self.assertIn("foo.gtfo", map)

    def test_PrefixAndSuffixSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping(prefix="pre.", suffix=".suf")

        self.assertIn("pre.foo.suf", map)

    def test_SuppliedNameDoesnotMatchePattern_PatternIsNotInMap(self):
        map = dns.Mapping(prefix="pre.", suffix=".suf")

        self.assertNotIn("foo", map)

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_PrefixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping(prefix="gtfo.")

        self.assertEqual("localhost:8000/foo", map["gtfo.foo"])

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_SuffixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping(suffix=".gtfo")

        self.assertEqual("localhost:8000/foo", map["foo.gtfo"])

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_PrefixAndSuffixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping(prefix="pre.", suffix=".suf")

        self.assertEqual("localhost:8000/foo", map["pre.foo.suf"])

    def test_SuppliedStringDoesNotMatchThePattern_KeyErrorIsRaised(self):
        map = dns.Mapping(prefix="pre.", suffix=".suf")

        self.assertRaises(KeyError, map.__getitem__, "foo")
