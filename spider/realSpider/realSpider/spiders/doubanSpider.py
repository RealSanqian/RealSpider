#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from ..items import DoubanItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class DoubanSpider(CrawlSpider) :

    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/top250"]
    rules = (
        #将所有符合正则表达式的url加入到抓取列表中
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/top250\?start=\d+&filter=&type=',))),
        #将所有符合正则表达式的url请求后下载网页代码, 形成response后调用自定义回调函数
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/subject/\d+', )), callback = 'parse_page', follow = True),
        )
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "zh,zh-TW;q=0.8,en;q=0.6,en-US;q=0.4,zh-CN;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
        "Referer": "http://www.zhihu.com/"
    }

    def parse_page(self, response) :
        sel = Selector(response)
        item = DoubanItem()
        item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        item['description'] = sel.xpath('//div/span[@property="v:summary"]/text()').extract()
        item['url'] = response.url
        print item.name
        return item