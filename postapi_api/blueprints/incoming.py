#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import postapi_api.lib.liblog
from flask import Blueprint
logger = logging.getLogger(__name__)
app = Flask(__name__)

incoming_bluep = Blueprint(name='incoming', import_name=__name__,  url_prefix='/api/v1')

@incoming_bluep.route('/incoming/message', methods=['POST'])
def incoming_pipe():
    """
    process inbound messages from the postfix pipe
    dump to redis
    """
    return 'ok'
