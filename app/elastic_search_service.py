from elasticsearch import Elasticsearch
from app.bd_lattes2 import bd_latts
import math


class ElasticSearchService():
    _fields = ["Área do Conhecimento", "Título em português", "Título em inglês",
              "Palavras-chave em português", "Palavras-chave em inglês",
             "Resumo em português", "Resumo em inglês"]
    _lates = bd_latts()
    _PIC_PLACEHOLDER = { 'url_imagem':'https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png'  }
    def __init__(self):
        self.con = self.connect_to_ES()

    def query(self, query_string):
        return self.results_query(query_string)


    def clean(self, dd):
        pass

    def connect_to_ES(self):
            es = Elasticsearch([{'host':'localhost','port':9200}])
            return es

    def results_query(self, search_query):
        es = self.con
        res= es.search(index='teses_usp',
                       body={ "query": { "multi_match" : { "query": search_query, "type": "best_fields", "fields": self._fields, "tie_breaker": 0.1 }}})

        results = []
        for hit in res['hits']['hits']:
            dic = dict()

            if type( hit['_source']['Orientador']) == list:
                dic['name'] = hit['_source']['Orientador'][0]
            else:
                dic['name'] = hit['_source']['Orientador']


            dic['score'] = math.ceil(float(hit['_score'])*10)
            dic['department'] = hit['_source']['Unidade da USP']
            dic['field'] = hit['_source']['Área do Conhecimento']
            dic['key_words'] = hit['_source']['Palavras-chave em português']
            dic['pt_abstract'] = hit['_source']['Título em português']
            dic['photo'] = self._lates.get(dic['name'],self._PIC_PLACEHOLDER ).get('url_imagem')
            dic['contato'] = self._lates.get(dic['name'], self._lates['placeholder']).get('tel')
            dic['email'] = self._lates.get(dic['name'], self._lates['placeholder']).get('email')



            results.append(dic)

        return results

    def get_professor_by_name(self, name):
        es = self.con
        res= es.search(index='teses_usp',body={'query':{'match':{'Orientador':name}}})
        results = []
        for hit in res['hits']['hits']:
            dic = dict()

            if type( hit['_source']['Orientador']) == list:
                dic['name'] = hit['_source']['Orientador'][0]
            else:
                dic['name'] = hit['_source']['Orientador']


            dic['score'] = float(hit['_score'])
            dic['department'] = hit['_source']['Unidade da USP']
            dic['field'] = hit['_source']['Área do Conhecimento']
            dic['key_words'] = hit['_source']['Palavras-chave em português']
            dic['pt_abstract'] = hit['_source']['Título em português']
            dic['photo'] = self._lates.get(dic['name'],self._PIC_PLACEHOLDER ).get('url_imagem')
            dic['contato'] = self._lates.get(dic['name'], self._lates['placeholder']).get('tel')
            dic['email'] = self._lates.get(dic['name'], self._lates['placeholder']).get('email')
            return dic




