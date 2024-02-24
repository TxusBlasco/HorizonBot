from application.services import get_grants_by_program as grants
import time
import json

subscriptions = {'digital': True}
#new = grants.HorizonEurope(subscriptions, 354).get_new_grants()
#print(new)
grants = grants.HorizonEurope(subscriptions, 354).get_added_deleted()
print(json.dumps(grants, indent=4))


"""from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-search')
time.sleep(10)"""

"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-search')

iframe = WebDriverWait(
	driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//iframe')))
	
driver.switch_to.frame(iframe)"""

"""button = WebDriverWait(
	driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//tr[1]//mat-card-header//button')))

button.click()"""

"""element = WebDriverWait(
	driver, 10).until(
	EC.presence_of_element_located((By.XPATH, '//tr[1]//mat-card-content//span')))

time.sleep(30)

print(element.text)"""
