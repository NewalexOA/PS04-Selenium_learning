# Wikipedia Search Bot

This Python script allows users to interact with Wikipedia through a web browser. The script uses Selenium to automate web interactions, enabling users to search for topics, navigate through paragraphs, and follow links to related articles.

## Features
- Search for topics on Wikipedia.
- Browse through paragraphs of the search results.
- Navigate to related articles.

## Requirements
- Python 3.x
- Selenium
- WebDriver for your browser (e.g., ChromeDriver for Google Chrome)

## Installation

1. Install Python 3.x if you haven't already: [Python Downloads](https://www.python.org/downloads/)
2. Install Selenium: 
    ```bash
    pip install selenium
    ```
3. Download the WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Google Chrome) and ensure it is in your system's PATH.

## Usage

1. Run the script:
    ```bash
    python main.py
    ```
2. Enter the search query when prompted.
3. Follow the on-screen instructions to navigate through the search results and related articles.

## Code Explanation

The script initializes a web browser using Selenium and navigates to the Wikipedia search page. It prompts the user to input a search query, performs the search, and displays the results. Users can then choose to browse through the paragraphs of the search results or navigate to related articles. The script continues to run until the user chooses to exit.

---

# Бот для поиска в Википедии

Этот скрипт на Python позволяет пользователям взаимодействовать с Википедией через веб-браузер. Скрипт использует Selenium для автоматизации веб-взаимодействий, позволяя пользователям искать темы, просматривать параграфы и переходить по ссылкам на связанные статьи.

## Возможности
- Поиск тем в Википедии.
- Просмотр параграфов результатов поиска.
- Переход к связанным статьям.

## Требования
- Python 3.x
- Selenium
- WebDriver для вашего браузера (например, ChromeDriver для Google Chrome)

## Установка

1. Установите Python 3.x, если он еще не установлен: [Загрузки Python](https://www.python.org/downloads/)
2. Установите Selenium: 
    ```bash
    pip install selenium
    ```
3. Загрузите WebDriver для вашего браузера (например, [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) для Google Chrome) и убедитесь, что он находится в PATH вашей системы.

## Использование

1. Запустите скрипт:
    ```bash
    python main.py
    ```
2. Введите запрос для поиска, когда будет предложено.
3. Следуйте инструкциям на экране для навигации по результатам поиска и связанным статьям.

## Описание кода

Скрипт инициализирует веб-браузер с помощью Selenium и переходит на страницу поиска Википедии. Он запрашивает у пользователя ввод поискового запроса, выполняет поиск и отображает результаты. Пользователи могут выбирать просмотр параграфов результатов поиска или переходить к связанным статьям. Скрипт продолжает работать, пока пользователь не выберет выход.

