from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x=int(x_element.text)

calc(x)
y = (calc(x))

answer = browser.find_element_by_xpath("//input[@id='answer']")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()