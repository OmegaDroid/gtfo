try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock
from django.test import TestCase
from gtfo.gtfo_site import dns


class Dns_Mapping(TestCase):
    def test_NoPrefixOrSuffixIsSupplied_ValueErrorIsRaised(self):
        self.assertRaises(ValueError, dns.Mapping, "localhost:8000")

    def test_PrefixIsSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping("localhost:8000", prefix="gtfo.")

        self.assertIn("gtfo.foo", map)

    def test_SuffixIsSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping("localhost:8000", suffix=".gtfo")

        self.assertIn("foo.gtfo", map)

    def test_PrefixAndSuffixSuppliedNameMatchesPattern_PatternIsInMap(self):
        map = dns.Mapping("localhost:8000", prefix="pre.", suffix=".suf")

        self.assertIn("pre.foo.suf", map)

    def test_SuppliedNameDoesnotMatchePattern_PatternIsNotInMap(self):
        map = dns.Mapping("localhost:8000", prefix="pre.", suffix=".suf")

        self.assertNotIn("foo", map)

    def test_PrefixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping("localhost:8000", prefix="gtfo.")

        self.assertEqual("localhost:8000/foo", map["gtfo.foo"])

    def test_SuffixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping("localhost:8000", suffix=".gtfo")

        self.assertEqual("localhost:8000/foo", map["foo.gtfo"])

    def test_PrefixAndSuffixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping("localhost:8000", prefix="pre.", suffix=".suf")

        self.assertEqual("localhost:8000/foo", map["pre.foo.suf"])

    def test_SuppliedStringDoesNotMatchThePattern_KeyErrorIsRaised(self):
        map = dns.Mapping("localhost:8000", prefix="pre.", suffix=".suf")

        self.assertRaises(KeyError, map.__getitem__, "foo")
