from typing import Type
from domain.services.web_interactors.selenium import Selenium


class WebInteractor:
	def __init__(self, interactor: str):
		self.inter = interactor

	def interactor(self) -> Type[Selenium]:
		match self.inter:
			case 'selenium':
				return Selenium


