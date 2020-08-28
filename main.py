#-*-coding:utf-8-*-

from random import choice
from string import digits
from urllib.parse import quote_plus
from requests import get
from time import sleep
from os.path import exists
from os import mkdir

def get_images(tag,pageno,count):
    base_filepath = 'C:/wallpaper/{}/'.format(tag)
    if exists(base_filepath):
        pass
    else:
        mkdir(base_filepath)
    base_url = 'http://wp.birdpaper.cn/intf/GetListByHotTag?tag={}&pageno={}&count={}'.format(quote_plus(tag), pageno, count)
    headers = {
      'Host': 'wp.birdpaper.cn',
      'Proxy-Connection': 'keep-alive',
      'Accept': 'application/json, text/plain, */*',
      'Origin': 'http://front.birdpaper.cn',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'en-US,en;q=0.8'
    }
    response = get(base_url,headers=headers,timeout=60)
    url_list = []
    if response.status_code == 200:
        json_info = response.json()
        data = json_info["data"]["list"]
        for id in data:
            url = id["url"]
            url_list.append(url)
    for img in url_list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
        }
        response = get(img,headers=headers,timeout=60)
        name = "".join(map(lambda x:choice(digits), range(20)))
        path = base_filepath+name+".jpg"
        with open(path,"wb") as f:
            f.write(response.content)
if __name__ == '__main__':

    for i in range(1, 200):
        print("===== 开始下载第{}页 =====".format(i))
        get_images(tag="清纯",pageno=i, count=10)
        sleep(60)

