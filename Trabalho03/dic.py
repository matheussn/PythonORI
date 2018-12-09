from func import *

def addIndex(index, vet, name):
  for p in vet:
    if index.get(p) == None:
      index[p] = {}
    
    v = index[p]

    if v.get(name) == None:
      v[name] = 0
    
    v[name] += 1



def initFileWeight(index, fileWeight, vet, name):
  for key in vet:
    freq = index[key].get(name)
    fileWeight[name][key] = tf(index[key].get(name))
    #print("Termo: " + key + " Freq: "+ str(freq))