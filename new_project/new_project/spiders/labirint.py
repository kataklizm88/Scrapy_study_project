import scrapy
from scrapy.http import HtmlResponse
from new_project.items import NewProjectItem


URL_FOR_SEARCH = 'https://www.labirint.ru/search/?'
URL_MAIN = 'https://www.labirint.ru'


class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = ['https://www.labirint.ru/search/?'
                  'discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1&page=1']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//div[@class='pagination-next']/a/@href").get()
        if next_page:
            yield response.follow(URL_FOR_SEARCH + next_page, callback=self.parse)
        book_links = response.xpath("//a[@class='product-title-link']/@href").getall()
        for link in book_links:
            yield response.follow(URL_MAIN + link, callback=self.parse_page)

    def parse_page(self, response: HtmlResponse):
        rating = response.xpath("//div[@id = 'rate']/text()").get()
        book_name = response.xpath("//div[@id = 'product-info']/@data-name").get()
        full_price = response.xpath("//div[@id = 'product-info']/@data-price").get()
        discount_price = response.xpath("//div[@id = 'product-info']/@data-discount-price").get()
        author = response.xpath("//a[@data-event-label]/text()").get()
        book_link = response.url
        yield NewProjectItem(
            book_name=book_name,
            author=author,
            rating=rating,
            full_price=full_price,
            discount_price=discount_price,
            book_link=book_link
        )
