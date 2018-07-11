from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time






#######################################
# Inputs
#######################################

homee_id = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'

# Download ChromeDriver from http://chromedriver.chromium.org/download
chromedriver = 'C:\\chromedriver.exe'# Path to chromedriver.exe (Backslashes must be escaped with Backslash so C:\  --> C:\\)



################################################










browser = webdriver.Chrome(chromedriver)
browser.get('http://my.hom.ee')

homee_id_input = browser.find_element_by_name("homeeId")
username_input = browser.find_element_by_name("username")
password_input = browser.find_element_by_name("password")

homee_id_input.send_keys(homee_id)
username_input.send_keys(username)
password_input.send_keys(password)

time.sleep(1)
browser.find_element_by_xpath("//div[@ng-click='login()']").click()

time.sleep(5)
browser.get('https://my.hom.ee/#!/deviceslist/device/id/1')
#browser.find_element_by_xpath("//li[@ng-click='exportNodeHistory()']/div").click()




n_devices = browser.find_element_by_xpath("//span[@ng-bind-html='deviceStatisticsString']").text
n_devices = int(n_devices[:n_devices.find(' ')])



li = []
bottom = browser.find_element_by_xpath("//div[@class='statisticsString selectable']")
for i in range(n_devices % 18):
    li.append(browser.find_elements_by_xpath("//div[@class='minHeight100']/ul/li"))
    browser.execute_script("arguments[0].scrollIntoView();", bottom)
    
li = list(set([item for sublist in li for item in sublist]))


node_id = []
for node in li:
    node_id.append(int(node.get_attribute("href").replace('#!/deviceslist/device/id/','')))





for id in node_id:
    print(id)
    browser.get('https://my.hom.ee/#!/deviceslist/device/id/'+str(id)+'/edit')
    browser.find_element_by_xpath("//li[@ng-click='exportNodeHistory()']/div").click()
    time.sleep(2)



