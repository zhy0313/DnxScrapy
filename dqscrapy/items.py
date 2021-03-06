# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class DqscrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QsbkItem(Item):
    desc = Field()
    nick = Field()
    avatarUrl = Field()
    qiniuUrl = Field()

class NewQsbkItem(Item):
    header = Field()
    author = Field()
    content = Field()
    thumb = Field()
    created_at = Field()
