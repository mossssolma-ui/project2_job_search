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


@pytest.fixture
def test_data() -> list[dict]:
    """Тестовые вакансии"""
    return [
        {
            "name": "Python Developer",
            "link": "https://hh.ru/vacancy/123",
            "description": "We need Python developer",
            "salary": {"from": 100000, "to": 150000},
        },
        {
            "name": "Java Developer",
            "link": "https://hh.ru/vacancy/234",
            "description": "Java position",
            "salary": {"from": 90000, "to": 140000},
        },
        {
            "name": "Python Data Scientist",
            "link": "https://hh.ru/vacancy/345",
            "description": "Python for data science",
            "salary": {"from": 120000, "to": 180000},
        },
    ]


@pytest.fixture
def sample_vacancies() -> list[Vacancy]:
    """Фикстура с набором вакансий для тестов."""
    return [
        Vacancy("Python Developer", "https://hh.ru/vacancy/1", {"from": 100000, "to": 150000}, "Опыт Python"),
        Vacancy("Java Developer", "https://hh.ru/vacancy/2", {"from": 120000}, "Опыт Java"),
        Vacancy("Data Scientist", "https://hh.ru/vacancy/3", {"to": 200000}, "ML, Python"),
        Vacancy("Frontend Dev", "https://hh.ru/vacancy/4", None, "React, TypeScript"),
        Vacancy("Intern", "https://hh.ru/vacancy/5", {"from": 30000, "to": 50000}, "Стажировка, Python"),
    ]
