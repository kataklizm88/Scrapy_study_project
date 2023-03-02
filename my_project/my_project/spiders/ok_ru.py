import scrapy
from scrapy.http import HtmlResponse
from my_project.items import MyProjectItem


"""
Парсинг сайта Гипермаркета "Ок", раздела со скидками
На всех предложенные по заданию сайта - сразу банят
"""


def get_real_data(arg: list):
    res = []
    for i in arg:
        try:
            res.append(int(i))
        except ValueError:
            pass
    return res[0]


class OkRuSpider(scrapy.Spider):
    name = "ok_ru"
    allowed_domains = ["ok.ru"]
    start_urls = ["http://www.okmarket.ru/customers/actions_types/"]

    def parse(self, response: HtmlResponse):
        products = response.xpath("//div[@class = 'ass-prod-card ']")
        for product in products:
            product_name = product.xpath(".//div[2]/div[2]/a/text()").get()
            product_price = get_real_data(product.xpath(".//div[@class='ass-prod-card__prices-base']/text()").getall())
            product_discount = get_real_data(product.xpath(".//div[1]/div/text()").getall())

            yield MyProjectItem(
                name=product_name,
                price=f'{product_price} рублей',
                discount=f'{product_discount} процентов',
            )
