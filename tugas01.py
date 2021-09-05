# import webdriver dan time
from selenium import webdriver
import time
import re

# gunakan list untuk setiap url
listurl = ['https://noobtest.id/','https://erzaf.com/','https://www.orangsiber.com/','https://www.demoqa.com/','https://automatetheboringstuff.com/']
# gunakan for untuk perulangan
for url in listurl:
#   buka browser setiap url dan tunggu 4 detik
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    driver.get(url)
    time.sleep(4)

#   print setiap url dan title
    Title = driver.title
    token1 =re.split(r'https://www.|https://',url)[1].split('/')[0]
    print(token1,'-',Title)

#   tutup browser
    driver.quit()