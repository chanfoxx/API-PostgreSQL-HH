from typing import Any


class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, vacancy_title: str, vacancy_link: str,
                 requirement: str, salary: int, employer_name: str,
                 employer_link: str, vacancy_area: str) -> None:
        """
        Создание экземпляра класса Vacancy.

        :param vacancy_title: Название вакансии.
        :param vacancy_link: Ссылка на вакансию.
        :param requirement: Описание требований.
        :param salary: Значение зарплаты.
        :param employer_name: Название компании.
        :param employer_link: Ссылка на компанию.
        :param vacancy_area: Местоположение.
        """
        if isinstance(vacancy_title, str):
            self._vacancy_title = vacancy_title
        else:
            raise ValueError("Название вакансии должно быть строкой.")

        if isinstance(vacancy_link, str):
            self._vacancy_link = vacancy_link
        else:
            raise ValueError("Ссылка на вакансию должна быть строкой.")

        if isinstance(requirement, str):
            self._requirement = requirement
        else:
            raise ValueError("Требования должны быть строкой.")

        if isinstance(salary, int) and salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Зарплата должна быть числом.")

        if isinstance(employer_name, str):
            self._employer_name = employer_name
        else:
            raise ValueError("Название компании должно быть строкой.")

        if isinstance(employer_link, str):
            self._employer_link = employer_link
        else:
            raise ValueError("Ссылка на компанию должна быть строкой.")

        if isinstance(vacancy_area, str):
            self._vacancy_area = vacancy_area
        else:
            raise ValueError("Местоположение должно быть строкой.")

    def __repr__(self) -> str:
        """Возвращает информацию об объекте класса в режиме отладки."""
        return (f"{self.__class__.__name__}"
                f"({self._vacancy_title}, {self._vacancy_link}, {self._requirement}, "
                f"{self._salary}, {self._employer_name}, {self._employer_link}, "
                f"{self._vacancy_area})")

    def __str__(self) -> str:
        """Возвращает информацию об объекте класса для пользователя."""
        return f"{self._vacancy_title}: {self._salary} руб. ({self._vacancy_link})"

    def to_data(self) -> dict[str, Any]:
        """Складывает данные о вакансии в словарь и возвращает его."""
        data_vacancy = {
            'vacancy_title': self._vacancy_title,
            'vacancy_link': self._vacancy_link,
            'salary': self._salary,
            'requirement': self._requirement,
            'employer_name': self._employer_name,
            'employer_link': self._employer_link,
            'vacancy_area': self._vacancy_area
        }

        return data_vacancy

    @property
    def vacancy_title(self) -> str:
        """Возвращает название вакансии."""
        return self._vacancy_title

    @property
    def vacancy_link(self) -> str:
        """Возвращает ссылку на вакансию."""
        return self._vacancy_link

    @property
    def requirement(self) -> str:
        """Возвращает описание требований."""
        return self._requirement

    @property
    def salary(self) -> int:
        """Возвращает значение зарплаты."""
        return self._salary

    @property
    def employer_name(self) -> str:
        """Возвращает название компании."""
        return self._employer_name

    @property
    def employer_link(self) -> str:
        """Возвращает ссылку на компанию."""
        return self._employer_link

    @property
    def vacancy_area(self) -> str:
        """Возвращает город вакансии/компании."""
        return self._vacancy_area
