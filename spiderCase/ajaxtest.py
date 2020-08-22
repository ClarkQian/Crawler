

from pyquery import PyQuery as pq

# document = pq(url = 'https://www.baidu.com/',encoding='utf-8')
# with open('./html/index.html','w',encoding='utf-8') as f:
#     f.write(document.html())
import requests

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    #User-Agent = Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
    # 'Referer': 'http://top.baidu.com/'
}
response = requests.get('https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',headers = header)
response.encoding = response.apparent_encoding
print(response.text)


# from selenium import webdriver
# import time
# options = webdriver.ChromeOptions()
# options.add_argument('User-Agent = Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
# driver = webdriver.Chrome(options = options)
# driver.get('https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D')
# time.sleep(3)
# driver.execute_script('window.scrollTo(0,document.body.clientHeight)')
#
#
# content = driver.page_source
# from pyquery import PyQuery as pq
# document = pq(content)
# for img in document.find('img').items():
#     print(img)
#
#
