#!/usr/bin/env python

import scrapy
import json
import os
from os import path

class ThesisSpider(scrapy.Spider):
    name = 'Usp'
    
    def __init__(self, links_file, prefix='out'):
        self.prefix = prefix
        with open(links_file) as f:
            self.urls = [link.strip() for link in f.readlines() if link.strip() != '']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_next_file(self):
        i = 0
        while os.path.exists(self.prefix + str(i)):
            i += 1
        return self.prefix + str(i)
            
    def parse(self, response):
        datas = []
        content = response.css('#CorpoTexto div')
        data = {}
        key = None
        for div in list(content):
            cls = div.css('::attr(class)').extract()[0]
            text = ''.join(div.xpath('.//text()').extract()).strip()
            if 'DocumentoTituloTexto' in cls:
                key = text
            elif 'DocumentoTexto' in cls:
                if key == 'E-mail':
                    data[key] = '@'.join(div.re("showEmail\('(.+)','(.+)'\)"))
                else:
                    vs = text.split('\n')
                    vs = [x.strip() for x in vs if x.strip() != '']
                    data[key] = vs[0] if len(vs) == 1 else vs
        data['url'] = response.url
        with open(self.get_next_file(), 'w') as f:
            print(json.dumps(data, ensure_ascii=False), file=f)
        