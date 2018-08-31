#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import postapi_api.lib.liblog
from postapi_api.lib.liblog import (MimeObject, Attachment, Template, Reply, MailItem)
from flask import Blueprint
logger = logging.getLogger(__name__)
app = Flask(__name__)

attachment_bluep = Blueprint(name='attachment', import_name=__name__,  url_prefix='/api/v1')

# @attachment_bluep.route('add/<message>', methods=['GET'])
# @attachment_bluep.route('add/', defaults={'message': 'sem mensagem no add'},methods=['GET'])
# @attachment_bluep.route('/', defaults={'message': 'sem mensagem'}, methods=['GET'])
@attachment_bluep.route('/attachment/', methods=['GET'])
def attachment_list(id):
    """
    generate a list of attachment urls
    """
    return 'ok'

@attachment_bluep.route('/attachment/<id>', methods=['GET', 'DELETE'])
def attachment(id):
    return 'ok'
