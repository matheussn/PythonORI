from func import *

def addIndex(index, vet, name):
  for p in vet:
    if index.get(p) == None:
      index[p] = {}
    
    v = index[p]

    if v.get(name) == None:
      v[name] = 0
    
    v[name] += 1

def initFileWeight(index, fileWeight, lenBase):
  keys = list(index.keys())
  keys.sort()

  for key in keys:
    #print("termo: " + key)
    for i in index.get(key):
      nameFile = i
      
      if fileWeight.get(nameFile) == None:
        fileWeight[nameFile] = {}
        
      index = keys.index(key)
      fileWeight[nameFile][index] = tfidf(
                                            index[key].get(i),
                                            len(index[key]),
                                            lenBase)