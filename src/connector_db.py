import psycopg2
import json


class ConnectorDB:
    """
    Обеспечивает взаимодействие с базой данных Postgres.
    Класс реализует методы, чтобы создать базу данных, таблицу,
    добавить данные в таблицу.
    """
    def __init__(self, database_name: str, params: dict, data: json,
                 table_name: str) -> None:
        """
        Создание экземпляра класса ConnectorDB.

        :param database_name: Название новой базы данных.
        :param params: Параметры подключения к Postgres.
        :param data: Данные вакансий.
        :param table_name: Название новой таблицы.
        """
        self.database_name = database_name
        self.params = params
        self.data = data
        self.table_name = table_name

    def create_database(self) -> None:
        """Создает базу данных для сохранения данных о вакансиях."""
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        # Проверяем существование базы данных.
        cur.execute(f"""SELECT 1 FROM pg_catalog.pg_database
                    WHERE datname = '{self.database_name}';""")
        exists = cur.fetchone()
        # Если она есть, удаляем ее.
        if exists:
            cur.execute(f'DROP DATABASE {self.database_name};')

        # Если нет - создаем.
        cur.execute(f'CREATE DATABASE {self.database_name};')

        conn.close()

    def create_table(self):
        """Создает таблицу для сохранения данных о вакансиях."""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        # Создаем таблицу с нужными столбцами.
        cur.execute(f"""CREATE TABLE {self.table_name} 
                                (vacancy_id SERIAL PRIMARY KEY,
                                title VARCHAR(100) NOT NULL,
                                company_name VARCHAR(50),
                                salary INTEGER,
                                city VARCHAR(50),
                                description TEXT,
                                link VARCHAR(150))
                                """)

        conn.close()

    def read_data_from_file(self):
        """Читает json файл с данными о вакансиях."""
        # Пробуем открыть переданный файл.
        try:
            with open(self.data, encoding='utf-8') as file:
                data_vacancies = json.load(file)
        # Обрабатываем ошибку, если файл не найден.
        except FileNotFoundError:
            print(f"Файл {self.data} не найден.")
            return None
        # Обрабатываем ошибку, если файл поврежден и не открывается.
        except json.JSONDecodeError:
            print(f"Не удалось открыть файл {self.data}.")
            return None

        return data_vacancies

    def insert_data_to_database(self):
        """Сохраняет данные о вакансиях в базу данных."""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        # Открываем файл с данными.
        data_vacancies = self.read_data_from_file()
        # Создаем цикл для парсинга данных.
        for vacancy in data_vacancies:
            vacancy_title = vacancy['vacancy_title']
            vacancy_link = vacancy['vacancy_link']
            requirement = vacancy['requirement']
            salary = vacancy['salary']
            company_name = vacancy['employer_name']
            vacancy_area = vacancy['vacancy_area']

            # Добавляем данные в созданную таблицу.
            cur.execute(
                f"""
                INSERT INTO {self.table_name} 
                (title, company_name, salary, city, description, link)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (vacancy_title, company_name, salary, vacancy_area,
                 requirement, vacancy_link)
            )

        conn.close()
