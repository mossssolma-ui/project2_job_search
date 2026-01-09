from unittest.mock import MagicMock, patch

from requests import Response

from src.project2_job_search.hh_api import AbstractApi, HeadHunterAPI


def test_abstract_api_is_abs() -> None:
    """
    Тест, что AbstractApi - абстрактный класс
    и содержит абстрактные методы
    """
    assert AbstractApi.__abstractmethods__ == {"_connect", "get_vacancies"}


def test_hh_api_is_abstract_api() -> None:
    """Тест, что HhApi наследуется от AbstractApi"""
    assert issubclass(HeadHunterAPI, AbstractApi)


@patch("src.project2_job_search.hh_api.requests.get")
def test_connect_and_vacancies_ok(mock_get: MagicMock, mock_resp: Response) -> None:
    """Тест, успешное подключение к api и получение вакансий"""

    mock_get.return_value = mock_resp

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("python")

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Backend-разработчик"
    assert vacancies[1]["name"] == "Python-разработчик"
