# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule

class LyricsSpiderWY(CrawlSpider):
    #爬取网易云音乐歌词爬虫
    name = "LSpiderWY"
    # 减慢爬取速度 为1s
    download_delay = 2

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)