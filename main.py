from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.parse


# Функция для проверки корректности ввода
def get_user_input(prompt, valid_choices):
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_choices:
            return user_input.lower()
        print(f"Неверный ввод. Пожалуйста, выберите из {valid_choices}")


# первоначальный запрос
user_initial_query = input("Что найти в Википедии? ")

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/w/index.php?search=&title=Служебная:Поиск&profile=advanced&fulltext=1&ns0=1")

try:
    assert "Википедия" in browser.title
except AssertionError:
    print("Заголовок страницы не содержит 'Википедия'. Проверьте URL или подключение к интернету.")
    browser.quit()
    exit()

while True:
    search_box = browser.find_element(By.ID, "ooui-php-1")
    search_box.clear()
    search_box.send_keys(user_initial_query)
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)

    try:
        search_results_container = browser.find_element(By.CLASS_NAME, "mw-search-results-container")
        max_relevant = search_results_container.find_element(By.CLASS_NAME, "searchmatch")
        max_relevant.click()
        break
    except:
        print("Не удалось найти результаты поиска. Поменяйте запрос.")
        user_initial_query = input("Введите новый запрос: ")


# Основной цикл
while True:
    user_choice = get_user_input("Что сделать дальше?\n"
                                 "1 - листать параграфы\n"
                                 "2 - перейти на одну из связанных страниц\n"
                                 "3 - выход\n"
                                 "Ваш выбор: ", ["1", "2", "3"])

    if user_choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        for paragraph in paragraphs:
            print(paragraph.text)
            user_choice_p = input("Для продолжения нажмите Enter, для выхода нажмите 'X': ")
            if user_choice_p.lower() == "x":
                break

    elif user_choice == "2":
        hatnote_divs = browser.find_elements(By.CSS_SELECTOR, "div.hatnote.navigation-not-searchable")
        links = []

        for div in hatnote_divs:
            if "Основная статья:" in div.text:
                links.extend(div.find_elements(By.TAG_NAME, "a"))

            for link in links:
                href = link.get_attribute("href")
                text = link.text
                if href and text:
                    decoded_href = urllib.parse.unquote(href)
                    print(f"{text}: {decoded_href}")
                    user_choice_p = input(
                        "Для перехода к следующей ссылке нажмите Enter, для выбора этой ссылки нажмите 'S': ")
                    if user_choice_p.lower() == "s":
                        browser.get(href)
                        break

    elif user_choice == "3":
        break


browser.quit()
