from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x=int(x_element.text)

calc(x)
y = (calc(x))

answer = browser.find_element_by_xpath("//input[@id='answer']")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()