Templates
=========

Templates follow the django specification (see https://docs.djangoproject.com/en/dev/topics/templates/), all standard
template tags and filters should be available.

Any named groups are available by name in the template as well as the name of the device host (referenced by "host").
For example, if there is a template file "foo.html"::

    Hello {{ host }}: The sky is {{ color }}


Is indexed by::

    "^sky/(?P<color>[^/])$"


The url "localhost:8000/world/sky/green" would give the following response::

    Hello world: The sky is green

