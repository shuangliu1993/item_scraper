# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pygame import mixer

from scrappers.allos_hooded_ski_suit_red_s_mytheresa import AllosHoodedSkiSuitRedSMytheresa
from scrappers.allos_hooded_ski_suit_red_s_perfectmoment import AllosHoodedSkiSuitRedSPerfectMoment
from scrappers.covid_vaccine import CovidVaccine


INTERVAL = 5
mixer.init()
alert = mixer.Sound("bell-ringing-02.wav")

options = Options()
options.add_argument("--headless")  # use headerless driver, comment this line to make web page visible
driver = webdriver.Chrome("/Users/shuangliu/Downloads/chromedriver", options=options)

scrappers = [
    AllosHoodedSkiSuitRedSMytheresa(driver),
    AllosHoodedSkiSuitRedSPerfectMoment(driver),
    CovidVaccine(driver)
]


def play_alert():
    alert.play()
    sleep(1)
    alert.fadeout(1000)
    sleep(1)


def main():
    registered_scrappers = []
    while True:
        found = False
        for scrapper in scrappers:
            # scrapper_id = hash(scrapper)
            # if scrapper_id not in registered_scrappers:
            #     registered_scrappers.append(scrapper_id)
            #     driver.execute_script(f"window.open('about:blank', '{scrapper_id}');")
            # driver.switch_to.window(f"{scrapper_id}")
            found = scrapper.search()
            if found:
                print(
                    f"Item {scrapper.item_name} found at {scrapper.url}! Please make a purchase ASAP."
                )
                play_alert()
                break
            else:
                print(
                    f"Item {scrapper.item_name} not found at {scrapper.url}. Searching for the next item in {INTERVAL} seconds."
                )
                sleep(INTERVAL)
        if found:
            break
    from IPython import embed
    embed()
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
