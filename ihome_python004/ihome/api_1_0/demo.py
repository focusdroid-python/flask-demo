# -*- coding:utf-8 -*-
from . import api
from ihome import db
import logging
from flask import current_app

@api.route("/index")
def index():
    current_app.logger.error("error manager")
    current_app.logger.warn("warn manager")
    current_app.logger.info("info manager")
    current_app.logger.debug("debug manager")
    return "index page"