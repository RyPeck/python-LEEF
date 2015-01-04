#!/usr/bin/python

"""
Based off of the IBM Guide for LEEF 1.0 - http://goo.gl/8u4Kfg
    Acquired November 17th, 2014 - 5a57f47d20d6e73da6fa7d6501b3b3cd

Currently can only use to construct a properly formatted LEEF Log message.
"""

from __future__ import print_function


__version__ = '0.0.1'


class Logger:
    """LEEFLOGGER"""

    # LEEF Headers
    version_major = None
    version_minor = None
    product_vendor = None
    product_name = None
    product_version = None

    def __init__(self, product_vendor, product_name, product_version,
                 version_major=1, version_minor=0):
        """ Define the LEEF Headers for the application logging """

        self.version_major = version_major
        self.version_minor = version_minor
        self.product_vendor = product_vendor
        self.product_name = product_name
        self.product_version = product_version

    def logEvent(self, event_id, keys):
        """
        Log an event
        """
        return self._createEventString(event_id, keys)

    def _createEventString(self, event_id, keys):
        header = self._createHeader(event_id)

        values = sorted([(str(k) + "=" + str(v)) for k, v in iter(keys.items())])

        payload = '\t'.join(values)

        return (header + payload)

    def _createHeader(self, event_id):
        return "LEEF:{0}.{1}|{2}|{3}|{4}|{5}|". \
               format(self.version_major,
                      self.version_minor,
                      self.product_vendor,
                      self.product_name,
                      self.product_version,
                      event_id
                      )
