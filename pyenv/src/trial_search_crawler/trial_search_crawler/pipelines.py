# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import os
from trial_search_crawler.utils.wrapper import Wrapper


class TrialSearchCrawlerPipeline:

    has_no_exception = True

    def open_spider(self, spider):
        if os.environ.get("SCRAPY_CHECK") != "true":
            self.connection = mysql.connector.connect(
                user=os.environ['USER'], password=os.environ['PASS'], 
                host=os.environ['HOST'], port=os.environ['PORT'], 
                database=os.environ['DB'])
            print("DB connected")
            self.cursor = self.connection.cursor()
            self.extractor = Wrapper(self.cursor)
            self.extractor.create_table("t_basic")
            self.extractor.create_table("t_summary")
            self.extractor.create_table("t_qualification")
            self.extractor.create_table("t_researcher")
            self.extractor.create_table("t_inquiry")
            self.extractor.create_table("t_committee")
            self.extractor.create_table("t_cancel")
            self.extractor.create_table("t_end")
            self.extractor.create_table("t_ipd")
    
    def process_item(self, item, spider):
        if os.environ.get("SCRAPY_CHECK") != "true":
            adapter = ItemAdapter(item)
            jrct_dict = self.extractor.preprocess(adapter)
            self.extractor.insert_record("t_basic", jrct_dict)
            self.extractor.insert_record("t_summary", jrct_dict)
            self.extractor.insert_record("t_qualification", jrct_dict)
            self.extractor.insert_record("t_researcher", jrct_dict)
            self.extractor.insert_record("t_inquiry", jrct_dict)
            self.extractor.insert_record("t_committee", jrct_dict)
            self.extractor.insert_record("t_cancel", jrct_dict)
            self.extractor.insert_record("t_end", jrct_dict)
            self.extractor.insert_record("t_ipd", jrct_dict)
            if self.extractor.no_exception == False:
                self.has_no_exception = False
                spider.logger.info("Exception occurred for jrctid: %s. The detail is %s" % (adapter["jrctid"], self.extractor.e))
                self.extractor.no_exception = True
        return item
    
    def close_spider(self, spider):
        if os.environ.get("SCRAPY_CHECK") != "true":
            if self.has_no_exception == False:
                self.connection.rollback()
            self.connection.commit()
            self.connection.close()
