from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.get("https://www.mobil123.com/#953718837")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    
def test_login_sukses(setup):
    actions = ActionChains(setup)
    select = setup.find_element_by_xpath('/html/body/main/nav[1]/div[1]/div/nav/ul[2]/li[1]')
    actions.move_to_element(select).perform()
    setup.find_element_by_css_selector('.dropdown__section .js-loginbtn').click()
    setup.find_element_by_id('user_name_login').send_keys('yulioferdinand@gmail.com')
    setup.find_element_by_id('password_login').send_keys('xxxx')
    setup.find_element_by_xpath('/html/body/div[4]/div/div[2]/form[1]/div[5]/div[5]/button').click()
    Badge = setup.find_element_by_xpath('/html/body/main/nav[1]/div[1]/div/nav/ul[2]/li[1]/a/img').get_attribute("alt")
    assert Badge == 'Yulio Ferdinand'

Accounts = [('yulioferdinand@gmail.com','wrongpassword'),
            ('testing@gmail.com','xxxxx'),
            ('testing@test.com','wrongpassword')]

@pytest.mark.parametrize('email,password', Accounts)
def test_login_unsuccess(setup, email, password):
    setup.get('https://www.mobil123.com/#953718837')
    actions = ActionChains(setup)
    select = setup.find_element_by_xpath('/html/body/main/nav[1]/div[1]/div/nav/ul[2]/li[1]')
    actions.move_to_element(select).perform()
    setup.find_element_by_css_selector('.dropdown__section .js-loginbtn').click()
    setup.find_element_by_id('user_name_login').send_keys(email)
    setup.find_element_by_id('password_login').send_keys(password)
    setup.find_element_by_xpath('/html/body/div[4]/div/div[2]/form[1]/div[5]/div[5]/button').click()

    Alert = setup.find_element_by_xpath('/html/body/div[4]/div/div[2]/form[1]/div[3]').is_displayed()
    assert Alert == True