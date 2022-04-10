from flask import Blueprint
from database import Query
from database import visit_occurence_sql, person_sql

from app import db

stats = Blueprint('stats', __name__)

# 환자 통계 /stats/patient
# In : None
# Out: {"통계 종류": "통계 값"}
@stats.route('/patient', methods = ['GET'])
def patient():
    q = Query(db)
    result = {}
    for type, query in visit_occurence_sql.stats_operation.items():
        q.execute(query)
        fetch = q.fetch()
        result.setdefault(type, fetch)
    q.close()
    del q
    return result

# 방문 통계 /stats/visit
# In : None
# Out: {"통계 종류": "통계 값"}
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
