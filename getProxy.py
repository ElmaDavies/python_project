import requests
from bs4 import BeautifulSoup
import time
headers = {

    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/62.0.3202.94 Safari/537.36",
    "Connection":"keep-alive"

}

def get_ips(url):
    ips_data = requests.get(url,headers=headers)
    soup_ips = BeautifulSoup(ips_data.text,'lxml')
    time.sleep(1000)
    ips = soup_ips.select('table#ip_list > tr > td')

    i = 1
    j = 2
    k = 5
    ips_list = []
    data = {}
    while(i < len(ips)):
        if ips[i]:
            data['ip'] = ips[i].text
        if ips[j]:
            data['port'] = ips[j].text
        if ips[k].text is not 'sock4/5':

            data['http_info'] = ips[k].text


        i = i + 8
        j = j + 8
        k = k + 8
        if data['http_info'] != 'socks4/5':

           ips_list.append(data['http_info'].lower()+"://"+data['ip']+":"+data['port'])
    return ips_list

