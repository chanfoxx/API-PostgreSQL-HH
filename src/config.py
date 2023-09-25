from configparser import ConfigParser


def config(filename='database.ini', section='postgresql') -> dict[str, str]:
    """
    Считывает значения из файла конфигурации
    и возвращает словарь параметров для указанной секции.
    """
    parser = ConfigParser()
    # Читаем переданный файл.
    parser.read(filename)
    db = {}
    # Проходим по условиям, если все успешно - данные складываются в словарь.
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            f'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
