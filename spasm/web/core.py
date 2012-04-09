import re
import time
import urllib2
import simplejson
from xml.dom import minidom

from spasm.web.util import *

def _grab(func):
    def _d(obj, url, *args, **kwargs):
        interval = kwargs.get('interval')
        obj._wait(interval)
        print "(%s) %s" % (time.ctime(), url)
        return func(obj, url, *args, **kwargs)
    return _d

class Web():

    TIMER_DELAY = 0.01
    INTERVAL = 2.0
    TIMEOUT = 10

    def __init__(self):
        self.lastHit = 0

    def is_idle(self, interval):
        return time.time() - self.lastHit > interval

    def _wait(self, interval=None):
        interval = self.INTERVAL if interval is None else interval
        while not self.is_idle(interval):
            time.sleep(self.TIMER_DELAY)
        self.lastHit = time.time()

    @_grab
    def grabJSON(self, url, default=None, **kwargs):
        try:
            f = urllib2.urlopen(url, timeout=self.TIMEOUT)
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to grab JSON from %s" % (time.ctime(), url)
            return default
        try:
            return simplejson.load(f)
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to parse JSON from %s" % (time.ctime(), url)
            return default

    @_grab
    def grabHTML(self, url, default='', **kwargs):
        try:
            return urllib2.urlopen(url, timeout=self.TIMEOUT).read()
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to grab HTML from %s" % (time.ctime(), url)
            return default

    @_grab
    def grabXML(self, url, default=[], conf=(0,1), **kwargs):
        try:
            xml = urllib2.urlopen(url, timeout=self.TIMEOUT).read()
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to grab XML from %s" % (time.ctime(), url)
            return default
        try:
            dom = minidom.parseString(xml)
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to parse XML from %s" % (time.ctime(), url)
            return default
        data = dom.childNodes[conf[0]].childNodes[conf[1]].childNodes
        return data

    @_grab
    def grabCSV(self, url, default=None, delimiter=",", **kwargs):
        try:
            data = urllib2.urlopen(url, timeout=self.TIMEOUT).read()
        except Exception, e:
            print "ERROR: %s" % e
            print "(%s) Failed to grab CSV from %s" % (time.ctime(), url)
            return default
        try:
            import os
            lines = data.split(os.linesep)
            csv = [[f.strip() for f in line.split(delimiter)] for line in lines]
            return csv
        except:
            print "ERROR: %s" % e
            print "(%s) Failed to parse CSV from %s" % (time.ctime(), url)
            return default
            
    def grabItems(self, rss, **kwargs):
        return [dict([(n.nodeName,safe_str(n.childNodes[0].nodeValue)) \
            for n in node.childNodes \
                if n.nodeType != n.TEXT_NODE \
                and not n.nodeName.count('feedburner') \
                and not n.nodeName.count('ttl')])\
                    for node in rss if node.nodeName == 'item']



