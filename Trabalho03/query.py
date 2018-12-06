from text import *

def initDicQuery():
  return {}

def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

def createDicQuery(dic, cont):
  cont = cont.replace('\n  ', '')
  cont = cont.split('\n\n')
  for c in cont:
    c = c.replace('\n', '')
    c = c.replace('?', '')
    a,n = c.split('NUMBER:')
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
