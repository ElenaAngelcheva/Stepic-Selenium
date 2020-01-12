from selenium import webdriver
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


id_element = browser.find_element_by_id("treasure")
x_element = id_element.get_attribute("valuex")
x=int(x_element)


calc(x)
y = (calc(x))
answer = browser.find_element_by_xpath("//input[@id='answer']")
answer.send_keys(y)

option1 =browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()