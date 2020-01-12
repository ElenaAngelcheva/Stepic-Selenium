from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_xpath("//span[@id='num1']")
x=int(x_element.text)
y_element = browser.find_element_by_xpath("//span[@id='num2']")
y=int(y_element.text)
sum = int(x)+int(y)
print(sum)
z=str(sum)
print(type(z))
print(z)
select = Select(browser.find_element_by_tag_name("select"))
browser.find_element_by_css_selector("option:nth-child(2)").click()
select.select_by_visible_text(z)

button = browser.find_element_by_css_selector("button.btn")
button.click()