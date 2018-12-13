from text import *
from files import *

def initDicQuery():
  return {}

def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

def createDicQuery(dicQuery, conteudo, index, lenBase):	
	
	queries = conteudo.split('\n\n')
	query = dict()
	for aux in queries:
		aux = patternQuery(aux)
			
		number = getString(aux, "NUMBER:", "TEXT:", False)

		text = getString(aux, "TEXT:", "NUMBER OF RELEVANT DOCS:")

		nRelevantDocs = getString(aux, "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:", False)

		relDocs = getString(aux, "RELEVANT DOCS AND SCORES:", "\n\n", False)

		relevantDocs = {}
		nRelevantDocs = int(nRelevantDocs[0])
		
		for i in range(nRelevantDocs):
			documento,score = relDocs[i].split(',')
			relevantDocs[documento] = score 
		
		number = int(number[0]) 
	
		dicQuery[number] = dict()
		createDicQueryPonderacao(dicQuery, lenBase, index, text, number)

		
		query[number] = {
			'text': text,
			'nRelevantDocs': nRelevantDocs,
			'relDocs': relevantDocs,	
		}	
	return query
	
def createDicQueryPonderacao(queries, totalFiles, invertedIndex, text, number):
	for termo in text:
		if queries[number].get(termo) == None:
			if invertedIndex.get(termo) != None:
				nTotalDocsTermo = len(invertedIndex[termo])
				freq = text.count(termo)
				tf1 = tf(freq)
				idf1 = idf(totalFiles,nTotalDocsTermo)
				queries[number][termo] = tf1 * idf1
			else:
				queries[number][termo] = 0

def calcSim(query, fileWeight):
	
	sim = dict();
	for file in fileWeight:
		for queries in query:
			sim[str(file) + ' ' + str(queries)] = {}
			sumConsDoc = 0
			sumConsulta = 0
			sumDocumento = 0
			similaridade= 0
			strFile = str(file)
			for termo in query[queries]:
				if fileWeight[strFile].get(termo) != None:
					sumConsDoc = sumConsDoc + query[queries][termo] * fileWeight[strFile][termo]
					sumDocumento = sumDocumento + fileWeight[file][termo]**2
					sumConsulta = sumConsulta + query[queries][termo]**2
			sumConsulta = sumConsulta**1/2
			sumDocumento = sumDocumento**1/2		
			denominador = (sumDocumento * sumConsulta)
			if denominador != 0:
				sim[str(file) + ' ' + str(queries)] = sumConsDoc/denominador
			else:
				sim[str(file) + ' ' + str(queries)] = 0
			
		break
	print(sim)
			
