import pytest 
from selenium import webdriver


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)

def test_input():
    driver.get('https://demoqa.com/text-box')
    driver.find_element_by_id('userName').send_keys('yuliooo')
    driver.find_element_by_id('userEmail').send_keys('yulio@gmail.com')
    driver.find_element_by_id('currentAddress').send_keys('bandung')
    driver.find_element_by_id('permanentAddress').send_keys('bandung jabar')
    driver.find_element_by_id('submit').click()

    Username = driver.find_element_by_id('name')
    Email = driver.find_element_by_id('email')
    Current_Address = driver.find_element_by_xpath("//div[@id='output']/div/p[3]")
    Permanent_Address = driver.find_element_by_xpath("//div[@id='output']/div/p[4]")

    assert Username.text == 'Name:yuliooo'
    assert Email.text == 'Email:yulio@gmail.com'
    assert Current_Address.text == 'Current Address :bandung'
    assert Permanent_Address.text == 'Permananet Address :bandung jabar'

    driver.close()