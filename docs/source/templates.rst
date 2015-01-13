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

Template Tags
=============

random
------

The random module supplies methods for creating random values. It is loaded by loading random at the top of your
template::

    {% load random %}

**Caching**

When a request is made with a particular set of parameters it's result is cached. This can be useful when generating one
responses per day or time so that the result doesn't change.

**rand_int**

rand_int creates a random integer between 2 optional parameters. If no parameters are supplied 0 or 1 are returned
randomly. If one parameter is supplied a random integer between 0 and the supplied value is produced. If two values are
supplied a random integer between the supplied values is supplied.

Usage::

    <div>0 or 1: {% rand_int %}</div>
    <div>0 - 10: {% rand_int 10 %}</div>
    <div>3 - 13: {% rand_int 3 13 %}</div>

**rand_float**

rand_float creates a random float between 2 optional parameters. If no parameters are supplied a float between 0 and 1
is produced. If one parameter is supplied a random float between 0 and the supplied value is produced. If two values are
supplied a random float between the supplied values is produced.

Usage::

    <div>0 - 1: {% rand_float %}</div>
    <div>0 - 10: {% rand_float 10 %}</div>
    <div>3 - 13: {% rand_float 3 13 %}</div>

**rand_from**

rand_from returns a random value from the list of supplied values.

Usage::

    <div>"a", "b" or "c": {% rand_from "a" "b" "c" %}</div>

