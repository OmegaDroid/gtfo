from unittest.mock import patch, Mock
from django.test import TestCase
from gtfo.gtfo_site import dns


class Dns_Mapping(TestCase):
    def test_NoPrefixOrSuffixIsSupplied_ValueErrorIsRaised(self):
        self.assertRaises(ValueError, dns.Mapping)

    @patch("gtfo.gtfo_site.utils.get_server_address", Mock(return_value="localhost:8000"))
    def test_PrefixIsSuppliedNameMatchesPattern_TheReturnedStringContainsTheServerHostAndDeviceHost(self):
        map = dns.Mapping(["ns_server"], prefix="gtfo.")

        self.assertEqual("localhost:8000/foo", map.lookupAddress("gtfo.foo"))
