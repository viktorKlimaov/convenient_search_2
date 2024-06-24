import json
from typing import Any
from abc import ABC, abstractmethod
from src.hh_api import Vacancy
import os


class AbstractJson(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def sort_vacancy(self, *args):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractJson):
    """
     Класс для сохранения вакансий в JSON-файл и получения вакансий из JSON-файл
    """

    def __init__(self):
        self.path = os.path.join('..', 'data', 'vacancies.json')

    # Функция для сохранения, вакансий в JSON-файл
    def add_vacancy(self, vacancies: list[Vacancy]):
        with open(self.path, 'r', encoding='utf-8') as file:
            try:
                data: list[dict[str, Any]] = json.load(file)
            except json.JSONDecodeError:
                data = []

                # добавление вакансии в список
                for vacancy in vacancies:
                    data.append(vacancy.cast_to_object_list())

        # добавление список вакансий в JSON-файл
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=3, ensure_ascii=False)

    # Функция для получения вакансий по критериям пользователя
    def sort_vacancy(self, salary_range, filter_words: str) -> list:
        with open(self.path, 'r', encoding='utf-8') as file:
            vacancy_list = json.load(file)

        # сортировка по зарплате
        sort_vacancies = sorted(vacancy_list, key=lambda x: x['salary_from'], reverse=True)

        # Фильтрация по критериям пользователя
        top_vacancies = []
        for vacancy in sort_vacancies:

            list_salary_range = salary_range
            if filter_words not in vacancy['name'] and filter_words is not None:
                continue
            else:
                if vacancy['salary_from'] < int(list_salary_range[0]):
                    continue
                if vacancy['salary_to'] > int(list_salary_range[-1]):
                    continue
            top_vacancies.append(vacancy)
        return top_vacancies

    @staticmethod
    # Получение вакансии для пользователя
    def reed_vacancy(sort_vacancy: list, element: int):
        name = sort_vacancy[element]['name']
        url = sort_vacancy[element]['url']
        salary_from = sort_vacancy[element]['salary_from']
        salary_to = sort_vacancy[element]['salary_to']
        description = sort_vacancy[element]['description']

        return f'{name}\n{url}\n{salary_from}\n{salary_to}\n{description}'

    # Функция для удаления вакансии
    def del_vacancy(self, vacancy):
        with open(self.path, 'r', encoding='utf-8') as file:
            vacancy_list = json.load(file)
        return vacancy_list.rmote(vacancy)