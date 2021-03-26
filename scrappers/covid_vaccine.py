from time import sleep

from .base_scrapper import BaseScrapper
from selenium.webdriver.remote.errorhandler import NoSuchElementException


class CovidVaccine(BaseScrapper):
	def __init__(
			self, driver,
			item_name="covid",
			url="https://www.cvs.com/vaccine/intake/store/cvd-schedule?icid=coronavirus-lp-vaccine-sd-statetool",
	):
		super().__init__(driver, item_name, url)
		# manually enter the website
		self.get_page()
		from IPython import embed
		embed()

	def search(self):
		schedule_button = self.driver.find_element_by_class_name("btn-control")
		schedule_button.click()
		sleep(3)
		try:
			stores = self.driver.find_element_by_class_name("store-list-container")
		except NoSuchElementException:
			return False
		return "We’re sorry" not in stores.text
