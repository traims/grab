.. _grab_redirect:

Redirect Handling
=================

Grab supports two types of redirects:

* HTTP redirect with 301 and 302 code
* HTML redirect with <meta> tag

HTTP 301/302 Redirect
---------------------

By default, Grab follows any 301 or 302 redirect. You can control maximum number
of redirects per one network query with :ref:`option_redirect_limit` option. To completely
disable handling of HTTP redirects set :ref:`option_follow_location` to False.

Let's see how it works::

    >>> g = Grab()
    >>> g.setup(follow_location=False)
    >>> g.go('http://google.com')
    <grab.response.Response object at 0x1246ae0>
    >>> g.response.code
    301
    >>> g.response.headers['Location']
    'http://www.google.com/'
    >>> g.setup(follow_location=True)
    >>> g.go('http://google.com')
    <grab.response.Response object at 0x1246ae0>
    >>> g.response.code
    200
    >>> g.response.url
    'http://www.google.ru/?gws_rd=cr&ei=BspFUtS8EOWq4ATAooGADA'

Meta Refresh Redirect
---------------------

HTML Page could contains special tag that instructs browser to go at specified URL::

    <meta http-equiv="Refresh" content="0; url=http://some/url" />

By default, Grab ignores such inststructions. If you want automatically follow meta refresh
tags then set :ref:`option_follow_refresh` to True.

Original and Destination URLs
-----------------------------

You can always get information about what URl you've requested intially and what URL you've got::

    >>> g = Grab()
    >>> g.go('http://google.com')
    <grab.response.Response object at 0x20fcae0>
    >>> g.config['url']
    'http://google.com'
    >>> g.response.url
    'http://www.google.ru/?gws_rd=cr&ei=8spFUo32Huem4gT6ooDwAg'

Initial URL is stored at the config object. The destination URL is writed into `response` object.

You can even to track redirect history with `response.head`::

    >>> print g.response.head
    HTTP/1.1 301 Moved Permanently
    Location: http://www.google.com/
    Content-Type: text/html; charset=UTF-8
    Date: Fri, 27 Sep 2013 18:19:13 GMT
    Expires: Sun, 27 Oct 2013 18:19:13 GMT
    Cache-Control: public, max-age=2592000
    Server: gws
    Content-Length: 219
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN

    HTTP/1.1 302 Found
    Location: http://www.google.ru/?gws_rd=cr&ei=IsxFUp-8CsT64QTZooDwBA
    Cache-Control: private
    Content-Type: text/html; charset=UTF-8
    Date: Fri, 27 Sep 2013 18:19:14 GMT
    Server: gws
    Content-Length: 258
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN

    HTTP/1.1 200 OK
    Date: Fri, 27 Sep 2013 18:19:14 GMT
    Expires: -1
    Cache-Control: private, max-age=0
    Content-Type: text/html; charset=UTF-8
    Content-Encoding: gzip
    Server: gws
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN
    Transfer-Encoding: chunked
