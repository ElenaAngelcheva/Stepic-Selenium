from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'),"$100"))
print(price)
button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
  )
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()


x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x=int(x_element.text)

calc(x)
y = (calc(x))

answer = browser.find_element_by_xpath("//input[@id='answer']")
answer.send_keys(y)

button = browser.find_element_by_xpath("//button[@id='solve']")
button.click()