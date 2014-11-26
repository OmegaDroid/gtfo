import os
import site
site.addsitedir(os.path.join(os.path.dirname(__file__), ".."))

import argparse
from django.core import management
from gtfo.gtfo_site.registry import load_registry



def parse_args():
    parser = argparse.ArgumentParser(
        prog="gtfo",
        description="Get The File Out, A Network Hardware Replacement Tool"
    )

    parser.add_argument('registry', type=str, help="Path to the url registration file")
    parser.add_argument('-ip', '--ip-address', type=str, help="The ip to open the server on (including port)", default="127.0.0.1:8000")

    return parser.parse_args()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gtfo_site.settings")
    args = parse_args()
    load_registry(args.registry)
    management.call_command('runserver', args.ip_address)

