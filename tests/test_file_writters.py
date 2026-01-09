import json
from pathlib import Path

from _pytest.capture import CaptureFixture

from src.project2_job_search.file_writers import FileWriter, JSONSaver
from src.project2_job_search.vacancy import Vacancy


def test_abstract_file_writer() -> None:
    """класс FileWriter абстрактный
    и содержит абстрактные методы"""
    assert FileWriter.__abstractmethods__ == {"add_vacancy", "read_vacancy", "delete_vacancy"}


def test_jsonsaver_init(tmp_path: Path) -> None:
    """Проверка инициализации что файл существует"""
    filepath = tmp_path / "data" / "test.json"
    assert not filepath.exists()

    storage = JSONSaver(filepath=filepath)
    assert storage.__class__.__name__ == "JSONSaver"
    assert isinstance(storage, JSONSaver)
    assert filepath.exists()

    with open(filepath, "r", encoding="utf-8") as file:
        assert json.load(file) == []


def test_jsonsaver_init_file_exists(tmp_path: Path) -> None:
    """Проверка инициализации когда файл уже существует"""
    filepath = tmp_path / "data" / "test.json"
    exists_data = [{"name": "Python Dev", "link": "https://hh.ru/123456"}]
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(exists_data, file, ensure_ascii=False, indent=4)

    with open(filepath, "r", encoding="utf-8") as file:
        assert json.load(file) == exists_data


def test_jsonsaver_add_vacancy_new_vacancies(
    tmp_path: Path, vacancies_init_full: Vacancy, capsys: CaptureFixture
) -> None:
    """Проверка добавления новых вакансий"""
    filepath = tmp_path / "data" / "test.json"
    storage = JSONSaver(filepath)

    storage.add_vacancy([vacancies_init_full])

    captured = capsys.readouterr()
    assert "Добавлено 1 новых вакансий" in captured.out

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["name"] == "Python Dev"
    assert data[0]["link"] == "https://hh.ru/vacancy/123"

    storage.add_vacancy([vacancies_init_full])
    captured = capsys.readouterr()
    assert "Вакансия существует, пропускаем" in captured.out
    assert "Нет новых вакансий" in captured.out


def test_load_vacancies_except(tmp_path: Path) -> None:
    """Проверка обработки исключения"""
    filepath = tmp_path / "data" / "test.json"
    storage = JSONSaver(filepath)

    filepath.unlink()
    assert not filepath.exists()

    res = storage.read_vacancy()
    assert res == []
    assert isinstance(res, list)


def test_read_vacancy_with_filter(tmp_path: Path, test_data: list[dict]) -> None:
    """Проверка чтения вакансий с фильтром"""
    filepath = tmp_path / "data" / "test.json"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)

    storage = JSONSaver(filepath)

    result = storage.read_vacancy("python")
    assert len(result) == 2

    result = storage.read_vacancy("java")
    assert len(result) == 1
    assert result[0].name == "Java Developer"

    result = storage.read_vacancy()
    assert len(result) == 3

    result = storage.read_vacancy("javascript")
    assert len(result) == 0


def test_delete_vacancy(tmp_path: Path, test_data: list[dict], capsys: CaptureFixture) -> None:
    """Тест удаления вакансии"""
    filepath = tmp_path / "data" / "test.json"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)

    storage = JSONSaver(filepath)
    storage.delete_vacancy("https://hh.ru/vacancy/234")

    capture = capsys.readouterr()
    assert "Вакансия удалена" in capture.out

    with open(filepath, "r", encoding="utf-8") as file:
        update_data = json.load(file)

    assert len(update_data) == 2
    assert all(v["link"] != "https://hh.ru/vacancy/234" for v in update_data)


def test_delete_vacancy_no_exist(tmp_path: Path, test_data: list[dict], capsys: CaptureFixture) -> None:
    """Тест удаления не существующей вакансии"""
    filepath = tmp_path / "data" / "test.json"
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)

    storage = JSONSaver(filepath)
    storage.delete_vacancy("https://test")
    capture = capsys.readouterr()
    assert "Вакансия с указанной ссылкой не найдена" in capture.out
