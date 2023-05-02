from flask import Blueprint, Response, request, jsonify
from typing import Tuple, Union
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    # запрос пользователя
    data = request.json

    # проверить запрос
    try:
        RequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    first_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        data=None,
        file_name=data['file_name'],
    )

    result = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        data=first_result,
        file_name=data['file_name'],
    )

    return jsonify(result)
