'''
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по link
'''
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_cart_button(browser):
    browser.get(link)
    #time.sleep(30)
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_button is not None, "Add button not found"
    #print(f"Button text is '{add_button.text}'")