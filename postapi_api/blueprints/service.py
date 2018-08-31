#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import postapi_api.lib.liblog
from flask import Blueprint
logger = logging.getLogger(__name__)
app = Flask(__name__)

service_bluep = Blueprint(name='service', import_name=__name__,  url_prefix='/api/v1')

@service_bluep.route('/queue/drop/<queue>/age/<minutes>', methods=['PUT'])
def get_queue_item(queue, minutes):
    """
    expire items older then
    """
    return 'ok'

@service_bluep.route('/queue/expire/<queue>', methods=['PUT'])
@service_bluep.route('/queue/expire/<queue>/age/<minutes>', methods=['PUT'])
def get_queue_item(queue, minutes=5):
    """
    expire items older then
    """
    return 'ok'

@service_bluep.route('/queue/<queue>/<uuid>', methods=['GET'])
def get_queue_item(queue, uuid):
    """
    retrieve or delete a message from read queue based on uuid
    """
    return 'ok'


@service_bluep.route('/queue/<queue>', methods=['GET'])
def get_queue(queue):
    """
    retrieve a list of active items out of the queue
    """
    return 'ok'
