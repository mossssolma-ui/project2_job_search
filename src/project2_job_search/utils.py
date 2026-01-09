from src.project2_job_search.vacancy import Vacancy


def get_top_vacancies(vacancies: list[Vacancy], n: int = 5) -> list[Vacancy]:
    """Возвращает топ N вакансий по зарплате (salary_from), по умолчанию 5 шт"""
    sorted_vacancies = sorted(vacancies, key=lambda v: v.salary_from, reverse=True)
    return sorted_vacancies[:n]


def filter_vacancies_by_keyword(vacancies: list[Vacancy], keyword: list[str]) -> list[Vacancy]:
    """Возвращает вакансии по ключевому слову (словам) в описании"""
    if not keyword:
        return vacancies

    filtered_vacancy = []
    keywords_lower = [kw.lower().strip() for kw in keyword]
    for vac in vacancies:
        name_lower = vac.name.lower()
        desc_lower = vac.description.lower()
        if any(kw in name_lower or kw in desc_lower for kw in keywords_lower):
            filtered_vacancy.append(vac)
    return filtered_vacancy


def filter_vacancies_by_salary_range(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """
    Фильтрует вакансии по интервалу зарплат.
    Вводить в таком формате: '100000 - 150000'
    """
    if not salary_range.strip():
        return vacancies

    try:
        salaries = salary_range.split("-")
        if len(salaries) != 2:
            raise ValueError("Неверный интервал зарплат")

        min_sal = int(salaries[0].strip())
        max_sal = int(salaries[1].strip())
    except (ValueError, IndexError):
        print("Ошибка ввода интервала зарплат. Введите в таком формате: 100000 - 150000")
        return vacancies

    filtered = []
    for vac in vacancies:
        sal_from = vac.salary_from or 0
        sal_to = vac.salary_to or sal_from

        if sal_to >= min_sal and sal_from <= max_sal:
            filtered.append(vac)

    return filtered
