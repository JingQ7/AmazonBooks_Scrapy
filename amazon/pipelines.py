# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class AmazonPipeline(object):

    def process_item(self, item, spider):
        db = pymysql.connect(host = 'localhost', user = 'root',
                             password = 'root', database = 'amazon')
        cursor = db.cursor()
        #cursor.execute('DROP TABLE IF EXISTS books')
        #cursor.execute('create table books (name varchar(200), '
        #               'author varchar(100), price varchar(50), link varchar(200))')
        for i in range(0, len(item['books_name'])):
            books_name = item['books_name'][i]
            author = item['author'][i]
            price = item['price'][i]
            books_link = item['books_link'][i]
            try:
                sql = 'insert into books(name, author, price, link) ' \
                  'values("'+books_name+'","'+author+'", "'+price+'", "'+books_link+'")'
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print('Error:' + str(e))
                db.rollback()

        db.close()
        return item
