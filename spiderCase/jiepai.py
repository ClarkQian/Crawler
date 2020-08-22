import json
import re
import time
import requests

# res = json.load(
#     "{\"count\":12,\"sub_images\":[],\"max_img_width\":1024,\"labels\":[],\"sub_abstracts\":[\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\"],\"sub_titles\":[\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\",\"\\u8857\\u62cd\\uff1a\\u8f7b\\u677e\\u51fa\\u884c\\uff0c\\u4e0d\\u5931\\u65f6\\u5c1a\"]}"),
# print(res)

def before():
    '''
    gallery: JSON.parse(
    '''

    part1Pattern = re.compile('gallery:(.*)')
    a = ''
    #get the page
    with open('./html/index.html','r',encoding='utf-8') as f:
        for line in f:
            tmpRes = part1Pattern.search(line)
            if tmpRes is not None:
                a = tmpRes.group(0)
                print(a)
                break




    # a = '''
    # {\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fed996c66b836497d983c05d9119918ea?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fed996c66b836497d983c05d9119918ea?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fed996c66b836497d983c05d9119918ea?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fed996c66b836497d983c05d9119918ea?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002Fed996c66b836497d983c05d9119918ea\",\"height\":1667},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F 665fd7bec483492d828a9fb016206c18?from=pc\",\"width\":673,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F665fd7bec483492d828a9fb016206c18?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F665fd7bec483492d828a9fb016206c18?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F665fd7bec483492d828a9fb016206c18?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F665fd7bec483492d828a9fb016206c18\",\"height\":1200},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F4f940733512b490f8030f9e86bd71910?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F4f940733512b490f8030f9e86bd71910?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F4f940733512b490f8030f9e86bd71910?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F4f940733512b490f8030f9e86bd71910?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F4f940733512b490f8030f9e86bd71910\",\"height\":1838},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F3f3432629e9d41efa9a4ac818a9c8612?from=pc\",\"width\":689,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F3f3432629e9d41efa9a4ac818a9c8612?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F3f3432629e9d41efa9a4ac818a9c8612?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F3f3432629e9d41efa9a4ac818a9c8612?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F3f3432629e9d41efa9a4ac818a9c8612\",\"height\":1200},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6af962c27d2e4633b5e10b6169ad7171?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6af962c27d2e4633b5e10b6169ad7171?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6af962c27d2e4633b5e10b6169ad7171?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6af962c27d2e4633b5e10b6169ad7171?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F6af962c27d2e4633b5e10b6169ad7171\",\"height\":1641},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F1868173fd57043f6bc7c101686bf94de?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F1868173fd57043f6bc7c101686bf94de?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F1868173fd57043f6bc7c101686bf94de?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F1868173fd57043f6bc7c101686bf94de?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F1868173fd57043f6bc7c101686bf94de\",\"height\":1637},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fdf7f78260c7346b2b9f00050e8ba6e26?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fdf7f78260c7346b2b9f00050e8ba6e26?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fdf7f78260c7346b2b9f00050e8ba6e26?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fdf7f78260c7346b2b9f00050e8ba6e26?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002Fdf7f78260c7346b2b9f00050e8ba6e26\",\"height\":1696},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fe486550ae70642758c70b86fb1e00ff0?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fe486550ae70642758c70b86fb1e00ff0?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fe486550ae70642758c70b86fb1e00ff0?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Fe486550ae70642758c70b86fb1e00ff0?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002Fe486550ae70642758c70b86fb1e00ff0\",\"height\":1658},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F8411b47881fb4eababc73e749d41a678?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F8411b47881fb4eababc73e749d41a678?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F8411b47881fb4eababc73e749d41a678?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F8411b47881fb4eababc73e749d41a678?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F8411b47881fb4eababc73e749d41a678\",\"height\":1721},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F39b4cec1ea094ee8afee994526b59392?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F39b4cec1ea094ee8afee994526b59392?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F39b4cec1ea094ee8afee994526b59392?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F39b4cec1ea094ee8afee994526b59392?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F39b4cec1ea094ee8afee994526b59392\",\"height\":1640},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Ff9c7f4cca733459cbd59eafe2272b15e?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Ff9c7f4cca733459cbd59eafe2272b15e?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Ff9c7f4cca733459cbd59eafe2272b15e?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp1-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002Ff9c7f4cca733459cbd59eafe2272b15e?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002Ff9c7f4cca733459cbd59eafe2272b15e\",\"height\":1661},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6add5345fc7a4f7c9ec139b3056ebf89?from=pc\",\"width\":1024,\"url_list\":[{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6add5345fc7a4f7c9ec139b3056ebf89?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp6-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6add5345fc7a4f7c9ec139b3056ebf89?from=pc\"},{\"url\":\"https:\\\u002F\\\u002Fp3-tt.byteimg.com\\\u002Forigin\\\u002Fpgc-image\\\u002F6add5345fc7a4f7c9ec139b3056ebf89?from=pc\"}],\"uri\":\"origin\\\u002Fpgc-image\\\u002F6add5345fc7a4f7c9ec139b3056ebf89\",\"height\":1663}
    # '''
    urlHead = 'https://p3-tt.byteimg.com/'
    a = a.replace(r'\\u002F','')
    a = a.replace(':\\',':')
    a = a.replace(' ','')
    a = a.replace('\\"uri\\','"uri')
    # a = a.replace('\\"url\\"','"url"')
    print(a)
    # # list = a.split(',')
    # # a  = dict()
    # # for item in list:
    # #     item = item.replace('{','')
    # #     item = item.replace('}', '')
    # #     print(item)
    pattern =  re.compile('\\"uri\\":"(.*?)\\"')
    resList = list()
    for elem in pattern.findall(a):
        elem = str(elem)
        imgUri = urlHead+elem.replace('\\','/')[0:-1]
        resList.append(imgUri)


    #write down
    for file in resList:
        with open('./img/%s.jpg'%time.time(),'wb') as f:
            f.write(requests.get(file).content)


#get the mother page
import requests
a = {
'aid': 24,
'app_name': 'web_search',
'offset': 0,
'format': 'json',
'keyword': '街拍',
'autoload': 'true',
'count': 20,
'en_qc': 1,
'cur_tab': 1,
'from': 'search_tab',
'pd': 'synthesis'
}

from urllib.parse import urlencode


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
response = requests.get('https://www.toutiao.com/api/search/content/?', urlencode(a),headers = header)
data = json.loads(response.text)

for element in data['data']:
    if 'article_url' in element:
        if re.match('.*?toutiao.*?',element['article_url']):
            print(element['article_url'])

