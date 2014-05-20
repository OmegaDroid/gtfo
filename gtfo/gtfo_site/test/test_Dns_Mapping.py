from unittest.mock import patch, Mock
from django.test import TestCase
from gtfo.gtfo_site import dns


class Dns_Mapping(TestCase):
    def test_NoPrefixOrSuffixIsSupplied_ValueErrorIsRaised(self):
        self.assertRaises(ValueError, dns.Mapping)

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_PrefixIsSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping([("ns_server", 8080)], prefix="gtfo.")

        self.assertEqual("localhost:8000/foo", map.lookupAddress("gtfo.foo"))

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_SuffixIsSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping([("ns_server", 8080)], suffix=".gtfo")

        self.assertEqual("localhost:8000/foo", map.lookupAddress("foo.gtfo"))

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_PrefixAndSuffixSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping([("ns_server", 8080)], prefix="pre.", suffix=".suf")

        self.assertEqual("localhost:8000/foo", map.lookupAddress("pre.foo.suf"))
