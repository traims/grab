# Copyright: 2011, Grigoriy Petukhov
# Author: Grigoriy Petukhov (http://lorien.name)
# License: BSD
"""
Interface to BeatifulSoup.
"""

class BeautifulSoupExtension(object):
    """
    This extension provides ``soup`` attribute which allows
    you to work with response DOM tree via BeautifulSoup interface.
    """

    def extra_reset(self):
        self._soup = None

    @property
    def soup(self):
        """
        Return BeautifulSoup descriptor.
        """

        from BeautifulSoup import BeautifulSoup

        if not self._soup:
            self._soup = BeautifulSoup(self.response.body)
        return self._soup
