def initDicQuery():
  return {}

def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

def createDicQuery(dic, cont):
  cont = cont.split('\n\n')
  for c in cont:
    c = c.replace('\n  ', '')
    c = c.replace('\n', '')
    c = c.replace('?', '')
    a,n = c.split('NUMBER:')
    index,n = n.split('TEXT:')
    dic[index] = {}
    
    text, n = n.split('NUMBER OF RELEVANT DOCS:')
    dic[index]["texto"] = text.split() # Tirar STOPWORDS

    for i in text:
      print(i)
    
    numDoc, n = n.split('RELEVANT DOCS AND SCORES:')
    dic[index]["NumDoc"] = numDoc

    dic[index]["Docs"] = {}
    '''for i in list(n):
      print(i)
      s,c = i.split(',')

    dic[index]["Docs"][s] = c'''
    

  return dic
