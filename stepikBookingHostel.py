from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    arendaPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    arendaButton = browser.find_element_by_css_selector("button[id='book']").click()

    find_el_x = browser.find_element_by_css_selector("span[id='input_value']")
    x = find_el_x.text
    y = calc(x)

    inputVvod = browser.find_element_by_css_selector("input[id='answer']").send_keys(y)

    sumbitClick = browser.find_element_by_css_selector("button[id='solve']").click()

finally:
    time.sleep(10)
    browser.quit()


