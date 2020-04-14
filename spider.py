from selenium.webdriver import Chrome, ChromeOptions
from selenium.common import exceptions
from time import sleep
import pickle

TEAMSTATS_URL = 'https://www.wanplus.com/kog/teamstats/'
PLAYERSTATS_URL = 'https://www.wanplus.com/kog/playerstats/'

def crawl_teamstats(browser, url):
	browser.get(url)
	sleep(5)
	assault_and_economy = browser.page_source
	xpath = "//div[@class='detail-list-title']/div"
	buttom = browser.find_elements_by_xpath(xpath)[-1]
	buttom.click()
	sleep(5)
	resource_control = browser.page_source
	return (assault_and_economy, resource_control)

def crawl_playerstats(browser, url):
	next_page_element = '//a[@class="paginate_button next"]'
	pre_page_element = '//a[@class="paginate_button previous"]'
	browser.get(url)
	sleep(5)
	kda_pages = [browser.page_source]
	
	while True:
		try:
			next_page = browser.find_element_by_xpath(next_page_element)
			next_page.click()	
			sleep(5)
			kda_pages.append(browser.page_source)
		except exceptions.NoSuchElementException as _:
			break

	xpath = "//div[@class='detail-list-title']/div"
	buttom = browser.find_elements_by_xpath(xpath)[-1]
	buttom.click()
	sleep(5)
	power_and_contribution_pages = [browser.page_source]
	while True:
		try:
			pre_page = browser.find_element_by_xpath(pre_page_element)
			pre_page.click()
			sleep(5)
			power_and_contribution_pages.append(browser.page_source)
		except exceptions.NoSuchElementException as _:
			break
	return (kda_pages, power_and_contribution_pages)

if __name__ == '__main__':
	options = ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('log-level=3')
	with Chrome(options=options) as browser:
		teamstats = crawl_teamstats(browser, TEAMSTATS_URL)
		print('Crawl teamstats successful')
		playerstats = crawl_playerstats(browser, PLAYERSTATS_URL)
		print('Crawl playerstats successful:', len(playerstats[0]), len(playerstats[1]))
		with open('teamstats.pickle', 'wb') as f:
			pickle.dump(teamstats, f)
		with open('playerstats.pickle', 'wb') as f:
			pickle.dump(playerstats, f)
