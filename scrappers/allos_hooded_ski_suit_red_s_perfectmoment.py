from time import sleep

from .base_scrapper import BaseScrapper


class AllosHoodedSkiSuitRedSPerfectMoment(BaseScrapper):
	def __init__(
			self, driver,
			item_name="allos_hooded_ski_suit_red_s",
			url="https://www.perfectmoment.com/us/women-allos-ski-suit-red"
	):
		super().__init__(driver, item_name, url)

	def search(self):
		self.get_page()
		sleep(1)  # wait a bit of time
		options = self.driver.find_element_by_name("super_attribute[146]")
		sizes = [x.get_attribute("value") for x in options.find_elements_by_tag_name("option")]
		return "56" in sizes  # "55" - XS, "56" - S, "57" - M, "58" - L, "59" - XL
