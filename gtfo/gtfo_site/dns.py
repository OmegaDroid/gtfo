import re
from twisted.names import client, dns, server, cache
from twisted.application import internet, service
from gtfo.gtfo_site import utils


class Mapping():
    def __init__(self, prefix: str=None, suffix: str=None):
        """
        Initialises the mapping. The mapped regex is "{{ prefix }}(.+){{ suffix }}". If neither a prefix or suffix are
        supplied a ValueError is raised

        :param prefix: The prefix for the host name
        :param suffix: The suffix of the hostname
        :raises ValueError: If neither a prefix or suffix are supplied
        """
        if not prefix and not suffix:
            raise ValueError("A hostname prefix or suffix must be supplied")

        self._mapper = re.compile("%s(.+)%s" % (prefix or "", suffix or ""))

    def __getitem__(self, key):
        m = self._mapper.match(key)
        if not m:
            raise KeyError

        return utils.get_server_address() + "/" + m.group(1)

    def __contains__(self, key):
        return self._mapper.match(key)


class Resolver(client.Resolver):
    def __init__(self, mapper: dict(str, str), servers: list(str, int)):
        """
        Initialises the Resolver. Mapper needs to behave as a readable dictionary, as a minimum it must implement
        __contains__ and __getitem__

        :param mapper: The object to control mapping host name to ip
        :param servers: List of other dns servers to try if the hostname is not present in the map. These should be
                        hostname, port pairs
        """
        self._mapper = mapper
        super().__init__(self, servers=servers)
        self.ttl = 10

    def lookupAddress(self, name, timeout=None):
        if name in self._mapper:
            result = self._mapper[name]
            return [(dns.RRHeader(name, dns.A, dns.IN, self.ttl, dns.Record_A(result, self.ttl)),), (), ()]
        else:
            return self._lookup(name, dns.IN, dns.A, timeout)


def start_dns(prefix=None, suffix=None, fallback_servers=None):
    resolver = Resolver(Mapping(prefix=prefix, suffix=suffix), servers=fallback_servers)

    # create the protocols
    f = server.DNSServerFactory(caches=[cache.CacheResolver()], clients=[resolver])
    p = dns.DNSDatagramProtocol(f)
    f.noisy = p.noisy = False

    # register as tcp and udp
    ret = service.MultiService()
    PORT=53

    for (klass, arg) in [(internet.TCPServer, f), (internet.UDPServer, p)]:
        s = klass(PORT, arg)
        s.setServiceParent(ret)


    # run all of the above as a twistd application## this sets up the application
    application = service.Application('dnsserver', 1, 1)
    ret.setServiceParent(service.IServiceCollection(application))