from func import *

def addIndex(index, vet, name):
  for p in vet:
    if index.get(p) == None:
      index[p] = {}
    
    v = index[p]

    if v.get(name) == None:
      v[name] = 0
    
    v[name] += 1

def initFileWeight(index, fileWeight, vet, name, lenBase, porcent = None):
  for key in vet:
    freq = index[key].get(name)
    nDoc = len(index[key])
    if porcent != None:
      fileWeight[name][key] = tfidf(index[key].get(name),lenBase, nDoc, porcent)
    else:
      fileWeight[name][key] = tfidf(index[key].get(name), lenBase, nDoc)
      
def initMetricas(met, sim, baseQuery):
  media = dict()
  for i in sim:
    if met.get(i) == None:
      met[i] = { 'r&p':dict(), 'niveis':dict() }
    
    relevantEsp = list(baseQuery[i]['relDocs'].keys())
    relevantSys = sorted(sim[i], key = sim[i].get, reverse=True)
    R = len(relevantEsp)
    
    for item in relevantSys:
      if item in relevantEsp:
        ind = relevantSys.index(item) +1

        intersect = len( list( set(relevantEsp).intersection(relevantSys[:ind]) ) )
        p = (intersect/ind) * 100
        r = (intersect/R) * 100
        met[i]['r&p'][item] = (r, p)
        test(met[i]['r&p'][item], met[i]['niveis']) 

def test(tup, media):
  for i in range(1, 12):
    inf = (i-2) * 10
    s = (i-1) * 10
    if i == 1:
      inf = s
    if inf < tup[0] <= s:
      if media.get(s) == None:
        media[s] = 0
      media[s] = tup[1] if tup[1] > media[s] else media[s]

def calcMedia(met, tam):
  media = {0:0, 10:0, 20:0, 30:0, 40:0, 50:0, 60:0, 70:0, 80:0, 90:0, 100:0}
  for i in range(0, 100, 10):
    for j in met:
      if met[j]['niveis'].get(i) != None:
        media[i] += met[j]['niveis'][i]/tam

  return media