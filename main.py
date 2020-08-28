from random import choice
from string import digits
from requests import get
from time import sleep

def get_images(pageno,count):
    base_filepath = '/Users/wenjun/Pictures/meizhi/'
    base_url = ' http://wp.birdpaper.cn/intf/GetListByHotTag?tag=%E6%B8%85%E7%BA%AF&pageno={}&count={}'.format(pageno,count)
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
        }
        response = get(img,headers=headers,timeout=60)
        name = "".join(map(lambda x:choice(digits), range(20)))
        path = base_filepath+name+".jpg"
        with open(path,"wb") as f:
            f.write(response.content)
if __name__ == '__main__':

    for i in range(1, 200):
        print("===== 开始下载第{}页 =====".format(i))
        get_images(i, 10)
        sleep(10)

