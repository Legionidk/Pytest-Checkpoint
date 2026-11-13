# Запуск

```
python -m venv .venv
pip install -r requirements.txt
```

Для запуска использовать **ТОЛЬКО** `python -m pytest tests` или `pytest --cov=schedule --cov-report=term-missing --cov-report=html --alluredir=allure-results`, иначе сломаются импорты.

# Ожидаемые результаты

`1 failed, 18 passed, 2 skipped`

## 1 failed

`test_is_correct_types.py`

Дает ошибку из-за воскресенья. В спецификации _(задании с LXP)_ валидным типом занятия указано только _мероприятие_, но в массиве есть вариант с _лекцией_.

## 2 skipped

`test_is_correct_types.py`

Скипнуты _суббота_ и _пятница_, потому что они отсутствуют в спецификации _(задании с LXP)_.

## Покрытие - 92%

`schedule.py`

`104` и `108` строчка - два `return`, которые отъедают 8% покрытия.
