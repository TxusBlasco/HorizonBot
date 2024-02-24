import time


class Subscriptions:
	def __init__(
			self,
			web_interactor,
			grants=True,
			tenders=False,
			forthcoming=True,
			open_=True,
			close=False,
			period='2021 - 2027',
			programme='Horizon Europe (HORIZON)'  # contains
	):
		self.grants = grants
		self.tenders = tenders
		self.forthcoming = forthcoming
		self.open = open_
		self.close = close
		self.wi = web_interactor

	def get_subscriptions(
			self,

			# Pillar I: Excellent science
			erc: bool = False,
			msca: bool = False,
			infra: bool = False,

			# Pillar II: Global Challenges and European Industrial Competitiveness
			health: bool = False,
			culture: bool = False,
			civil: bool = False,
			digital: bool = False,
			climate: bool = False,
			food: bool = False,

			# Pillar III: innovative europe
			eic: bool = False,
			innovative: bool = False,
			eit: bool = False,

			# Widening Participation and Strengthening the European Research Area
			widening: bool = False,
			reforming: bool = False
	):
		"""
		Sets to which one of the topics one wants to be subscribed. Corresponds to "Programme part field"
		:param erc: European Research Council
		:param msca: Marie Skłodowska-Curie Actions
		:param infra: Research infrastructures
		:param health: Health
		:param culture: Culture, creativity and inclusive society
		:param civil: Civil Security for Society
		:param digital: Digital, Industry and Space
		:param climate: Climate, Energy and Mobility
		:param food: Food, Bioeconomy Natural Resources, Agriculture and Environment
		:param eic: The European Innovation Council
		:param innovative: European innovation ecosystems
		:param eit: The European Institute of Innovation and Technology (EIT)
		:param widening: Widening participation and spreading excellence
		:param reforming: Reforming and enhancing the European R&I System
		:return: a dictionary with funding topic keywords
		"""
		return {
			'erc': erc,
			'msca': msca,
			'infra': infra,
			'health': health,
			'culture': culture,
			'civil': civil,
			'digital': digital,
			'climate': climate,
			'food': food,
			'eic': eic,
			'innovative': innovative,
			'eit': eit,
			'widening': widening,
			'reforming': reforming
		}

	def check_mark(self, subscriptions: dict):
		true_subs = [key for key, value in subscriptions.items() if value]
		check = [self.wi.check for _ in true_subs]

	def uncheck_mark(self, subscriptions: dict):
		false_subs = [key for key, value in subscriptions.items() if not value]
		uncheck = [self.wi.uncheck for _ in false_subs]

	def go_to(self, url):
		pass


class Steps:
	def __init__(self, interactor, subscriptions: dict):
		self.interactor = interactor
		subs = Subscriptions(web_interactor=interactor)
		subscriptions = subs.get_subscriptions(*subscriptions)

	def close_cookies(self, only_essential: str, close: str):
		self.interactor.click(only_essential)
		self.interactor.click(close)

	def go_to_funding_opportunities_page(self, url: str):
		self.interactor.go_to(url)

	def switch_to_iframe(self, xpath: str):
		self.interactor.switch_to_iframe(xpath)

	def uncheck_tenders(self, xpath: str):
		self.interactor.click(xpath)

	def deploy_program(self, xpath: str):
		self.interactor.click(xpath)

	def choose_horizon_europe(self, xpath: str):
		self.interactor.click(xpath)

	def wait_for_items_to_load(self, seconds):
		time.sleep(seconds)

	def get_number_of_items(self, xpath: str):
		nb_items = self.interactor.get_text(xpath)['text']
		return nb_items

	def deploy_sort_by(self, xpath: str):
		self.interactor.click(xpath)

	def select_publication_date(self, xpath: str):
		self.interactor.click(xpath)

	def sort_grants_inverse_order(self, xpath: str, xpath_inv: str):
		self.interactor.click(xpath_inv)
		"""if self.interactor.find_element(xpath_inv)['success']:
			print()
			self.interactor.click(xpath_inv)
		else:
			self.interactor.click(xpath)"""

	def deploy_grant_content(self, xpath: str, nb: int):
		self.interactor.click(xpath % nb)

	def get_grant_info(self, _xpaths: dict, nb: int) -> dict:
		"""
		Recovers the text of each grant element
		:param _xpaths: a dictionary of grant elements in keys and xpaths in values
		:param nb: order of grant in the grant list. nb=1 means take the first grant in list, nb=7 means take the
		grant seven and so on.
		:return: a dictionary of grant elements in keys and corresponding grant element text in values
		"""
		grant = dict(map(lambda x: (x[0], self.interactor.get_text(x[1] % nb)['text']), _xpaths.items()))
		return grant

	def set_50_items_per_page(self, deploy, set_50):
		self.interactor.click(deploy)
		self.interactor.click(set_50)

	def get_all_grant_ids(self, grant_list: str, grant_id: str, next_: str, next_disabled: str) -> list[str]:
		"""
		Gets all grant ids (e.g. HORIZON-MSCA-2024-COFUND-01-01) from one page in the grant results, and iterates the
		paginator until no more grants are available to recover
		:param grant_list: xpath
		:param grant_id: xpath
		:param next_: xpath
		:param next_disabled: xpath
		:return: the list of grant ids (strings)
		"""
		grant_ids = []
		while True:
			self.wait_for_items_to_load(1)
			nb = self.interactor.get_nb_elements(grant_list)  # nb of grants in page
			for grant in range(1, nb + 1):
				grant_ids.append(self.interactor.get_text(grant_id % grant)['text'])
			if self.interactor.find_element(next_disabled)['success']:  # while still available pages in paginator
				return grant_ids
			else:
				self.interactor.click(next_)

	def get_all_grant_details(self, grants: str, _xpaths: dict, next_: str, disabled: str, deploy: str) -> list[dict]:
		grant_details = []
		while True:
			self.wait_for_items_to_load(1)
			nb = self.interactor.get_nb_elements(grants)  # nb of grants in page
			for grant_nb in range(1, nb + 1):
				grant_details.append(self.get_grant_info(_xpaths=_xpaths, nb=grant_nb))
			if self.interactor.find_element(disabled)['success']:  # while still available pages in paginator
				return grant_details
			else:
				self.interactor.click(next_)

	def expand_all(self, expand: str):
		self.interactor.click(expand)


