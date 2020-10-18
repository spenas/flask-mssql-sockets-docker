from flask import Blueprint

socket_client = Blueprint('socket_client', __name__)

from . import events