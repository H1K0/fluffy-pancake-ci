# fluffy-pancake-ci

![CI](https://github.com/H1K0/fluffy-pancake-ci/actions/workflows/main.yml/badge.svg)

Консольный TODO-менеджер на Python. Проект для практики по CI/CD.

## Запуск
```
python main.py
```

## Тесты
```
pip install -r requirements-dev.txt
flake8 .
pytest --cov=.
```

## Документация
Собирается автоматически из docstring при каждом изменении `main`.
