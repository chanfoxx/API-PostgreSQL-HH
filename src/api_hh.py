from error_response import ErrorResponse
from abc import ABC, abstractmethod
from vacancy import Vacancy
from typing import Any
import requests
import json


class PageAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_data_from_api(self, data_id):
        pass

    @abstractmethod
    def data_organize(self, filename):
        pass


class HeadHunterAPI(PageAPI):
    """
    Класс, наследующийся от абстрактного класса,
    для работы с платформой HeadHunter.
    """
    employers_id = [9286153, 1723062, 10213158, 1358439, 3746122,
                    460838, 4919467, 51167, 41862, 737268]

    def get_data_from_api(self, employer_id: int) -> Any:
        """
        Производит поиск вакансий по employer_id из списка,
        и получает json данные о вакансиях и компаниях.

        Параметры запроса:
        'only_with_salary' - вывод вакансий с указанием зарплаты (True).
        """
        url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        params = {"only_with_salary": True}

        # Отправляем запрос с установленными параметрами.
        response = requests.get(url, params=params)

        # Если запрос выполнен успешно, возвращает json данные,
        # в противном случае выбрасывает ошибку.
        if response.status_code == 200:
            data_vacancy = response.json()
            return data_vacancy
        else:
            raise ErrorResponse("Ошибка при выполнении запроса: ",
                                response.status_code)

    def data_organize(self, filename: json) -> None:
        """
        Организация данных по вакансиям.
        Возвращает сформированный список словарей.
        """
        data_list = []
        # Проводим цикл по списку employers_id,
        # складывая данные в переменную data_vacancies.
        for employer_id in HeadHunterAPI.employers_id:
            data_vacancies = self.get_data_from_api(employer_id)
            # Выбираем нужные данные из json данных по ключу 'items'.
            if data_vacancies is not None:
                for data in data_vacancies['items']:
                    vacancy_title = data['name']
                    vacancy_link = data['alternate_url']
                    requirement = data['snippet'].get('requirement', None)
                    salary_from = data['salary'].get('from', None)
                    salary_to = data['salary'].get('to', None)
                    employer_name = data['employer']['name']
                    employer_link = data['employer']['alternate_url']
                    vacancy_area = data['area'].get('name', 'Санкт-Петербург')

                    # Устанавливаем значение зарплаты.
                    # Если есть обе границы - устанавливаем минимальное значение.
                    # В ином случае, устанавливаем то значение, которое существует.
                    if salary_from and salary_to:
                        salary = min(salary_from, salary_to)
                    else:
                        salary = salary_from or salary_to

                    # Устанавливаем значение требований.
                    # Если значение есть - приводим его к нижнему регистру.
                    # В ином случае, устанавливаем значение, что данных нет.
                    if requirement:
                        requirement = requirement.lower()
                    else:
                        requirement = 'Нет данных.'

                    # Создаем экземпляры класса Vacancy из отфильтрованных данных.
                    vacancy = Vacancy(vacancy_title, vacancy_link, requirement,
                                      salary, employer_name, employer_link,
                                      vacancy_area)
                    # Переводим данные в словарь и складываем их список data_list.
                    data_list.append(vacancy.to_data())

        # Сохраняем список в json файл.
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_list, file, indent=2, ensure_ascii=False)
