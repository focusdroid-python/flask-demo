# -*- coding:utf-8 -*-

from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request, Response
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.modules import User
from ihome import db, constants


@api.route("/areas")
def get_area_info():
    """获取城区"""
    # xunsh