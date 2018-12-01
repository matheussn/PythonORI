'''
  Classe que possui todos os dicionários que serão utilizados pelo sistema de RI
'''
class Dicionarios:
  def __init__(self, files):
    self.index = {}       # Indice invertido
    self.fileWeight = {}  # Peso dos arquivos
    self.queryWeight = {} # Peso da consulta
    self.answer = {}      # Conjunto da resposta
    self.file = files     # 
    
  '''
    Add palavras no indice invertido
  '''
  def addToIndex(self, vet, num):
    for p in vet:
      if self.index.get(p) == None:
        self.index[p] = {}
      
      v = self.index[p]

      if v.get(num) == None:
        v[num] = 0
      
      v[num] += 1

  def addToFileWeight(self, num):
    key = list(self.index.keys())
    key.sort()
    print(key)

  def getIndex(self):
    return self.index