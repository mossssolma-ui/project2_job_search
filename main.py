from project2_job_search.file_writers import JSONSaver  # type: ignore
from project2_job_search.hh_api import HeadHunterAPI  # type: ignore
from project2_job_search.utils import (  # type: ignore
    filter_vacancies_by_keyword,
    filter_vacancies_by_salary_range,
    get_top_vacancies,
)
from project2_job_search.vacancy import Vacancy  # type: ignore


def user_interaction() -> None:
    """Основная функция взаимодействия с пользователем через консоль."""
    print("Добро пожаловать в систему поиска вакансий!\n")

    # 1. Запрос у пользователя
    search_query = input("Введите поисковый запрос (например, 'Python разработчик'): ").strip()
    if not search_query:
        print("Поисковый запрос не может быть пустым.")
        return

    # 2. Получение вакансий с hh.ru в формате JSON
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    if not hh_vacancies:
        print("По вашему запросу ничего не найдено.")
        return

    # 3. Преобразование набора данных из JSON в список объектов
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    # 4. Сохранение в файл
    saver = JSONSaver()
    saver.add_vacancy(vacancies)

    # 5. Дополнительные параметры от пользователя
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        if top_n <= 0:
            top_n = 5
    except ValueError:
        top_n = 5

    keywords_input = input("Введите ключевые слова для фильтрации (через пробел): ").strip()
    keywords = keywords_input.split() if keywords_input else []

    salary_range = input("Введите диапазон зарплат (например: 100000 - 150000): ").strip()

    # 6. Применение фильтров
    filtered_by_keyword = filter_vacancies_by_keyword(vacancies, keywords)
    filtered_by_salary = filter_vacancies_by_salary_range(filtered_by_keyword, salary_range)
    top_vacancies = get_top_vacancies(filtered_by_salary, top_n)

    # 7. Вывод результатов
    if not top_vacancies:
        print("Нет вакансий, по вашим критериям.")
        return

    print(f"\nТоп {len(top_vacancies)} вакансий по вашему запросу:\n")
    for i, vac in enumerate(top_vacancies, 1):
        print(f"Вакансия {i}")
        print(vac)
        print()

    # 8. Удаление вакансии
    delete_choice = input("Хотите удалить одну из вакансий в файле? (да/нет): ").strip().lower()
    if delete_choice in ("да", "lf"):
        try:
            index = int(input(f"Введите номер вакансии (1–{len(top_vacancies)}): ")) - 1
            if 0 <= index < len(top_vacancies):
                link_to_delete = top_vacancies[index].link
                saver.delete_vacancy(link_to_delete)
            else:
                print("Неверный номер вакансии.")
        except ValueError:
            print("Некорректный ввод номера.")

    print("Работа программы завершена.")


if __name__ == "__main__":
    user_interaction()
