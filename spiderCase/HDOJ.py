

# import requests
# from pyquery import PyQuery as pq
import re;
#
#
class problem(object):
    def __init__(self,id, title:str,ratio ,ac, sub):
        self.id = id
        self.title = title
        # self.ratio = float(ac)/sub
        self.ratio = ratio
        self.ac = ac
        self.sub = sub

    def show(self):
        print("%s %s %s"%(self.id,self.title,self.ratio))

    def __str__(self):
        return("%s||%s||%s||%s||%s\n" % (str(self.id).ljust(6),str(self.title.strip()).ljust(50),str(self.ratio).ljust(8),str(self.ac).ljust(8),str(self.sub).ljust(8)))



#
#
#
# html = "http://acm.hdu.edu.cn/listproblem.php?vol=2"
# response = requests.get(html)
# document = pq(response.text)
# table = document('table').eq(4)
# content = str(table)
# divs = content.split('p(')
# divs = divs[1:]
# res = list();
# count = 0
# for elem in divs:
#     elem = elem[:-2]
#     subelement = elem.split(',')
#     if count == 99:
#         subelement[-1] = subelement[-1].split(');')[0]
#         print("danger %s"%subelement[-1])
#     count += 1
#     print(count)
#     # obj = problem(subelement[1],subelement[3],subelement[4],subelement[5])
#     print(subelement)
#     obj = problem(subelement[1],subelement[3],int(subelement[-2]),int(subelement[-1]))
#     res.append(obj)
#
#     # print(subelement[1],subelement[3],(subelement[4]),(subelement[5]))
#
#
def sort_key(s:problem):
    return s.ratio
#
#
#
def sortList(res):
    res.sort(key = sort_key,reverse=True)


# tr = document('body > table > tbody > tr:nth-child(6) > td > table > tbody > tr:nth-child(3)')
# print(tr)

# with open('index2.html','w') as f:
#     f.write(response.text)
# with open('index2.html','w',encoding='utf-8') as f:
#     f.write(str(document))

# table = document('body > table > tbody > tr:nth-child(6) > td > table')

# print(table)

# with open("index.html",'w') as f:
#     f.write(response.text)


from selenium import webdriver
from pyquery import PyQuery as pq



def getPagenAndReturnRes(n):
    html = 'http://acm.hdu.edu.cn/listproblem.php?vol=%s'%n
    driver.get(html)
    document = pq(driver.page_source)
    res = list()

    table = document("body > table > tbody > tr:nth-child(6) > td > table > tbody")
    trs = table('tr')
    count = 0
    for tr in trs.items():
        count += 1
        if count == 1:
            continue
        info = tr('td') # there are three element
        id = info.eq(0).text()
        title = info.eq(1).text()
        # for i in range(2):
        #     print(info.eq(i).text(),end=" ")
        ratio = float(re.search('(.*)%', info.eq(2).text()).group(1))
        ac = int(re.search('\(([0-9]+)/([0-9]+)\)', info.eq(2).text()).group(1))
        submit = int(re.search('\(([0-9]+)/([0-9]+)\)', info.eq(2).text()).group(2))

        obj = problem(id,title,ratio,ac,submit)
        # obj.show()
        res.append(obj)

    return res

def start():
    res = list()
    for i in range(1,60):
        print("getting page %s"%(i))
        res.extend(getPagenAndReturnRes(i))

    res.sort(key=sort_key,reverse=True)

    with open('res.txt','w',encoding='utf-8')as f:
        for obj in res:
            f.write(str(obj))
    print("finished")
driver = webdriver.Chrome()
start()
driver.close()

