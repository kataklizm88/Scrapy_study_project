import scrapy


class MyProjectItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
