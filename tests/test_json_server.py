from src.json_saver import JSONSaver
import pytest

@pytest.fixture()
def json_server():
    return JSONSaver()



def test_sort_vacancy(json_server):
    assert json_server.sort_vacancy("0 - 1000000", 'python') == [
        {'name': 'Разработчик AI-решений (python + no-code платформы)', 'url': 'https://hh.ru/vacancy/99862545',
         'salary_from': 120000, 'salary_to': 200000,
         'description': 'Кроме того, мы разрабатываем высокоэффективных AI-агентов, которые берут на себя ряд рутинных задач, таких как обработка данных, составление отчетов...'},
        {'name': 'Младший python-разработчик', 'url': 'https://hh.ru/vacancy/99725937', 'salary_from': 85000,
         'salary_to': 100000,
         'description': 'Разработка внутренних серверных приложений на <highlighttext>Python</highlighttext> для автоматизации бизнес-процессов. Организация взаимообмена данными между собственными и сторонними сервисами через API. '},
        {'name': 'Junior python-программист в техподдержку (FastAPI)', 'url': 'https://hh.ru/vacancy/102012417',
         'salary_from': 0, 'salary_to': 0,
         'description': 'Доработка интеграций по документации партнера. Улучшение действующих микросервисов. Поддержка действующего функционала. Работа с агрегированными запросами SQL/NoSQL. Работа с настройками...'}]

def test_reed_vacancy(json_server):
    assert json_server.reed_vacancy([
        {'name': 'Разработчик AI-решений (python + no-code платформы)', 'url': 'https://hh.ru/vacancy/99862545',
         'salary_from': 120000, 'salary_to': 200000,
         'description': 'Кроме того, мы разрабатываем высокоэффективных AI-агентов, которые берут на себя ряд рутинных задач, таких как обработка данных, составление отчетов...'},
        {'name': 'Младший python-разработчик', 'url': 'https://hh.ru/vacancy/99725937', 'salary_from': 85000,
         'salary_to': 100000,
         'description': 'Разработка внутренних серверных приложений на <highlighttext>Python</highlighttext> для автоматизации бизнес-процессов. Организация взаимообмена данными между собственными и сторонними сервисами через API. '},
        {'name': 'Junior python-программист в техподдержку (FastAPI)', 'url': 'https://hh.ru/vacancy/102012417',
         'salary_from': 0, 'salary_to': 0,
         'description': 'Доработка интеграций по документации партнера. Улучшение действующих микросервисов. Поддержка действующего функционала. Работа с агрегированными запросами SQL/NoSQL. Работа с настройками...'}]
, 0) == ('Разработчик AI-решений (python + no-code платформы)\n'
                'https://hh.ru/vacancy/99862545\n'
                '120000\n'
                '200000\n'
                'Кроме того, мы разрабатываем высокоэффективных AI-агентов, которые берут на себя ряд рутинных задач, таких как обработка данных, составление отчетов...')

