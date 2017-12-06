from multiprocessing import Pool
from ganji_information import get_link_from,get_item_info,url_list,item_info,links
from list_ganji import channel_list
#取得第一页链接
import time


def get_all_links(channel):
    for i in range(1,100):
        try:

            get_link_from(channel,i)
        except Exception:
            continue




if __name__ == '__main__':
    for url in url_list.find():
        try:
            get_item_info(url['url'])
        except Exception:
            continue


    #
    pool = Pool(processes=6)
    pool.map(get_all_links,channel_list)
    pool.close()
    pool.join()








