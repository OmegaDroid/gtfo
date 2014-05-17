import json
import os
import re
from django.conf import settings


def load_registry(path):
    with open(path, 'r') as f:
        reg = json.load(f)
        reg = {k: os.path.join(os.path.dirname(path), v) for k, v in reg.items()}
        settings.TEMPLATE_REGISTRY = TemplateRegistry(reg)
        settings.GTFO_CACHE_DIR = os.path.join(os.path.dirname(path), "cache")


class TemplateRegistry():
    def __init__(self, reg):
        """
        Registers a set of templates to regular expression paths

        :param reg: A set of template file paths indexed against it's url regex
        """
        self._registry = reg

    def get_template(self, url):
        """
        Gets the template path and the context gathered from the url. If the url does not match any of the registration
        regexes None is returned.

        Named groups are stored in the context element as group name value pairs

        :param url: The url to find the template for

        :return: A dictionary containing the template file path and context gathered from the url if the ur matches a
                 registered regex. None otherwise
        """
        for k, v in self._registry.items():
            m = re.match(k, url)
            if m:
                return {
                    "template": v,
                    "context": m.groupdict()
                }

        return None
