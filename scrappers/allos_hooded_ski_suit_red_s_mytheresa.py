from selenium.webdriver.remote.errorhandler import NoSuchElementException

from .base_scrapper import BaseScrapper


class AllosHoodedSkiSuitRedSMytheresa(BaseScrapper):
	def __init__(
			self, driver,
			item_name="allos_hooded_ski_suit_red_s",
			url="https://www.mytheresa.com/en-us/perfect-moment-allos-hooded-ski-suit-1698807.html?utm_source=affiliate&utm_medium=affiliate.stylight.us"
	):
		super().__init__(driver, item_name, url)

	def search(self):
		try:
			self.get_page()
			sizes = self.driver.find_element_by_class_name("sizes")
			s_size = sizes.find_elements_by_xpath(".//li")[1]  # 0: XS, 1: S, 2: M, 3: L, 4: XL
			s_size.find_element_by_class_name("addtocart-trigger")
			return True
		except NoSuchElementException:
			return False
