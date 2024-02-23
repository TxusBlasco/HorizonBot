from application.services.web_interactor import WebInteractor
from domain.services.programs import horizon_europe as heu
import yaml

with open(r'../../config.yaml', 'r') as file:
	config = yaml.safe_load(file)

with open(r'../../HEU_xpaths.yaml', 'r') as file:
	HEU_xpaths = yaml.safe_load(file)


class HorizonEurope:
	def __init__(self, subscriptions: dict, last_nb: int):
		self.interactor = WebInteractor(
			interactor=config['horizon_europe']['interactor']).interactor()  # class
		self.subscriptions = subscriptions
		self.url = config['horizon_europe']['start_page']
		self.last_nb = last_nb
		self.browser = config['horizon_europe']['browser']

	def get_new_grants(self) -> list[dict]:
		grants = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		new_grants = grants.provide_new_grants(self.last_nb)
		return new_grants

	def get_all_grant_ids(self) -> list[str]:
		grants = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		grant_ids = grants.get_all_grant_ids()
		return grant_ids

	def get_all_grant_details(self) -> list[str]:
		grants = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		grant_ids = grants.get_all_grant_details()
		return grant_ids

