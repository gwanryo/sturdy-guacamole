from flask import Blueprint, request

table = Blueprint('table', __name__)

@table.route('/', methods = ['GET'])
def tables():
    return {}
