from flask import Blueprint, request
from database import Query
from database import drug_exposure_sql

from app import db

table = Blueprint('table', __name__)

# Drug Exposure 테이블 조회 /table/drug-exposure
# In :
#   keyword (str) - concept_name 검색 (Optional)
#   limit (int) - 조회 수 (Optional, default = 100)
#   page (int) - 페이지 (Optional, default = 1)
# Out: {"search": "drug_exposure 테이블 조회 결과"}
@table.route('/drug-exposure', methods = ['GET'])
def tables():
    q = Query(db)

    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    page = request.args.get("page")

    keyword = '%'.join(keyword.split()) if keyword else ''
    limit = int(limit) if limit else 100
    offset = limit * (int(page) - 1) if page else 0

    result = {}
    for type, query in drug_exposure_sql.table_operation.items():
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
