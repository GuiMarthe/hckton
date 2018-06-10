from elasticsearch import Elasticsearch 

import json
import os

# Connect to the elastic cluster
def connect_to_ES():
	es=Elasticsearch([{'host':'localhost','port':9200}])
	return es

def insert_docs(docs, index, doc_type, connection):
	ide = 1
	for doc in docs:
	    res = connection.index(index=index, doc_type=doc_type, id=ide, body=doc)
	    ide += 1

def main():
	PWD_DADOS = os.environ['PWD_DADOS']
	INDEX = os.environ['INDEX']
	DOC_TYPE = os.environ['DOC_TYPE']

	docs = json.loads(open(PWD_DADOS).read())
	es = connect_to_ES()
	# inserting theses
	insert_docs(docs, INDEX, DOC_TYPE, es)

if __name__=='__main__':
	main()