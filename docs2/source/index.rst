Grab documentation
==================

Grab is a python framework for building site scrapers. Grab library consists of two main interfaces:

1) Grab. The main interface to configure network requests and to handle network response.
2) Grab::Spider. More complex interface to build asynchronous site scrapers. Spider interface has many common with Scrapy interface. The main benefits of Spider are asynchronous concurrent request engine, network cache and internal design that forcew you to organize your scraping logic in well structured blocks.

Consider to use Grab API:

* When you want to submit signle network request and process the response
* Inside Grab::Spider to configure complex parameters of network request
* Inside Grab::Spider to handle data received in network response 
* In most of cases when you think to use urllib, urllib2, pycurl or requests libs.

Grab::Spider probably will useful to you:

* When you need to exract data from web site with multiple concurrent web workers
* In most of cases when you think to use scrapy lib.

You can think of Grab and Spider from this point: Grab is like a Requests library and Grab::Spider is like a Scrapy library. Good news, you can use Grab inside Grab::Spider to configure network requests as you want.

Grab is not only a tool to build network requests and download network responses, it is also a tool to handle data of network response and extract information you need. Grab provides flexible API to query parts of DOM-tree of the HTML document.

See quick start tutorials to quickly get main ideas about how to use Grab and Grab::Spider:

Grab User Manual
----------------

.. toctree::
    :maxdepth: 2

    grab_quickstart
    grab_installation
    grab_configuration
    grab_debugging
    grab_options
    grab_http_headers
    grab_http_methods
    grab_response_body
    grab_redirect
    grab_forms
    grab_charset
    pycurl
    changelog

API Reference
-------------

Using API Reference you can get ideas about what modules, classes, methods exists,
 what they do, what returns, what parameters accepts.

Base Grab Interface
~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 2

    api_grab_base
    api_grab_error
