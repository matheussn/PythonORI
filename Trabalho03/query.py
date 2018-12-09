from text import *
from files import *

def initDicQuery():
  return {}

def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

def createDicQuery(dicQuery, conteudo):	
	
	queries = conteudo.split('\n\n')
		
	n = len(queries)
	del(queries[n-1])
	n = len(queries)
		
	for aux in range(n):
		queries[aux] = patternQuery(queries[aux])
			
		number = getString(queries[aux], "NUMBER:", "TEXT:", False)

		text = getString(queries[aux], "TEXT:", "NUMBER OF RELEVANT DOCS:")

		nRelevantDocs = getString(queries[aux], "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:", False)

		relDocs = getString(queries[aux], "RELEVANT DOCS AND SCORES:", "\n\n", False)

		relevantDocs = {}
		nRelevantDocs = int(nRelevantDocs[0])
		
		for i in range(nRelevantDocs):
			documento,score = relDocs[i].split(',')
			relevantDocs[documento] = score 
		
		number = int(number[0])
			
		
		dicQuery[number] = {
			'text': text,
			'nRelevantDocs': nRelevantDocs,
			'relDocs': relevantDocs,	
		}	
	return dicQuery
	
def createPonderacao(query, invertedIndex):

	totalDocmentos = len(invertedIndex)
	
	
	print(len(invertedIndex['effect']))
