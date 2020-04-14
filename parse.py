import pickle
import pandas as pd
from bs4 import BeautifulSoup

TEAMFILE = 'teamstats.pickle'
PLAYERFILE = 'playerstats.pickle'

def parse_teamstats(soup):
	thead = soup.find('thead')
	titles = [title.text for title in thead.findChildren('th')]
	titles[1] = titles[1][:2]
	tbody = soup.find('tbody')
	trs = tbody.find_all('tr')
	data = []
	for tr in trs:
		team_data = [td.text for td in tr.find_all('td')]
		data.append(team_data)
	return pd.DataFrame(data, columns=titles)

def parse_playerstats(soups):
	thead = soups[0].find('thead')
	titles = [title.text for title in thead.findChildren('th')]
	titles[1] = titles[1][:2]
	titles[2] = titles[2][:2]

	data = []
	for soup in soups:
		tbody = soup.find('tbody')
		trs = tbody.find_all('tr')
		for tr in trs:
			player_data = [td.text for td in tr.find_all('td')]
			data.append(player_data)
	return pd.DataFrame(data, columns=titles)

with open(TEAMFILE, 'rb') as f:
	teamstats = pickle.load(f)

assault_soup = BeautifulSoup(teamstats[0], 'lxml')
resource_soup = BeautifulSoup(teamstats[1], 'lxml')
assault_df = parse_teamstats(assault_soup)
resource_df = parse_teamstats(resource_soup)
assault_df.to_csv('team_assault.csv')
resource_df.to_csv('team_resource.csv')

with open(PLAYERFILE, 'rb') as f:
	playerstats = pickle.load(f)

kda_soups = [BeautifulSoup(_, 'lxml') for _ in playerstats[0]]
power_soups = [BeautifulSoup(_, 'lxml') for _ in playerstats[1]]
kda_df = parse_playerstats(kda_soups)
power_df = parse_playerstats(power_soups)
kda_df.to_csv('player_kda.csv')
power_df.to_csv('player_power.csv')
