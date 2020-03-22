from scrapy.crawler import CrawlerProcess
from omcc_scraper.omcc_scraper.spiders.omcc import OmccSpider
from utils.data_ingest import ingest_full

items_found = []

class ItemCollectorPipeline():
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        items_found.append(item)

process = CrawlerProcess({
        'ITEM_PIPELINES': { '__main__.ItemCollectorPipeline': 100 }
})

process.crawl(OmccSpider)
process.start()

ingest_full(items_found, 'web')