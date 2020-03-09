# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from datetime import datetime
import mysql.connector
import random

class FbcrawlPipeline(object):
    def open_spider (self,spider):
        self.cnx = mysql.connector.connect(user = 'root',password = 'Htpftsat2015@gmail.com',
                                     host='127.0.0.1',
                                     database = 'Test')
        self.cursor = self.cnx.cursor()


    def process_item(self, item, spider):
        s = 'INSERT INTO post5 (Post_id) VALUES ({})'.format(
            item.get('post_id'))
        print(s)
        val = "INSERT INTO post (Post_id,fb_source,shared_for,post_datetime,post_text,url)values(%s, %s,%s, %s, %s, %s)"
        value = (item.get('post_id'),str(item.get('source')[0]),item.get('shared_from'),item.get('date')[0],item.get('text'),item.get('url'),)
        # re_val = ""
        # self.cursor.execute(s)
        self.cursor.execute(val,value)
        print("<><><><><><><><><><><><><><><port3")
        print(item.get('post_id'))
        print(str(item.get('source')[0]))
        print(item.get('shared_from'))
        print(item.get('date')[0])
        print(item.get('text'))
        print(item.get('url'))
        print("<><><><><><><><><><><><><><><")
        self.cnx.commit()
        return item

    def close_spider (self,spider):
        self.cursor.close()
        self.cnx.close()
