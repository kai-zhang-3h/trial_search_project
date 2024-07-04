import scrapy 
import json
from trial_search_crawler.items import TrialSearchCrawlerItem
from trial_search_crawler.utils.wrapper import Wrapper

class JrctSpider(scrapy.Spider):
    name = "jrct"

    # The initial page for scraping
    start_urls = ["https://rctportal.niph.go.jp/s/result?t=chiken&l=10&s=0&crc%5B0%5D=clinical_research&crc%5B1%5D=chiken&date%5Bdate_item%5D%5B0%5D=none&date%5Bstart_date%5D%5B0%5D=&date%5Bend_date%5D%5B0%5D=&other%5Bother_item%5D%5B0%5D=none&other%5Bkeyword%5D%5B0%5D=&other%5Bnegative_keyword%5D%5B0%5D="]

    def parse(self, response):

        """
        This function parses a sample response. Some contracts are mingled
        with this docstring.

        @url https://rctportal.niph.go.jp/s/result?age%5Bage_gt%5D=&age%5Bage_lt%5D=&age%5Bage_range%5D=&date%5Bdate_item%5D%5B%5D=none&date%5Bstart_date%5D%5B%5D=&date%5Bend_date%5D%5B%5D=&crc%5B%5D=clinical_research&crc%5B%5D=chiken&q=&t=chiken&other%5Bother_item%5D%5B%5D=none&other%5Bkeyword%5D%5B%5D=&other%5Bnegative_keyword%5D%5B%5D=&submit=%E5%86%8D%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B
        @returns items 0
        @returns requests 11
        """

        # Get all the jrct id in the current page
        jsonRaw = response.css("input::attr(value)")[-5].get()
        urllist = list(map(lambda x:x['url'], json.loads(jsonRaw)))
        
        # Parse the detailed page with jrct ids above
        yield from response.follow_all(urllist, self.parse_item)

        # Get the link of next page
        pagination_link = response.css("ul.pageNav a::attr(href)")[-1].get()

        # Parse the next page until there are no more pages
        if response.css("ul.pageNav a::text")[-1].get() != "次 »":
            yield None
        
        else:
            yield response.follow(pagination_link, self.parse)   

    def parse_item(self, response):

        """
        This function parses the detail of a sample response. Some contracts are mingled
        with this docstring.

        @url https://rctportal.niph.go.jp/s/detail/um?trial_id=jRCTs052230073
        @returns items 1
        @returns requests 0
        @scrapes jrctid t_basic t_summary t_qualification t_researcher t_inquiry t_committee t_cancel t_end t_ipd        """
        
        item = TrialSearchCrawlerItem()
       
        item["jrctid"] = Wrapper.extract_id(response)

        item["t_basic"] = Wrapper.extract_table(response, "t_basic")

        item["t_summary"] = Wrapper.extract_table(response, "t_summary")

        item["t_qualification"] = Wrapper.extract_table(response, "t_qualification")

        item["t_researcher"] = Wrapper.extract_table(response, "t_researcher")

        item["t_inquiry"] = Wrapper.extract_table(response, "t_inquiry")

        item["t_committee"] = Wrapper.extract_table(response, "t_committee")

        item["t_cancel"] = Wrapper.extract_table(response, "t_cancel")

        item["t_end"] = Wrapper.extract_table(response, "t_end")

        item["t_ipd"] = Wrapper.extract_table(response, "t_ipd")
        
        yield item