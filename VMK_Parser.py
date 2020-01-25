import requests
from bs4 import BeautifulSoup as bs


html_code = requests.get('https://store.steampowered.com/search/?specials=1&page=1').text


soup = bs(html_code, 'lxml')

print(soup.find('a', {'class':'search_result_row ds_collapse_flag  app_impression_tracked', 'data-search-page':'1'}))

'''
for one_game in soup.find_all(''):
	print(one_game)
	print(one_game.get('href'))
	print(one_game.find('span', {'class':'title'}).text)
	print(one_game.find('div', {'class':'col search_released responsive_secondrow'}).text)
'''


#print(soup.find('span', {'class':'title'}).text)


