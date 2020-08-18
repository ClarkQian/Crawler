import requests
import time
from pyquery import PyQuery as pq
from selenium import webdriver
import requests
import datetime
import re
import os
import requests.exceptions
from selenium.common.exceptions import InvalidSessionIdException

#user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36

class loveGetImage(object):
    def __init__(self,baseUrl, imgPattern, dirDstByImg, kw, waitTime=3,n=4):
        self.url = baseUrl
        self.pattern = imgPattern
        self.dirDst = dirDstByImg
        self.kw = kw
        self.waitTime = waitTime
        self.driver = webdriver.Chrome()
        self.n = n
    def setKw(self,kw):
        self.kw = kw

    def start(self):
        self.driver.get(self.url)
        self.getSearchPage(self.kw)
        self.scrollToLoadPage(self.n)
        res = self.getActors()
        self.writeDown(res)
        self.delete()
    # def initialization(self,url,imgPattern):
    #     driver = webdriver.Chrome()
    #     
    #     pattern = '.*?(https.*?.jpg)".*?'
    #     dir_dst = './img'
    #     driver.get(url)
    #     # getAllImg(driver, url,pattern,dir_dst)
    #     return driver,url,pattern,dir_dst

    def scrollToLoadPage(self, n):
        print('finishing scroll loading in %s s'%(n*self.waitTime))
        for i in range(n):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight*%s/%s)'%(i,n))
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
            url = "https://cn.pornhub.com%s"%(actor.attr('href'))
            name = actor.find('.title-album').text()
            res[name] = url

        return res


    def getAllImg(self,url,dir_dst):
        self.driver.get(url)
        self.scrollToLoadPage(self.n)

        #hold on to load all the page content
        document = pq(self.driver.page_source)
        imgPattern = re.compile(self.pattern)
        items = document.find('.js_lazy_bkg.photoAlbumListBlock')
        for item in items.items():
            content = item.attr("style")
            if content is None:
                continue

            patternRes = imgPattern.findall(content);
            if patternRes is not None:
                src = patternRes[0]
                print(src)
                if not os.path.exists(dir_dst):
                    os.makedirs(dir_dst)
                try:
                    with open('%s/%s.jpg'%(dir_dst,str(datetime.datetime.now().timestamp()).replace('.','_')),'wb') as f:
                        f.write(requests.get(src).content)
                except requests.exceptions.ProxyError :
                    print('Proxy Error')
                    continue

    def delete(self):
        self.driver.close()

    def writeDown(self, listToWrite):
        for name, url in listToWrite.items():
            # pattern = '.*?(https.*?.jpg)".*?'
            name = name.replace('?','6')
            name = name.replace(':','k')
            print('downloading album named in \' %s  \' '%name)
            self.getAllImg(url,'%s/%s'%(self.dirDst,name))

    def getDriver(self):
        return self.driver
if __name__ == '__main__':
    try:
        pattern = '.*?(https.*?.jpg)".*?'
        dir_dst = './img'
        kw = 'cute'
        solve = loveGetImage(url,pattern,dir_dst,kw,4,n=5)
        solve.start()
        print('finished!')
    finally:
        try:
            solve.delete()
        except InvalidSessionIdException:
            print('session id problem')
