import requests
import time
from pyquery import PyQuery as pq
from selenium import webdriver
import requests
import datetime
import re
import os
import requests.exceptions
from selenium.common.exceptions import InvalidSessionIdException, TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from multiprocessing import Pool



# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36


def processPageN(n):
    try:
        print('processing %s' % n)
        dt = pornGetImage(dir_dst, kw).startProcess(n)
        print('finishing processing %s' % n)
    except InvalidSessionIdException:
        print('session id problem')
    except NoSuchWindowException:
        print('screenshot: available via screen')


class pornGetImage(object):

    def __init__(self, dirDstByImg, kw, baseUrl='',
                 imgPattern='.*?(https.*?.jpg)".*?', waitTime=3, n=4):
        self.url = baseUrl
        self.pattern = imgPattern
        self.dirDst = dirDstByImg
        self.kw = kw
        self.waitTime = waitTime
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
        self.driver.set_window_position(1400, 900)
        self.n = n
        self.wait = WebDriverWait(self.driver, 10)

    def setKw(self, kw):
        self.kw = kw

    def startProcess(self, n):
        self.goNextPage(n)
        self.scrollToLoadPage(self.n)
        res = self.getActors()
        self.writeDown(res)
        self.delete()
        return self

    def start(self):
        self.driver.get(self.url)
        self.getSearchPage(self.kw)
        self.scrollToLoadPage(self.n)
        res = self.getActors()
        self.writeDown(res)
        for i in range(1, 40):
            self.goNextPage(i)
            print(self.getUrl())
            self.scrollToLoadPage(self.n)
            res = self.getActors()
            self.writeDown(res)
        self.delete()

    # def initialization(self,url,imgPattern):
    #     driver = webdriver.Chrome()
    #     url = 'https://cn.pornhub.com/albums/female-straight-uncategorized'
    #     pattern = '.*?(https.*?.jpg)".*?'
    #     dir_dst = './img'
    #     driver.get(url)
    #     # getAllImg(driver, url,pattern,dir_dst)
    #     return driver,url,pattern,dir_dst

    def scrollToLoadPage(self, n):
        print('finishing scroll loading in %s s' % (n * self.waitTime))
        for i in range(n):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight*%s/%s)' % (i, n))
            time.sleep(self.waitTime)

    def getSearchPage(self, kw):
        input = self.driver.find_element_by_id('searchInput')
        input.send_keys(kw)
        btn = self.driver.find_element_by_id('btnSearch')
        time.sleep(2)
        btn.click()
        time.sleep(5)

    def getActors(self):
        actors = pq(self.driver.page_source).find('.photoAlbumListContainer').find('.photoAlbumListBlock a')
        res = dict()
        for actor in actors.items():
            url = "https://cn.pornhub.com%s" % (actor.attr('href'))
            name = actor.find('.title-album').text()
            res[name] = url

        return res

    def getAllImg(self, url, dir_dst):
        self.driver.get(url)
        # self.scrollToLoadPage(self.n)
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'photoAlbumListContainer')))
        except TimeoutException:
            return self.getAllImg(url, dir_dst)

        # hold on to load all the page content
        document = pq(self.driver.page_source)
        imgPattern = re.compile(self.pattern)
        items = document.find('.js_lazy_bkg.photoAlbumListBlock')
        for item in items.items():
            src = item.attr("data-bkg")
            print(src)
            if not os.path.exists(dir_dst):
                os.makedirs(dir_dst)

            file_name = str(datetime.datetime.now().timestamp()).replace('.', '_')
            try:
                with open('%s/%s.jpg' % (dir_dst, file_name),
                          'wb') as f:
                    content = requests.get(src).content
                    f.write(content)
            except requests.exceptions.ProxyError:
                print('Proxy Error')
                os.remove('%s/%s.jpg' % (dir_dst, file_name))
                #retrying
                try:
                    with open('%s/%s.jpg' % (dir_dst, file_name),
                              'wb') as f:
                        content = requests.get(src).content
                        f.write(content)
                except requests.exceptions.ProxyError:
                    os.remove('%s/%s.jpg' % (dir_dst, file_name))
                    print('Proxy Error Again!')
                continue
            # patternRes = imgPattern.findall(content);
            # if patternRes is not None:
            #     src = patternRes[0]
            #     print(src)
            #     if not os.path.exists(dir_dst):
            #         os.makedirs(dir_dst)
            #     try:
            #         with open('%s/%s.jpg'%(dir_dst,str(datetime.datetime.now().timestamp()).replace('.','_')),'wb') as f:
            #             f.write(requests.get(src).content)
            #     except requests.exceptions.ProxyError :
            #         print('Proxy Error')
            #         continue

    def delete(self):
        self.driver.close()

    def writeDown(self, listToWrite):
        for name, url in listToWrite.items():
            # pattern = '.*?(https.*?.jpg)".*?'
            name = name.replace('?', '6')
            name = name.replace(':', 'k')
            name = name.replace('|', 'p')
            name = name.replace('<', 'h')
            name = name.replace('>', 'l')
            name = name.replace('*', 'l')
            name = name.replace('\\', 'l')
            name = name.replace('/', 'l')
            name = name.replace('\"', 'l')
            print('downloading album named in \' %s  \' ' % name)
            self.getAllImg(url, '%s/%s' % (self.dirDst, name))

    def goNextPage(self, n):
        # https: // cn.pornhub.com / albums / female - straight - uncategorized?search = cute & page = 2
        print('going to page %s' % (n))
        self.driver.get("https://cn.pornhub.com/albums/female-straight-uncategorized?search=%s&page=%s" % (self.kw, n))

    def getDriver(self):
        return self.driver

    def getUrl(self):
        return self.driver.current_url


if __name__ == '__main__':
    # try:
    #     url =
    #     pattern = '.*?(https.*?.jpg)".*?'
    #     dir_dst = './img/teen'
    #     kw = 'angel'
    #     solve = pornGetImage(dir_dst, kw)
    #     solve.start()
    #     print('finished!')
    # finally:
    #     try:
    #         solve.delete()
    #     except InvalidSessionIdException:
    #         print('session id problem')
    #     except NoSuchWindowException:
    #         print('screenshot: available via screen')
    pool = Pool(processes=6)
    pool.map(processPageN,[i for i in range(30)])
