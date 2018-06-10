from elasticsearch import Elasticsearch


class ElasticSearchService():
    _fields = ["Área do Conhecimento", "Título em português", "Título em inglês",
              "Palavras-chave em português", "Palavras-chave em inglês",
             "Resumo em português", "Resumo em inglês"]

    def __init__(self):
        self.con = self.connect_to_ES()

    def query(self, query_string):
        return self.results_query(query_string)


    def clean(self, dd):
        pass

    def connect_to_ES(self):
            es=Elasticsearch([{'host':'localhost','port':9200}])
            return es

    def results_query(self, search_query):
        es = self.con
        res= es.search(index='teses_usp',
                       body={ "query": { "multi_match" : { "query": search_query, "type": "best_fields", "fields": self._fields, "tie_breaker": 0.1 }}})

        results = []
        for hit in res['hits']['hits']:
            dic = dict()
            if type( hit['_source']['Orientador']) == list:
                dic['orientador'] = hit['_source']['Orientador'][0]
            else:
                dic['orientador'] = hit['_source']['Orientador']
                dic['relevant_score'] = hit['_score']
                dic['Unidade_da_USP'] = hit['_source']['Unidade da USP']
                dic['area_do_conhecimento'] = hit['_source']['Área do Conhecimento']
                dic['palavras_chave_em_portugues'] = hit['_source']['Palavras-chave em português']
                dic['artigos_recentes'] = hit['_source']['Título em português']
            results.append(dic)

        return results
