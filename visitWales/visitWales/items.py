
from scrapy.item import Item, Field

class Activity(Item):
    name = Field()
    addr = Field()
    site = Field()
    tel = Field()
    desc = Field()
    catid = Field()
    catname = Field()