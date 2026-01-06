from _pytest.capture import CaptureFixture

from src.project2_job_search.utils import (
    filter_vacancies_by_keyword,
    filter_vacancies_by_salary_range,
    get_top_vacancies,
)
from src.project2_job_search.vacancy import Vacancy


def test_get_top_vacancies_default(sample_vacancies: list[Vacancy]) -> None:
    """Возврат топ-5 вакансий по умолчанию."""
    result = get_top_vacancies(sample_vacancies)
    assert len(result) == 5
    assert result[0].salary_from == 120000
    assert result[1].salary_from == 100000
    assert result[2].salary_from == 30000
    assert result[3].salary_from == 0
    assert result[4].salary_from == 0


def test_filter_vacancies_by_keyword_keywords_null(sample_vacancies: list[Vacancy]) -> None:
    """Список ключевых слов пустой"""
    result = filter_vacancies_by_keyword(sample_vacancies, [])
    assert len(result) != 0
    names = {v.name for v in result}
    assert names == {"Data Scientist", "Python Developer", "Intern", "Java Developer", "Frontend Dev"}


def test_filter_vacancies_by_keyword_keywords(sample_vacancies: list[Vacancy]) -> None:
    """Несколько ключевых слов"""
    result = filter_vacancies_by_keyword(sample_vacancies, ["java", "react"])
    assert len(result) == 2
    names = {v.name for v in result}
    assert names == {"Java Developer", "Frontend Dev"}


def test_filter_vacancies_by_salary_range_empty_input(sample_vacancies: list[Vacancy]) -> None:
    """Пустая строка диапазона, возвращаются все."""
    result = filter_vacancies_by_salary_range(sample_vacancies, "")
    assert len(result) == len(sample_vacancies)


def test_filter_vacancies_by_salary_range_invalid_format(
    sample_vacancies: list[Vacancy], capsys: CaptureFixture
) -> None:
    """Некорректный формат диапазона, возвращаются все + сообщение."""
    result2 = filter_vacancies_by_salary_range(sample_vacancies, "abc")
    assert result2 == sample_vacancies
    captured = capsys.readouterr()
    assert "Ошибка ввода интервала зарплат" in captured.out


def test_filter_vacancies_by_salary_range_valid(sample_vacancies: list[Vacancy]) -> None:
    """Фильтр по зарплате '90000 - 130000'"""
    result = filter_vacancies_by_salary_range(sample_vacancies, "90000 - 130000")
    names = {v.name for v in result}
    assert names == {"Java Developer", "Python Developer", "Data Scientist"}
