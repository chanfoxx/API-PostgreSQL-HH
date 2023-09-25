# Парсер вакансий в PostgreSQL

Добро пожаловать!
Данный проект представляет собой парсер, которой извлекает информацию
о вакансиях и компаниях с сайта HeadHunter и впоследующем загружает ее
в новосозданную базу данных в PostgreSQL.

## Введение

Парсер вакансий предназначен для автоматического сбора информации 
о вакансиях с сайта HeadHunter. Он позволяет сохранять полученные 
данные в удобном формате и загружать их в новую базу данных в PostgreSQL.

## Особенности

- Получает данные о вакансиях с сайта HeadHunter по 10 компаниям.
- Поддерживает сохранение извлеченных данных в формате JSON.
- Позволяет создавать новую БД, а также новые таблицы в PostgreSQL.
- Позволяет работать с данными из БД с помощью запросов по нужному номеру.

## Структура проекта

В файле README.md представлена общая информация о каждом файле и его 
назначении.

- 'api_hh.py' - классы для работы с API сайтом с вакансиями.
- 'config.py' - файл для парсинга конфигурационного файла database.ini (требуется создать).
- 'connector_db.py' - класс для подключения к БД, а так же ее создания.
- 'db_manager.py' - класс для работы с данными из таблиц БД.
- 'error_response.py' - файл обрабатывающий ошибку запроса.
- 'main.py' - главный файл с запуском программы.
- 'vac_emp_data.json' - файл куда загружаются вакансии.
- 'vacancy.py' - класс для работы с вакансиями.


## Установка

1. Клонируйте данный репозиторий на свой локальный компьютер.
2. Установите Python если он еще не установлен.
3. Установите Poetry, если еще не установлено.
4. Установите и активируйте виртуальное окружение.
5. Перейдите в корневую папку проекта и установите все зависимости с помощью
Poetry:
poetry install
6. Создайте конфигурационный файл('database.ini') с данными для подключения к БД:
<img width="204" alt="Снимок экрана 2023-09-25 в 23 32 21" src="https://github.com/chanfoxx/API-PostgreSQL-HH/assets/133925881/b0b6ba45-97d3-4574-8dc7-f3d962d6e2fe">


7. Запустите парсер:
main.py

## Пример вывода вакансий


<img width="1042" alt="Снимок экрана 2023-09-25 в 23 10 04" src="https://github.com/chanfoxx/API-PostgreSQL-HH/assets/133925881/0c505876-cb49-48ef-a211-f005779fe10b">


## Ошибки и улучшения

Если вы обнаружили ошибки, у вас есть предложения по улучшению данного проекта
или у вас есть вопросы по использованию парсера, пожалуйста, пожалуйста, 
присылайте pull request.

