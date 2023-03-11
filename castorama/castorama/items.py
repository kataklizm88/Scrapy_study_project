import scrapy
from itemloaders.processors import TakeFirst, Compose


def clean_name(value: list):
    try:
        value = value[0].replace('\n', '').replace('  ', '')
    except:
        return value
    return value


class CastoramaItem(scrapy.Item):
    name = scrapy.Field(input_processor=Compose(clean_name), output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field()
    product_link = scrapy.Field()
