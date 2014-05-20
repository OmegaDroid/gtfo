import re
from twisted.names import client, dns
from gtfo.gtfo_site import utils

class Mapping(client.Resolver):
#class Mapping():
    def __init__(self, servers=None, prefix=None, suffix=None):
        super().__init__(servers=servers)
        if not prefix and not suffix:
            raise ValueError("A hostname prefix or suffix must be supplied")

        self._mapper = re.compile("%s(.+)%s" % (prefix or "", suffix or ""))

    def lookupAddress(self, name, timeout=None):
        m = self._mapper.match(name)
        if m:
            return utils.get_server_address() + "/" + m.group(1)
        else:
            return self._lookup(name, dns.IN, dns.A, timeout)