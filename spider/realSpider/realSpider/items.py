#coding=utf-8

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class RealspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    url = scrapy.Field()

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  #电影名称
    description = scrapy.Field()  #电影描述
    url = scrapy.Field()  #抓取的url

class NewsItem(scrapy.Item):
    name = scrapy.Field() #网站名称
    title = scrapy.Field() #新闻标题
    detail = scrapy.Field() #文章内容
    url = scrapy.Field() #网站地址
    link = scrapy.Field() #爬虫爬取地址
    time = scrapy.Field() #爬虫爬取时间
    vn = scrapy.Field() #爬虫爬取次数

