# Установить виртуальное окружение
python -m venv venv
## Активировать venv
Windows: venv\Scripts\activate
MacOS/Linux: source venv/bin/activate
## Скачать зависимости
pip install -r requirements.txt
# Запустить
python main.py <номер задачи (1-5)>
# Запустить тесты
pytest
