import json

import pytest
import requests
from requests import Response

from src.project2_job_search.vacancy import Vacancy


@pytest.fixture
def mock_resp() -> Response:
    """Мок - ответ"""
    resp = requests.Response()
    resp.status_code = 200
    resp._content = json.dumps({"items": [{"name": "Backend-разработчик"}, {"name": "Python-разработчик"}]}).encode(
        "utf-8"
    )
    return resp


@pytest.fixture
def vacancies_init_full() -> Vacancy:
    """Тестовая вакансия фулл запись"""
    return Vacancy(
        name="Python Dev",
        link="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000},
        description="Разработка на Python",
    )


@pytest.fixture
def vacancies_salary_from() -> Vacancy:
    """Зарплата только from"""
    return Vacancy(
        name="Python Dev",
        link="https://hh.ru/vacancy/123",
        salary={"from": 100000},
        description="Разработка на Python",
    )


@pytest.fixture
def vacancies_salary_to() -> Vacancy:
    """Зарплата только to"""
    return Vacancy(
        name="Python Dev", link="https://hh.ru/vacancy/123", salary={"to": 150000}, description="Разработка на Python"
    )


@pytest.fixture
def vacancies_salary_none() -> Vacancy:
    """Зарплата None"""
    return Vacancy(
        name="Python Dev", link="https://hh.ru/vacancy/123", salary=None, description="Разработка на Python"
    )


@pytest.fixture
def vacancies_list_dict() -> list[dict]:
    """Список словарей с вакансиями"""
    data = [
        {
            "name": "Python Dev",
            "alternate_url": "https://hh.ru/vacancy/123",
            "salary": {"from": 100000, "to": 150000},
            "snippet": {"requirement": "Опыт с Django", "responsibility": "Писать код"},
        },
        {
            "name": "Python Jun",
            "alternate_url": "https://hh.ru/vacancy/321",
            "salary": {"from": 10000, "to": 15000},
            "snippet": {"requirement": "Разработка на Python", "responsibility": "Писать код"},
        },
    ]
    return data
