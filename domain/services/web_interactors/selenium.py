from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class Selenium:
	def __init__(self, browser):
		match browser:
			case 'chrome':
				self.driver = webdriver.Chrome()
			case 'firefox':
				self.driver = webdriver.Firefox()
			case 'edge':
				self.driver = webdriver.Edge()
			case _:
				print('[ERROR] Browser not implemented')

	def go_to(self, url: str) -> dict:
		try:
			self.driver.get(url)
			WebDriverWait(self.driver, 15).until(lambda d: d.current_url == url)
			print("[INFO] Successfully navigated to %s." % url)
			return {'success': True}
		except TimeoutException:
			print("[ERROR] Timed out waiting for URL to change to %s." % url)
			return {'success': False}

	def find_element(self, xpath: str) -> dict:
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.XPATH, xpath))
			)
			print("[INFO] Element found: %s" % xpath)
			return {'success': True, 'element': element}
		except TimeoutException:
			print("[ERROR] Element not found: %s" % xpath)
			return {'success': False, 'element': None}

	def click(self, xpath: str) -> dict:
		element = self.find_element(xpath)['element']
		try:
			element.click()
			print("[INFO] Success clicking in: %s" % xpath)
			return {'success': True}
		except :
			print("[ERROR] Element not clickable: %s" % xpath)
			return {'success': False}

	def input(self, xpath: str, content: str) -> dict:
		element = self.find_element(xpath)['element']
		try:
			element.clear()
			element.send_keys(content + Keys.RETURN)
			print("[INFO] Keys sent to element: %s" % xpath)
			return {'success': True}
		except TimeoutException:
			print("[ERROR] Keys not sent to element: %s" % xpath)
			return {'success': False}

	def get_text(self, xpath) -> dict:
		element = self.find_element(xpath)['element']

		try:
			text = element.text
			print("[INFO] Text '%s' acquired from element: %s" % (text, xpath))
			return {'success': True, 'text': text}
		except TimeoutException:
			print("[ERROR] Text NOT acquired from element: %s" % xpath)
			return {'success': False, 'text': None}

	def switch_to_iframe(self, xpath) -> dict:
		iframe = self.find_element(xpath)['element']
		try:
			self.driver.switch_to.frame(iframe)
			print("[INFO] Element found: %s" % xpath)
			return {'success': True}
		except TimeoutException:
			print("[ERROR] Element not found: %s" % xpath)
			return {'success': False}

	def get_nb_elements(self, xpath) -> int:
		elements = self.driver.find_elements(By.XPATH, xpath)
		return len(elements)
