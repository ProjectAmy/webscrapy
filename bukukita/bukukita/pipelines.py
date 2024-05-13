# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import mysql.connector
from itemadapter import ItemAdapter
from scrapy.exceptions import NotConfigured
# import sqlite3

class BukukitaPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.conn = sqlite3.connect("furbhin.db")
        # self.curr = self.conn.cursor()

        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='bhinneka'
            )
            self.curr = self.conn.cursor()
        except mysql.connector.Error as err:
            raise NotConfigured(f'error connecting to mysql : {err}')

    def create_table(self):
        # self.curr.execute("""DROP TABLE IF EXISTS furnitur""")
        # self.curr.execute("""CREATE TABLE furnitur (
        #                         nama_product TEXT,
        #                         harga TEXT,
        #                         cicilan TEXT
        #                     )""")

        try:
            self.curr.execute("""CREATE TABLE IF NOT EXISTS data_bhinneka (
                                    nama_product TEXT,
                                    harga INT,
                                    cicilan TEXT
                                    )""")
        except mysql.connector.Error as err:
            raise NotConfigured(f'error creating table : {err}')

    def process_item(self, item, spider):
        # self.store_db(item)
        # print('pipeline : ') + item['judul']
        try:
            self.store_db(item)
            print('pipeline : ' + item['nama_product'])
        except mysql.connector.Error as err:
            spider.log(f'error storing item in database : {err}')
        return item

    def store_db(self, item):
        # self.curr.execute("""
        #     INSERT INTO furnitur (nama_porduct, harga, cicilan)
        #     VALUES (?, ?, ?)
        #     """, (item['nama_product'], item['harga'], item['cicilan']))
        #
        # self.conn.commit()

        self.curr.execute("""
            INSERT INTO data_bhinneka (nama_product, harga, cicilan)
            VALUES (%s, %s, %s)
        """, (item['nama_product'], item['harga'], item['cicilan']))
        self.conn.commit()

    def close_spider(self, spider):
        try:
            self.conn.close()
        except mysql.connector.Error as err:
            spider.log(f'error closing spider : {err}')