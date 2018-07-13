import time
from selenium import webdriver

driver=webdriver.Chrome('C:\Cogito\chromedriver')
#driver=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome')
driver.get('https://acomics.ru/settings/subscribes');

driver.find_element_by_link_text('Вход').click()
name_box=driver.find_element_by_name('username')
name_box.send_keys('***')
pass_box=driver.find_element_by_name('password')
pass_box.send_keys('***')
button1=driver.find_element_by_name('submit').click()

checkboxes=[]
checkboxes=driver.find_elements_by_name('toDelete[]')

len=0
for bruh in checkboxes:
    if len>500:
        break
    bruh.click()
    len+=1
print(wololo)
