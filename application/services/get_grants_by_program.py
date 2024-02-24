import pandas as pd

from application.services.web_interactor import WebInteractor
from domain.services.programs import horizon_europe as heu
from domain.services.data import process
import yaml

with open(r'../../config.yaml', 'r') as file:
	config = yaml.safe_load(file)

with open(r'../../HEU_xpaths.yaml', 'r') as file:
	HEU_xpaths = yaml.safe_load(file)

NEW_GRANTS = r'../../new_grants.csv'
OLD_GRANTS = r'../../old_grants.csv'


class HorizonEurope:
	def __init__(self, subscriptions: dict, last_nb: int):
		self.interactor = WebInteractor(
			interactor=config['horizon_europe']['interactor']).interactor()  # class
		self.subscriptions = subscriptions
		self.url = config['horizon_europe']['start_page']
		self.last_nb = last_nb
		self.browser = config['horizon_europe']['browser']

	"""def get_new_grants(self) -> list[dict]:
		grants = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		new_grants = grants.provide_new_grants(self.last_nb)
		return new_grants

	def get_all_grant_ids(self) -> list[str]:
		grants = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		grant_ids = grants.get_all_grant_ids()
		return grant_ids"""

	def get_current_grants(self) -> list[dict]:
		"""
		Goes to the European Commission web page and scrapes the info from grants, given the available subscriptions.
		A subscription can be done to one or more call topics, e.g. Civil and Aerospace. Then, only information
		related to that topic will be retrieved.
		:return: a dictionary of Pandas df with added and deleted grants
		"""
		gr = heu.Grants(self.interactor(browser=self.browser), self.subscriptions, self.url, HEU_xpaths)
		grants = gr.get_all_grant_details()
		return grants

	def get_added_deleted(self) -> dict[str, list[dict[str, str]]]:
		"""
		Replaces the OLD_GRANTS with the contents of NEW_GRANTS, explores the EC website and saves in NEW_GRANTS the
		content of the current grants. Then compares both and returns a dict with the results
		:return: A dictionary in the form:
			{
				'deleted':
					[
						{
							'title': 'HORIZON-CL4-23-45'
							...
							'closing_date': '25-09-2025'
						}
					]
				'added':
					[
						{
							'title': 'HORIZON-CL3-34-12'
							...
							'closing_date': '10-06-2023'
						}
					]
			}

		"""
		# Replace the old list of grants with the contents of the file NEW_GRANTS
		old_grants_df = process.csv_to_df(NEW_GRANTS)
		process.df_to_csv(df=old_grants_df, file_path=OLD_GRANTS)

		# analyze the web looking for the new grant list and transform the results to a dataframe
		grants = self.get_current_grants()
		new_grants_df = process.raw_to_df(grants)

		# make the current list of grants to be inside NEW_GRANTS file
		process.df_to_csv(df=new_grants_df, file_path=NEW_GRANTS)

		# compare both, looking for added or deleted grants
		diff = process.compare_df(old_grants_df, new_grants_df)
		results = {
			'deleted': diff['deleted'].to_dict(orient='records'),
			'added': diff['added'].to_dict(orient='records')
		}

		return results
