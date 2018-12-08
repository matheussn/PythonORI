from text import *
from files import *

def initDicQuery():
  return {}

def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

def createDicQuery(dic, conteudo):
    	
  for texto in conteudo:
	  number = getString(c, "NUMBER:", "TEXT:")
	  addIndex(dic, number, number)

	  text = getString(c, "TEXT:", "NUMBER OF RELEVANT DOCS:")
	  addIndex(dic, text, number)
	  
	  nRelevantDocs = getNumber(c, "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:" )
	  addIndex(dic, nDocsRelevant, number)
	  
	  relDocs = getNumber(c, "RELEVANT DOCS AND SCORES:", "\n\n" )
	  
	  for i in int(nRelevantDocs):
		documento,score = relevantDocs[i].split(',')
		relevantDocs[documento] = score 
		  	  
	  
	 dic[int(number)] = {
		  'text': text,
		  'nRelevantDocs': nRelevantDocs,
		  'relevantDocs': relevantDocs,

      }
	  
	  
	  

'''
 for texto in conteudo:
    texto = texto.replace('\n', '')
    texto = c.replace('?', '')
    a,n = texto.split('NUMBER:')
    index,n = n.split('TEXT:')
    dic[index] = {}
    
    text, n = n.split('NUMBER OF RELEVANT DOCS:')
    text = text.lower()
    text = removeSR(text.split())
    dic[index]["texto"] = {}
    tfidf = 1
    for i in text:
      #tfidf = função
      if tfidf > 0:
        dic[index]["texto"][i] = tfidf

    numDoc, n = n.split('RELEVANT DOCS AND SCORES:')
    dic[index]["NumDoc"] = numDoc
    n = n.split()
    
    dic[index]["Docs"] = {}
    for i in n:
      s,c = i.split(',')
      dic[index]["Docs"][s] = c   

  return dic
'''