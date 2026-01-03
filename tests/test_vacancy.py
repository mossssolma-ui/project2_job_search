from src.project2_job_search.vacancy import Vacancy


def test_vacancy_init(vacancies_init_full: Vacancy) -> None:
    """Инициализация при полных данных"""
    assert vacancies_init_full.name == "Python Dev"
    assert vacancies_init_full.link == "https://hh.ru/vacancy/123"
    assert vacancies_init_full.description == "Разработка на Python"
    assert vacancies_init_full.salary_from == 100000
    assert vacancies_init_full.salary_to == 150000


def test_vacancy_salary_from(vacancies_salary_from: Vacancy) -> None:
    """Инициализация при зарплате from"""
    assert vacancies_salary_from.salary_from == 100000
    assert vacancies_salary_from.salary_to == 0


def test_vacancy_salary_to(vacancies_salary_to: Vacancy) -> None:
    """Инициализация при зарплате to"""
    assert vacancies_salary_to.salary_from == 0
    assert vacancies_salary_to.salary_to == 150000


def test_vacancy_salary_none(vacancies_salary_none: Vacancy) -> None:
    """Зарплата None"""
    assert vacancies_salary_none.salary_from == 0
    assert vacancies_salary_none.salary_to == 0


def test_vacancy_lt() -> None:
    """Сравнение вакансий по зарплате"""
    vac1 = Vacancy("Dev1", "link1", {"from": 50000}, "desc1")
    vac2 = Vacancy("Dev2", "link2", {"from": 70000}, "desc2")
    vac3 = Vacancy("Dev3", "link3", None, "desc3")

    assert vac1 < vac2
    assert vac3 < vac1


def test_vacancy_str(vacancies_init_full: Vacancy) -> None:
    """Вывод __str__ с полной зарплатой"""
    out = str(vacancies_init_full)
    assert "Название: Python Dev" in out
    assert "Ссылка: https://hh.ru/vacancy/123" in out
    assert "Описание: Разработка на Python" in out
    assert "Зарплата: от 100000 до 150000" in out


def test_vacancy_str_none(vacancies_salary_none: Vacancy) -> None:
    """Вывод __str__ без зарплаты"""
    out = str(vacancies_salary_none)
    assert "Зарплата не указана" in out


def test_vacancy_repr(vacancies_init_full: Vacancy) -> None:
    """Вывод __repr__ с полной зарплатой"""
    out = repr(vacancies_init_full)
    assert "name=Python Dev" in out
    assert "link=https://hh.ru/vacancy/123" in out
    assert "salary_from=100000" in out
    assert "salary_to=150000" in out


def test_cast_to_object_list(vacancies_list_dict: list[dict]) -> None:
    """Преобразования списка словарей в объекты Vacancy"""
    vac = Vacancy.cast_to_object_list(vacancies_list_dict)
    assert len(vac) == 2
    assert vac[0].name == "Python Dev"
    assert "Опыт с Django" in vac[0].description
    assert vac[1].name == "Python Jun"
    assert "Разработка на Python" in vac[1].description
