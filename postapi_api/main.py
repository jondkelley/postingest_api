#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from blueprints.attachment import attachment_bluep
from blueprints.incoming import incoming_bluep
from blueprints.service import service_bluep
import logging
import postapi_api.lib.liblog

logger = logging.getLogger(__name__)
app = Flask(__name__)

app.register_blueprint(attachment_bluep)
app.register_blueprint(ingest_bluep)

logger.debug("test")

if __name__ == '__main__':
    app.run(debug=True)
