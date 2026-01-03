from src.project2_job_search.hh_api import HeadHunterAPI
from src.project2_job_search.vacancy import Vacancy


def main() -> None:
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)


if __name__ == "__main__":
    main()
