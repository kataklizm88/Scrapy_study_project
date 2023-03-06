import scrapy


class NewProjectItem(scrapy.Item):
    _id = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    full_price = scrapy.Field()
    discount_price = scrapy.Field()
    book_link = scrapy.Field()
