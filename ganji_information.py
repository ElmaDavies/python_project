import requests
from bs4 import BeautifulSoup
import pymongo
import random

from getProxy import get_ips
client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji_data']
url_list = ganji['url_list']
item_info = ganji['item_info']
#获取请求头信息
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Connection":"keep-alive"

}
def proxys():
	url = "http://www.xicidaili.com/"

	ips_list = get_ips(url)
	proxy_ip = random.choice(ips_list)
	if proxy_ip.startswith('http'):
		proxies = {'http':proxy_ip}
	elif proxy_ip.startswith('https'):
		proxies = {'https':proxy_ip}
	return proxies






links = []
def get_link_from(channel,pages):
	#http://lz.ganji.com//o3/

	pages_url = '{}o{}/'.format(channel,str(pages))
	wb_data = requests.get(url=pages_url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')



	for link in soup.select('td.t > a'):

			item_link = link.get('href').split('?')[0]

			url_list.insert_one({'url':item_link})
			links.append(item_link)


	return links










def get_item_info(url):
	info_data = requests.get(url,headers=headers,proxies=proxys())
	if info_data.status_code == 404:

		pass

	elif url.endswith(".shtml"):

		##wrapper > div.content.clearfix > div.leftBox > div:nth-child(2) > div > ul > li:nth-child(1) > i
		# wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1
		soup = BeautifulSoup(info_data.text, 'lxml')

		data = {
				'title': soup.select('body > div.content > div > div.box_left > div.info_lubotu > div.box_left_top > h1')[
					0].text,
				'price': soup.select(
					'body > div.content > div > div.box_left > div.info_lubotu > div.info_massege > div.price_li > span > i')[
					0].text.strip(),
				'area': soup.select(
					'body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')[
					0].text.strip(),
				'detail': soup.select(
					'body > div.content > div > div.box_left > div.info_baby > div.baby_talk > div.baby_kuang > p')[
					0].text.strip('\n')

			}



		item_info.insert_one(data)
	else:
		pass









