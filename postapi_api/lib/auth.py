#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Permissions(object):
    """
    permission matrix
    """
    attachment_get = False
    attachment_post = False
    pipe_post = False
    service_post = False
    service_get = False
    queue_manage = False

class ValidRoles(object):
    """
    retrieve and validate a user role, set permissions for role
    """
    pass

class ValidUsers(object):
    """
    validate user tokens
    """
    pass
