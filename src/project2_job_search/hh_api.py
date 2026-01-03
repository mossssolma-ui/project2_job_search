from abc import ABC, abstractmethod

import requests
from requests import Response


class AbstractApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _connect(self, text: str) -> Response:
        """Абстрактный метод для подключения к API"""
        ...

    @abstractmethod
    def get_vacancies(self, text: str) -> list[dict]:
        """Абстрактный метод для получения вакансий"""
        ...


class HeadHunterAPI(AbstractApi):
    """Класс для работы c hh.ru"""

    def __init__(self, page: int = 0):
        """Инициалиализация подключения"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"page": page, "per_page": 30}

    def _connect(self, text: str) -> Response:
        """Метод для подключения к hh.ru"""
        self.__params["text"] = text  # type: ignore
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        response.raise_for_status()
        return response

    def get_vacancies(self, text: str) -> list[dict]:
        """Метод получения вакансий"""
        return self._connect(text).json().get("items", [])  # type: ignore
