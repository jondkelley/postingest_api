#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Queue(object):
    """
    class to manage queues
    """
    self.queue = None
    self.from =  str()
    self.subject =  str()
    self.body = str()
    self.headers = []
    self.attachments = []
    def __init__(self):
        self.uuid = []


class RedisConnection(object):
    """
    handle a connection
    """
    def __init__(host, port):
        pass
    def create_queue(self, qname):
        """
        creates a new queue if missing
        """
        pass
    def expire_attachment(self, attachmentid):
        """
        issues a delete command for X minutes on a retrieved attachment
        """
        pass
