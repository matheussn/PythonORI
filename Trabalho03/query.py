from text import *
from files import *

def createDicQuery(dicQuery, conteudo, index, lenBase):	
	
	queries = conteudo.split('\n\n')
	query = dict()
	for aux in queries:
		if not aux:
			break
		
		aux = patternQuery(aux)
			
		number = getString(aux, "NUMBER:", "TEXT:", False)
		number = int(number[0]) 

		text = getString(aux, "TEXT:", "NUMBER OF RELEVANT DOCS:")
		addIndex(index["Queries"], text, number)

		nRelevantDocs = getString(aux, "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:", False)

		relDocs = getString(aux, "RELEVANT DOCS AND SCORES:", "\n\n", False)

		relevantDocs = {}
		nRelevantDocs = int(nRelevantDocs[0])
		
		for i in range(nRelevantDocs):
			documento,score = relDocs[i].split(',')
			relevantDocs[documento] = score 
	
		dicQuery[number] = dict()
		createDicQueryPonderacao(dicQuery, lenBase, index["BaseFiles"], text, number)

		
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

def calcSim(query, fileWeight, sim):

	for file in fileWeight:
		for queries in query:
			if sim.get(queries) == None:
				sim[queries] = dict()

			sumConsDoc = 0
			sumConsulta = 0
			sumDocumento = 0
			similaridade= 0
			strFile = str(file)
			for termo in query[queries]:
				if fileWeight[strFile].get(termo) != None:
					sumConsDoc = sumConsDoc + query[queries][termo] * fileWeight[strFile][termo]
					sumConsulta = sumConsulta + query[queries][termo]**2
			for termo in fileWeight[strFile]:
				sumDocumento = sumDocumento + fileWeight[strFile][termo]**2
			sumConsulta = sumConsulta**(1/2)
			sumDocumento = sumDocumento**(1/2)		
			denominador = (sumDocumento * sumConsulta)
			if denominador != 0:
				similaridade = sumConsDoc/denominador
			
			if similaridade != 0 and similaridade > 0.15:
				sim[queries][file] = similaridade