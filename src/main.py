from connector_db import ConnectorDB
from api_hh import HeadHunterAPI
from db_manager import DBManager
from settings import PATH_FILE
from config import config


def main_create_db_and_table():
    """Создает базу данных и таблицу с данными."""
    # Создаем экземпляр класса HeadHunterAPI и
    # выгружаем данные по API в json файл.
    hh_api = HeadHunterAPI()
    hh_api.data_organize('vac_emp_data.json')

    # Подтягиваем конфигурационный файл подключения к БД.
    params = config()

    # Создаем экземпляр класса ConnectorDB.
    connect = ConnectorDB('hh_database', params, PATH_FILE, 'vacancies')
    # Создаем базу данных hh_database.
    connect.create_database()
    # Создаем таблицу vacancies.
    connect.create_table()
    # Добавляем данные из файла vac_emp_data.json в таблицу в БД hh_database.
    connect.insert_data_to_database()


def main_db_manager():
    """Выводит по числу запросы."""
    # Подтягиваем конфигурационный файл подключения к БД.
    params = config()
    # Создаем экземпляр класса DBManager.
    db1 = DBManager('hh_database', params, 'vacancies')

    print('Выберите запрос из списка:')
    print('1 - вывести все компании и количество вакансий у каждой компании.\n'
          '2 - вывести все вакансии с указанием компании, вакансии, зарплаты и ссылки на вакансию.\n'
          '3 - вывести среднюю зарплату по вакансиям.\n'
          '4 - вывести все вакансии, у которых зарплата выше средней по всем вакансиям.\n'
          '5 - вывести все вакансии, в названии которых содержится переданное слово, например python.\n')

    search_number = int(input('Введите цифру нужного запроса: '))

    if search_number == 1:
        data = db1.get_companies_and_vacancies_count()
        print(f"Нашлось {len(data)}:")
        # Создаем цикл по вакансиям и выводим их пронумерованными.
        for index, vacancy in enumerate(data, start=1):
            print(f"{index}. {vacancy['company_name']} - {vacancy['vacancies_count']}.")
    elif search_number == 2:
        data = db1.get_all_vacancies()
        print(f"Нашлось {len(data)}:")
        # Создаем цикл по вакансиям и выводим их пронумерованными.
        for index, vacancy in enumerate(data, start=1):
            print(f"{index}. Компания: {vacancy['company_name']} - {vacancy['vacancy_title']}.")
            print(f"Зарплата: {vacancy['salary']} руб. --> {vacancy['vacancy_link']}")
    elif search_number == 3:
        data = db1.get_avg_salary()
        print("Средняя зарплата: ", round(data, 2), "руб.")
    elif search_number == 4:
        data = db1.get_vacancies_with_higher_salary()
        print(f"Нашлось {len(data)}:")
        # Создаем цикл по вакансиям и выводим их пронумерованными.
        for index, vacancy in enumerate(data, start=1):
            print(f"{index}. Компания: {vacancy['company_name']} - {vacancy['vacancy_title']}.")
            print(f"Зарплата: {vacancy['salary']} руб. --> {vacancy['link']}.")
            print(f"Город: {vacancy['city']}.\nОписание вакансии: {vacancy['description']}")
    elif search_number == 5:
        search_word = input('Введите слово для поиска вакансии, например python: ')
        data = db1.get_vacancies_with_keyword(search_word)
        print(f"Нашлось {len(data)}:")
        # Создаем цикл по вакансиям и выводим их пронумерованными.
        for index, vacancy in enumerate(data, start=1):
            print(f"{index}. Компания: {vacancy['company_name']} - {vacancy['vacancy_title']}.")
            print(f"Зарплата: {vacancy['salary']} руб. --> {vacancy['link']}.")
            print(f"Город: {vacancy['city']}.\nОписание вакансии: {vacancy['description']}")


if __name__ == '__main__':
    main_create_db_and_table()
    # main_db_manager()
