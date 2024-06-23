class Vacancy:
    """
    Класс для создания вакансии
    """
    def __init__(self, name_vacancies: str, link: str, salary: dict, description: str):
        self.name_vacancies = name_vacancies
        self.link = link
        self.description = self.validate_description(description)
        self.salary_from = self.salary_from(salary)
        self.salary_to = self.salary_to(salary)

    @staticmethod
    def validate_description(description):
        return description if bool(description) is True else 'Описания нет'

    @staticmethod
    def salary_from(salary) -> int:
        try:
            salary_from = salary.get('from')
        except Exception:
            return 0
        else:
            return salary_from or 0

    @staticmethod
    def salary_to(salary) -> int:
        try:
            salary_to = salary.get('to')
        except Exception:
            return 0
        else:
            return salary_to or 0

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    # Функция сохранения вакансии в словарь
    def cast_to_object_list(self):
        dict_vacancy = {"name": self.name_vacancies,
                        "url": self.link,
                        "salary_from": self.salary_from,
                        "salary_to": self.salary_to,
                        "description": self.description}

        return dict_vacancy
