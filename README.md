# Запуск

```
python -m venv .venv
pip install -r requirements.txt
python -m pytest tests
```

Для запуска использовать **ТОЛЬКО** `python -m pytest tests`, иначе сломаются импорты.

# Ожидаемые результаты

`1 failed, 18 passed, 2 skipped`

## 1 failed

`test_is_correct_types.py`

Дает ошибку из-за воскресенья. В спецификации _(задании с LXP)_ валидным типом занятия указано только _мероприятие_, но в массиве есть вариант с _лекцией_.

## 2 skipped

`test_is_correct_types.py`

Скипнуты _суббота_ и _пятница_, потому что они отсутствуют в спецификации _(задании с LXP)_.
