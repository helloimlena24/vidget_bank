# Виджет банковских операций.

## Описание:
Цель проекта - создать виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:
1. Клонируйте репозиторий:
```
git@github.com:helloimlena24/vidget_bank.git
```
## Тестирование:
Проект покрыт юнит-тестами Pytest. Для их запуска в терминале выполнить команду:
```commandline
pytest
```

## Использование функций:
1. В модуле src\masks.py находится подготовительный функционал для работы функций в модуле src\widget.py.

2. В модуле src\widget.py находятся функции, которые маскируют информацию и о картах, и о счетах,
также там имеется функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ".
3. 
Для запуска функций перейдите в модуль main.py и в параметр функции подставьте, например, номер карты или счета:
```
print(mask_account_card("Счет 64686473678894779589"))
```
4.В модуле src\processing.py созданы функции, которые обрабатывают информацию о банковских операциях, а также сортируют их по дате свершения.

5.В модуле src\generators содержатся новые функции, реализующие генераторы для обработки данных.

## Документация:
Для получения дополнительной документации обратитесь к [документации](https://github.com/helloimlena24)
