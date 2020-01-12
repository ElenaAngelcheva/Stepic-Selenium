from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x=int(x_element.text)

calc(x)
y = (calc(x))
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

answer = browser.find_element_by_xpath("//input[@id='answer']")
answer.send_keys(y)


option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()
button.click()


