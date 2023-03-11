import scrapy
from scrapy.http import HtmlResponse
from castorama.items import CastoramaItem
from scrapy.loader import ItemLoader


URL = 'https://www.castorama.ru'


"""
Парсим сайт магазина Касторама, для работы выбран раздел "Дача и сад/Почтовые ящики"
"""


class CastoRuSpider(scrapy.Spider):
    name = "casto_ru"
    allowed_domains = ["castorama.ru"]
    start_urls = ['https://www.castorama.ru/gardening-and-outdoor/pochtovye-jaschiki/']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(URL + next_page, callback=self.parse)
        product_links = response.xpath("//a[@class='product-card__img-link']/@href").getall()
        for link in product_links:
            yield response.follow(URL + link, callback=self.parse_page)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photo', "//ul[@class='swiper-wrapper']/li[1]/span/@content")
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_value('product_link', response.url)
        yield loader.load_item()
