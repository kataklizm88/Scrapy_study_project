from pymongo import MongoClient



class MyProjectPipeline:

    def __init__(self):
        client = MongoClient('mongodb://localhost:27017')
        self.mongo_db = client.parser_ok

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)
        return item
