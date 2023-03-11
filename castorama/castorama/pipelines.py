from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class PhotosPipeline(ImagesPipeline):

    @staticmethod
    def add_url(link):
        return 'https://www.castorama.ru' + link

    def get_media_requests(self, item, info):
        if item['photo']:
            if isinstance(item['photo'], str):
                try:
                    yield Request(PhotosPipeline.add_url(item['photo']))
                except Exception as e:
                    print(e)
            elif isinstance(item['photo'], list):
                for img in (item['photo']):
                    try:
                        yield Request(PhotosPipeline.add_url(img))
                    except Exception as e:
                        print(e)
