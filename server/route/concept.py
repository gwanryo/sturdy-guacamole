from flask import Blueprint, request
from database import Query
from database import concept_sql

from app import db

concept = Blueprint('concept', __name__)

# Concept 테이블 조회 /concept
# In :
#   keyword (str) - concept_name 검색 (Optional)
#   limit (int) - 조회 수 (Optional, default = 100)
#   page (int) - 페이지 (Optional, default = 1)
# Out: {"search": "Concept 테이블 조회 결과"}
@concept.route('/', methods = ['GET'])
def concepts():
    q = Query(db)

    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    page = request.args.get("page")

    keyword = '%'.join(keyword.split()) if keyword else ''
    limit = int(limit) if limit else 100
    offset = limit * (int(page) - 1) if page else 0

    result = {}
    for type, query in concept_sql.concept_operation.items():
        q.execute(query, {
            "keyword": f"%{keyword}%",
            "offset": offset,
            "limit": limit
        })
        fetch = q.fetch()
        result.setdefault(type, fetch)
    q.close()
    del q
    return result