# TODO This class should not have business logic, just steps. Reformat
class Grants:
	def __init__(self, interactor, subscriptions: dict, url: str, xpaths: dict):
		self.interactor = interactor  # class
		self.subscriptions = subscriptions
		self.url = url
		self.steps = Steps(self.interactor, self.subscriptions)
		self.xpaths = xpaths

	def get_nb_grants(self) -> int:
		self.steps.go_to_funding_opportunities_page(self.url)
		self.steps.switch_to_iframe(self.xpaths['funding_tenders']['iframe'])
		self.steps.uncheck_tenders(self.xpaths['funding_tenders']['tenders'])
		self.steps.deploy_program(self.xpaths['funding_tenders']['program_group']['field'])
		self.steps.choose_horizon_europe(self.xpaths['funding_tenders']['program_group']['heu'])
		self.steps.wait_for_items_to_load(5)
		nb_grants = self.steps.get_number_of_items(self.xpaths['funding_tenders']['nb_grants'])
		print('[INFO] Number of grants found: ', nb_grants)
		return int(nb_grants)

	@staticmethod
	def is_new_grant(current: int, last: int):
		new = current - last
		return new

	def get_last_added_grant(self, nb: int) -> dict:
		#self.steps.wait_for_items_to_load(5)
		#self.steps.deploy_sort_by(self.xpaths['funding_tenders']['sort_by']['field'])
		self.steps.select_publication_date(self.xpaths['funding_tenders']['sort_by']['opening_date'])
		self.steps.wait_for_items_to_load(2)
		self.steps.sort_grants_inverse_order(
			self.xpaths['funding_tenders']['sort_by']['sort'],
			self.xpaths['funding_tenders']['sort_by']['sort_inv']
		)
		#self.steps.wait_for_items_to_load(5)
		self.steps.deploy_grant_content(self.xpaths['funding_tenders']['deploy_content_btn'], nb)
		self.steps.wait_for_items_to_load(1)
		grant = self.steps.get_grant_info(self.xpaths['funding_tenders']['items_found'], nb)
		#self.steps.wait_for_items_to_load(30)
		return grant

	def provide_new_grants(self, last_nb_grants) -> (int, list[dict]):
		nb_grants = self.get_nb_grants()
		new = self.is_new_grant(nb_grants, last_nb_grants)
		new_grants = []
		if new > 0:
			for i in range(new):
				new_grants.append(self.get_last_added_grant(nb=i+1))
		return new_grants

	def get_all_grant_ids(self):
		self.steps.go_to_funding_opportunities_page(self.url)
		self.steps.close_cookies(
			only_essential=self.xpaths['cookies']['only_essentials'],
			close=self.xpaths['cookies']['close'])
		self.steps.switch_to_iframe(self.xpaths['funding_tenders']['iframe'])
		self.steps.uncheck_tenders(self.xpaths['funding_tenders']['tenders'])
		self.steps.deploy_program(self.xpaths['funding_tenders']['program_group']['field'])
		self.steps.choose_horizon_europe(self.xpaths['funding_tenders']['program_group']['heu'])
		self.steps.wait_for_items_to_load(3)
		self.steps.set_50_items_per_page(
			deploy=self.xpaths['funding_tenders']['items_per_page']['btn'],
			set_50=self.xpaths['funding_tenders']['items_per_page']['fifty'])
		grant_ids = self.steps.get_all_grant_ids(
			grant_list=self.xpaths['funding_tenders']['items_per_page']['grant_list'],
			grant_id=self.xpaths['funding_tenders']['items_found']['id'],
			next_=self.xpaths['funding_tenders']['items_per_page']['next'],
			next_disabled=self.xpaths['funding_tenders']['items_per_page']['next_disabled'])
		return grant_ids

	def get_all_grant_details(self) -> list[dict]:
		self.steps.go_to_funding_opportunities_page(self.url)
		self.steps.close_cookies(
			only_essential=self.xpaths['cookies']['only_essentials'],
			close=self.xpaths['cookies']['close'])
		self.steps.switch_to_iframe(self.xpaths['funding_tenders']['iframe'])
		self.steps.uncheck_tenders(self.xpaths['funding_tenders']['tenders'])
		self.steps.deploy_program(self.xpaths['funding_tenders']['program_group']['field'])
		self.steps.choose_horizon_europe(self.xpaths['funding_tenders']['program_group']['heu'])
		self.steps.wait_for_items_to_load(3)
		self.steps.set_50_items_per_page(
			deploy=self.xpaths['funding_tenders']['items_per_page']['btn'],
			set_50=self.xpaths['funding_tenders']['items_per_page']['fifty'])
		self.steps.expand_all(self.xpaths['funding_tenders']['expand_hide_all'])
		grant_ids = self.steps.get_all_grant_details(
			_xpaths=self.xpaths['funding_tenders']['items_found'],
			deploy=self.xpaths['funding_tenders']['deploy_content_btn'],
			grants=self.xpaths['funding_tenders']['items_per_page']['grant_list'],
			next_=self.xpaths['funding_tenders']['items_per_page']['next'],
			disabled=self.xpaths['funding_tenders']['items_per_page']['next_disabled'])
		return grant_ids
