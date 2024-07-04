# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrialSearchCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   
    jrctid = scrapy.Field()
    # table 0
    t_basic = scrapy.Field()
    #table 1
    t_summary = scrapy.Field()
    #table 2
    t_qualification = scrapy.Field()
    #table 3
    t_researcher = scrapy.Field()
    #table 4
    t_inquiry = scrapy.Field()
    #table 5
    t_committee = scrapy.Field()
    #table 6
    t_cancel = scrapy.Field()
    #table 7
    t_end = scrapy.Field()
    #table 8
    t_ipd = scrapy.Field()