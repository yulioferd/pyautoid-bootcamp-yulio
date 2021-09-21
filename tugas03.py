from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get('https://demoqa.com/alerts')

driver.find_element_by_id('timerAlertButton').click()
try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
except TimeoutException:
    pass
driver.close()