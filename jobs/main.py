from scrapy.crawler import CrawlerProcess
from omcc_scraper.omcc_scraper.spiders.omcc import OmccSpider
from utils.data_ingest import is_duplicate, add_data

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

print('ITEMS FOUND')
print(len(items_found))

import json


with open('errors.json', 'w+') as fp:
    fp.write(json.dumps(items_found[0]))

for item in items_found:
    # TODO - theres certainly a way to dedup incoming data in memory 
    # by comparing different sources in memory. We should do that instead
    # of constantly clanging against the db.
    if item and 'phone' in item and not is_duplicate(item['phone']):
        try:
            add_data(item, 'CA')
        except:
            with open('errors.json','a+') as fp:
                fp.write(json.dumps(item))

