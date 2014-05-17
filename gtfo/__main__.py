import argparse
import os
from django.core import management
from gtfo.gtfo.registry import load_registry


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gtfo",
        description="Get The File Out, A Network Hardware Replacement Tool"
    )

    parser.add_argument('registry', type=str, help="Path to the url registration file")

    return parser.parse_args()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gtfo.gtfo.settings")
    args = parse_args()
    load_registry(args.registry)
    management.call_command('runserver')

