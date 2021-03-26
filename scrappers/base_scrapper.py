from selenium import webdriver


class BaseScrapper:
	def __init__(self, driver, item_name, url):
		self.item_name = item_name
		self.driver = driver
		self.url = url

	def get_page(self):
		self.driver.get(self.url)

	def search(self):
		raise NotImplementedError
