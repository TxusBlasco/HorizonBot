from application.services.web_interactor import WebInteractor

class WebSteps:
	def __init__(self, interactor):
		self.interactor = WebInteractor(interactor)
	def search_grants(self):
		self.interactor.go_to()
