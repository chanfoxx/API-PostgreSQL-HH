import psycopg2
from typing import Any


class DBManager:
    """Класс подключается к БД PostgreSQL и работает с запросами."""
    def __init__(self, database_name: str, params: dict, table_name: str) -> None:
        """
        Создание экземпляра класса DBManager.

        :param database_name: Название базы данных.
        :param params: Параметры подключения к Postgres.
        :param table_name: Название таблицы."""
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()
        self.table_name = table_name

    def get_companies_and_vacancies_count(self) -> list[dict[str, Any]]:
        """
        Получает список всех компаний и
        количество вакансий у каждой компании.
        """
        with self.conn:
            self.cur.execute(f"""
                            SELECT company_name, COUNT(*) AS vacancies_count
                            FROM {self.table_name}
                            GROUP BY company_name
                            """)
            data_from_sql = self.cur.fetchall()
            data_dict = []
            for data in data_from_sql:
                data_dict.append({
                    'company_name': data[0],
                    'vacancies_count': data[1]
                })

            return data_dict

    def get_all_vacancies(self) -> list[dict[str, Any]]:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        with self.conn:
            self.cur.execute(f"""
                            SELECT company_name, title, salary, link
                            FROM {self.table_name}
                            """)
            data_from_sql = self.cur.fetchall()
            data_dict = []
            for data in data_from_sql:
                data_dict.append({
                    'company_name': data[0],
                    'vacancy_title': data[1],
                    'salary': data[2],
                    'vacancy_link': data[3]
                })

            return data_dict

    def get_avg_salary(self) -> float:
        """Получает среднюю зарплату по вакансиям."""
        with self.conn:
            self.cur.execute(f"""SELECT AVG(salary) AS avg_salary
                            FROM {self.table_name}
                            """)
            data_from_sql = self.cur.fetchone()
            avg_salary = data_from_sql[0]

            return avg_salary

    def get_vacancies_with_higher_salary(self) -> list[dict[str, Any]]:
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        with self.conn:
            self.cur.execute(f"""SELECT * FROM {self.table_name}
                            WHERE salary > (SELECT AVG(salary)
                            FROM {self.table_name})
                            """)
            data_from_sql = self.cur.fetchall()
            data_dict = []
            for data in data_from_sql:
                data_dict.append({
                    'vacancy_title': data[1],
                    'company_name': data[2],
                    'salary': data[3],
                    'city': data[4],
                    'description': data[5],
                    'link': data[6]
                })

            return data_dict

    def get_vacancies_with_keyword(self, search_word) -> list[dict[str, Any]]:
        """
        Получает список всех вакансий, в названии которых
        содержатся переданные в метод слова, например python.
        """
        with self.conn:
            self.cur.execute(f"""SELECT * FROM {self.table_name}
                            WHERE title LIKE '%{search_word.title()}%'
                            """)
            data_from_sql = self.cur.fetchall()
            data_dict = []
            for data in data_from_sql:
                data_dict.append({
                    'vacancy_title': data[1],
                    'company_name': data[2],
                    'salary': data[3],
                    'city': data[4],
                    'description': data[5],
                    'link': data[6]
                })

            return data_dict
