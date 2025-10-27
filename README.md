# qa_guru_homework

Проект для сдачи домашних заданий [курса](https://qa.guru/python)

# Домашняя работа №2
1. Изменить тест на поиск в google
2. Добавить тест на открытие страницы github.com

```python
@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url
```

3. Исправить ошибки в коде (PEP8, PEP20)
```python
print("Hello, README!")
Text = "Lorem Ipsum - это текст-'рыба', часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum."


def add(a, b): return a + b


def greet(name): print("Привет," + name)


NUMS = [1, 2, 3, 4, 5]
greet("мир")
print(add(2, 2))
```
4. Запушить код в свой репозиторий

## Критерии приемки

* При создании пользователя и проекта, помните что в будущем это профиль будет вашей визитной карточкой 
* Код читабелен и соответствует PEP 8(понятные имена, длина строки ≤ 100)
* requirements.txt обязателен (selenium, webdriver-manager, pytest, линтеры)
* Все тесты должны проходить: pytest -q → 0 failed
* Структура проекта логически обоснована
* Отсутствуют мусорные файлы (.idea, venv и тд.)
* Каждое задание выполняется в отдельном файле