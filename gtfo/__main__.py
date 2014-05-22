import argparse
import os
from django.core import management
from gtfo.gtfo_site.dns import start_dns
from gtfo.gtfo_site.registry import load_registry


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gtfo",
        description="Get The File Out, A Network Hardware Replacement Tool"
    )

    parser.add_argument('registry', type=str, help="Path to the url registration file")
    parser.add_argument('-ip', '--ip-address', type=str, help="The ip to open the server on (including port)", default="127.0.0.1:8000")
    parser.add_argument('-dns', '--dns-fallbacks', type=str, help="The ip address and ports for the fallback dns servers", default=None, nargs="*")
    parser.add_argument('-p', '--dns-prefix', type=str, help="The prefix for hostnames to map to the server", default=None)
    parser.add_argument('-s', '--dns-suffix', type=str, help="The suffix for hostnames to map to the server", default=None)

    return parser.parse_args()


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gtfo_site.settings")
    args = parse_args()

    load_registry(args.registry)
    if args.dns_prefix or args.dns_suffix:
        if not args.dns_fallbacks:
            print("You must supply at least one dns fallback server to enable the dns")
            return

        start_dns(args.ip_address, args.dns_fallbacks, prefix=args.dns_prefix, suffix=args.dns_suffix)
    management.call_command('runserver', args.ip_address)


if __name__ == "__main__":
    main()

