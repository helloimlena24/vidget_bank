from functools import wraps


def log(predicate, error_message, filename: str = ""):
    """Декоратор log, который автоматически логирует начало и конец выполнения функции,
        а также результаты или возникшие ошибки.

        Аргументы:
            predicate (callable): Функция-предикат, которая проверяет условия для выполнения функции.
            error_message (str): Сообщение об ошибке, которое будет выведено или записано при неудаче.
            filename (str): Имя файла, в который будут записываться логи.
                            Если не указано, логи выводятся в консоль.
        Возвращает:
            callable: Обернутая функция с логированием.
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль."""

    def my_decorator_error(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not predicate(*args, **kwargs):
                if filename:
                    with open(filename, "a+") as file:
                        file.write(f"{function.__name__}\nError: {error_message}\nInputs: {repr(args)}\n")
                else:
                    print(f"{function.__name__}\nError: {error_message}\nInputs: {repr(args)}")
                raise ValueError(error_message)
            else:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a+") as file:
                        file.write(f"{function.__name__} ok\n")
                else:
                    print(f"Getting started with the {function.__name__}")
                    print("Finished the function")
                return result

        return wrapper

    return my_decorator_error


def predicate_is_filter(arg_1, arg_2):
    """Предикат, который проверяет, соответствуют ли переданные аргументы
    ожидаемому списку словарей.

    Аргументы:
        arg_1 (any): Первый аргумент для проверки.
        arg_2 (any): Второй аргумент для проверки.

    Возвращает:
        tuple: Кортеж из переданных аргументов, если они соответствуют ожидаемому значению.
    """
    return arg_1, arg_2 == [
        {"id": 41428829, "state": "EXECUTED", "date": " 2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def predicate_is_sort(arg_1, arg_2: bool = True):
    """Предикат, который проверяет, соответствуют ли переданные аргументы
    ожидаемому списку словарей с учетом сортировки.

    Аргументы:
        arg_1 (any): Первый аргумент для проверки.
        arg_2 (bool): Флаг сортировки (по умолчанию True).

    Возвращает:
        tuple: Кортеж из переданных аргументов, если они соответствуют ожидаемому значению.
    """
    return arg_1, arg_2 == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512366"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"10": 594226727, "state": "CANCELED", "date": "2018-09-12721:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T06:21:33.419441"},
    ]


def predicate_is_mask(arg):
    """Предикат, который проверяет, равен ли переданный аргумент ожидаемому значению.

    Аргументы:
        arg (any): Аргумент для проверки.

    Возвращает:
        bool: True, если аргумент равен '1234567891234567', иначе False.
    """
    return arg == "1234567891234567"
