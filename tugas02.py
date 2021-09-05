from selenium import webdriver

Data = [
    ["Aria","Suseno","uno@noobtest.id","55","15000000","Store"],
    ["John","Doe","john@gmail.id","65","25000000","people"],
    ["Yulio","Ferdinand","yul@example.id","15","7000000","finance"]]

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.get("https://demoqa.com/webtables")


for url in Data:
    driver.find_element_by_id('addNewRecordButton').click()
    driver.find_element_by_id('firstName').send_keys(url[0])
    driver.find_element_by_id('lastName').send_keys(url[1])
    driver.find_element_by_id('userEmail').send_keys(url[2])
    driver.find_element_by_id('age').send_keys(url[3])
    driver.find_element_by_id('salary').send_keys(url[4])
    driver.find_element_by_id('department').send_keys(url[5])
    driver.find_element_by_id('submit').click()
    

