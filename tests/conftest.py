import json

import pytest
import requests
from requests import Response


@pytest.fixture
def mock_resp() -> Response:
    """Мок - ответ"""
    resp = requests.Response()
    resp.status_code = 200
    resp._content = json.dumps({"items": [{"name": "Backend-разработчик"}, {"name": "Python-разработчик"}]}).encode(
        "utf-8"
    )
    return resp
