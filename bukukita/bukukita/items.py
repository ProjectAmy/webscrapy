# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BukukitaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # ini untuk spider yang linkbuku

    # source = scrapy.Field()
    # judul = scrapy.Field()
    # penulis = scrapy.Field()
    # penerbit = scrapy.Field()

    # ini untuk yang bhinneka

    nama_product = scrapy.Field()
    harga = scrapy.Field()
    cicilan = scrapy.Field()