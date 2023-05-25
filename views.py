from flask import Blueprint, Response, request, jsonify
from typing import Tuple, Dict
from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response | Tuple[Response, int]:
    data: dict = request.json  # type: ignore

    try:
        BatchRequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    result = None
    for query in data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
            file_name=data['file_name'],
        )

    return jsonify(result)
