from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
input1.send_keys("ivan")
input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
input2.send_keys("Ivanov")
input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
input3.send_keys("vano@bk.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'summary.txt')
file = browser.find_element_by_xpath("//input[@id='file']")
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()