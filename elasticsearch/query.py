from elasticsearch import Elasticsearch
from inject_data_ES import connect_to_ES

import json
import os

fields = ["Área do Conhecimento", "Título em português", "Título em inglês",
          "Palavras-chave em português", "Palavras-chave em inglês",
         "Resumo em português", "Resumo em inglês"]

def results_query(search_query):
	es = connect_to_ES()
	res= es.search(index='teses_usp',body={
  		"query": {
    	"multi_match" : {
      	"query": search_query,
      	"type": "best_fields",
      "fields": fields,
      "tie_breaker": 0.1
    		}
  		}
		})

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

