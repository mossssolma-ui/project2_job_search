import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.project2_job_search.vacancy import Vacancy


class FileWriter(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: list[Vacancy]) -> None:
        """Добавление вакансии в файл"""
        ...

    @abstractmethod
    def read_vacancy(self, text: str = "") -> list[Vacancy]:
        """Получение данных из файла по указанным критериям"""
        ...

    @abstractmethod
    def delete_vacancy(self, link: str) -> None:
        """Удаление вакансии по ссылке"""
        ...


class JSONSaver(FileWriter):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, filepath: str | Path = "data/vacancy.json") -> None:
        """Инициализация пути к json-файлу, по умолчанию: "data/vacancy.json"""
        self.__filepath = Path(filepath)
        self.__filepath.parent.mkdir(parents=True, exist_ok=True)
        if not self.__filepath.exists():
            with open(self.__filepath, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def __load_vacancies(self) -> list[dict]:
        """Загружаем все вакансии из файла"""
        try:
            with open(self.__filepath, "r", encoding="utf-8") as file:
                return json.load(file)  # type: ignore
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __save_vacancy_in_file(self, vacancy: list[dict]) -> None:
        """Сохранение вакансий в json-файл"""
        with open(self.__filepath, "w", encoding="utf-8") as file:
            json.dump(vacancy, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: list[Vacancy]) -> None:
        """Добавление вакансии в json-файл"""
        exist_vacancies = self.__load_vacancies()
        add_count = 0
        exist_links = {v.get("link") for v in exist_vacancies}
        res = []
        for vac in vacancy:
            vac_dict = vac.to_dict()
            if vac_dict["link"] not in exist_links:
                res.append(vac_dict)
                exist_links.add(vac_dict["link"])
                add_count += 1
            else:
                print("Вакансия существует, пропускаем")
                continue

        if res:
            upd_vac = exist_vacancies + res
            self.__save_vacancy_in_file(upd_vac)
            print(f"Добавлено {add_count} новых вакансий")
        else:
            print("Нет новых вакансий")

    def read_vacancy(self, text: str = "") -> list[Vacancy]:
        """Чтение вакансий"""
        data = self.__load_vacancies()
        vacancies = []
        for vac in data:
            vacancies.append(Vacancy(**vac))

        if text:
            text = text.lower()
            vacancies = [vac for vac in vacancies if text in vac.name.lower() or text in vac.description.lower()]
        return vacancies

    def delete_vacancy(self, link: str) -> None:
        """Удаление вакансии по ссылке"""
        data = self.__load_vacancies()
        count_vac_data = len(data)
        data = [v for v in data if v.get("link") != link]
        if len(data) < count_vac_data:
            self.__save_vacancy_in_file(data)
            print("Вакансия удалена")
        else:
            print("Вакансия с указанной ссылкой не найдена")
