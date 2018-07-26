import requests
import sys
"""
访问任意的贴吧的指定页数并保存到本地,使用面向对象的思维
"""

# 实现翻页的功能： 通过url的pn参数


class Tieba(object):
    def __init__(self, kw, pn):
        self.kw = kw
        self.pn = int(pn)
        self.url_list = ['https://tieba.baidu.com/f?kw={}&pn={}'.format(kw, 50*i) for i in range(pn)]
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

    def request(self, url):
        resp = requests.get(url, headers=self.headers)
        return resp.content

    def save(self, data, page):
        with open(self.kw+str(page)+'.html', 'wb') as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            response = self.request(url)
            self.save(response,self.url_list.index(url)+1)



if __name__ == '__main__':
    kw = sys.argv[1]
    pn = sys.argv[2]
    tieba = Tieba(kw, int(pn))
    tieba.run()




