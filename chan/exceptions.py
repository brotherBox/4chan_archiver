#!/usr/bin/env python

class URLParsingFailed(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class Received404NotFound(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class WTFKindOfJsonAreYougetting(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return repr()
