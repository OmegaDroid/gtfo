Setup
=====

To install GTFO run::

    pip install git+git://github.com/OmegaDroid/gtfo


You will then need to create a registry file that contains a json dictionary with template paths indexed against their
url regex. Note: the actual url you navigate to is::

    {{ server_host }}/{{ device_host }}/{{ page_url }}


For example, if GTFO is running on localhost:8000::

    {
        "^$": "index.html",
        "^hello$: "hello.html
    }


Would give a server where "localhost:8000/foo/" would give the "index.html" response for device "foo" and
"localhost:8000/bar/hello" would give the "hello.html" response for device "bar". All paths in the registry are given
relative to the registry file.