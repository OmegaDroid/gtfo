.. GTFO documentation master file, created by
   sphinx-quickstart on Mon Dec  8 23:09:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Get The File Out
================

Imagine you are creating a cloud based application that draws data from lots of network hardware. Now imagine you
have been developing with a test system that has 3 or 4 instances of this hardware. You now deliver to the customer who
is running over 1000 instances of the hardware and all of a sudden the interface is sluggish due to the high load on the
stats generation. This is where you should GTFO.

GTFO allows for rapid setup of a test and development environment which is similar to what will be seen in the wild
without needing to invest in lots of hardware. Once the server is configured you can navigate to any url that matches
one of the registered regular expressions and the server will return a response created from the registered template.

**Contents:**

.. toctree::
   :maxdepth: 2

   setup
   templates
