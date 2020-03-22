# -*- coding: utf-8 -*-
import scrapy


class OmccSpider(scrapy.Spider):
    name = 'omcc'
    allowed_domains = ['naccrrapps.naccrra.org']
    start_urls = ['http://naccrrapps.naccrra.org/navy/directory/programs.php?program=omcc&state=CA&pagenum=1']
    last_page_num = None

    def parse(self, response):
        # table = response.css('#tablekit-table-1') seemed right but it failed.
        # The id is dynamically added, so unfourtunately we cant use it. 
        # a combination of align and class properties will work for now.
        # in something that needs to be more sustainable, I might consider pitching a switch
        # to cypress or another headless browser based scraping strategy, since there is 
        # dynamic content
        table = response.xpath('//table[@align="center"]').css('.gray')

        heads = [self.setup_header(head) for head in table.xpath('//th/text()').getall()]
        cells = [cell for cell in table.xpath('//td/text()').getall()]
        row = {}
        for ix, cell in enumerate(cells):
            header_index = ix%8
            header = heads[header_index]
            if header_index == 0:
                # this row was complete, yield it and start a new one.
                yield row
                row = {}
                row[header] = cell if cell else ''
            else:
                row[header] = cell if cell else ''

        # Extract next page and keep going (IF this page isnt the last page.)
        if not self.last_page_num:
            last_page_link = [link.attrib['href'] for link in response.css('a') if 'Last Page' in link.get()][0]
            self.last_page_num = int(self.get_url_param('pagenum=', last_page_link))
        this_url = response.request.url
        next_page_num = int(self.get_url_param('pagenum=', this_url)) + 1
        if self.last_page_num >= next_page_num:
            next_page = this_url.replace(
                self.get_url_param('pagenum=', this_url),
                str(next_page_num)
            )
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            print('finished at page' + str(next_page_num))

    @staticmethod
    def get_url_param(param_string, url):
        # sub string the url to the param, then remove the param
        return url[url.index(param_string) + len(param_string):]

    @staticmethod
    def setup_header(header_string):
        return header_string.lower().replace(' ', '_')
