class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ["name", "link", "description", "salary_from", "salary_to"]

    def __init__(self, name: str, link: str, salary: dict | None, description: str) -> None:
        """Инициализация атрибутов вакансии"""
        self.name = name
        self.link = link
        self.description = description
        self.__validate(salary)

    def __validate(self, salary: dict | None) -> None:
        if not salary or not isinstance(salary, dict):
            self.salary_from = 0
            self.salary_to = 0
            return

        from_val = salary.get("from")
        to_val = salary.get("to")

        self.salary_from = from_val if from_val is not None else 0
        self.salary_to = to_val if to_val is not None else 0

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение через '<'"""
        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """Вывод для пользователя"""
        if self.salary_from == 0 and self.salary_to == 0:
            salary_info = "Зарплата не указана"
        else:
            parts = []
            if self.salary_from:
                parts.append(f"от {self.salary_from}")
            if self.salary_to:
                parts.append(f"до {self.salary_to}")
            salary_info = " ".join(parts) if parts else "Зарплата не указана"

        return (
            f"Название: {self.name}\n"
            f"Ссылка: {self.link}\n"
            f"Описание: {self.description}\n"
            f"Зарплата: {salary_info}\n"
        )

    def __repr__(self) -> str:
        """Вывод для отладки"""
        return f"name={self.name}, link={self.link}, salary_from={self.salary_from}, salary_to={self.salary_to}"

    def to_dict(self) -> dict:
        """Преобразует объект Vacancy в словарь для сохранения в JSON"""
        salary_dict = None
        if self.salary_from or self.salary_to:
            salary_dict = {}
            if self.salary_from:
                salary_dict["from"] = self.salary_from
            if self.salary_to:
                salary_dict["to"] = self.salary_to

        return {
            "name": self.name,
            "link": self.link,
            "description": self.description,
            "salary": salary_dict,
        }

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list[Vacancy]:
        """Преобразует данные из JSON в список объектов Vacancy"""
        res = []
        for vac in vacancies:
            snippet = vac.get("snippet", {})
            req = snippet.get("requirement") or ""
            resp = snippet.get("responsibility") or ""
            description = (req + " " + resp).strip() or "Описание отсутствует"
            res.append(
                cls(name=vac["name"], link=vac["alternate_url"], salary=vac.get("salary"), description=description)
            )
        return res
