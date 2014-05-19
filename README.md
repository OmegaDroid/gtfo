GTFO
====

Get The file Out - A Network Hardware Replacement Tool

Scenario
========

Imagine you are creating a cloud based application that draws data from lots of network hardware. Now imagine you
have been developing with a test system that has 3 or 4 instances of this hardware. You now deliver to the customer who
is running over 1000 instances of the hardware and all of a sudden the interface is sluggish due to the high load on the
stats generation. This is where you should GTFO.

GTFO allows for rapid setup of a test and development environment which is similar to what will be seen in the wild
without needing to invest in lots of hardware. Once the server is configured you can navigate to any url that matches
one of the registered regular expressions and the server will return a response created from the registered template.

Setup
=====

To install GTFO run.

'''
pip install git+git://github.com/OmegaDroid/gtfo
'''

You will then need to create a registry file that contains a json dictionary with template paths indexed against their
url regex. Note: the actual url you navigate to is {{ server_host }}/{{ device_host }}/{{ page_url }}

For example, if GTFO is running on localhost:8000:

'''
{
    "^$": "index.html",
    "^hello$: "hello.html
}
'''

Would give a server where "localhost:8000/foo/" would give the "index.html" response for device "foo" and
"localhost:8000/bar/hello" would give the "hello.html" response for device "bar". All paths in the registry are given
relative to the registry file.
