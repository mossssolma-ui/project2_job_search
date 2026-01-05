# from src.project2_job_search.file_writers import JSONSaver
# from src.project2_job_search.hh_api import HeadHunterAPI
# from src.project2_job_search.vacancy import Vacancy
#
#
# def main() -> None:
#     # Создание экземпляра класса для работы с API сайтов с вакансиями
#     hh_api = HeadHunterAPI()
#
#     # Получение вакансий с hh.ru в формате JSON
#     hh_vacancies = hh_api.get_vacancies("Python")
#
#     # Преобразование набора данных из JSON в список объектов
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
#     # Пример работы контструктора класса с одной вакансией
#     vacancy1 = Vacancy(
#         "Python Developer",
#         "<https://hh.ru/vacancy/123456>",
#         {"from": 100000, "to": 150000},
#         "Требования: опыт работы от 3 лет...",
#     )
#     vacancy2 = Vacancy(
#         "Java Developer",
#         "<https://hh.ru/vacancy/234567>",
#         {"from": 1900000, "to": 240000},
#         "Требования: опыт работы от 6 лет...",
#     )
#     vacancy3 = Vacancy(
#         "javascript Developer",
#         "<https://hh.ru/vacancy/34567>",
#         {"from": 90000, "to": 140000},
#         "Требования: опыт работы от 1 года...",
#     )
#
#     # Сохранение информации о вакансиях в файл
#     json_saver = JSONSaver()
#     json_saver.add_vacancy([vacancy1, vacancy2, vacancy3])
#     # json_saver.delete_vacancy(vacancy.link)
#
#     # Функция для взаимодействия с пользователем
#     def user_interaction() -> None:
#         platforms = ["HeadHunter"]
#         search_query = input("Введите поисковый запрос: ")
#         top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#         filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#         salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
#
#     #     # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#     #     #
#     #     # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#     #     #
#     #     # sorted_vacancies = sort_vacancies(ranged_vacancies)
#     #     # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     #     # print_vacancies(top_vacancies)
#     #
#     # user_interaction()
#
#
# if __name__ == "__main__":
#     main()
