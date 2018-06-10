#!/usr/bin/env python

import scrapy

class UspSpider(scrapy.Spider):
    name = 'Usp'
    
    def __init__(self, year=2018, startpage=1, endpage=1):
        self.urls = ['http://www.teses.usp.br/index.php?option=com_jumi&fileid=29&Itemid=158&lang=pt-br&id={0}&pagina={1}'.format(year, i)
                     for i in range(int(startpage), int(endpage)+1)]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('.dadosLinha')[1:-1].css('.dadosDocNome a::attr(href)').extract()
        print('\n'.join(links))
        