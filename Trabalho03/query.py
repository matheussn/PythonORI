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
	c = conteudo.strip()
	c = patternQuery(c)
	s = c.count("NUMBER:")
	c = c.split()
	c.append("FIM!!!!!!!!!!!!")
	
	list2 = []
	
	for queries in range(s):
		list = []
		n = len(c)
		del(c[0])
		pos = 0
		for aux in range(n):			
			if c[aux]!= "NUMBER:" and c[aux]!= "FIM!!!!!!!!!!!!":
				list.insert(pos, c[aux])
			else:	
				break
			pos = pos +1 
		list.insert(0,"NUMBER:")	
		list = ' '.join(list)
		list2.insert(queries,list)
		for dele in range(pos):
			del(c[0])
		
		
	return list2

	
	
	
	
	
	
	
	'''
	for consulta in range(aux):
		number = getString(c, "NUMBER:", "TEXT:", False)
		print(number)
		
		text = getString(c, "TEXT:", "NUMBER OF RELEVANT DOCS:")
		print(text)
		
		nRelevantDocs = getString(c, "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:", False)
		print(nRelevantDocs)
		
		relDocs = getString(c, "RELEVANT DOCS AND SCORES:", "\n\n", False)
		print(relDocs)	
		
		subString = getSubstring(c, "NUMBER:", "\n\n") 
		
		c = c.replace(subString,'')
		
		#print(c)
		#break
'''



'''
  number = getString(c, "NUMBER:", "TEXT:", False)
  print(number)
  
  text = getString(c, "TEXT:", "NUMBER OF RELEVANT DOCS:")
  print(text)
  
  nRelevantDocs = getString(c, "NUMBER OF RELEVANT DOCS:", "RELEVANT DOCS AND SCORES:", False)
  print(nRelevantDocs)
  
  relDocs = getString(c, "RELEVANT DOCS AND SCORES:", "\n\n", False)
  print(relDocs)
  
  #string = getSubString(c, "NUMBER:", "\n\n")
  
  #print (string)
			
			'''
			
			
		

'''		
		
		
		



		relevantDocs = {}

		for i in nRelevantDocs:
			documento,score = relevantDocs[i].split(',')
			relevantDocs[documento] = score 

		dic[int(number)] = {
		'text': text,
		'nRelevantDocs': nRelevantDocs,
		'relevantDocs': relevantDocs,
		}	  

	return dic'''


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