from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Connection': 'keep-alive'
}

cap = DesiredCapabilities.PHANTOMJS.copy()  # 使用copy()防止修改原代码定义dict

for key, value in headers.items():
    cap['phantomjs.page.customHeaders.{}'.format(
        key)] = value
driver = webdriver.PhantomJS(desired_capabilities=cap,service_args=['--ssl-protocol=any'])

driver.set_window_position(1400,900)
