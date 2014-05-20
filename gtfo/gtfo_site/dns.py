import re
from twisted.names import client

#class Mapping(client.Resolver):
from gtfo.gtfo_site import utils


class Mapping():
    def __init__(self, servers=None, prefix=None, suffix=None):
        #super().__init__(servers)
        if not prefix:
            raise ValueError("A hostname prefix or suffix must be supplied")

        self._mapper = re.compile(prefix + "(.+)")

    def lookupAddress(self, name, timeout=None):
        m = self._mapper.match(name)
        if m:
            return utils.get_server_address() + "/" + m.group(1)