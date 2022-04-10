from flask import Blueprint
from database import Query
from database import patient_sql, person_sql

from app import db

stats = Blueprint('stats', __name__)

@stats.route('/patient', methods = ['GET'])
def patient():
    q = Query(db)
    result = {}
    for type, query in patient_sql.stats_operation.items():
        q.execute(query)
        fetch = q.fetch()
        result.setdefault(type, fetch)
    q.close()
    del q
    return result

@stats.route('/visit', methods = ['GET'])
def visit():
    q = Query(db)
    result = {}
    for type, query in person_sql.stats_operation.items():
        q.execute(query)
        fetch = q.fetch()
        result.setdefault(type, fetch)
    q.close()
    del q
    return result
